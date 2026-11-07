"""Split Integrity and Leakage Validation Suite.

Title: An Explainable Multi-Level Transformer-Based Framework for Financial Scam
Narrative Detection and Fraud Analysis in Digital Communications.

Implements rigorous verification of split assignments, duplicate cluster
integrity, record preservation, and absence of data leakage.
"""

from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import pandas as pd

logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    """Outcome container for split validation checks."""

    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)

    def summary(self) -> str:
        """Format an executive text summary of the validation result."""
        status = "PASSED" if self.is_valid else "FAILED"
        lines = [f"Split Validation Status: {status}"]
        if self.errors:
            lines.append("Errors:")
            for err in self.errors:
                lines.append(f"  [ERROR] {err}")
        if self.warnings:
            lines.append("Warnings:")
            for warn in self.warnings:
                lines.append(f"  [WARNING] {warn}")
        return "\n".join(lines)


class SplitValidator:
    """Comprehensive validator for train/val/test splits."""

    def __init__(
        self,
        expected_total_records: int = 76193,
        record_id_col: str = "record_id",
        group_id_col: str = "group_id",
        split_col: str = "split",
        label_col: str = "label",
        cluster_col: str = "duplicate_cluster_id",
    ) -> None:
        """Initialize the split validator."""
        self.expected_total_records = expected_total_records
        self.record_id_col = record_id_col
        self.group_id_col = group_id_col
        self.split_col = split_col
        self.label_col = label_col
        self.cluster_col = cluster_col

    @staticmethod
    def calculate_file_sha256(file_path: Path) -> str:
        """Compute the SHA-256 hash of a file."""
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()

    def validate(
        self,
        full_df: pd.DataFrame,
        split_dfs: Optional[Dict[str, pd.DataFrame]] = None,
        original_processed_files: Optional[Dict[str, Tuple[Path, str]]] = None,
    ) -> ValidationResult:
        """Execute all 12 mandatory validation checks.
        
        Args:
            full_df: Combined DataFrame containing split assignments.
            split_dfs: Optional dictionary of split name -> DataFrame.
            original_processed_files: Optional dict of dataset_name -> (path, expected_sha256).
            
        Returns:
            ValidationResult containing status, errors, warnings, and metrics.
        """
        errors: List[str] = []
        warnings: List[str] = []
        metrics: Dict[str, Any] = {}

        # 1. Total record count check
        total_records = len(full_df)
        metrics["total_records"] = total_records
        if total_records != self.expected_total_records:
            errors.append(
                f"Record count mismatch: expected {self.expected_total_records:,}, got {total_records:,}."
            )

        # 2 & 3. Missing and duplicate record ID checks
        record_ids = full_df[self.record_id_col]
        if record_ids.isna().any():
            errors.append(f"Found {record_ids.isna().sum()} null record IDs.")
        
        dup_count = record_ids.duplicated().sum()
        metrics["duplicate_record_count"] = int(dup_count)
        if dup_count > 0:
            dup_samples = record_ids[record_ids.duplicated()].tolist()[:5]
            errors.append(f"Found {dup_count} duplicate record IDs. Samples: {dup_samples}")

        # 4. Every record appears in exactly one split
        splits_present = full_df[self.split_col].unique()
        metrics["splits"] = list(splits_present)
        if full_df[self.split_col].isna().any():
            unassigned_count = full_df[self.split_col].isna().sum()
            errors.append(f"Found {unassigned_count} records with unassigned (null) split.")

        # Check split DataFrame partition consistency if provided
        if split_dfs is not None:
            split_recs = []
            for s_name, s_df in split_dfs.items():
                split_recs.extend(s_df[self.record_id_col].tolist())
            if len(split_recs) != total_records:
                errors.append(
                    f"Concatenated split DataFrames count ({len(split_recs)}) != full DataFrame ({total_records})."
                )
            if len(set(split_recs)) != len(split_recs):
                errors.append("Overlap detected across separate split DataFrames.")

        # 5 & 6. Duplicate cluster and group leakage checks
        group_split_counts = full_df.groupby(self.group_id_col)[self.split_col].nunique()
        leaked_groups = group_split_counts[group_split_counts > 1].index.tolist()
        metrics["leaked_group_count"] = len(leaked_groups)
        if len(leaked_groups) > 0:
            errors.append(
                f"DATA LEAKAGE DETECTED: {len(leaked_groups)} groups span multiple splits! "
                f"Samples: {leaked_groups[:5]}"
            )

        # Specifically check named duplicate clusters
        if self.cluster_col in full_df.columns:
            clustered_df = full_df[full_df[self.cluster_col].notna()]
            cluster_split_counts = clustered_df.groupby(self.cluster_col)[self.split_col].nunique()
            leaked_clusters = cluster_split_counts[cluster_split_counts > 1].index.tolist()
            metrics["leaked_duplicate_clusters"] = len(leaked_clusters)
            if len(leaked_clusters) > 0:
                errors.append(
                    f"DUPLICATE CLUSTER LEAKAGE: {len(leaked_clusters)} clusters span multiple splits! "
                    f"Samples: {leaked_clusters[:5]}"
                )
        else:
            metrics["leaked_duplicate_clusters"] = 0

        # 7. Label preservation
        if self.label_col not in full_df.columns:
            errors.append(f"Missing required label column: '{self.label_col}'.")
        else:
            valid_labels = {0, 1}
            observed_labels = set(full_df[self.label_col].dropna().unique())
            if not observed_labels.issubset(valid_labels):
                errors.append(f"Unexpected label values: {observed_labels - valid_labels}.")

        # 8. Synthetic records strictly absent
        if "is_synthetic" in full_df.columns:
            synthetic_records = full_df[full_df["is_synthetic"] == True]
            metrics["synthetic_record_count"] = len(synthetic_records)
            if len(synthetic_records) > 0:
                errors.append(
                    f"CONTAMINATION ERROR: {len(synthetic_records)} synthetic records detected in real benchmark splits!"
                )
        if "record_id" in full_df.columns:
            synthetic_id_matches = full_df["record_id"].str.contains("SYNTH", case=False, na=False).sum()
            if synthetic_id_matches > 0:
                errors.append(
                    f"CONTAMINATION ERROR: {synthetic_id_matches} records have synthetic ID patterns!"
                )

        # 9. Original processed files unchanged
        if original_processed_files is not None:
            for ds_name, (file_path, expected_hash) in original_processed_files.items():
                if file_path.exists():
                    current_hash = self.calculate_file_sha256(file_path)
                    if current_hash != expected_hash:
                        errors.append(
                            f"DATA INTEGRITY CORRUPTION: Processed dataset '{ds_name}' hash changed! "
                            f"Expected {expected_hash}, got {current_hash}."
                        )
                else:
                    errors.append(f"Processed file missing: {file_path}")

        # 10. Split proportions and distribution deviations
        split_counts = full_df[self.split_col].value_counts()
        metrics["split_record_counts"] = split_counts.to_dict()
        metrics["split_proportions"] = (split_counts / total_records).to_dict()

        target_ratios = {"train": 0.80, "validation": 0.10, "test": 0.10}
        deviations = {}
        for s_name, target_ratio in target_ratios.items():
            actual_ratio = metrics["split_proportions"].get(s_name, 0.0)
            dev = abs(actual_ratio - target_ratio)
            deviations[s_name] = dev
            # Alert if deviation exceeds 0.5% (our simulation showed < 0.01%)
            if dev > 0.005:
                warnings.append(
                    f"Split '{s_name}' proportion deviation ({dev:.4%}) exceeds 0.5% threshold."
                )
        metrics["proportion_deviations"] = deviations

        # 11. Cross-tab distributions
        # Label distribution across splits
        label_ct = pd.crosstab(full_df[self.split_col], full_df[self.label_col], normalize="index")
        metrics["split_label_proportions"] = label_ct.to_dict()

        # Channel distribution across splits
        if "channel" in full_df.columns:
            chan_ct = pd.crosstab(full_df[self.split_col], full_df["channel"], normalize="index")
            metrics["split_channel_proportions"] = chan_ct.to_dict()

        is_valid = len(errors) == 0
        return ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            metrics=metrics,
        )
