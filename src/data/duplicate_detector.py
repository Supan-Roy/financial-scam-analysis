"""Duplicate, near-duplicate, and cross-dataset overlap analysis module."""

import hashlib
import logging
import re
from collections import defaultdict
from typing import Any, Dict, List, Set, Tuple

import numpy as np
import pandas as pd

from src.data.schemas import DuplicateAuditResult

logger = logging.getLogger(__name__)


def normalize_text_conservative(text: str) -> str:
    """Normalize text with case folding and whitespace collapsing."""
    if not isinstance(text, str):
        return ""
    return " ".join(text.lower().split())


def get_word_shingles(text: str, k: int = 3) -> Set[str]:
    """Extract word k-shingles from text."""
    words = re.findall(r"\w+", text.lower())
    if len(words) < k:
        return set(words)
    return set(" ".join(words[i : i + k]) for i in range(len(words) - k + 1))


class VectorizedMinHashLSH:
    """Fast Locality Sensitive Hashing (LSH) for MinHash Jaccard similarity."""

    def __init__(self, num_perm: int = 64, num_bands: int = 16, seed: int = 42):
        self.num_perm = num_perm
        self.num_bands = num_bands
        self.rows_per_band = num_perm // num_bands
        self.prime = 4294967311  # Mersenne-adjacent prime > 2^32

        rng = np.random.default_rng(seed)
        self.a = rng.integers(1, self.prime, size=num_perm, dtype=np.uint64)
        self.b = rng.integers(0, self.prime, size=num_perm, dtype=np.uint64)

        self.buckets: List[Dict[Tuple[int, ...], List[int]]] = [defaultdict(list) for _ in range(num_bands)]
        self.doc_ids: List[str] = []
        self.doc_shingles: List[Set[str]] = []

    def add_documents(self, doc_ids: List[str], texts: List[str]) -> None:
        """Add a batch of documents into the LSH index."""
        start_idx = len(self.doc_ids)
        for i, (doc_id, text) in enumerate(zip(doc_ids, texts)):
            shingles = get_word_shingles(text, k=3)
            self.doc_ids.append(doc_id)
            self.doc_shingles.append(shingles)

            curr_idx = start_idx + i
            if not shingles:
                sig = np.zeros(self.num_perm, dtype=np.uint64)
            else:
                th = np.array([int(hashlib.md5(t.encode("utf-8")).hexdigest()[:8], 16) for t in shingles], dtype=np.uint64)
                # Outer product + b mod prime, then take minimum across shingles
                sig = ((np.outer(self.a, th) + self.b[:, None]) % self.prime).min(axis=1)

            for band in range(self.num_bands):
                start = band * self.rows_per_band
                band_sig = tuple(sig[start : start + self.rows_per_band])
                self.buckets[band][band_sig].append(curr_idx)

    def find_near_duplicates(self, min_jaccard: float = 0.85) -> List[Tuple[str, str, float]]:
        """Identify verified near-duplicate pairs above min_jaccard threshold."""
        candidate_pairs: Set[Tuple[int, int]] = set()
        for band in range(self.num_bands):
            for bucket in self.buckets[band].values():
                if len(bucket) > 1:
                    for i in range(len(bucket)):
                        for j in range(i + 1, len(bucket)):
                            candidate_pairs.add((min(bucket[i], bucket[j]), max(bucket[i], bucket[j])))

        logger.info(f"LSH candidate pairs to verify: {len(candidate_pairs)}")
        verified_pairs: List[Tuple[str, str, float]] = []

        for i, j in candidate_pairs:
            s1 = self.doc_shingles[i]
            s2 = self.doc_shingles[j]
            if not s1 or not s2:
                continue
            intersection = len(s1 & s2)
            union = len(s1 | s2)
            if union > 0:
                jaccard = intersection / union
                if jaccard >= min_jaccard:
                    verified_pairs.append((self.doc_ids[i], self.doc_ids[j], round(jaccard, 4)))

        return verified_pairs


def audit_duplicates_and_overlap(
    dataset_dict: Dict[str, pd.DataFrame],
    text_col: str = "text",
    id_col: str = "id",
    min_jaccard: float = 0.85,
    sample_for_lsh: int = 25000,
) -> DuplicateAuditResult:
    """
    Perform exact duplicate analysis, normalized duplicate analysis, and scalable
    near-duplicate detection within and across all datasets.
    """
    logger.info("Executing exact, normalized, and near-duplicate audit")
    
    exact_dups_within: Dict[str, int] = {}
    norm_dups_within: Dict[str, int] = {}
    raw_text_sets: Dict[str, Set[str]] = {}
    norm_text_sets: Dict[str, Set[str]] = {}

    for name, df in dataset_dict.items():
        raw_series = df[text_col].astype(str)
        exact_dups = int(raw_series.duplicated().sum())
        exact_dups_within[name] = exact_dups
        raw_text_sets[name] = set(raw_series.unique())

        norm_series = raw_series.apply(normalize_text_conservative)
        norm_dups = int(norm_series.duplicated().sum())
        norm_dups_within[name] = norm_dups
        norm_text_sets[name] = set(norm_series.unique())

    # Cross-dataset exact overlaps
    names = list(dataset_dict.keys())
    exact_overlaps_cross: Dict[str, int] = {}
    norm_overlaps_cross: Dict[str, int] = {}

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pair_key = f"{names[i]} vs {names[j]}"
            exact_overlap = len(raw_text_sets[names[i]] & raw_text_sets[names[j]])
            exact_overlaps_cross[pair_key] = exact_overlap

            norm_overlap = len(norm_text_sets[names[i]] & norm_text_sets[names[j]])
            norm_overlaps_cross[pair_key] = norm_overlap

    # 3-way exact overlap
    three_way_exact = len(set.intersection(*raw_text_sets.values()))
    exact_overlaps_cross["all_three_datasets"] = three_way_exact
    three_way_norm = len(set.intersection(*norm_text_sets.values()))
    norm_overlaps_cross["all_three_datasets"] = three_way_norm

    # Near-duplicate analysis via LSH
    logger.info("Building MinHash LSH index for near-duplicate detection...")
    lsh = VectorizedMinHashLSH(num_perm=64, num_bands=16, seed=42)

    for name, df in dataset_dict.items():
        # Scoped sample if dataset is massive to ensure fast deterministic run
        if len(df) > sample_for_lsh:
            sampled_df = df.sample(sample_for_lsh, random_state=42)
            logger.info(f"Using representative sample of {sample_for_lsh} for {name} LSH audit")
        else:
            sampled_df = df

        doc_ids = [f"{name}:{row[id_col]}" if id_col in df.columns else f"{name}:{idx}" for idx, row in sampled_df.iterrows()]
        texts = sampled_df[text_col].astype(str).tolist()
        lsh.add_documents(doc_ids, texts)

    verified_near_pairs = lsh.find_near_duplicates(min_jaccard=min_jaccard)
    logger.info(f"Verified near-duplicate pairs (Jaccard >= {min_jaccard}): {len(verified_near_pairs)}")

    near_dups_within: Dict[str, int] = {name: 0 for name in names}
    near_dups_cross: Dict[str, int] = {f"{names[i]} vs {names[j]}": 0 for i in range(len(names)) for j in range(i + 1, len(names))}

    sample_near_duplicates: List[Dict[str, Any]] = []

    for doc1, doc2, sim in verified_near_pairs:
        d1_name = doc1.split(":")[0]
        d2_name = doc2.split(":")[0]

        if d1_name == d2_name:
            near_dups_within[d1_name] += 1
        else:
            pair_key = f"{d1_name} vs {d2_name}"
            inv_key = f"{d2_name} vs {d1_name}"
            if pair_key in near_dups_cross:
                near_dups_cross[pair_key] += 1
            elif inv_key in near_dups_cross:
                near_dups_cross[inv_key] += 1

        if len(sample_near_duplicates) < 10:
            sample_near_duplicates.append({
                "doc1": doc1,
                "doc2": doc2,
                "jaccard_similarity": sim,
            })

    return DuplicateAuditResult(
        exact_duplicates_within=exact_dups_within,
        normalized_duplicates_within=norm_dups_within,
        exact_overlaps_cross=exact_overlaps_cross,
        normalized_overlaps_cross=norm_overlaps_cross,
        near_duplicates_within=near_dups_within,
        near_duplicates_cross=near_dups_cross,
        sample_near_duplicates=sample_near_duplicates,
    )

