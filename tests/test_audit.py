"""Unit tests for dataset auditing and inspection modules."""

import pandas as pd
import pytest

from src.data.composition import audit_dataset_composition
from src.data.duplicate_detector import (
    VectorizedMinHashLSH,
    audit_duplicates_and_overlap,
    normalize_text_conservative,
)
from src.data.inspector import (
    detect_id_column,
    detect_label_column,
    detect_text_column,
)
from src.data.quality import audit_data_quality
from src.data.research_bias import compute_lexical_diversity
from src.data.text_profiler import profile_text_distribution


def test_detect_column_helpers():
    """Verify field detection heuristics."""
    cols = ["record_id", "email_subject", "text", "label"]
    assert detect_text_column(cols) == "text"
    assert detect_id_column(cols) == "record_id"
    assert detect_label_column(cols) == "label"

    cols_alt = ["id", "content", "target"]
    assert detect_text_column(cols_alt) == "content"
    assert detect_id_column(cols_alt) == "id"
    assert detect_label_column(cols_alt) == "target"


def test_data_quality_audit():
    """Verify data quality checks on synthetic test dataframe."""
    df = pd.DataFrame({
        "id": ["T-01", "T-02", "T-03", "T-04"],
        "text": [
            "Your urgent invoice is ready. Please click <URL>.",
            "Normal banking notification [FINANCIAL_INFO].",
            "",  # Empty text
            "Short",  # Short text (<10 chars)
        ],
        "label": [1, 0, 1, 99],  # 99 is invalid label
    })

    res = audit_data_quality(df, "test_set", text_col="text", label_col="label", id_col="id")
    assert res.total_records == 4
    assert res.empty_text_count == 1
    assert res.invalid_labels_count == 1
    assert res.suspiciously_short_count == 2  # empty and 'Short'
    assert res.angle_bracket_placeholders == 1
    assert res.square_bracket_placeholders == 1


def test_composition_audit():
    """Verify composition audit on test dataframe."""
    df = pd.DataFrame({
        "label": [1, 1, 0],
        "scam_channel": ["sms", "email", "sms"],
        "phishing_type": ["card_fraud", "loan_offer", "card_fraud"],
        "social_engineering_tactics": ['["urgency", "scarcity"]', '["urgency"]', None],
    })

    comp = audit_dataset_composition(df, "test_comp")
    assert comp.total_records == 3
    assert comp.label_distribution == {"1": 2, "0": 1}
    assert comp.channel_distribution == {"sms": 2, "email": 1}
    assert comp.subtypes_distribution == {"card_fraud": 2, "loan_offer": 1}
    assert comp.social_engineering_tactics_distribution == {"urgency": 2, "scarcity": 1}


def test_text_profiler():
    """Verify text length statistics calculation."""
    df = pd.DataFrame({
        "text": [
            "one two three four five",  # 5 words, 23 chars
            "one two three",  # 3 words, 13 chars
            "one two three four five six seven eight nine ten",  # 10 words, 48 chars
        ]
    })

    stats, chars, words = profile_text_distribution(df, "test_text", text_col="text")
    assert stats.total_records == 3
    assert stats.word_min == 3
    assert stats.word_max == 10
    assert stats.word_median == 5.0
    assert stats.empty_count == 0


def test_duplicate_and_lsh_detection():
    """Verify exact, normalized, and LSH near-duplicate detection."""
    df1 = pd.DataFrame({
        "id": ["A-1", "A-2", "A-3"],
        "text": [
            "This is a test notification about your bank account.",
            "THIS IS A TEST NOTIFICATION ABOUT YOUR BANK ACCOUNT.",  # Normalized duplicate of A-1
            "Completely different message about dinner plans tonight.",
        ]
    })
    df2 = pd.DataFrame({
        "id": ["B-1"],
        "text": [
            "This is a test notification about your bank account hold.",  # Near-duplicate of A-1
        ]
    })

    assert normalize_text_conservative("  Hello   WORLD!  ") == "hello world!"

    dups = audit_duplicates_and_overlap(
        {"df1": df1, "df2": df2},
        text_col="text",
        id_col="id",
        min_jaccard=0.70,
        sample_for_lsh=10,
    )

    assert dups.exact_duplicates_within["df1"] == 0
    assert dups.normalized_duplicates_within["df1"] == 1
    assert dups.exact_overlaps_cross["df1 vs df2"] == 0

