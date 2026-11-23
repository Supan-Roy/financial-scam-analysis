# Dataset Card: LLM-Authored Financial Scam Dataset

## 1. Dataset Overview

- **Dataset Name:** `llm_authored_financial_scams.csv` (Processed: `llm_authored_financial_scams_processed.csv`)
- **Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*
- **Total Records:** 2,730
- **Primary Task:** Out-of-distribution generalization testing and multi-level financial scam narrative modeling across scam subtypes, fraudulent intents, and social-engineering tactics.
- **Generation Method:** Contextual LLM reasoning via `gemini-3.8-flash-low` executed through the local Antigravity CLI engine.
- **Safety Standard:** 100% fictional institutions, reserved RFC 2606 domains (`.example`), and synthetic telephone/identifier placeholders.

---

## 2. Volume Justification & Architecture

The dataset contains exactly **2,730 records**, derived from balanced multi-dimensional coverage across the framework's analytical dimensions:

$$\text{Total Records} = 13 \text{ Subtypes} \times 10 \text{ Scenario Families} \times 21 \text{ Records} = 2,730 \text{ Records}$$

- **13 Canonical Scam Subtypes:** 210 records per subtype.
- **130 Grounded Scenario Families:** 21 records per scenario family.
- **7-Style Balance:** Exactly 3 records per writing style per scenario family ($7 \times 3 = 21$ records/family $\rightarrow$ 390 records per writing style).
- **Group-Aware Partitioning (Scenario Family Isolated):**
  - **Train:** 8 families per subtype $\times$ 21 records = **168 records/subtype** $\rightarrow$ **2,184 records (80.0%)** across 104 families.
  - **Validation:** 1 family per subtype $\times$ 21 records = **21 records/subtype** $\rightarrow$ **273 records (10.0%)** across 13 families.
  - **Test:** 1 family per subtype $\times$ 21 records = **21 records/subtype** $\rightarrow$ **273 records (10.0%)** across 13 families.
  - **Partition Leakage:** **0.0% scenario family overlap** across Train, Validation, and Test.

---

## 3. Writing Style Taxonomy

The dataset incorporates an explicit, controlled 7-style taxonomy ($390$ records / $14.29\%$ each):

| Writing Style | Records | % | Mean Words | Word Range | Mean Chars | Style Description |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `direct_terse` | 390 | 14.29% | 26.1 | 14 – 45 | 218.2 | Ultra-concise, urgent bullet or notification style, minimal pleasantries |
| `casual_informal` | 390 | 14.29% | 54.1 | 26 – 107 | 340.2 | Relaxed grammar, colloquial phrasing, informal punctuation, abbreviations |
| `sophisticated_formal` | 390 | 14.29% | 67.7 | 22 – 169 | 549.8 | High-register vocabulary, elaborate syntax, polished prose |
| `dialogue_interactive` | 390 | 14.29% | 82.3 | 26 – 163 | 535.9 | Conversational chat flow, back-and-forth prompt-and-response pacing |
| `corporate_institutional` | 390 | 14.29% | 85.3 | 24 – 156 | 676.0 | Formal bureau/department framing, statutory citations, legalistic structure |
| `professional_neutral` | 390 | 14.29% | 88.9 | 34 – 141 | 689.2 | Standard business email tone, balanced corporate correspondence |
| `conversational_personal` | 390 | 14.29% | 104.6 | 45 – 185 | 693.3 | Warm, relatable, storytelling, interpersonal emotional appeal |

---

## 4. Channel Representations

| Channel | Message Count | Percentage | Mean Words | Median Words | Word Range |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `email` | 1,145 | 41.94% | 101.4 | 99 | 57 – 185 |
| `notification` | 659 | 24.14% | 32.5 | 31 | 14 – 76 |
| `chat` | 543 | 19.89% | 82.1 | 81 | 35 – 163 |
| `sms` | 383 | 14.03% | 42.7 | 40 | 16 – 96 |

### Notification Delivery Modality Balance
- **Notifications with `.example` URL Link:** 308 records (46.74%)
- **Notifications without URL (App open / status alert):** 351 records (53.26%)
- *Status:* Resolves the artificial link monopoly, providing a natural mobile alert distribution.

---

## 5. Multi-Level Annotations & Evidence Verification

### Level 1: Scam Subtypes (13 Classes, 210 records each)
`account_verification`, `card_transaction_alert`, `charity_donation`, `family_emergency_request`, `investment_crypto`, `invoice_payment_request`, `job_task_commission`, `loan_offer`, `prize_reward`, `recovery_support`, `refund_chargeback`, `romance_financial_manipulation`, `tax_payment`.

### Level 2: Fraudulent Intents (5 Classes)
- `induce_payment_or_transfer`: 1,247 records (45.68%)
- `obtain_credentials_or_codes`: 582 records (21.32%)
- `obtain_personal_or_financial_information`: 506 records (18.53%)
- `gain_account_or_device_access`: 228 records (8.35%)
- `induce_fraudulent_investment`: 167 records (6.12%)
- **Character Offset Verification:** 100.0% exact substring match (`original_text[start:end] == primary_intent_evidence`). Mismatches: **0 / 2,730**.

### Level 3: Social Engineering Tactics (9 Classes)
- `false_legitimacy`: 1,857 records (68.02%)
- `urgency`: 1,743 records (63.85%)
- `reward_or_benefit`: 1,046 records (38.32%)
- `authority_impersonation`: 971 records (35.57%)
- `fear_or_threat`: 883 records (32.34%)
- `trust_exploitation`: 802 records (29.38%)
- `emotional_manipulation`: 554 records (20.29%)
- `scarcity`: 300 records (10.99%)
- `secrecy`: 40 records (1.47%)
- **Tactics Span Verification:** 100.0% exact substring match across all 8,148 annotated spans (`original_text[start:end] == span_text`). Mismatches: **0 / 8,148**.

---

## 6. Real-World Missingness Analysis

- **Supervisory Targets:** 0.0% missing (`record_id`, `original_text`, `normalized_text`, `scam_subtype`, `fraudulent_intent`, `social_engineering_tactics`, `writing_style`, `channel`, `split_partition`).
- **Auxiliary Metadata:** Controlled missingness:
  - `optional_scenario_description`: 14.76% missing (403 records)
  - `urgency_rating`: 13.99% missing (382 records)
  - `secondary_channel_source`: 15.49% missing (423 records)
  - `email_subject`: 58.06% missing (1,585 records; 100% present for email, 100% null for SMS/chat/notification).

---

## 7. Deduplication & MinHash LSH

- **Configuration:** 64 permutation hashes, 16 bands $\times$ 4 rows, Jaccard threshold $\ge 0.85$ over word 3-shingles.
- **Clustered Near-Duplicates:** 0 records (0.00%).
- **Distinct Duplicate Clusters:** 0.
- **Result:** Contextual LLM reasoning produced completely unique sentence structures with zero template repetition.

---

## 8. Usage in Generalization Evaluation (Notebook 05)

The dataset serves as the independent evaluation benchmark in [`notebooks/05_llm_authored_generalization_evaluation.ipynb`](../notebooks/05_llm_authored_generalization_evaluation.ipynb), revealing:
1. **Generalization Gap:** Programmatic V3.1-only models experience significant performance drops when evaluated on LLM-authored communications:
   - Scam Subtype Macro F1 drops from **0.9962** on V3.1 to **0.4819** on LLM-authored (-51.43%).
   - Fraudulent Intent Macro F1 drops from **0.9960** on V3.1 to **0.5354** on LLM-authored (-46.06%).
   - Social Engineering Tactic Macro F1 drops from **0.9941** on V3.1 to **0.2046** on LLM-authored (-78.95%).
2. **Cross-Generation Resilience:** Combined training (V3.1 + LLM) restores Macro F1 on LLM-authored data to **0.7099** (Subtype), **0.6716** (Intent), and **0.6667** (Tactics) while retaining **0.9962 / 0.9891 / 0.9746** on V3.1.
3. **Size-Controlled Robustness:** Even when total training samples are held equal to V3.1-only, mixed generation training yields **0.7060 / 0.6559 / 0.6576** Macro F1 on the LLM-authored distribution.

---

## 9. Role in Binary Classification & Augmentation (Notebook 08)

In [`notebooks/08_synthetic_data_augmentation_evaluation.ipynb`](../notebooks/08_synthetic_data_augmentation_evaluation.ipynb), the 2,730 LLM-authored records (mapped to binary scam label `1`) were evaluated within a contextual DistilBERT binary classification framework:

1. **Cross-Distribution Transfer (Model A):** When evaluated on the held-out LLM test partition (273 records) paired with real legitimate test messages, the real-only DistilBERT model achieved **99.8309% accuracy**, **97.4638% precision**, and **98.5348% recall** (269/273 detected). The 4 missed scams represented subtle charity appeals and invoice payment requests lacking overt urgency markers.
2. **Synthetic-Only Risk Diagnostic (Experiment B):** Utilizing 2,184 LLM-authored and 6,240 V3.1 synthetic scams as the sole fraudulent training signal yielded 100% validation scores, but resulted in an 88.30% false-negative rate on real scams (11.70% recall), confirming that synthetic diversity cannot replace real fraud narratives when source and label are correlated.
3. **Combined Real + Synthetic Augmentation (Experiment C):** Combining LLM-authored scams, V3.1 scams, and real scam data successfully preserved real-world detection capability (**99.8819% accuracy**, **99.8556% scam recall**, **99.8017% macro F1** across 7,618 test records), showing complete robustness with no catastrophic interference.

*For full experimental details, see [`reports/dataset_audits/synthetic_data_augmentation_evaluation_report.md`](../reports/dataset_audits/synthetic_data_augmentation_evaluation_report.md).*

