# Task 03: Canonical Dataset Engineering & Preprocessing Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Execution Status:** Completed & Cryptographically Verified  
**Total Records Processed:** 83,836 (100% of raw records preserved)

---

## 1. Executive Summary & Core Deliverables

This module transforms the three audited raw research datasets into a unified, research-ready canonical schema without modifying, truncating, or discarding any raw data.

### Processed Datasets Generated (`data/processed/`):
- `real_fin_scam_processed.csv`: **13,861 records** (all `label=1`, `is_synthetic=False`)
- `synthetic_financial_scams_processed.csv`: **7,643 records** (all `label=1`, `is_synthetic=True`)
- `real_fin_legit_processed.csv`: **62,332 records** (all `label=0`, `is_synthetic=False`)
- **Total Corpus Size:** **83,836 records**

### Preprocessing Reports Generated (`reports/preprocessing/`):
- `column_mapping.csv`: Complete field-by-field schema documentation.
- `channel_harmonization_stats.csv`: Empirical distribution of channels before and after mapping.
- `placeholder_normalization_stats.csv`: Token replacement counts and unresolved pattern tracking.
- `text_integrity_stats.csv`: Distributional metrics comparing raw vs normalized texts.
- `record_counts_and_labels.csv`: Record count, label, and cluster summary.
- `missing_values_summary.csv`: Column-by-column missing value breakdown.
- `integrity_verification.json`: Automated cryptographic and row-count verification.

---

## 2. Cryptographic Raw Data Verification

Raw datasets in `data/raw/` were verified against their audited SHA-256 reference hashes:

| Raw File | Verified SHA-256 Checksum | Row Count | Status |
| :--- | :--- | :--- | :--- |
| `real_fin_scam.csv` | `e00822c1e6469ea7e35fe7f2339c3fc557bdc13d13545cca4bda47385d3b4021` | 13,861 | **VERIFIED INTACT** |
| `synthetic_financial_scams.csv` | `8e708fa30aeaed63067db56c9b5c10e1cbb90b6fb8574c53882e32b3654240d7` | 7,643 | **VERIFIED INTACT** |
| `real_fin_legit.csv` | `6810244c341b8f484e19b16a6e13482b38877f5608debfb829874e145adac6bc` | 62,332 | **VERIFIED INTACT** |

---

## 3. Canonical Schema Architecture

The canonical schema preserves all original attributes while providing normalized text, harmonized channels, and duplicate cluster identifiers for group-aware splitting:

1. `record_id`: Stable unique identifier (`FIN-xxxxx`, `SYNTH_FIN_xxxx`, `MEAJOR-LEG-xxxxxx`, `SMS-LEG-xxxxxx`, `MENDELEY-LEG-xxxxxx`).
2. `original_text`: Exact raw text preserved verbatim.
3. `normalized_text`: Deterministically harmonized text with canonical entity tokens.
4. `label`: Binary classification target (`1` = scam, `0` = legitimate).
5. `channel`: Canonical medium (`email`, `sms`, `chat`, `notification`).
6. `original_channel`: Preserved raw channel string.
7. `is_email_gateway`: True for user-reported smishing originating via carrier email-to-SMS gateways.
8. `has_gateway_headers`: True for messages containing explicit carrier gateway transport headers.
9. `source`: Dataset provenance.
10. `source_url`: Upstream repository link.
11. `source_license`: Corpus license.
12. `source_record_id`: Upstream record ID before ingestion.
13. `is_synthetic`: Boolean indicator separating synthetic and real data.
14. `scam_subtype`: Scam taxonomy classification.
15. `fraudulent_intent`: Objective annotation (synthetic only).
16. `social_engineering_tactics`: Manipulation tactic annotation (synthetic only).
17. `legitimate_category`: Benign domain (`financial_legitimate` vs `general_legitimate`).
18. `email_subject`: Extracted email subject line.
19. `email_body`: Extracted email body payload.
20. `duplicate_cluster_id`: Near-duplicate cluster identifier; `None` for unclustered singletons.
21. Text integrity profiling: `char_count_original`, `word_count_original`, `char_count_normalized`, `word_count_normalized`, `placeholder_count_original`, `placeholder_count_normalized`.
22. Source-specific metadata: `generation_scenario`, `risk_or_safety_note`, `language`, `communication_type`.

---

## 4. Channel Harmonization & Gateway Transmission Findings

Harmonization resolved the compound `sms/email` channel in `real_fin_scam.csv`:
- **9,600 IMC25 Records:** Harmonized to canonical channel **`sms`** (`original_channel = 'sms/email'`). Only records with empirical carrier gateway transport evidence receive `is_email_gateway = True` (**24 verified records**). Ordinary mobile SMS messages receive `is_email_gateway = False` (**9,576 records**).
- **Gateway Transport Headers:**
  - In IMC25: Exactly **24 records** contain carrier gateway headers (`FRM:...`, `FROM:... SUBJ:... MSG:...`) and are flagged with `has_gateway_headers = True` and `is_email_gateway = True`.
  - In smishtank: Exactly **22 records** contain carrier gateway headers and are flagged with `has_gateway_headers = True` and `is_email_gateway = True`.
- **Other Channels:**
  - 57,662 legitimate emails + 3,765 real scam emails + 1,911 synthetic emails = **63,338 canonical `email` records**.
  - 4,670 legitimate SMS + 496 smishtank SMS + 9,600 IMC25 SMS + 1,911 synthetic SMS = **16,677 canonical `sms` records**.
  - 1,911 synthetic **`chat`** records.
  - 1,910 synthetic **`notification`** records.

---

## 5. Placeholder Harmonization & Bracket Artifact Cleaning

### Canonical Placeholder Ontology:
All anonymized entities were standardized into canonical square-bracket tokens:
- **`[URL]`**: `<URL>`, `[URL]`, `[LINK REDACTED]`
- **`[PHONE_NUMBER]`**: `<PHONE>`, `<PHONE_NUMBER>`, `[PHONE_NUMBER]`, `[FAX_NUMBER]`
- **`[EMAIL_ADDRESS]`**: `<EMAIL>`, `<EMAIL_ADDRESS>`, `[EMAIL_ADDRESS]`
- **`[PERSON_NAME]`**: `[NAME]`, `[USERNAME]`, `[INITIALS]`, `[Fictional Contact]`
- **`[ORGANIZATION]`**: `[ORGANIZATION]`, `[FICTIONAL ORGANIZATION]`, `[FICTITIOUS SERVICE DESK]`, `[FICTIONAL SERVICE]`
- **`[FINANCIAL_DATA]`**: `<US_BANK_NUMBER>`, `[FINANCIAL_INFO]`, `[AMOUNT REDACTED]`, `[ACCOUNT_NUMBER]`, `<CREDIT_CARD>`
- **`[IDENTIFIER]`**: `<US_DRIVER_LICENSE>`, `<US_SSN>`, `<US_PASSPORT>`, `<UK_NHS>`, `<MEDICAL_LICENSE>`, `[REFERENCE_NUMBER]`, `[CASE REDACTED]`
- **`[DATE_TIME]`**: `<DATE_TIME>`, `[DATE]`, `[TIME]`
- **`[LOCATION]`**: `<LOCATION>`, `[ADDRESS]`
- **`[CREDENTIAL]`**: `[PASSWORD]` (Targeted ontology extension for authentication secrets)
- **`[NAMED_ENTITY]`**: `<NAMED_ENTITY>` (Preserves general entity category from IMC25 without fabricating personal names)
- **`[NRP]`**: `<NRP>` (Standardizes SpaCy NORP demographic/national entity token to bracket style)
- **`[SYSTEM_ARTIFACT]`**: `<IP_ADDRESS>`, `[IP_ADDRESS]`, `[FILE_NAME]`, `[FILE_PATH]`, `[SYMBOL]`, `[VERSION]`, `[alternative HTML version deleted]`
- **`[PRODUCT]`**: Preserved domain entity from MeAJOR (retained to prevent converting commercial products into organizations).
- **`[You]`**: Preserved dialogue turn marker in synthetic chat transcripts.

### Nested Bracket Artifact Cleaning:
- Redundant nested brackets (e.g. `[[[[[PRODUCT]]]]]`, `[[NAME]]`, `<<[FILE_NAME]>>`) were safely collapsed to canonical tokens.
- Natural language bracketed phrases in Nigerian fraud emails (e.g. `[Flight AF4590]`, `[Direct]`, `[heir]`) were preserved intact rather than arbitrarily forced into system artifact categories.
- Normalization was verified to be strictly deterministic and idempotent: $f(f(x)) = f(x)$.

---

## 6. Duplicate Cluster Integration & Data Leakage Prevention

Near-duplicate connected components from Task 02 were mapped to `duplicate_cluster_id`:
- **`real_fin_scam`**: **3,206 records** mapped to 1,217 clusters (max size: 18).
- **`synthetic_financial_scams`**: **345 records** mapped to 130 clusters (max size: 4).
- **`real_fin_legit`**: **4,005 records** mapped to 1,334 clusters (max size: 166).
- **Total Records Clustered:** **7,556 records**.
- **Unclustered Records:** **76,280 singletons** receive `duplicate_cluster_id = None`.

> **Group-Aware Splitting Directive:**  
> When performing dataset partitioning in future tasks, splitting MUST be grouped by `duplicate_cluster_id` (treating `None` as independent single-record groups) to prevent near-duplicate template leakage across train/validation/test sets.

---

## 7. Transformer Tokenizer Profiling & Windowing Guidance

During canonical preprocessing, all texts were preserved in full without truncation:
- **Short Messages (<10 chars):** 30 records preserved for channel-specific SMS evaluation.
- **Long Messages (>10,000 chars):** 25 records preserved in full (max length: 121,724 characters / 23,486 words in `FIN-00350`).

### Recommendations for Future Transformer Tokenization:
1. Standard Transformer tokenizers truncate at 512 tokens. For short SMS and chat messages (median: 22–47 words), this accommodates the entire message with zero truncation loss.
2. For long email records (>512 tokens):
   - A naive head-only truncation discards the closing signature, return contact details, and payment instructions.
   - We recommend implementing a **dual-window tokenization** (first 256 tokens + last 256 tokens) or hierarchical segment pooling during feature extraction.
