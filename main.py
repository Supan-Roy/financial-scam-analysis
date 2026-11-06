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
        "--skip-plots",
        action="store_true",
        help="Skip figure generation during audit.",
    )

    args = parser.parse_args()

    if args.audit:
        from scripts.run_dataset_audit import run_pipeline
        project_root = Path(__file__).resolve().parent
        exit_code = run_pipeline(
            raw_dir=project_root / "data" / "raw",
            output_dir=project_root / "reports" / "dataset_audits",
            skip_plots=args.skip_plots,
        )
        sys.exit(exit_code)

    print("=" * 70)
    print("Financial Scam Research Framework")
    print("An Explainable Multi-Level Transformer-Based Framework for Financial Scam")
    print("Narrative Detection and Fraud Analysis in Digital Communications")
    print("=" * 70)
    print("\nAvailable Commands:")
    print("  python main.py --audit            Run the complete dataset audit pipeline")
    print("  python scripts/run_dataset_audit.py  Run dataset audit with custom flags")
    print("\nStatus: Framework initialized. Dataset auditing pipeline ready.")


if __name__ == "__main__":
    main()
