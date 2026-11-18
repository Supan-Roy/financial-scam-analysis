"""
Automated Validation and Integrity Test Suite for Synthetic Financial Scams Version 3 Corrected.

Verifies:
  1. File existence, row counts, and schema conformance for raw and processed datasets.
  2. Mathematical scenario-family isolation across Train, Validation, and Test partitions (0 leakage).
  3. Near-duplicate cluster isolation (0 cluster leakage across splits).
  4. Generation template ID isolation (0 template leakage).
  5. Exact subtype representation and balance (480 Train, 60 Val, 60 Test for all 13 subtypes).
  6. Fraudulent intent and communication channel representation across all partitions.
  7. Semantic tactic mapping integrity (no fall-through to urgency strings in reward tactics).
  8. 100% Character-level evidence substring slicing accuracy.
  9. Safe synthetic URL compliance (.example domains) and absence of prohibited meta-tokens.
  10. Strict parity between raw and processed candidate datasets.
  11. Notification word count bounds (realistic lockscreen alerts: 14-28 words).
"""

import json
import re
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "synthetic_financial_scams_v3_corrected.csv"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed" / "synthetic_financial_scams_v3_corrected_processed.csv"

CANONICAL_SUBTYPES = [
    "account_verification",
    "card_transaction_alert",
    "refund_chargeback",
    "invoice_payment_request",
    "loan_offer",
    "investment_crypto",
    "prize_reward",
    "tax_payment",
    "job_task_commission",
    "romance_financial_manipulation",
    "family_emergency_request",
    "recovery_support",
    "charity_donation",
]

CANONICAL_INTENTS = [
    "induce_payment_or_transfer",
    "obtain_credentials_or_codes",
    "induce_fraudulent_investment",
    "obtain_personal_or_financial_information",
    "gain_account_or_device_access",
]

CANONICAL_TACTICS = [
    "urgency",
    "fear_or_threat",
    "reward_or_benefit",
    "authority_impersonation",
    "trust_exploitation",
    "false_legitimacy",
    "scarcity",
    "emotional_manipulation",
    "secrecy",
]


@pytest.fixture(scope="module")
def raw_df():
    assert RAW_PATH.exists(), f"Raw dataset not found at {RAW_PATH}"
    df = pd.read_csv(RAW_PATH)
    return df


@pytest.fixture(scope="module")
def processed_df():
    assert PROCESSED_PATH.exists(), f"Processed dataset not found at {PROCESSED_PATH}"
    df = pd.read_csv(PROCESSED_PATH)
    return df


def test_file_existence_and_row_counts(raw_df, processed_df):
    """Verifies row counts, column counts, and split record ratios."""
    assert len(raw_df) == 7800, f"Expected 7,800 raw rows, got {len(raw_df)}"
    assert len(processed_df) == 7800, f"Expected 7,800 processed rows, got {len(processed_df)}"
    assert raw_df.shape[1] == 16, f"Expected 16 raw columns, got {raw_df.shape[1]}"
    assert processed_df.shape[1] == 36, f"Expected 36 processed columns, got {processed_df.shape[1]}"

    part_counts = processed_df["split_partition"].value_counts().to_dict()
    assert part_counts["train"] == 6240, f"Expected 6,240 train records, got {part_counts.get('train')}"
    assert part_counts["val"] == 780, f"Expected 780 val records, got {part_counts.get('val')}"
    assert part_counts["test"] == 780, f"Expected 780 test records, got {part_counts.get('test')}"


def test_scenario_family_isolation(processed_df):
    """Verifies that 100% of scenario families reside in exactly one partition (zero leakage)."""
    assert processed_df["scenario_family"].nunique() == 104, "Expected exactly 104 unique scenario families"

    scen_part = processed_df.groupby("scenario_family")["split_partition"].nunique()
    leaked_families = scen_part[scen_part > 1]
    assert len(leaked_families) == 0, f"Found {len(leaked_families)} leaking scenario families: {leaked_families}"

    train_scens = set(processed_df[processed_df["split_partition"] == "train"]["scenario_family"])
    val_scens = set(processed_df[processed_df["split_partition"] == "val"]["scenario_family"])
    test_scens = set(processed_df[processed_df["split_partition"] == "test"]["scenario_family"])

    assert len(train_scens) == 78, f"Expected 78 train families, got {len(train_scens)}"
    assert len(val_scens) == 13, f"Expected 13 val families, got {len(val_scens)}"
    assert len(test_scens) == 13, f"Expected 13 test families, got {len(test_scens)}"

    assert len(train_scens.intersection(val_scens)) == 0, "Train-Val scenario family overlap detected"
    assert len(train_scens.intersection(test_scens)) == 0, "Train-Test scenario family overlap detected"
    assert len(val_scens.intersection(test_scens)) == 0, "Val-Test scenario family overlap detected"


def test_near_duplicate_cluster_isolation(processed_df):
    """Verifies that all near-duplicate clusters are strictly confined to single partitions."""
    clustered = processed_df[processed_df["duplicate_cluster_id"].notna()]
    assert len(clustered) > 0, "Expected clustered near-duplicates"

    clust_part = clustered.groupby("duplicate_cluster_id")["split_partition"].nunique()
    leaked_clusters = clust_part[clust_part > 1]
    assert len(leaked_clusters) == 0, f"Found {len(leaked_clusters)} leaking near-duplicate clusters"


def test_template_id_isolation(processed_df):
    """Verifies that generation template IDs do not cross partition boundaries."""
    tpl_part = processed_df.groupby("generation_template_id")["split_partition"].nunique()
    leaked_templates = tpl_part[tpl_part > 1]
    assert len(leaked_templates) == 0, f"Found {len(leaked_templates)} leaking templates: {leaked_templates}"


def test_subtype_representation_and_balance(processed_df):
    """Verifies that all 13 canonical subtypes are represented in Train, Val, and Test."""
    ct = pd.crosstab(processed_df["scam_subtype"], processed_df["split_partition"])
    assert len(ct) == 13, f"Expected 13 subtypes, found {len(ct)}"

    for sub in CANONICAL_SUBTYPES:
        assert sub in ct.index, f"Subtype {sub} missing from crosstab"
        assert ct.loc[sub, "train"] == 480, f"Subtype {sub} train count != 480"
        assert ct.loc[sub, "val"] == 60, f"Subtype {sub} val count != 60"
        assert ct.loc[sub, "test"] == 60, f"Subtype {sub} test count != 60"


def test_intent_and_channel_coverage(processed_df):
    """Verifies all 5 intents and 4 channels are represented across all partitions."""
    intent_ct = pd.crosstab(processed_df["fraudulent_intent"], processed_df["split_partition"])
    assert len(intent_ct) == 5, f"Expected 5 intents, found {len(intent_ct)}"
    for intent in CANONICAL_INTENTS:
        assert intent in intent_ct.index
        for part in ["train", "val", "test"]:
            assert intent_ct.loc[intent, part] > 0, f"Intent {intent} missing in {part}"

    chan_ct = pd.crosstab(processed_df["channel"], processed_df["split_partition"])
    assert len(chan_ct) == 4, f"Expected 4 channels, found {len(chan_ct)}"
    for chan in ["sms", "email", "chat", "notification"]:
        assert chan in chan_ct.index
        for part in ["train", "val", "test"]:
            assert chan_ct.loc[chan, part] > 0, f"Channel {chan} missing in {part}"


def test_tactic_semantics_and_fallbacks(processed_df):
    """Verifies that tactic annotations do not contain fall-through errors."""
    for idx, row in processed_df.iterrows():
        t_ev = json.loads(row["tactics_evidence"])
        for item in t_ev:
            tactic = item["tactic"]
            span_text = item["span_text"]
            assert tactic in CANONICAL_TACTICS, f"Unknown tactic: {tactic}"
            if tactic == "reward_or_benefit":
                assert "Immediate response required" not in span_text, (
                    f"Urgency fallback found in reward_or_benefit for {row['record_id']}: {span_text}"
                )


def test_character_span_slices(processed_df):
    """Verifies 100% exact substring match for evidence spans across a large sample."""
    sample = processed_df.sample(n=500, random_state=42)
    for idx, row in sample.iterrows():
        orig_text = row["original_text"]

        # Primary intent evidence
        p_ev = json.loads(row["primary_intent_evidence"])
        p_text = orig_text[p_ev["start_char"]:p_ev["end_char"]]
        assert p_text == p_ev["span_text"], (
            f"Intent slice mismatch for {row['record_id']}: '{p_text}' != '{p_ev['span_text']}'"
        )

        # Narrative evidence
        n_ev = json.loads(row["narrative_evidence"])
        n_text = orig_text[n_ev["start_char"]:n_ev["end_char"]]
        assert n_text == n_ev["span_text"], (
            f"Narrative slice mismatch for {row['record_id']}: '{n_text}' != '{n_ev['span_text']}'"
        )

        # Tactics evidence
        t_ev = json.loads(row["tactics_evidence"])
        for t_item in t_ev:
            t_text = orig_text[t_item["start_char"]:t_item["end_char"]]
            assert t_text == t_item["span_text"], (
                f"Tactic slice mismatch for {row['record_id']}: '{t_text}' != '{t_item['span_text']}'"
            )


def test_safe_synthetic_representations(processed_df):
    """Verifies absence of prohibited meta-tokens and RFC 2606 domain compliance."""
    url_pattern = re.compile(r'https?://([^\s/\'\"<>]+)')
    prohibited_tokens = ["NOTICE ", "fictional", "synthetic financial scam", "Task: Rebuild"]

    for idx, row in processed_df.iterrows():
        text = row["original_text"]
        for p in prohibited_tokens:
            assert p not in text, f"Prohibited token '{p}' found in {row['record_id']}: {text}"

        urls = url_pattern.findall(text)
        for u in urls:
            assert u.endswith(".example"), f"Non-RFC 2606 URL domain found in {row['record_id']}: {u}"


def test_raw_processed_parity(raw_df, processed_df):
    """Verifies row-by-row parity between raw and processed candidate datasets."""
    assert (raw_df["id"].values == processed_df["record_id"].values).all(), "Record ID mismatch between raw and processed"
    assert (raw_df["text"].values == processed_df["original_text"].values).all(), "Text mismatch between raw and processed"
    assert (raw_df["phishing_type"].values == processed_df["scam_subtype"].values).all(), "Subtype mismatch"
    assert (raw_df["fraudulent_intent"].values == processed_df["fraudulent_intent"].values).all(), "Intent mismatch"
    assert (raw_df["social_engineering_tactics"].values == processed_df["social_engineering_tactics"].values).all(), "Tactics mismatch"


def test_notification_length_bounds(processed_df):
    """Verifies that all notifications are concise lockscreen push notifications (14-28 words)."""
    notifs = processed_df[processed_df["channel"] == "notification"]
    assert len(notifs) > 0, "Expected notification records"
    for idx, row in notifs.iterrows():
        w_cnt = len(row["original_text"].split())
        assert 14 <= w_cnt <= 28, f"Notification word count {w_cnt} outside 14-28 range: {row['original_text']}"
