"""Command-line orchestrator for executing the complete dataset audit pipeline."""

import argparse
import logging
import sys
import time
from pathlib import Path

# Add project root to path for reliable imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data import (
    analyze_research_biases,
    audit_data_quality,
    audit_dataset_composition,
    audit_duplicates_and_overlap,
    generate_all_audit_figures,
    generate_audit_csv_reports,
    generate_audit_json_summary,
    generate_audit_markdown_report,
    inspect_file_structure,
    profile_text_distribution,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("DatasetAuditor")


def run_pipeline(
    raw_dir: Path,
    output_dir: Path,
    skip_plots: bool = False,
    min_jaccard: float = 0.85,
) -> int:
    """Execute the dataset audit pipeline end-to-end."""
    start_time = time.time()
    logger.info("=" * 70)
    logger.info("STARTING COMPREHENSIVE DATASET AUDIT PIPELINE")
    logger.info(f"Raw data directory: {raw_dir}")
    logger.info(f"Output report directory: {output_dir}")
    logger.info("=" * 70)

    dataset_files = {
        "real_fin_scam": raw_dir / "real_fin_scam.csv",
        "synthetic_financial_scams": raw_dir / "synthetic_financial_scams.csv",
        "real_fin_legit": raw_dir / "real_fin_legit.csv",
    }

    # Verify all raw files exist
    for name, path in dataset_files.items():
        if not path.exists():
            logger.error(f"Required raw dataset not found: {path}")
            return 1

    structural_infos = {}
    loaded_dfs = {}
    quality_results = {}
    compositions = {}
    text_stats = {}

    # Stage 1: Structural, Quality, Composition, and Text Inspection
    logger.info("\n--- STAGE 1: Individual Dataset Audits ---")
    for name, path in dataset_files.items():
        t0 = time.time()
        logger.info(f"\n[Dataset: {name}]")
        
        # 1. Structural
        s_info, df = inspect_file_structure(path, name)
        structural_infos[name] = s_info
        loaded_dfs[name] = df
        logger.info(f"  Rows: {s_info.num_rows:,}, Cols: {s_info.num_cols}, Size: {s_info.file_size_mb:.2f} MB")
        logger.info(f"  SHA-256: {s_info.sha256_hash}")

        # 2. Quality
        q_res = audit_data_quality(df, name, text_col=s_info.text_column, label_col=s_info.label_column or "label")
        quality_results[name] = q_res
        logger.info(f"  Quality: Empty texts={q_res.empty_text_count}, Invalid labels={q_res.invalid_labels_count}")

        # 3. Composition
        c_res = audit_dataset_composition(df, name)
        compositions[name] = c_res
        logger.info(f"  Composition: Labels={c_res.label_distribution}, Channels={list(c_res.channel_distribution.keys())}")

        # 4. Text Profiling
        t_stat, _, _ = profile_text_distribution(df, name, text_col=s_info.text_column)
        text_stats[name] = t_stat
        logger.info(f"  Words: Mean={t_stat.word_mean:.1f}, Median={t_stat.word_median:.1f}, Max={t_stat.word_max:,}")
        logger.info(f"  Dataset audit completed in {time.time() - t0:.2f}s")

    # Stage 2: Duplicates & Overlap Analysis
    logger.info("\n--- STAGE 2: Duplicate & Cross-Dataset Overlap Analysis ---")
    t0 = time.time()
    duplicates = audit_duplicates_and_overlap(
        dataset_dict=loaded_dfs,
        text_col="text",
        id_col="id",
        min_jaccard=min_jaccard,
        sample_for_lsh=25000,
    )
    logger.info(f"Duplicate analysis completed in {time.time() - t0:.2f}s")
    for name in dataset_files.keys():
        logger.info(f"  {name}: Exact dupes={duplicates.exact_duplicates_within.get(name, 0)}, Near-dupe pairs={duplicates.near_duplicates_within.get(name, 0):,}")
    for pair, count in duplicates.exact_overlaps_cross.items():
        logger.info(f"  Cross exact overlap [{pair}]: {count}")

    # Stage 3: Research-Specific Biases
    logger.info("\n--- STAGE 3: Research Biases & Shortcut Learning Risks ---")
    t0 = time.time()
    biases = analyze_research_biases(loaded_dfs)
    logger.info(f"Bias analysis completed in {time.time() - t0:.2f}s")

    # Stage 4: Visualizations
    figures_dir = output_dir / "figures"
    if not skip_plots:
        logger.info("\n--- STAGE 4: Generating Publication-Quality Figures ---")
        t0 = time.time()
        figures = generate_all_audit_figures(
            dfs=loaded_dfs,
            structural_infos=structural_infos,
            compositions=compositions,
            text_stats=text_stats,
            duplicates=duplicates,
            biases=biases,
            output_dir=figures_dir,
        )
        logger.info(f"Generated {len(figures)} figures in {time.time() - t0:.2f}s at {figures_dir}")
    else:
        logger.info("\n--- STAGE 4: Skipping figure generation (--skip-plots active) ---")

    # Stage 5: Reports Generation
    logger.info("\n--- STAGE 5: Generating Audit Reports ---")
    t0 = time.time()
    csv_paths = generate_audit_csv_reports(
        structural_infos=structural_infos,
        quality_results=quality_results,
        compositions=compositions,
        text_stats=text_stats,
        duplicates=duplicates,
        output_dir=output_dir,
    )
    json_path = generate_audit_json_summary(
        structural_infos=structural_infos,
        quality_results=quality_results,
        compositions=compositions,
        text_stats=text_stats,
        duplicates=duplicates,
        biases=biases,
        output_dir=output_dir,
    )
    md_path = generate_audit_markdown_report(
        structural_infos=structural_infos,
        quality_results=quality_results,
        compositions=compositions,
        text_stats=text_stats,
        duplicates=duplicates,
        biases=biases,
        output_dir=output_dir,
    )
    logger.info(f"Reports generated in {time.time() - t0:.2f}s")
    for k, p in csv_paths.items():
        logger.info(f"  CSV:  {p}")
    logger.info(f"  JSON: {json_path}")
    logger.info(f"  MD:   {md_path}")

    elapsed = time.time() - start_time
    logger.info("=" * 70)
    logger.info(f"AUDIT PIPELINE COMPLETED SUCCESSFULLY IN {elapsed:.2f}s")
    logger.info("=" * 70)
    return 0


def main() -> None:
    """CLI entry point for dataset audit."""
    parser = argparse.ArgumentParser(
        description="Dataset Auditing Pipeline for Financial Scam Research Framework."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=PROJECT_ROOT / "data" / "raw",
        help="Path to directory containing raw CSV datasets.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "reports" / "dataset_audits",
        help="Path to output directory for reports and figures.",
    )
    parser.add_argument(
        "--skip-plots",
        action="store_true",
        help="Skip figure generation for faster headless execution.",
    )
    parser.add_argument(
        "--min-jaccard",
        type=float,
        default=0.85,
        help="Minimum 3-gram word Jaccard similarity threshold for near-duplicates.",
    )

    args = parser.parse_args()
    exit_code = run_pipeline(
        raw_dir=args.raw_dir,
        output_dir=args.output_dir,
        skip_plots=args.skip_plots,
        min_jaccard=args.min_jaccard,
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

