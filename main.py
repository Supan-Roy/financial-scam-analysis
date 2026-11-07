"""Financial Scam Research Framework.

Title: An Explainable Multi-Level Transformer-Based Framework for Financial Scam
Narrative Detection and Fraud Analysis in Digital Communications.

Entry point for orchestrating data pipelines, model training, evaluation,
and explainability workflows.
"""

import argparse
import sys
from pathlib import Path


def main() -> None:
    """Main execution entry point."""
    parser = argparse.ArgumentParser(
        description="Explainable Multi-Level Transformer Framework for Financial Scam Detection."
    )
    parser.add_argument(
        "--audit",
        action="store_true",
        help="Run the complete dataset audit pipeline (Task 01).",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run the dataset audit validation & leakage investigation pipeline (Task 02).",
    )
    parser.add_argument(
        "--preprocess",
        action="store_true",
        help="Run the canonical preprocessing and harmonization pipeline (Task 03).",
    )
    parser.add_argument(
        "--skip-plots",
        action="store_true",
        help="Skip figure generation during audit.",
    )

    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent

    if args.audit:
        from scripts.run_dataset_audit import run_pipeline
        exit_code = run_pipeline(
            raw_dir=project_root / "data" / "raw",
            output_dir=project_root / "reports" / "dataset_audits",
            skip_plots=args.skip_plots,
        )
        sys.exit(exit_code)

    if args.validate:
        from scripts.run_audit_validation import run_validation_pipeline
        exit_code = run_validation_pipeline(
            raw_dir=project_root / "data" / "raw",
            output_dir=project_root / "reports" / "dataset_audits",
        )
        sys.exit(exit_code)

    if args.preprocess:
        from src.preprocessing.pipeline import CanonicalPreprocessingPipeline
        pipeline = CanonicalPreprocessingPipeline(
            raw_dir=project_root / "data" / "raw",
            processed_dir=project_root / "data" / "processed",
            reports_dir=project_root / "reports" / "preprocessing",
            cluster_csv_path=project_root / "reports" / "dataset_audits" / "near_duplicate_clusters.csv",
        )
        pipeline.run_pipeline()
        sys.exit(0)

    print("=" * 70)
    print("Financial Scam Research Framework")
    print("An Explainable Multi-Level Transformer-Based Framework for Financial Scam")
    print("Narrative Detection and Fraud Analysis in Digital Communications")
    print("=" * 70)
    print("\nAvailable Commands:")
    print("  python main.py --audit            Run the complete dataset audit pipeline (Task 01)")
    print("  python main.py --validate         Run audit validation & leakage investigation (Task 02)")
    print("  python main.py --preprocess       Run canonical preprocessing pipeline (Task 03)")
    print("  python scripts/run_dataset_audit.py     Run dataset audit with custom flags")
    print("  python scripts/run_audit_validation.py  Run validation pipeline with custom flags")
    print("  python scripts/run_preprocessing.py     Run canonical preprocessing directly")
    print("\nStatus: Framework initialized. Preprocessing and auditing pipelines ready.")


if __name__ == "__main__":
    main()
