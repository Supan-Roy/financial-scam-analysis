"""Group-Aware Leakage-Resistant Dataset Splitter.

Title: An Explainable Multi-Level Transformer-Based Framework for Financial Scam
Narrative Detection and Fraud Analysis in Digital Communications.

Implements deterministic group-aware stratified partitioning (SGGP) to create
train, validation, and test splits for the real-world binary benchmark while
strictly preventing duplicate cluster leakage across partitions.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


@dataclass
class GroupMetadata:
    """Metadata container for an indivisible group of records."""

    group_id: str
    record_ids: List[str]
    size: int
    is_clustered: bool
    labels: Set[int]
    channels: Set[str]
    sources: Set[str]
    legitimate_categories: Set[str]

    @property
    def primary_label(self) -> int:
        """Return the label for this group; raises if heterogeneous."""
        if len(self.labels) > 1:
            raise ValueError(f"Group {self.group_id} has mixed labels: {self.labels}")
        return next(iter(self.labels))

    @property
    def primary_channel(self) -> str:
        """Return the channel for this group; raises if heterogeneous."""
        if len(self.channels) > 1:
            raise ValueError(f"Group {self.group_id} has mixed channels: {self.channels}")
        return next(iter(self.channels))

    @property
    def stratum_key(self) -> Tuple[int, str]:
        """Return the primary stratification tuple (label, channel)."""
        return (self.primary_label, self.primary_channel)


class GroupAwareSplitter:
    """Deterministic, leakage-resistant group-aware stratified splitter."""

    def __init__(
        self,
        cluster_col: str = "duplicate_cluster_id",
        record_id_col: str = "record_id",
        label_col: str = "label",
        channel_col: str = "channel",
        source_col: str = "source",
        legit_cat_col: str = "legitimate_category",
        singleton_prefix: str = "singleton_",
        random_seed: int = 42,
    ) -> None:
        """Initialize the splitter configuration."""
        self.cluster_col = cluster_col
        self.record_id_col = record_id_col
        self.label_col = label_col
        self.channel_col = channel_col
        self.source_col = source_col
        self.legit_cat_col = legit_cat_col
        self.singleton_prefix = singleton_prefix
        self.random_seed = random_seed

    def construct_group_ids(self, df: pd.DataFrame) -> pd.Series:
        """Construct indivisible group IDs.
        
        If duplicate_cluster_id is present and non-empty, use it.
        Otherwise, assign an independent unique singleton group ID.
        Never group all null/empty cluster IDs together.
        """
        if self.record_id_col not in df.columns:
            raise KeyError(f"Missing required record ID column: {self.record_id_col}")

        # Check if record IDs are unique
        if df[self.record_id_col].duplicated().any():
            dups = df[self.record_id_col][df[self.record_id_col].duplicated()].tolist()[:5]
            raise ValueError(f"Input DataFrame contains duplicate record IDs: {dups}")

        if self.cluster_col in df.columns:
            cluster_series = df[self.cluster_col]
            # Replace whitespace-only strings with NA
            is_valid_cluster = cluster_series.notna() & (
                cluster_series.astype(str).str.strip() != ""
            ) & (cluster_series.astype(str).str.strip().str.lower() != "nan")
            
            group_ids = cluster_series.where(
                is_valid_cluster,
                self.singleton_prefix + df[self.record_id_col].astype(str),
            )
        else:
            group_ids = self.singleton_prefix + df[self.record_id_col].astype(str)

        return group_ids.astype(str)

    def extract_group_metadata(self, df: pd.DataFrame) -> Dict[str, GroupMetadata]:
        """Aggregate records into indivisible groups and check internal consistency."""
        if "group_id" not in df.columns:
            df = df.copy()
            df["group_id"] = self.construct_group_ids(df)

        cols_to_use = ["group_id", self.record_id_col, self.label_col, self.channel_col]
        if self.source_col in df.columns:
            cols_to_use.append(self.source_col)
        if self.legit_cat_col in df.columns:
            cols_to_use.append(self.legit_cat_col)

        sub_df = df[cols_to_use]

        # Vectorized consistency checks
        agg_dict: Dict[str, Any] = {
            "size": (self.record_id_col, "count"),
            "label_nunique": (self.label_col, "nunique"),
            "label_first": (self.label_col, "first"),
            "channel_nunique": (self.channel_col, "nunique"),
            "channel_first": (self.channel_col, "first"),
        }

        group_summary = sub_df.groupby("group_id").agg(**agg_dict).reset_index()

        # Check for mixed labels
        if (group_summary["label_nunique"] > 1).any():
            bad = group_summary[group_summary["label_nunique"] > 1]["group_id"].tolist()[:5]
            raise ValueError(
                f"Integrity Error: Groups span multiple labels: {bad}. Duplicate clusters must be 100% class-pure."
            )

        # Check for mixed channels
        if (group_summary["channel_nunique"] > 1).any():
            bad = group_summary[group_summary["channel_nunique"] > 1]["group_id"].tolist()[:5]
            raise ValueError(
                f"Integrity Error: Groups span multiple channels: {bad}. Duplicate clusters must be channel-pure."
            )

        # Build GroupMetadata objects quickly using itertuples
        groups: Dict[str, GroupMetadata] = {}
        for row in group_summary.itertuples(index=False):
            gid = str(row.group_id)
            is_clustered = not gid.startswith(self.singleton_prefix)
            groups[gid] = GroupMetadata(
                group_id=gid,
                record_ids=[],  # mapped via DataFrame directly
                size=int(row.size),
                is_clustered=is_clustered,
                labels={int(row.label_first)},
                channels={str(row.channel_first)},
                sources=set(),
                legitimate_categories=set(),
            )

        return groups

    def split(
        self,
        df: pd.DataFrame,
        target_ratios: Optional[Dict[str, float]] = None,
    ) -> Tuple[pd.DataFrame, Dict[str, str]]:
        """Perform deterministic group-aware stratified greedy partitioning.
        
        Args:
            df: Canonical DataFrame of real-world communications.
            target_ratios: Dict of split names to target proportions (e.g. {'train': 0.8, 'val': 0.1, 'test': 0.1}).
            
        Returns:
            Tuple of (DataFrame with added 'split' and 'group_id' columns, dict mapping group_id to split name).
        """
        if target_ratios is None:
            target_ratios = {"train": 0.80, "validation": 0.10, "test": 0.10}

        ratio_sum = sum(target_ratios.values())
        if not np.isclose(ratio_sum, 1.0, atol=1e-5):
            raise ValueError(f"Target split ratios must sum to 1.0; got {ratio_sum}")

        # Ensure group_id is constructed
        df = df.copy()
        df["group_id"] = self.construct_group_ids(df)

        groups = self.extract_group_metadata(df)
        group_assignments: Dict[str, str] = {}

        # Organize groups into strata by (label, channel)
        strata: Dict[Tuple[int, str], List[GroupMetadata]] = {}
        for g in groups.values():
            s_key = g.stratum_key
            strata.setdefault(s_key, []).append(g)

        # Process each stratum independently
        # Sort strata keys deterministically
        for s_key in sorted(strata.keys()):
            stratum_groups = strata[s_key]

            # Bin-packing heuristic: sort groups descending by size
            # Secondary sort: group_id ascending for 100% deterministic reproducibility
            stratum_groups.sort(key=lambda g: (-g.size, g.group_id))

            total_records_in_stratum = sum(g.size for g in stratum_groups)
            targets = {split: total_records_in_stratum * ratio for split, ratio in target_ratios.items()}
            current_counts = {split: 0 for split in target_ratios.keys()}

            for g in stratum_groups:
                # Find split with minimum relative filling
                # min over (current_count + g.size) / target
                best_split = min(
                    target_ratios.keys(),
                    key=lambda s: (current_counts[s] + g.size) / targets[s] if targets[s] > 0 else float("inf"),
                )
                group_assignments[g.group_id] = best_split
                current_counts[best_split] += g.size

        # Map split assignments back to DataFrame
        df["split"] = df["group_id"].map(group_assignments)

        # Check that all records received an assignment
        if df["split"].isna().any():
            missing_groups = df[df["split"].isna()]["group_id"].unique().tolist()
            raise RuntimeError(f"Allocation failure: records in groups {missing_groups[:5]} have no split assigned.")

        return df, group_assignments
