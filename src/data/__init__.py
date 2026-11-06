"""Data ingestion, schema inspection, quality auditing, validation, and reporting modules."""

from src.data.composition import audit_dataset_composition
from src.data.duplicate_detector import audit_duplicates_and_overlap
from src.data.inspector import inspect_file_structure
from src.data.quality import audit_data_quality
from src.data.reporter import (
    generate_audit_csv_reports,
    generate_audit_json_summary,
    generate_audit_markdown_report,
)
from src.data.research_bias import analyze_research_biases
from src.data.schemas import (
    CompositionAuditResult,
    DuplicateAuditResult,
    FileStructuralInfo,
    QualityAuditResult,
    TextDistributionStats,
)
from src.data.text_profiler import profile_text_distribution
from src.data.validation import (
    compute_lsh_theoretical_probabilities,
    run_channel_mapping_audit,
    run_extreme_message_investigation,
    run_intra_dataset_clustering,
    run_placeholder_investigation,
)
from src.data.visualizer import generate_all_audit_figures

__all__ = [
    "inspect_file_structure",
    "audit_data_quality",
    "audit_dataset_composition",
    "profile_text_distribution",
    "audit_duplicates_and_overlap",
    "analyze_research_biases",
    "generate_all_audit_figures",
    "generate_audit_csv_reports",
    "generate_audit_json_summary",
    "generate_audit_markdown_report",
    "run_intra_dataset_clustering",
    "run_placeholder_investigation",
    "run_extreme_message_investigation",
    "run_channel_mapping_audit",
    "compute_lsh_theoretical_probabilities",
    "FileStructuralInfo",
    "QualityAuditResult",
    "CompositionAuditResult",
    "TextDistributionStats",
    "DuplicateAuditResult",
]
