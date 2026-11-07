"""Unit and Integration Tests for Group-Aware Dataset Splitter.

Title: An Explainable Multi-Level Transformer-Based Framework for Financial Scam
Narrative Detection and Fraud Analysis in Digital Communications.

Tests singleton group construction, cluster integrity, leakage prevention,
deterministic reproducibility, synthetic data exclusion, and distribution metrics.
"""

import pytest
import numpy as np
import pandas as pd
from pathlib import Path

from src.data.splitter import GroupAwareSplitter, GroupMetadata
from src.data.split_validator import SplitValidator, ValidationResult


@pytest.fixture
def sample_dataset():
    """Create a controlled mock dataset with clustered and unclustered records."""
    data = {
        "record_id": [f"REC_{i:04d}" for i in range(20)],
        "duplicate_cluster_id": [
            "CLUSTER_A", "CLUSTER_A", "CLUSTER_A",  # Cluster A (3 recs, label 1, sms)
            "CLUSTER_B", "CLUSTER_B",                # Cluster B (2 recs, label 0, email)
            "CLUSTER_C", "CLUSTER_C", "CLUSTER_C", "CLUSTER_C",  # Cluster C (4 recs, label 1, email)
            None, None, "", "nan", "   ",            # Unclustered singletons
            None, None, None, None, None, None,
        ],
        "label": [
            1, 1, 1,
            0, 0,
            1, 1, 1, 1,
            0, 0, 0, 1, 1,
            0, 0, 0, 1, 1, 0,
        ],
        "channel": [
            "sms", "sms", "sms",
            "email", "email",
            "email", "email", "email", "email",
            "email", "email", "sms", "sms", "email",
            "email", "sms", "email", "sms", "email", "email",
        ],
        "source": ["SRC_1"] * 10 + ["SRC_2"] * 10,
        "is_synthetic": [False] * 20,
    }
    return pd.DataFrame(data)


def test_singleton_group_construction(sample_dataset):
    """Test that unclustered records become independent unique singleton groups."""
    splitter = GroupAwareSplitter()
    group_ids = splitter.construct_group_ids(sample_dataset)

    # Clustered records must retain their cluster IDs
    assert group_ids.iloc[0] == "CLUSTER_A"
    assert group_ids.iloc[1] == "CLUSTER_A"
    assert group_ids.iloc[3] == "CLUSTER_B"
    assert group_ids.iloc[5] == "CLUSTER_C"

    # None, empty, whitespace, and 'nan' must become singleton_{record_id}
    assert group_ids.iloc[9] == "singleton_REC_0009"
    assert group_ids.iloc[10] == "singleton_REC_0010"
    assert group_ids.iloc[11] == "singleton_REC_0011"
    assert group_ids.iloc[12] == "singleton_REC_0012"
    assert group_ids.iloc[13] == "singleton_REC_0013"

    # Crucial: Unclustered records must NEVER be grouped into a single monolithic group
    singletons = group_ids[group_ids.str.startswith("singleton_")]
    assert singletons.nunique() == len(singletons)


def test_global_group_id_uniqueness(sample_dataset):
    """Test that group IDs are globally unique across all independent entities."""
    splitter = GroupAwareSplitter()
    group_ids = splitter.construct_group_ids(sample_dataset)
    sample_dataset["group_id"] = group_ids

    # For each group, verify all its members share the exact same group_id
    for gid, grp in sample_dataset.groupby("group_id"):
        if gid.startswith("singleton_"):
            assert len(grp) == 1
        else:
            assert len(grp) > 1


def test_duplicate_cluster_integrity_no_split_leakage(sample_dataset):
    """Verify that duplicate clusters are never divided across splits."""
    splitter = GroupAwareSplitter()
    target_ratios = {"train": 0.60, "validation": 0.20, "test": 0.20}
    split_df, _ = splitter.split(sample_dataset, target_ratios=target_ratios)

    # Every duplicate cluster must appear in exactly one split
    cluster_splits = split_df[split_df["duplicate_cluster_id"].notna() & (split_df["duplicate_cluster_id"] != "")].groupby(
        "duplicate_cluster_id"
    )["split"].nunique()

    for cid, num_splits in cluster_splits.items():
        if cid in ["CLUSTER_A", "CLUSTER_B", "CLUSTER_C"]:
            assert num_splits == 1, f"Cluster {cid} leaked across {num_splits} splits!"


def test_deterministic_reproducibility(sample_dataset):
    """Verify that repeated executions produce 100% bitwise identical assignments."""
    splitter = GroupAwareSplitter(random_seed=42)
    split_df_1, map_1 = splitter.split(sample_dataset)
    split_df_2, map_2 = splitter.split(sample_dataset)

    assert map_1 == map_2
    assert split_df_1["split"].equals(split_df_2["split"])


def test_mixed_stratum_group_detection():
    """Verify that a cluster with conflicting labels or channels raises an error."""
    splitter = GroupAwareSplitter()
    
    # Inconsistent labels in cluster
    df_bad_label = pd.DataFrame({
        "record_id": ["R1", "R2"],
        "duplicate_cluster_id": ["CLUSTER_X", "CLUSTER_X"],
        "label": [0, 1],  # Mixed labels!
        "channel": ["email", "email"],
    })
    with pytest.raises(ValueError, match="multiple labels"):
        splitter.split(df_bad_label)

    # Inconsistent channels in cluster
    df_bad_channel = pd.DataFrame({
        "record_id": ["R1", "R2"],
        "duplicate_cluster_id": ["CLUSTER_Y", "CLUSTER_Y"],
        "label": [1, 1],
        "channel": ["email", "sms"],  # Mixed channels!
    })
    with pytest.raises(ValueError, match="multiple channels"):
        splitter.split(df_bad_channel)


def test_synthetic_dataset_exclusion():
    """Verify that validator flags contamination if synthetic records are present."""
    df_contaminated = pd.DataFrame({
        "record_id": ["REAL_01", "REAL_02", "SYNTH_01"],
        "duplicate_cluster_id": [None, None, None],
        "label": [0, 1, 1],
        "channel": ["email", "sms", "sms"],
        "is_synthetic": [False, False, True],  # Synthetic contaminated!
        "split": ["train", "validation", "test"],
        "group_id": ["singleton_REAL_01", "singleton_REAL_02", "singleton_SYNTH_01"],
    })

    validator = SplitValidator(expected_total_records=3)
    result = validator.validate(df_contaminated)
    assert not result.is_valid
    assert any("synthetic records detected" in err.lower() or "synthetic id patterns" in err.lower() for err in result.errors)


def test_record_preservation_and_duplicate_detection():
    """Verify that validator flags missing, duplicate, or unassigned records."""
    df = pd.DataFrame({
        "record_id": ["R1", "R2", "R2"],  # Duplicate record ID
        "group_id": ["singleton_R1", "singleton_R2", "singleton_R2"],
        "label": [0, 1, 1],
        "channel": ["email", "sms", "sms"],
        "split": ["train", "validation", None],  # Unassigned split
    })

    validator = SplitValidator(expected_total_records=3)
    result = validator.validate(df)
    assert not result.is_valid
    assert any("duplicate record" in err.lower() for err in result.errors)
    assert any("unassigned" in err.lower() for err in result.errors)


def test_invalid_target_ratios():
    """Verify that invalid target ratios (not summing to 1.0) are rejected."""
    splitter = GroupAwareSplitter()
    df = pd.DataFrame({
        "record_id": ["R1"],
        "label": [0],
        "channel": ["email"],
    })
    with pytest.raises(ValueError, match="must sum to 1.0"):
        splitter.split(df, target_ratios={"train": 0.8, "validation": 0.1})  # Sums to 0.9
