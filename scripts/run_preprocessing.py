"""
CLI Script to execute Canonical Dataset Engineering & Preprocessing Pipeline.

Usage:
    python scripts/run_preprocessing.py
"""

import sys
import logging
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.preprocessing.pipeline import CanonicalPreprocessingPipeline


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


def main():
    setup_logging()
    logger = logging.getLogger("run_preprocessing")
    logger.info("Initializing Canonical Dataset Engineering & Preprocessing Pipeline...")

    raw_dir = PROJECT_ROOT / "data" / "raw"
    processed_dir = PROJECT_ROOT / "data" / "processed"
    reports_dir = PROJECT_ROOT / "reports" / "preprocessing"
    cluster_csv_path = PROJECT_ROOT / "reports" / "dataset_audits" / "near_duplicate_clusters.csv"

    pipeline = CanonicalPreprocessingPipeline(
        raw_dir=raw_dir,
        processed_dir=processed_dir,
        reports_dir=reports_dir,
        cluster_csv_path=cluster_csv_path,
    )

    try:
        processed_dfs = pipeline.run_pipeline()
        logger.info("=" * 60)
        logger.info("Preprocessing complete! Dataset summary:")
        for name, df in processed_dfs.items():
            logger.info(f"  - {name}: {len(df):,} records, {len(df.columns)} columns")
        logger.info(f"Processed files saved to: {processed_dir}")
        logger.info(f"Reports generated in:     {reports_dir}")
        logger.info("=" * 60)
    except Exception as e:
        logger.exception(f"Preprocessing pipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

