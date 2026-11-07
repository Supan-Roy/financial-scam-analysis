"""
Unit tests for Canonical Preprocessing Pipeline (Tasks 03 & 03.1).
"""

import pytest
import pandas as pd
from pathlib import Path

from src.preprocessing.harmonizer import (
    PlaceholderHarmonizer,
    CANONICAL_PLACEHOLDER_MAPPINGS,
    CANONICAL_TOKENS,
)
from src.preprocessing.channel_mapper import ChannelHarmonizer
from src.preprocessing.pipeline import (
    CanonicalPreprocessingPipeline,
    CANONICAL_COLUMNS,
    EXPECTED_RAW_HASHES,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_raw_dataset_hash_preservation():
    """Verify that raw CSV datasets match reference SHA-256 hashes."""
    pipeline = CanonicalPreprocessingPipeline(
        raw_dir=PROJECT_ROOT / "data" / "raw",
        processed_dir=PROJECT_ROOT / "data" / "processed",
        reports_dir=PROJECT_ROOT / "reports" / "preprocessing",
    )
    results = pipeline.verify_raw_data_integrity()
    for filename, res in results.items():
        assert res["verified"] is True, f"Hash mismatch for {filename}!"


def test_placeholder_normalization_categories():
    """Test placeholder normalization across all canonical entity categories."""
    harmonizer = PlaceholderHarmonizer()

    sample_text = (
        "Visit <URL> or [LINK REDACTED]. Call <PHONE> or <PHONE_NUMBER> or [PHONE_NUMBER]. "
        "Email <EMAIL> or [EMAIL_ADDRESS]. Spoke with [NAME] and [Fictional Contact]. "
        "Issued by [FICTIONAL ORGANIZATION] for [AMOUNT REDACTED] from <US_BANK_NUMBER>. "
        "Check <US_DRIVER_LICENSE>, <US_SSN>, and [REFERENCE_NUMBER] on <DATE_TIME> at <LOCATION>. "
        "Review file [FILE_NAME] with commodity [PRODUCT]. Enter password [PASSWORD]."
    )

    norm = harmonizer.normalize_text(sample_text)

    # Verify canonical tokens are present
    assert "[URL]" in norm
    assert "<URL>" not in norm
    assert "[LINK REDACTED]" not in norm

    assert "[PHONE_NUMBER]" in norm
    assert "<PHONE>" not in norm

    assert "[EMAIL_ADDRESS]" in norm
    assert "<EMAIL>" not in norm

    assert "[PERSON_NAME]" in norm
    assert "[NAME]" not in norm
    assert "[Fictional Contact]" not in norm

    assert "[ORGANIZATION]" in norm
    assert "[FICTIONAL ORGANIZATION]" not in norm

    assert "[FINANCIAL_DATA]" in norm
    assert "<US_BANK_NUMBER>" not in norm
    assert "[AMOUNT REDACTED]" not in norm

    assert "[IDENTIFIER]" in norm
    assert "<US_DRIVER_LICENSE>" not in norm
    assert "<US_SSN>" not in norm
    assert "[REFERENCE_NUMBER]" not in norm

    assert "[DATE_TIME]" in norm
    assert "<DATE_TIME>" not in norm

    assert "[LOCATION]" in norm
    assert "<LOCATION>" not in norm

    assert "[SYSTEM_ARTIFACT]" in norm
    assert "[FILE_NAME]" not in norm

    assert "[CREDENTIAL]" in norm
    assert "[PASSWORD]" not in norm

    assert "[PRODUCT]" in norm


def test_targeted_placeholder_corrections():
    """Test Task 03.1 semantic corrections: NAMED_ENTITY, NRP, You, and PASSWORD."""
    harmonizer = PlaceholderHarmonizer()

    # 1. <NAMED_ENTITY> preserved as [NAMED_ENTITY] (not person name)
    t1 = "Your <NAMED_ENTITY> account is locked."
    n1 = harmonizer.normalize_text(t1)
    assert "[NAMED_ENTITY]" in n1
    assert "[PERSON_NAME]" not in n1

    # 2. <NRP> preserved as [NRP] (NORP demographic entity, not organization)
    t2 = "The mission is to help <NRP> taxpayers in the <NRP> market."
    n2 = harmonizer.normalize_text(t2)
    assert "[NRP]" in n2
    assert "[ORGANIZATION]" not in n2

    # 3. [You] preserved as [You] (dialogue turn marker, not person name)
    t3 = "[Fictional Contact]: Alert! [You]: Can you provide details?"
    n3 = harmonizer.normalize_text(t3)
    assert "[You]:" in n3
    assert "[PERSON_NAME]: Can you" not in n3

    # 4. [PASSWORD] mapped to [CREDENTIAL] (not system artifact)
    t4 = "User ID: [USERNAME] PW: [PASSWORD]"
    n4 = harmonizer.normalize_text(t4)
    assert "[CREDENTIAL]" in n4
    assert "[SYSTEM_ARTIFACT]" not in n4


def test_nested_and_malformed_placeholders():
    """Test collapsing of nested brackets and malformed bracket artifacts."""
    harmonizer = PlaceholderHarmonizer()

    cases = [
        ("[[[[[PRODUCT]]]]]", "[PRODUCT]"),
        ("[[NAME]]", "[PERSON_NAME]"),
        ("[[[[USERNAME]]]]", "[PERSON_NAME]"),
        ("<<<URL>>>", "[URL]"),
        ("<<[FILE_NAME]>>", "[SYSTEM_ARTIFACT]"),
        ("<< File: [FILE_NAME] >>", "[SYSTEM_ARTIFACT]"),
        ("[[[ORGANIZATION]]]", "[ORGANIZATION]"),
        ("[[FINANCIAL_INFO]]", "[FINANCIAL_DATA]"),
    ]

    for inp, expected in cases:
        norm = harmonizer.normalize_text(inp)
        assert norm == expected, f"Failed for {inp}: expected {expected}, got {norm}"


def test_nested_cleanup_preserves_words():
    """Verify that bracket un-nesting does not strip natural language words."""
    harmonizer = PlaceholderHarmonizer()

    text = "Important notice: please review [[[[[PRODUCT]]]]] and [[NAME]] before deadline tomorrow."
    norm = harmonizer.normalize_text(text)

    # Natural words must be completely intact
    for word in ["Important", "notice:", "please", "review", "before", "deadline", "tomorrow."]:
        assert word in norm


def test_placeholder_idempotency():
    """Verify that normalization is strictly idempotent: f(f(x)) == f(x)."""
    harmonizer = PlaceholderHarmonizer()

    texts = [
        "Alert: <URL> for <US_BANK_NUMBER> with [AMOUNT REDACTED] on <DATE_TIME>.",
        "[[[[[PRODUCT]]]]] from [ORGANIZATION] sent to [[NAME]] <<[FILE_NAME]>>.",
        "Simple plain text with no placeholders at all.",
        "Mixed: <PHONE> and [PHONE_NUMBER] and [unknown_bracket_token].",
        "Your <NAMED_ENTITY> account is locked. Contact <NRP> with [PASSWORD]. [You]: OK.",
    ]

    for t in texts:
        first_pass = harmonizer.normalize_text(t)
        second_pass = harmonizer.normalize_text(first_pass)
        assert first_pass == second_pass, f"Idempotency failed for: {t}"


def test_unknown_placeholder_preservation():
    """Verify unknown placeholders are preserved intact and recorded."""
    harmonizer = PlaceholderHarmonizer()

    text = "Hello <UNKNOWN_ENTITY> and [Flight AF4590] and [heir] at [URL]."
    norm = harmonizer.normalize_text(text)

    # Unknown tokens should not be converted to SYSTEM_ARTIFACT
    assert "<UNKNOWN_ENTITY>" in norm
    assert "[Flight AF4590]" in norm
    assert "[heir]" in norm
    assert "[SYSTEM_ARTIFACT]" not in norm

    unresolved = harmonizer.find_unresolved_placeholders(norm)
    assert "<UNKNOWN_ENTITY>" in unresolved
    assert "[Flight AF4590]" in unresolved
    assert "[heir]" in unresolved
    assert "[URL]" not in unresolved


def test_channel_harmonization_rules():
    """Test channel mapping rules and email-to-SMS gateway identification."""
    mapper = ChannelHarmonizer()

    # 1. IMC25 sms/email without gateway headers (ordinary SMS)
    ch, is_gw, has_hdr = mapper.harmonize_channel("sms/email", "Smishing Dataset IMC25", "Your code is 12345")
    assert ch == "sms"
    assert is_gw is False
    assert has_hdr is False

    # 2. IMC25 sms/email with FRM header (verified gateway transmission)
    ch, is_gw, has_hdr = mapper.harmonize_channel("sms/email", "Smishing Dataset IMC25", "FRM:Bank MSG:Alert")
    assert ch == "sms"
    assert is_gw is True
    assert has_hdr is True

    # 3. Standard SMS
    ch, is_gw, has_hdr = mapper.harmonize_channel("sms", "UCI SMS", "Hello there")
    assert ch == "sms"
    assert is_gw is False
    assert has_hdr is False

    # 4. Standard Email
    ch, is_gw, has_hdr = mapper.harmonize_channel("email", "Nigerian_Fraud.csv", "Dear friend, I am...")
    assert ch == "email"
    assert is_gw is False
    assert has_hdr is False

    # 5. Synthetic Chat and Notification
    ch, is_gw, has_hdr = mapper.harmonize_channel("chat", "synthetic", "Hello")
    assert ch == "chat"
    assert is_gw is False

    ch, is_gw, has_hdr = mapper.harmonize_channel("notification", "synthetic", "Security alert")
    assert ch == "notification"
    assert is_gw is False


def test_schema_mapping_and_columns():
    """Test canonical schema fields and nullability constraints on mock data."""
    raw_dir = PROJECT_ROOT / "data" / "raw"
    pipeline = CanonicalPreprocessingPipeline(
        raw_dir=raw_dir,
        processed_dir=PROJECT_ROOT / "data" / "processed",
        reports_dir=PROJECT_ROOT / "reports" / "preprocessing",
    )

    mock_df = pd.DataFrame([{
        "id": "TEST-0001",
        "text": "FRM:Bank MSG:Hello <URL> for [NAME]",
        "label": 1,
        "scam_channel": "sms/email",
        "source": "Smishing Dataset IMC25 (public user reports)",
        "source_url": "https://example.com",
        "source_license": "CC BY",
        "source_record_id": "RAW-01",
        "phishing_type": "banking",
    }])

    cluster_map = {"TEST-0001": "TEST_C0001"}
    proc = pipeline.process_real_fin_scam(mock_df, cluster_map)

    # Check all columns exist
    assert list(proc.columns) == CANONICAL_COLUMNS
    row = proc.iloc[0]

    assert row["record_id"] == "TEST-0001"
    assert row["original_text"] == "FRM:Bank MSG:Hello <URL> for [NAME]"
    assert row["normalized_text"] == "FRM:Bank MSG:Hello [URL] for [PERSON_NAME]"
    assert row["label"] == 1
    assert row["channel"] == "sms"
    assert row["original_channel"] == "sms/email"
    assert bool(row["is_email_gateway"]) is True
    assert bool(row["has_gateway_headers"]) is True
    assert row["duplicate_cluster_id"] == "TEST_C0001"
    assert bool(row["is_synthetic"]) is False
    assert row["char_count_original"] == len(mock_df["text"].iloc[0])
    assert row["word_count_original"] == len(mock_df["text"].iloc[0].split())


def test_cluster_mapping_loader():
    """Verify cluster mapping correctly loads from near_duplicate_clusters.csv."""
    cluster_csv = PROJECT_ROOT / "reports" / "dataset_audits" / "near_duplicate_clusters.csv"
    pipeline = CanonicalPreprocessingPipeline(
        raw_dir=PROJECT_ROOT / "data" / "raw",
        processed_dir=PROJECT_ROOT / "data" / "processed",
        reports_dir=PROJECT_ROOT / "reports" / "preprocessing",
        cluster_csv_path=cluster_csv,
    )
    mapping = pipeline.load_cluster_mapping()
    assert len(mapping) == 7556
    # Check that known clusters are mapped
    assert "FIN-00681" in mapping
    assert mapping["FIN-00681"].startswith("REAL_FIN_SCAM_C")


def test_synthetic_and_legit_processing_mock():
    """Verify processing for synthetic and legitimate dataset schemas."""
    pipeline = CanonicalPreprocessingPipeline(
        raw_dir=PROJECT_ROOT / "data" / "raw",
        processed_dir=PROJECT_ROOT / "data" / "processed",
        reports_dir=PROJECT_ROOT / "reports" / "preprocessing",
    )

    # Synthetic mock
    synth_df = pd.DataFrame([{
        "id": "SYNTH-01",
        "text": "Transfer [AMOUNT REDACTED] to [Fictional Contact] at [FICTIONAL SERVICE]. [You]: OK",
        "label": 1,
        "scam_channel": "chat",
        "fraudulent_intent": "Advance Fee",
        "social_engineering_tactics": "Urgency, Authority",
        "language": "en",
        "synthetic": True,
        "generation_scenario": "Scenario A",
        "risk_or_safety_note": "Educational note",
    }])
    synth_proc = pipeline.process_synthetic_financial_scams(synth_df, {})
    assert list(synth_proc.columns) == CANONICAL_COLUMNS
    s_row = synth_proc.iloc[0]
    assert s_row["record_id"] == "SYNTH-01"
    assert s_row["channel"] == "chat"
    assert bool(s_row["is_synthetic"]) is True
    assert s_row["fraudulent_intent"] == "Advance Fee"
    assert "[FINANCIAL_DATA]" in s_row["normalized_text"]
    assert "[PERSON_NAME]" in s_row["normalized_text"]
    assert "[ORGANIZATION]" in s_row["normalized_text"]
    assert "[You]: OK" in s_row["normalized_text"]

    # Legit mock
    legit_df = pd.DataFrame([{
        "id": "LEGIT-01",
        "text": "Meeting with [[NAME]] regarding [PRODUCT] and login [PASSWORD]",
        "email_subject": "Meeting",
        "email_body": "Meeting details",
        "label": 0,
        "legitimate_category": "financial_legitimate",
        "communication_type": "email",
        "scam_channel": "email",
        "source": "MeAJOR (trec5)",
        "source_url": "https://example.com",
        "source_license": "CC BY 4.0",
        "source_record_id": "REC-01",
        "synthetic": False,
    }])
    legit_proc = pipeline.process_real_fin_legit(legit_df, {})
    assert list(legit_proc.columns) == CANONICAL_COLUMNS
    l_row = legit_proc.iloc[0]
    assert l_row["record_id"] == "LEGIT-01"
    assert l_row["channel"] == "email"
    assert bool(l_row["is_synthetic"]) is False
    assert l_row["label"] == 0
    assert l_row["legitimate_category"] == "financial_legitimate"
    assert "[PERSON_NAME]" in l_row["normalized_text"]
    assert "[PRODUCT]" in l_row["normalized_text"]
    assert "[CREDENTIAL]" in l_row["normalized_text"]
