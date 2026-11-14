# Canonical Preprocessing Pipeline & Unified Schema Specification

## 1. Pipeline Overview & Design Principles

The preprocessing and harmonization pipeline (`src/preprocessing/`) standardizes three disparate raw research datasets into an integrated, research-ready benchmark while strictly preserving data integrity:

1. **Strict Immutability:** Raw CSV files in `data/raw/` are strictly read-only. Their SHA-256 hashes are verified before and after pipeline execution.
2. **Text Verbatim Preservation:** Original raw text is preserved untouched in `original_text`. All cleaning and normalization produce derived fields (`normalized_text`).
3. **No Information Fabrication:** Missing metadata is recorded as null/empty, never fabricated.
4. **Deterministic Normalization:** Multi-pass regex normalizers are idempotent ($f(f(x)) = f(x)$) and mathematically verified to prevent accidental word deletion.

---

## 2. Canonical 30-Column Dataset Schema

Every processed dataset (`data/processed/*.csv`) conforms to this standardized schema:

| Column Name | Data Type | Nullable | Description & Research Semantics |
| :--- | :---: | :---: | :--- |
| `record_id` | String | No | Globally unique identifier (e.g. `FIN-00001`, `SYNTH-00001`, `MEAJOR-LEG-000001`). |
| `original_text` | String | No | Raw, unedited source message text preserved verbatim. |
| `normalized_text` | String | No | Cleaned, placeholder-standardized, whitespace-normalized message text. |
| `label` | Integer | No | Ground-truth binary classification: `1` = Scam, `0` = Legitimate. |
| `channel` | String | No | Canonical communication channel: `email`, `sms`, `chat`, or `notification`. |
| `original_channel` | String | No | Upstream reported channel (e.g. `sms/email`, `email`, `sms`). |
| `is_email_gateway` | Boolean | No | True **only** when empirical gateway transport headers are present. |
| `has_gateway_headers`| Boolean | No | True if carrier gateway signatures (`FRM:`, `FROM:`, `SUBJ:`, `MSG:`) exist. |
| `source` | String | No | Upstream origin dataset or corpus name. |
| `source_url` | String | Yes | Published source link, Zenodo DOI, or repository URL. |
| `source_license` | String | Yes | Upstream distribution license (e.g. CC BY 4.0, Public Domain). |
| `source_record_id` | String | Yes | Original identifier assigned by upstream collectors. |
| `is_synthetic` | Boolean | No | True for synthetic generation, False for real-world empirical data. |
| `scam_subtype` | String | Yes | Granular scam category (populated in synthetic corpus; 13 subtypes). |
| `fraudulent_intent` | String | Yes | Underlying criminal goal (e.g. `induce a payment`, `obtain sensitive information`). |
| `social_engineering_tactics` | String | Yes | JSON array of evidenced psychological manipulation tactics. |
| `legitimate_category` | String | Yes | `financial_legitimate` or `general_legitimate` (legitimate corpus). |
| `email_subject` | String | Yes | Extracted email subject line where available. |
| `email_body` | String | Yes | Extracted email body text where available. |
| `duplicate_cluster_id`| String | Yes | Indivisible MinHash LSH duplicate cluster identifier (e.g. `REAL_FIN_SCAM_C0001`). |
| `char_count_original` | Integer | No | Character count of `original_text`. |
| `word_count_original` | Integer | No | Whitespace-tokenized word count of `original_text`. |
| `char_count_normalized` | Integer | No | Character count of `normalized_text`. |
| `word_count_normalized` | Integer | No | Whitespace-tokenized word count of `normalized_text`. |
| `placeholder_count_original` | Integer | No | Frequency of placeholder tokens detected in raw text. |
| `placeholder_count_normalized` | Integer | No | Frequency of canonical placeholder tokens in normalized text. |
| `generation_scenario` | String | Yes | Synthetic generation context scenario description. |
| `risk_or_safety_note` | String | Yes | Confirmation of fictional entity generation and PII redaction. |
| `language` | String | No | Language designation (`English`). |
| `communication_type` | String | No | High-level modality (`email`, `sms`, `instant_message`, `push_notification`). |

---

## 3. Semantic Placeholder Ontology & Harmonization

Upstream anonymization delimiters (`<...>` and `[...]`) are standardized to square brackets (`[...]`) while preserving semantic fidelity:

| Original Raw Tokens | Canonical Token | Upstream Scope & Semantic Definition |
| :--- | :--- | :--- |
| `<NAMED_ENTITY>` | `[NAMED_ENTITY]` | IMC25 catch-all for banks, payment apps, platforms, and persons. |
| `[You]` | `[You]` | Synthetic dialogue recipient turn marker; preserved verbatim. |
| `[PASSWORD]`, `<password>` | `[CREDENTIAL]` | Authentication secrets targeted in phishing attacks. |
| `<NRP>` | `[NRP]` | SpaCy NORP demographic, nationality, and political entities. |
| `[PRODUCT]` | `[PRODUCT]` | Financial banking products, account types, and loan facilities. |
| `[LINK REDACTED]`, `<URL>` | `[URL]` | Web addresses, hyperlinks, and phishing domains. |
| `[PHONE_NUMBER]`, `<PHONE>` | `[PHONE_NUMBER]` | Telephone numbers and call-back targets. |
| `[AMOUNT]`, `[FINANCIAL_DATA]` | `[AMOUNT]` | Currencies, transaction amounts, and fee claims. |
| `[PERSON_NAME]`, `[NAME]` | `[PERSON_NAME]` | Anonymized individual personal names. |
| `[ORGANIZATION]`, `[COMPANY]`| `[ORGANIZATION]` | Commercial enterprises, corporations, and institutions. |

---

## 4. Execution & Pipeline Driver

To regenerate canonical processed datasets from raw inputs:
```powershell
.\.venv\Scripts\python.exe main.py --preprocess
```
Artifacts are generated in:
- `data/processed/real_fin_scam_processed.csv` (13,861 records)
- `data/processed/real_fin_legit_processed.csv` (62,332 records)
- `data/processed/synthetic_financial_scams_processed.csv` (7,643 records)
- Statistical summaries in `reports/preprocessing/`.
