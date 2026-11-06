"""Text length profiling, statistical characterization, and token analysis."""

import logging
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from src.data.schemas import TextDistributionStats

logger = logging.getLogger(__name__)


def profile_text_distribution(
    df: pd.DataFrame,
    dataset_name: str,
    text_col: str = "text",
) -> Tuple[TextDistributionStats, pd.Series, pd.Series]:
    """
    Compute comprehensive character and word length statistics and return distributions.
    
    Returns:
        Tuple of (TextDistributionStats, char_lengths_series, word_lengths_series)
    """
    logger.info(f"Profiling text length distribution for {dataset_name} (N={len(df)})")
    
    if text_col not in df.columns:
        raise ValueError(f"Text column '{text_col}' not found in dataframe.")

    # Convert to string series safely
    text_series = df[text_col].fillna("").astype(str)
    empty_count = int((text_series.str.strip() == "").sum())

    char_lengths = text_series.str.len()
    word_lengths = text_series.str.split().apply(len)

    # Compute character length statistics
    char_min = int(char_lengths.min()) if len(char_lengths) > 0 else 0
    char_max = int(char_lengths.max()) if len(char_lengths) > 0 else 0
    char_mean = float(char_lengths.mean()) if len(char_lengths) > 0 else 0.0
    char_std = float(char_lengths.std()) if len(char_lengths) > 0 else 0.0
    char_median = float(char_lengths.median()) if len(char_lengths) > 0 else 0.0
    char_p25 = float(char_lengths.quantile(0.25)) if len(char_lengths) > 0 else 0.0
    char_p75 = float(char_lengths.quantile(0.75)) if len(char_lengths) > 0 else 0.0
    char_p90 = float(char_lengths.quantile(0.90)) if len(char_lengths) > 0 else 0.0
    char_p95 = float(char_lengths.quantile(0.95)) if len(char_lengths) > 0 else 0.0

    # Compute word length statistics
    word_min = int(word_lengths.min()) if len(word_lengths) > 0 else 0
    word_max = int(word_lengths.max()) if len(word_lengths) > 0 else 0
    word_mean = float(word_lengths.mean()) if len(word_lengths) > 0 else 0.0
    word_std = float(word_lengths.std()) if len(word_lengths) > 0 else 0.0
    word_median = float(word_lengths.median()) if len(word_lengths) > 0 else 0.0
    word_p25 = float(word_lengths.quantile(0.25)) if len(word_lengths) > 0 else 0.0
    word_p75 = float(word_lengths.quantile(0.75)) if len(word_lengths) > 0 else 0.0
    word_p90 = float(word_lengths.quantile(0.90)) if len(word_lengths) > 0 else 0.0
    word_p95 = float(word_lengths.quantile(0.95)) if len(word_lengths) > 0 else 0.0

    stats = TextDistributionStats(
        dataset_name=dataset_name,
        total_records=len(df),
        empty_count=empty_count,
        char_min=char_min,
        char_max=char_max,
        char_mean=round(char_mean, 2),
        char_std=round(char_std, 2),
        char_median=round(char_median, 2),
        char_p25=round(char_p25, 2),
        char_p75=round(char_p75, 2),
        char_p90=round(char_p90, 2),
        char_p95=round(char_p95, 2),
        word_min=word_min,
        word_max=word_max,
        word_mean=round(word_mean, 2),
        word_std=round(word_std, 2),
        word_median=round(word_median, 2),
        word_p25=round(word_p25, 2),
        word_p75=round(word_p75, 2),
        word_p90=round(word_p90, 2),
        word_p95=round(word_p95, 2),
    )

    return stats, char_lengths, word_lengths

