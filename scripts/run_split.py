"""Execution Pipeline for Dataset Splitting.

Title: An Explainable Multi-Level Transformer-Based Framework for Financial Scam
Narrative Detection and Fraud Analysis in Digital Communications.

Executes the group-aware, leakage-resistant dataset splitting pipeline,
performs all 12 validation checks, and exports datasets and audit reports.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sys
from pathlib import Path
from typing import Dict, Tuple

import pandas as pd

try:
    import yaml
except ImportError:
    yaml = None

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("run_split")

# Project root calculation
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data.splitter import GroupAwareSplitter
from src.data.split_validator import SplitValidator
from src.data.split_reporter import SplitReporter


def calculate_sha256(file_path: Path) -> str:
    """Calculate the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def run_splitting_pipeline(config_path: Optional[Path] = None) -> int:
    """Execute the complete dataset splitting workflow.
    
    Args:
        config_path: Optional path to splitting_config.yaml.
        
    Returns:
        0 on success, non-zero on error.
    """
    logger.info("=" * 70)
    logger.info("TASK 04.1: GROUP-AWARE DATASET SPLITTING PIPELINE")
    logger.info("=" * 70)

    if config_path is None:
        config_path = PROJECT_ROOT / "configs" / "splitting_config.yaml"

    if yaml is not None and config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        logger.info(f"Loaded configuration from {config_path}")
    else:
        logger.warning(f"Config file not found at {config_path}; using defaults.")
        config = {
            "dataset_scope": {
                "scam_dataset_path": "data/processed/real_fin_scam_processed.csv",
                "legit_dataset_path": "data/processed/real_fin_legit_processed.csv",
                "expected_record_count": 76193,
            },
            "target_proportions": {"train": 0.80, "validation": 0.10, "test": 0.10},
            "grouping": {
                "cluster_column": "duplicate_cluster_id",
                "record_id_column": "record_id",
                "singleton_prefix": "singleton_",
            },
            "algorithm": {"random_seed": 42},
            "output_paths": {
                "splits_dir": "data/splits",
                "reports_dir": "reports/splitting",
            },
        }

    # 1. Resolve paths
    scam_path = PROJECT_ROOT / config["dataset_scope"]["scam_dataset_path"]
    legit_path = PROJECT_ROOT / config["dataset_scope"]["legit_dataset_path"]
    splits_dir = PROJECT_ROOT / config["output_paths"]["splits_dir"]
    reports_dir = PROJECT_ROOT / config["output_paths"]["reports_dir"]

    splits_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    # 2. Record pre-split hashes of processed files
    processed_files_pre: Dict[str, Tuple[Path, str]] = {
        "real_fin_scam": (scam_path, calculate_sha256(scam_path)),
        "real_fin_legit": (legit_path, calculate_sha256(legit_path)),
    }
    logger.info("Verified processed datasets exist:")
    for ds_name, (fpath, fhash) in processed_files_pre.items():
        logger.info(f"  {ds_name}: {fhash}")

    # 3. Load datasets
    logger.info("Loading processed datasets...")
    df_scam = pd.read_csv(scam_path)
    df_legit = pd.read_csv(legit_path)

    logger.info(f"  Scam records loaded: {len(df_scam):,}")
    logger.info(f"  Legitimate records loaded: {len(df_legit):,}")

    # Combine datasets
    full_df = pd.concat([df_scam, df_legit], ignore_index=True)
    total_recs = len(full_df)
    logger.info(f"  Combined real corpus records: {total_recs:,}")

    expected_recs = config["dataset_scope"].get("expected_record_count", 76193)
    if total_recs != expected_recs:
        logger.error(f"Expected {expected_recs:,} records, got {total_recs:,}!")
        return 1

    # 4. Instantiate Splitter and execute allocation
    target_proportions = config["target_proportions"]
    splitter = GroupAwareSplitter(
        cluster_col=config["grouping"].get("cluster_column", "duplicate_cluster_id"),
        record_id_col=config["grouping"].get("record_id_column", "record_id"),
        singleton_prefix=config["grouping"].get("singleton_prefix", "singleton_"),
        random_seed=config["algorithm"].get("random_seed", 42),
    )

    logger.info("Executing Stratified Group-Aware Greedy Partitioning (SGGP)...")
    split_df, group_assignments = splitter.split(full_df, target_ratios=target_proportions)

    # 5. Export split datasets
    train_file = splits_dir / "train.csv"
    val_file = splits_dir / "validation.csv"
    test_file = splits_dir / "test.csv"
    assignments_file = splits_dir / "split_assignments.csv"

    logger.info(f"Writing split files to {splits_dir}...")
    train_df = split_df[split_df["split"] == "train"].copy()
    val_df = split_df[split_df["split"] == "validation"].copy()
    test_df = split_df[split_df["split"] == "test"].copy()

    train_df.to_csv(train_file, index=False)
    val_df.to_csv(val_file, index=False)
    test_df.to_csv(test_file, index=False)
    logger.info(f"  train.csv: {len(train_df):,} records ({len(train_df)/total_recs:.2%})")
    logger.info(f"  validation.csv: {len(val_df):,} records ({len(val_df)/total_recs:.2%})")
    logger.info(f"  test.csv: {len(test_df):,} records ({len(test_df)/total_recs:.2%})")

    # Export reproducibility assignment artifact
    assignment_cols = [
        "record_id",
        "group_id",
        "split",
        "label",
        "channel",
        "source",
        "duplicate_cluster_id",
    ]
    available_cols = [c for c in assignment_cols if c in split_df.columns]
    assignments_df = split_df[available_cols].copy()
    assignments_df.to_csv(assignments_file, index=False)
    logger.info(f"  split_assignments.csv: {len(assignments_df):,} records saved.")

    # 6. Execute Mandatory Validation Checks
    logger.info("Executing 12 mandatory validation checks...")
    validator = SplitValidator(
        expected_total_records=expected_recs,
        record_id_col="record_id",
        group_id_col="group_id",
        split_col="split",
        label_col="label",
        cluster_col="duplicate_cluster_id",
    )

    split_dfs = {
        "train": train_df,
        "validation": val_df,
        "test": test_df,
    }

    validation_result = validator.validate(
        full_df=split_df,
        split_dfs=split_dfs,
        original_processed_files=processed_files_pre,
    )

    print(validation_result.summary())
    if not validation_result.is_valid:
        logger.error("VALIDATION FAILED! Halting pipeline.")
        return 1

    # Verify idempotency / deterministic reproducibility
    logger.info("Verifying deterministic reproducibility...")
    split_df_run2, _ = splitter.split(full_df, target_ratios=target_proportions)
    if not split_df["split"].equals(split_df_run2["split"]):
        logger.error("REPRODUCIBILITY ERROR: Secondary run produced differing split assignments!")
        return 1
    logger.info("Deterministic reproducibility: 100% verified.")

    # 7. Generate Audit Reports
    logger.info("Generating split audit reports...")
    reporter = SplitReporter(reports_dir=reports_dir)

    dist_csv = reports_dir / "split_distribution.csv"
    integ_csv = reports_dir / "split_group_integrity.csv"
    summary_md = reports_dir / "split_summary.md"

    reporter.generate_distribution_csv(split_df, dist_csv)
    reporter.generate_group_integrity_csv(split_df, integ_csv)
    reporter.generate_summary_markdown(
        split_df,
        split_files={"train": train_file, "validation": val_file, "test": test_file, "assignments": assignments_file},
        output_path=summary_md,
    )

    logger.info("=" * 70)
    logger.info("SPLITTING PIPELINE SUCCESSFULLY COMPLETED")
    logger.info("=" * 70)
    return 0


def main() -> None:
    """Entry point for CLI execution."""
    parser = argparse.ArgumentParser(
        description="Run group-aware leakage-resistant dataset splitting pipeline."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to splitting_config.yaml",
    )
    args = parser.parse_args()

    exit_code = run_splitting_pipeline(config_path=args.config)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
