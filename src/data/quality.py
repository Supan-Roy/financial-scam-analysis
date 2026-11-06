"""Data quality and integrity auditing module."""

import logging
import re
from typing import Any, Dict, List

import pandas as pd

from src.data.schemas import QualityAuditResult

logger = logging.getLogger(__name__)


def audit_data_quality(
    df: pd.DataFrame,
    dataset_name: str,
    text_col: str = "text",
    label_col: str = "label",
    id_col: str = "id",
) -> QualityAuditResult:
    """
    Perform deep data quality and integrity checks on a dataset.
    """
    logger.info(f"Auditing data quality for {dataset_name} (N={len(df)})")
    total_records = len(df)

    # 1. Null counts and percentages
    null_counts = {col: int(df[col].isnull().sum()) for col in df.columns}
    null_percentages = {col: round((count / total_records) * 100, 2) for col, count in null_counts.items()}

    # 2. Text quality checks
    if text_col in df.columns:
        text_series = df[text_col]
        non_string_mask = ~text_series.apply(lambda x: isinstance(x, str))
        non_string_text_count = int(non_string_mask.sum())

        # Clean string representation for checks
        str_texts = text_series.fillna("").astype(str)
        empty_text_count = int((str_texts == "").sum())
        whitespace_only_text_count = int(((str_texts.str.strip() == "") & (str_texts != "")).sum())

        char_lengths = str_texts.str.len()
        suspiciously_short_mask = char_lengths < 10
        suspiciously_long_mask = char_lengths > 10000

        suspiciously_short_count = int(suspiciously_short_mask.sum())
        suspiciously_long_count = int(suspiciously_long_mask.sum())

        # Extract shortest and longest samples
        shortest_indices = char_lengths.sort_values().index[:5]
        shortest_samples = []
        for idx in shortest_indices:
            row = df.loc[idx]
            shortest_samples.append({
                "id": str(row[id_col]) if id_col in df.columns else str(idx),
                "char_length": int(char_lengths.loc[idx]),
                "word_count": len(str_texts.loc[idx].split()),
                "text_snippet": str_texts.loc[idx][:120],
            })

        longest_indices = char_lengths.sort_values(ascending=False).index[:5]
        longest_samples = []
        for idx in longest_indices:
            row = df.loc[idx]
            longest_samples.append({
                "id": str(row[id_col]) if id_col in df.columns else str(idx),
                "char_length": int(char_lengths.loc[idx]),
                "word_count": len(str_texts.loc[idx].split()),
                "text_snippet": str_texts.loc[idx][:120],
            })

        # Placeholder and HTML token detection
        angle_bracket_placeholders = int(str_texts.str.contains(r"<[A-Z0-9_]+>", regex=True).sum())
        square_bracket_placeholders = int(str_texts.str.contains(r"\[[A-Z0-9_]+\]", regex=True).sum())
        potential_html_count = int(str_texts.str.contains(r"<[a-zA-Z/][^>]*>", regex=True).sum())
    else:
        non_string_text_count = 0
        empty_text_count = 0
        whitespace_only_text_count = 0
        suspiciously_short_count = 0
        suspiciously_long_count = 0
        shortest_samples = []
        longest_samples = []
        angle_bracket_placeholders = 0
        square_bracket_placeholders = 0
        potential_html_count = 0

    # 3. Label validity
    if label_col and label_col in df.columns:
        unique_labels = df[label_col].unique().tolist()
        valid_labels = {0, 1}
        invalid_labels_count = int((~df[label_col].isin(valid_labels)).sum())
    else:
        unique_labels = []
        invalid_labels_count = 0

    return QualityAuditResult(
        dataset_name=dataset_name,
        total_records=total_records,
        null_counts=null_counts,
        null_percentages=null_percentages,
        empty_text_count=empty_text_count,
        whitespace_only_text_count=whitespace_only_text_count,
        non_string_text_count=non_string_text_count,
        invalid_labels_count=invalid_labels_count,
        unique_labels=unique_labels,
        suspiciously_short_count=suspiciously_short_count,
        suspiciously_long_count=suspiciously_long_count,
        shortest_samples=shortest_samples,
        longest_samples=longest_samples,
        angle_bracket_placeholders=angle_bracket_placeholders,
        square_bracket_placeholders=square_bracket_placeholders,
        potential_html_count=potential_html_count,
    )

