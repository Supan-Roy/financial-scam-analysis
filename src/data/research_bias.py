"""Research-specific bias analysis and shortcut learning risk evaluation module."""

import logging
import re
from typing import Any, Dict

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def compute_lexical_diversity(texts: pd.Series) -> Dict[str, float]:
    """Compute Type-Token Ratio (TTR) and unique token stats."""
    sample_texts = texts.dropna().sample(min(2000, len(texts)), random_state=42)
    all_tokens = []
    for t in sample_texts:
        all_tokens.extend(re.findall(r"\w+", t.lower()))
    total_tokens = len(all_tokens)
    unique_tokens = len(set(all_tokens))
    ttr = (unique_tokens / total_tokens) if total_tokens > 0 else 0.0
    return {
        "sample_total_tokens": total_tokens,
        "sample_unique_tokens": unique_tokens,
        "type_token_ratio": round(ttr, 4),
    }


def analyze_research_biases(dfs: Dict[str, pd.DataFrame]) -> Dict[str, Any]:
    """
    Perform deep quantitative investigation into research biases:
    1. SMS vs Email length disparity
    2. Financial legitimate vs General legitimate characteristics
    3. Real scam vs Synthetic scam structural differences
    4. Spurious prediction shortcuts (placeholder leakage)
    5. Template overlap risks
    """
    logger.info("Executing research-specific bias audit")
    results: Dict[str, Any] = {}

    scam_df = dfs.get("real_fin_scam")
    syn_df = dfs.get("synthetic_financial_scams")
    legit_df = dfs.get("real_fin_legit")

    # 1. Channel vs Length disparity (SMS vs Email)
    channel_records = []
    for name, df in dfs.items():
        if "scam_channel" in df.columns:
            for ch in df["scam_channel"].dropna().unique():
                sub = df[df["scam_channel"] == ch]["text"].astype(str)
                words = sub.str.split().apply(len)
                channel_records.append({
                    "dataset": name,
                    "channel": ch,
                    "count": len(sub),
                    "mean_words": round(float(words.mean()), 1),
                    "median_words": round(float(words.median()), 1),
                    "p25_words": round(float(words.quantile(0.25)), 1),
                    "p75_words": round(float(words.quantile(0.75)), 1),
                    "p95_words": round(float(words.quantile(0.95)), 1),
                })
    results["channel_length_disparity"] = channel_records

    # 2. Legitimate categories: Financial vs General
    if legit_df is not None and "legitimate_category" in legit_df.columns:
        legit_cats = {}
        for cat in legit_df["legitimate_category"].unique():
            sub = legit_df[legit_df["legitimate_category"] == cat]["text"].astype(str)
            words = sub.str.split().apply(len)
            chars = sub.str.len()
            legit_cats[cat] = {
                "count": len(sub),
                "mean_words": round(float(words.mean()), 1),
                "median_words": round(float(words.median()), 1),
                "mean_chars": round(float(chars.mean()), 1),
                "median_chars": round(float(chars.median()), 1),
                "lexical_diversity": compute_lexical_diversity(sub),
            }
        results["legitimate_category_comparison"] = legit_cats

    # 3. Real Scam vs Synthetic Scam Structural Comparison
    if scam_df is not None and syn_df is not None:
        scam_words = scam_df["text"].astype(str).str.split().apply(len)
        syn_words = syn_df["text"].astype(str).str.split().apply(len)

        scam_cv = float(scam_words.std() / scam_words.mean()) if scam_words.mean() > 0 else 0
        syn_cv = float(syn_words.std() / syn_words.mean()) if syn_words.mean() > 0 else 0

        results["real_vs_synthetic_scam"] = {
            "real_scam": {
                "count": len(scam_df),
                "mean_words": round(float(scam_words.mean()), 1),
                "std_words": round(float(scam_words.std()), 1),
                "median_words": round(float(scam_words.median()), 1),
                "coefficient_of_variation": round(scam_cv, 2),
                "max_words": int(scam_words.max()),
                "min_words": int(scam_words.min()),
                "lexical_diversity": compute_lexical_diversity(scam_df["text"]),
            },
            "synthetic_scam": {
                "count": len(syn_df),
                "mean_words": round(float(syn_words.mean()), 1),
                "std_words": round(float(syn_words.std()), 1),
                "median_words": round(float(syn_words.median()), 1),
                "coefficient_of_variation": round(syn_cv, 2),
                "max_words": int(syn_words.max()),
                "min_words": int(syn_words.min()),
                "lexical_diversity": compute_lexical_diversity(syn_df["text"]),
            },
        }

    # 4. Spurious Shortcut Analysis (Placeholder Artifacts)
    shortcut_stats = {}
    for name, df in dfs.items():
        str_text = df["text"].astype(str)
        n = len(df)
        angle_count = int(str_text.str.contains(r"<[A-Z0-9_]+>", regex=True).sum())
        square_count = int(str_text.str.contains(r"\[[A-Z0-9_]+\]", regex=True).sum())
        shortcut_stats[name] = {
            "total_records": n,
            "angle_bracket_placeholders": angle_count,
            "angle_bracket_rate_pct": round((angle_count / n) * 100, 2),
            "square_bracket_placeholders": square_count,
            "square_bracket_rate_pct": round((square_count / n) * 100, 2),
        }
    results["spurious_shortcut_risks"] = shortcut_stats

    return results

