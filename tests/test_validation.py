"""Unit tests for Task 02 validation and leakage investigation modules."""

import pandas as pd
import pytest

from src.data.validation import (
    compute_lsh_theoretical_probabilities,
    get_word_shingles,
    run_channel_mapping_audit,
    run_extreme_message_investigation,
    run_intra_dataset_clustering,
    run_placeholder_investigation,
)


def test_lsh_theoretical_probabilities():
    """Verify LSH theoretical probability math."""
    probs = compute_lsh_theoretical_probabilities(num_bands=16, rows_per_band=4)
    assert 0.85 in probs
    assert probs[0.85] > 0.999  # ~0.999997
    assert probs[0.10] < 0.01   # Very low false positive at low similarity
    assert probs[0.99] > 0.9999


def test_word_shingles():
    """Verify word 3-gram shingling."""
    sh = get_word_shingles("The quick brown fox jumps over the lazy dog", k=3)
    assert "the quick brown" in sh
    assert "quick brown fox" in sh
    assert len(sh) == 7

    # Short string (<3 words)
    sh_short = get_word_shingles("quick brown", k=3)
    assert "quick" in sh_short
    assert "brown" in sh_short


def test_connected_component_clustering():
    """Verify connected component cluster formation on synthetic data."""
    df = pd.DataFrame({
        "id": ["T1", "T2", "T3", "T4"],
        "text": [
            "Attention: We noticed suspicious activity on your banking card. Please call immediately.",
            "Attention: We noticed suspicious activity on your banking card. Please call us immediately.", # Near-duplicate of T1
            "Attention: We noticed suspicious activity on your banking card. Please call right immediately.", # Near-duplicate of T1/T2
            "A completely unrelated message about tonight's football match.", # Disjoint
        ]
    })

    clusters, pairs, summary = run_intra_dataset_clustering(
        df=df,
        dataset_name="test_cluster",
        min_jaccard=0.75,
        num_perm=64,
        num_bands=16,
    )

    assert summary["total_records"] == 4
    assert summary["records_in_clusters"] == 3
    assert summary["total_clusters"] == 1
    assert summary["max_cluster_size"] == 3
    assert len(clusters) == 1
    assert "T1" in clusters[0]["member_ids"]


def test_placeholder_investigation():
    """Verify placeholder token extraction and density detection."""
    df1 = pd.DataFrame({
        "id": ["P1", "P2"],
        "text": [
            "Your invoice is ready at <URL>. Call <PHONE>.",
            "<URL> <PHONE> <US_DRIVER_LICENSE>", # Placeholder-dominated
        ],
        "source": ["src1", "src1"],
        "scam_channel": ["sms", "sms"],
    })
    df2 = pd.DataFrame({
        "id": ["P3"],
        "text": [
            "Hello [NAME], your [ORGANIZATION] account has balance [FINANCIAL_INFO].",
        ],
        "source": ["src2"],
        "scam_channel": ["email"],
    })

    df_inv, df_rec = run_placeholder_investigation({"d1": df1, "d2": df2})
    tokens_found = df_inv["token"].tolist()
    assert "<URL>" in tokens_found
    assert "<PHONE>" in tokens_found
    assert "[NAME]" in tokens_found
    assert "[FINANCIAL_INFO]" in tokens_found

    # P2 should be flagged as placeholder dominated
    p2_rec = df_rec[df_rec["id"] == "P2"].iloc[0]
    assert p2_rec["is_placeholder_dominated"] == True


def test_extreme_message_investigation():
    """Verify extreme short and long message detection."""
    df = pd.DataFrame({
        "id": ["S1", "N1", "L1"],
        "text": [
            ":)", # 2 chars (<10)
            "Normal normal normal normal normal text.",
            "A" * 10500, # >10,000 chars
        ],
        "source": ["src_s", "src_n", "src_l"],
        "scam_channel": ["sms", "email", "email"],
    })

    df_ext = run_extreme_message_investigation({"test": df})
    assert len(df_ext) == 2
    ids_flagged = df_ext["id"].tolist()
    assert "S1" in ids_flagged
    assert "L1" in ids_flagged

