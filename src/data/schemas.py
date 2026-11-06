"""Data models and type definitions for dataset auditing."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class FileStructuralInfo:
    """Structural properties of a raw dataset file."""
    dataset_name: str
    file_path: str
    file_size_bytes: int
    file_size_mb: float
    sha256_hash: str
    num_rows: int
    num_cols: int
    columns: List[str]
    dtypes: Dict[str, str]
    duplicate_columns: List[str]
    id_column: Optional[str]
    id_unique: bool
    id_unique_count: int
    text_column: str
    label_column: Optional[str]


@dataclass
class QualityAuditResult:
    """Data quality and integrity audit results."""
    dataset_name: str
    total_records: int
    null_counts: Dict[str, int]
    null_percentages: Dict[str, float]
    empty_text_count: int
    whitespace_only_text_count: int
    non_string_text_count: int
    invalid_labels_count: int
    unique_labels: List[Any]
    suspiciously_short_count: int  # < 10 chars
    suspiciously_long_count: int   # > 10,000 chars
    shortest_samples: List[Dict[str, Any]]
    longest_samples: List[Dict[str, Any]]
    angle_bracket_placeholders: int  # e.g. <URL>, <PHONE>
    square_bracket_placeholders: int # e.g. [NAME], [FINANCIAL_INFO]
    potential_html_count: int


@dataclass
class CompositionAuditResult:
    """Categorical and demographic composition of a dataset."""
    dataset_name: str
    total_records: int
    label_distribution: Dict[str, int]
    channel_distribution: Dict[str, int]
    source_distribution: Dict[str, int]
    synthetic_distribution: Dict[str, int]
    subtypes_distribution: Dict[str, int] = field(default_factory=dict)
    fraudulent_intent_distribution: Dict[str, int] = field(default_factory=dict)
    social_engineering_tactics_distribution: Dict[str, int] = field(default_factory=dict)
    communication_types_distribution: Dict[str, int] = field(default_factory=dict)


@dataclass
class TextDistributionStats:
    """Text length, word count, and percentiles."""
    dataset_name: str
    total_records: int
    empty_count: int
    char_min: int
    char_max: int
    char_mean: float
    char_std: float
    char_median: float
    char_p25: float
    char_p75: float
    char_p90: float
    char_p95: float
    word_min: int
    word_max: int
    word_mean: float
    word_std: float
    word_median: float
    word_p25: float
    word_p75: float
    word_p90: float
    word_p95: float


@dataclass
class DuplicateAuditResult:
    """Exact, normalized, and near-duplicate audit results."""
    exact_duplicates_within: Dict[str, int]
    normalized_duplicates_within: Dict[str, int]
    exact_overlaps_cross: Dict[str, int]
    normalized_overlaps_cross: Dict[str, int]
    near_duplicates_within: Dict[str, int]
    near_duplicates_cross: Dict[str, int]
    sample_near_duplicates: List[Dict[str, Any]]

