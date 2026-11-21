# Synthetic Financial-Scam Research Dataset (Version 3.1)

## 1. Active Dataset: Version 3.1

The active programmatic synthetic corpus is **`synthetic_financial_scams_v3_1.csv`** (and processed [`data/processed/synthetic_financial_scams_v3_1_processed.csv`](../data/processed/synthetic_financial_scams_v3_1_processed.csv)).

- **Total Records:** Exactly 7,800 records (exactly 600 records per subtype across 13 canonical subtypes).
- **Group Isolation:** 104 scenario families partitioned into Train (83 families / 6,240 records), Validation (10 families / 780 records), and Test (11 families / 780 records) with **0.0% scenario-family leakage** and **0.0% cluster leakage**.
- **Character-Level Evidence Spans:** 100.0% exact substring match verification across all 7,800 records for `primary_intent_evidence`, `narrative_evidence`, and `tactics_evidence`.
- **Channels:** SMS (2,752), Email (2,504), Chat (1,724), and Notification (820).
- **Notification Modality Balance:** Resolves the artificial link monopoly in notifications:
  - 416 notifications with safe RFC 2606 `.example` URLs (50.73%).
  - 404 notifications without URLs (app opening / status alerts) (49.27%).
- **Intent-Conditioned Notification Generation:** Every notification expresses intent-specific phrasing and evidence, completely resolving the intent decoupling bug identified in earlier versions.
- **Safety & RFC 2606:** 100% of URLs strictly use reserved `.example` domains. 0 prohibited meta-tokens (`fictional`, `NOTICE <N>:`).
- **Audit Reports:** [`reports/dataset_audits/synthetic_v3_1_validation.md`](../reports/dataset_audits/synthetic_v3_1_validation.md).

*Historical Note:* Prior iterations (Version 1: 7,643 records, Version 2, Version 3, and Version 3 Corrected) have been archived to `data/archive/synthetic_iterations/` for scientific provenance.

---

## 2. Research Purpose

The synthetic corpus provides controlled, leak-free supervision for multi-level financial scam narrative detection, fraudulent intent analysis, and social-engineering pattern recognition. It is evaluated separately from the real-world binary benchmark and serves as the training foundation for multi-level classifiers.

---

## 3. Annotation Taxonomy & Schema Definitions

- `record_id`: Unique identifier (e.g., `SYNTH-V3-00001`).
- `scam_subtype` / `phishing_type`: 13 canonical scam subtypes.
- `channel` / `scam_channel`: `email`, `sms`, `chat`, or `notification`.
- `fraudulent_intent`: 5 canonical intent classes.
- `social_engineering_tactics`: JSON list containing verified tactics present in the message.
- `primary_intent_evidence`: Verbatim substring evidence supporting the assigned intent.
- `tactics_evidence`: JSON array containing `{tactic, span_text, start, end}` for each tactic.
- `narrative_evidence`: Verbatim substring evidence of the core scam narrative.
- `split_partition`: Group-aware split (`train`, `val`, `test`).
- `duplicate_cluster_id`: MinHash LSH duplicate cluster identifier.

---

## 4. Multi-Level Target Distributions

### A. Subtypes (600 records each = 7,800 total)
- `account_verification`: 600
- `card_transaction_alert`: 600
- `refund_chargeback`: 600
- `invoice_payment_request`: 600
- `loan_offer`: 600
- `investment_crypto`: 600
- `prize_reward`: 600
- `tax_payment`: 600
- `job_task_commission`: 600
- `romance_financial_manipulation`: 600
- `family_emergency_request`: 600
- `recovery_support`: 600
- `charity_donation`: 600

### B. Fraudulent Intent (5 Classes)
- `induce_payment_or_transfer`: 4,772 records (61.18%)
- `obtain_personal_or_financial_information`: 1,538 records (19.72%)
- `obtain_credentials_or_codes`: 796 records (10.21%)
- `induce_fraudulent_investment`: 482 records (6.18%)
- `gain_account_or_device_access`: 212 records (2.72%)

### C. Social Engineering Tactics (9 Classes)
- `urgency`: 4,008 records (51.38%)
- `false_legitimacy`: 3,858 records (49.46%)
- `reward_or_benefit`: 2,059 records (26.40%)
- `authority_impersonation`: 1,939 records (24.86%)
- `trust_exploitation`: 1,468 records (18.82%)
- `fear_or_threat`: 1,180 records (15.13%)
- `emotional_manipulation`: 904 records (11.59%)
- `scarcity`: 804 records (10.31%)
- `secrecy`: 625 records (8.01%)

---

## 5. Partition Integrity & Isolation

| Split | Scenario Families | Records | % of Dataset | Partition Leakage |
| :--- | :---: | :---: | :---: | :---: |
| **Train** | 83 | 6,240 | 80.00% | **0.0% (Zero)** |
| **Validation** | 10 | 780 | 10.00% | **0.0% (Zero)** |
| **Test** | 11 | 780 | 10.00% | **0.0% (Zero)** |
| **Total** | **104** | **7,800** | **100.00%** | **Strictly Disjoint** |

---

## 6. Usage & Generalization Experiments

In [`notebooks/04_synthetic_multilevel_baselines.ipynb`](../notebooks/04_synthetic_multilevel_baselines.ipynb), models trained and evaluated on V3.1 achieved high in-distribution performance:
- Scam Subtype Accuracy: **96.92%**
- Fraudulent Intent Accuracy: **98.21%**
- Social-Engineering Multi-Label Micro-F1: **98.73%**

However, in [`notebooks/05_llm_authored_generalization_evaluation.ipynb`](../notebooks/05_llm_authored_generalization_evaluation.ipynb), cross-generation evaluation demonstrated that V3.1-only models experience significant generalization degradation on independently reasoned LLM-authored scam messages, motivating combined training regimes and contextual Transformer modeling.
