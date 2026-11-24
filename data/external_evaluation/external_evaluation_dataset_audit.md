# External Financial Scam Evaluation Dataset Construction & Quality Audit Report

**Research Project Title:**  
*Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*

**Report Date:** November 2026  
**Module:** Evaluation Dataset Preparation & Quality Verification  
**Canonical Model Evaluated:** Real-Only Fine-Tuned DistilBERT Binary Classifier (`notebooks/06_transformer_based_modeling.ipynb`)  
**Target Output Directory:** `data/external_evaluation/`  

---

## 1. Executive Summary

This report documents the rigorous forensic curation, deduplication, schema alignment, and programmatic validation of an expanded external evaluation dataset for financial scam classification.

### The Research Problem
Our existing real benchmark contains 76,193 digital communications partitioned into train (60,957), validation (7,618), and test (7,618) splits. While our saved fine-tuned DistilBERT binary classifier achieves near-perfect identically distributed test performance (99.78% accuracy, 99.40% F1-score), previous diagnostic audits identified two structural risks:
1. **Source Dependency:** Model predictions may exploit source-specific artifacts rather than semantic fraud intent.
2. **Channel–Class Confounding:** The legitimate class is 93.1% corporate/developer email (MeAJOR/TREC), while scam communications contain substantial mobile SMS smishing.

### Objective and Core Design
To assess true generalization, we constructed an expanded evaluation dataset combining:
1. **Newly verified, independently sourced real financial scam communications ($N = 792$)** curated from the Jose Nazario Phishing Corpus, the Mishra & Soni SMS Phishing Dataset, and the AbayomiAlli SMS Dataset, following forensic decontamination (excluding corrupt attacker loops, non-English payloads, and non-financial quota alerts).
2. **Our existing, untouched legitimate test partition ($N = 6,233$)** from `data/splits/test.csv` (`label == 0`).

```
                    EXPANDED EVALUATION DATASET ARCHITECTURE
                                    (N = 7,025)
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
[EXTERNAL SCAM COHORT]                                      [HELD-OUT LEGITIMATE TEST COHORT]
  Count: 792 records (11.27%)                                  Count: 6,233 records (88.73%)
  Origin: external_real_scam                                    Origin: existing_real_test_legitimate
  Label: 1 (Scam)                                               Label: 0 (Legitimate)
  Sources:                                                      Sources:
   • Jose Nazario Corpus (522 emails)                            • MeAJOR trec5 (2,727 emails)
   • Mishra & Soni (268 SMS)                                     • MeAJOR trec7 (1,926 emails)
   • AbayomiAlli (2 SMS)                                         • MeAJOR trec6 (1,113 emails)
                                                                 • UCI SMS Collection (451 SMS)
                                                                 • Mendeley Data V2 (16 emails)
```

---

## 2. Dataset Composition & Class Distribution

The primary generated evaluation dataset (`expanded_binary_external_test.csv`) contains **7,025 total records**. A balanced evaluation companion (`balanced_binary_external_test.csv`) provides **1,584 records** (792 scam, 792 legitimate sampled reproducibly with seed 42).

### Class & Channel Distribution (Expanded Dataset: $N = 7,025$)

| Communication Channel | Legitimate (`label = 0`) | Scam (`label = 1`) | Total Records | Class Ratio (% Scam) |
| :--- | :--- | :--- | :--- | :--- |
| **Email** | 5,766 | 522 | 6,288 | 8.30% |
| **SMS** | 467 | 270 | 737 | 36.63% |
| **Combined Total** | **6,233 (88.73%)** | **792 (11.27%)** | **7,025 (100.0%)** | **11.27%** |

### Breakdown by Originating Source

| Source Dataset | Communication Channel | Assigned Label | Record Count | Percentage of Corpus | Provenance & Lineage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MeAJOR (trec5)** | Email | 0 (Legit) | 2,727 | 38.82% | Held-out benchmark test partition |
| **MeAJOR (trec7)** | Email | 0 (Legit) | 1,926 | 27.42% | Held-out benchmark test partition |
| **MeAJOR (trec6)** | Email | 0 (Legit) | 1,113 | 15.84% | Held-out benchmark test partition |
| **Jose Nazario Phishing Corpus** | Email | 1 (Scam) | 522 | 7.43% | Verified external phishing honeypot (Zenodo 8339691) |
| **UCI SMS Spam Collection** | SMS | 0 (Legit) | 451 | 6.42% | Held-out benchmark test partition |
| **Mishra & Soni SMS Phishing** | SMS | 1 (Scam) | 268 | 3.82% | Verified external web OCR smishing (Mendeley f45bkkt8pr) |
| **Mendeley Data V2** | Email | 0 (Legit) | 16 | 0.23% | Held-out benchmark test partition |
| **AbayomiAlli SMS Dataset** | SMS | 1 (Scam) | 2 | 0.03% | Verified Nigerian mobile prize smishing |
| **Total** | -- | -- | **7,025** | **100.00%** | -- |

### Financial Scam Subtype Distribution ($N = 792$)

Every curated scam record was assigned a fine-grained scam subtype based on explicit semantic evidence in the narrative:

| Scam Subtype | Channel | Record Count | Percentage | Representative Entities & Modalities |
| :--- | :--- | :--- | :--- | :--- |
| `bank_impersonation` | Email | 280 | 35.35% | Chase, Wells Fargo, BofA, Citibank, Barclays, HSBC, USAA |
| `fake_prize_or_compensation` | SMS | 210 | 26.52% | Cash prize awards, PPI claims, lottery cheques requiring call/fee |
| `account_security_phishing` | Email | 82 | 10.35% | Unauthorized access notices, security updates, account lock warnings |
| `payment_service_phishing` | Email | 82 | 10.35% | PayPal dispute notices, unauthorized payments, billing updates |
| `bank_smishing` | SMS | 50 | 6.31% | BofA alerts, Barclays OTP, NatWest account locks, Paytm KYC blocks |
| `billing_invoice_scam` | Email | 34 | 4.29% | Overdue invoices, payment reconciliation requests, fake receipts |
| `card_verification_fraud` | Email | 25 | 3.16% | Debit/credit card suspension, card re-activation credential forms |
| `tax_refund_phishing` | Email | 17 | 2.15% | IRS and government tax refund credential theft forms |
| `tax_refund_smishing` | SMS | 8 | 1.01% | HMRC tax rebate SMS, COVID-19 relief fund smishing links |
| `money_transfer_fraud` | Email | 2 | 0.25% | Western Union, MoneyGram uncollected funds / transfer clearance |
| `payment_service_smishing` | SMS | 2 | 0.25% | Apple ID / Apple Pay suspension, Venmo security alerts |
| **Total External Scams** | -- | **792** | **100.00%** | -- |

---

## 3. Forensic Curation, Decontamination & Exclusion Audit

A total of **12,776 raw candidate records** across the three candidate corpora were audited at the individual record level. Every inclusion and exclusion decision is recorded in `external_scam_annotation_audit.csv`, with excluded records logged in `external_scam_exclusion_log.csv`.

```
Candidate Corpus Ingestion Funnel:
12,776 Audited Candidates 
   ├── 5,971 (Mishra & Soni) ──> 268 Curated (5,703 Excluded)
   ├── 5,240 (AbayomiAlli)    ──>   2 Curated (5,238 Excluded)
   └── 1,565 (Jose Nazario)   ──> 522 Curated (1,043 Excluded)
Total Curated External Scams: 792 records (6.20% yield)
Total Excluded Non-Eligible: 11,984 records (93.80%)
```

### Forensic Quality Decontamination Pass (Exclusion of Anomalous Records)

Following pre-evaluation forensic auditing, an additional **5 anomalous records** were excluded to guarantee rigorous dataset hygiene:
1. **Malformed Script Defect (`EXT-SCAM-00224` / `nazario_row_533`):**  
   Forensic analysis revealed an attacker mail-merge script defect containing **45,146 email addresses repeated twice** (1,023,605 characters, ~46,580 words, ~463,696 DistilBERT tokens). The substantive payload is a generic webmail password alert with zero financial content. Excluded under `excluded_malformed_script_defect`.
2. **Foreign-Language / Mixed-Language Records (English-Only Scope Enforcement):**  
   - `EXT-SCAM-00449` (`nazario_row_1230`): Corrupted payload concatenating an English Amex security lure with a duplicated French e-commerce order confirmation (`COMMANDE #11344 Votre commande est en route`). Excluded under `excluded_foreign_language`.
   - `EXT-SCAM-00450` (`nazario_row_1243`): PayPal security alert written 100% in German (`Wir haben ungewöhnliche Aktivitäten festgestellt!`). Excluded under `excluded_foreign_language`.
   - `EXT-SCAM-00485` (`nazario_row_1414`): Apple ID verification phish written 100% in German (`Liebes Apple-Mitglied IDENTITÄTSÜBERPRÜFUNG ERFORDERLICH`). Excluded under `excluded_foreign_language`.
3. **Non-Financial IT Webmail Quota Alert (`EXT-SCAM-00106` / `nazario_row_237`):**  
   Generic email mailbox storage exhaustion alert (`"mailbox 95.77% full, verify email ID to avoid suspension and receive 1000MB free storage"`). Substantive text contains zero financial transaction or banking content. Excluded under `excluded_it_helpdesk_non_financial`.
4. **Individual Review of Webmail / Quarantine Digest Alerts:**  
   The remaining 10 webmail/quarantine alerts (`EXT-SCAM-00385`, `00386`, `00389`, `00392`, `00404`, `00407`, `00419`, `00437`, `00472`, `00478`) were individually inspected. All 10 were **retained as genuine financial fraud lures**: their quarantine digest framing is simply the delivery mechanism for explicit financial deception, including blocked HSBC wire transfers (`"Incoming Transfer from Sale@.... [HSBC]"`), contract invoice copies, sales orders (`SO: 0057528`), payment vouchers, proforma invoice payments, and telegraphic transfer (T/T) copies.

### Detailed Breakdown of Exclusions ($N = 11,984$)

| Exclusion Category | Candidate Source | Count | Rationale & Forensic Evidence |
| :--- | :--- | :--- | :--- |
| `excluded_ham_uci_duplicate` | Mishra & Soni | 4,844 | **Critical Overlap Elimination:** The authors copied the legitimate partition from the UCI SMS Spam Collection, which already provides 4,500 records in our canonical benchmark (`real_fin_legit.csv`). Ingesting this would cause circular evaluation leakage. |
| `excluded_carrier_promo_or_personal_noise` | AbayomiAlli | 2,076 | Telecom network promotional broadcasts (MTN, Glo, Etisalat bonus airtime, data plans, ringback tunes). |
| `excluded_personal_sms_ham` | AbayomiAlli | 1,838 | Personal user SMS messages (family, friends, non-financial chat). |
| `excluded_outgoing_carrier_command` | AbayomiAlli | 1,045 | Outgoing telephony commands (`direction = send`) typed by device owners (`"CANCLE"`, `"STOP"`, `"PAYYOU"`, `"1"`) incorrectly labeled as SPAM in raw files. |
| `excluded_non_financial_phishing` | Jose Nazario | 800 | General phishing lures lacking banking, financial transaction, or payment account narratives (e.g., lottery without bank, generic survey lures). |
| `excluded_general_telecom_spam` | Mishra & Soni | 489 | General commercial marketing spam (ringtones, horoscopes, discounts) without phishing or financial deception. |
| `excluded_non_financial_smishing` | Mishra & Soni | 338 | Non-financial smishing attacks (mobile dating service solicitations, adult chat, voicemail notification lures). |
| `excluded_empty_or_corrupt` | AbayomiAlli | 238 | Corrupt, truncated, or unparseable text payloads (<10 characters). |
| `excluded_it_helpdesk_non_financial` | Jose Nazario | 169 | Non-financial IT credential phishing targeting personal email account quotas (`"Your Mailbox Quota Almost Full"`, `"Roundcube Webmail Alert"`, mailbox full verification). |
| `excluded_foreign_language` | Jose Nazario | 66 | Non-English emails (French, German, Spanish, Portuguese, Italian, Chinese). |
| `excluded_legitimate_bank_alert_mislabeled` | AbayomiAlli | 41 | Legitimate Nigerian bank transaction alerts (Access Bank, GTBank, Zenith Bank) erroneously labeled as SPAM by device owners. |
| `excluded_internal_duplicate` | Nazario / Mishra | 25 | Lexically identical smishing text messages repeated within Mishra & Soni ($N=20$) or Nazario ($N=5$). |
| `excluded_benchmark_overlap` | Mishra & Soni | 12 | **Critical Benchmark Overlap:** 12 smishing records were identified as direct near-duplicate template matches (Jaccard similarity $\ge 0.70$) of IMC25 smishing records in our existing benchmark training split. Excluded to preserve strict source independence. |
| `excluded_mbox_artifact` | Jose Nazario | 2 | Unix mbox system internal format lines (`"DON'T DELETE THIS MESSAGE -- FOLDER INTERNAL DATA"`). |
| `excluded_malformed_script_defect` | Jose Nazario | 1 | Attacker script defect loop containing 45,146 email recipients and 1M+ characters (`EXT-SCAM-00224`). |
| **Total Excluded** | -- | **11,984** | -- |

---

## 4. Benchmark Overlap & Independence Verification

To guarantee that the 792 curated external scams represent genuinely unseen evaluation data, cross-dataset deduplication was executed against all 76,193 canonical benchmark records:

1. **Exact String Overlap:**
   - Matches with `real_fin_scam.csv`: **0 records (0.00%)**.
   - Matches with `real_fin_legit.csv`: **0 records (0.00%)**.
   - Matches with canonical `train.csv`, `val.csv`, `test.csv`: **0 records (0.00%)**.
2. **MinHash Locality Sensitive Hashing (LSH) & Shingle Jaccard Audit:**
   - 64 permutations, 16 bands, word 3-shingles.
   - Identified and excluded 12 candidate smishing records from Mishra & Soni that shared near-identical templates with IMC25 smishing records in our benchmark training split.
   - Following exclusion, **zero cross-corpus near-duplicates exist between the curated external scams and the benchmark**.
3. **Internal Candidate Deduplication:**
   - All internal duplicates within Nazario ($N = 5$) and Mishra & Soni ($N = 20$) were eliminated. Every record in `external_fin_scam_curated.csv` is lexically unique.

---

## 5. Preprocessing & Schema Integrity

### Preprocessing Protocol
Preprocessing followed the project's canonical pipeline (`src/preprocessing/harmonizer.py` and `src/preprocessing/channel_mapper.py`):
1. **Deterministic Placeholder Harmonization:** Un-nested bracket artifacts and mapped anonymized entity tokens to canonical ontology tokens (`[URL]`, `[PHONE_NUMBER]`, `[EMAIL_ADDRESS]`, `[FINANCIAL_DATA]`, `[ORGANIZATION]`, `[PERSON_NAME]`, `[IDENTIFIER]`, `[DATE_TIME]`, `[LOCATION]`, `[CREDENTIAL]`).
2. **Channel Harmonization & Gateway Transmission:** Evaluated carrier gateway headers (`FRM:... SUBJ:... MSG:...`). Populated `channel`, `original_channel`, `is_email_gateway`, and `has_gateway_headers`.
3. **Preservation of Natural Text:** No arbitrary stopword removal, lemmatization, or semantic distortion was performed. The exact original text is preserved in `original_text`, while `normalized_text` provides tokenizer compatibility.
4. **DistilBERT Compatibility:** Evaluated DistilBERT tokenization requirements. 100% of rows contain valid `normalized_text` and `label` fields ready for `Dataset.from_pandas(...)` ingestion. Following exclusion of the 1M-character outlier (`EXT-SCAM-00224`), the maximum character length is 16,078, with a mean normalized character count of 1,116.2.

### Complete 35-Column Canonical Schema
Both `external_fin_scam_curated.csv` and `expanded_binary_external_test.csv` adhere to the canonical 35-column schema:
```
['record_id', 'original_text', 'normalized_text', 'label', 'channel', 
 'original_channel', 'is_email_gateway', 'has_gateway_headers', 'source', 
 'source_url', 'source_license', 'source_record_id', 'is_synthetic', 
 'scam_subtype', 'fraudulent_intent', 'social_engineering_tactics', 
 'legitimate_category', 'email_subject', 'email_body', 'duplicate_cluster_id', 
 'char_count_original', 'word_count_original', 'char_count_normalized', 
 'word_count_normalized', 'placeholder_count_original', 'placeholder_count_normalized', 
 'generation_scenario', 'risk_or_safety_note', 'language', 'communication_type', 
 'group_id', 'split', 'evaluation_origin', 'financial_relevance', 'annotation_status']
```

---

## 6. Programmatic Integrity Validation

The generated artifacts were validated via automated assertions (`validate_updated_datasets.py`):
- [x] **File Existence:** All 5 CSV outputs exist in `data/external_evaluation/`.
- [x] **Record ID Uniqueness & Stability:** 100% unique record IDs across all files (`EXT-SCAM-00001` through `EXT-SCAM-00809` with stable IDs preserved for surviving records).
- [x] **Label Integrity:** Labels in `expanded_binary_external_test.csv` are strictly binary (`{0, 1}`) with zero nulls.
- [x] **Channel Constraints:** Channel values are strictly canonical (`'email'`, `'sms'`).
- [x] **Synthetic Flag:** 100% of rows have `is_synthetic == False`.
- [x] **Legitimate Preservation:** The 6,233 legitimate test records are an exact, byte-for-byte, unedited match with `data/splits/test.csv` where `label == 0`.
- [x] **Balanced Dataset Alignment:** `balanced_binary_external_test.csv` contains exactly 1,584 records (792 legitimate, 792 scam; 50/50 balance) sampled reproducibly with seed 42.
- [x] **Data Hygiene:** Zero null values in essential columns (`record_id`, `original_text`, `normalized_text`, `label`, `channel`, `source`, `evaluation_origin`).
- [x] **No Tokenizer Outliers:** Maximum text length dropped from 1,023,605 characters to 16,078 characters.

---

## 7. Research Evaluation Limitations & Disclosure Guidelines

When reporting experimental results on this expanded evaluation dataset, researchers must explicitly disclose the following methodological constraints:

1. **Hybrid Provenance (Asymmetric Independence):**
   - The 792 scam records are **independently sourced external communications** never seen during model training or benchmark validation.
   - The 6,233 legitimate records originate from the **established held-out benchmark test partition** (`MeAJOR` and `UCI SMS`).
   - Consequently, the expanded test set is **not a fully external independent benchmark for both classes**. It specifically measures **scam generalization** against held-out legitimate controls.
2. **Evaluation Sampling vs. Real-World Prevalence:**
   - The expanded class ratio (11.27% scam, 88.73% legitimate) reflects the full retention of our held-out legitimate test set paired with all verified external scams.
   - The balanced companion dataset (50% scam, 50% legitimate; $N = 1,584$) provides a controlled balanced evaluation to isolate class bias from base rate shifts.
   - Metrics should be reported using precision, recall, F1-score, and ROC-AUC rather than accuracy alone.
3. **Channel Imbalance in Legitimate Controls:**
   - Legitimate email is strongly represented ($N = 5,766$), but legitimate SMS remains modest ($N = 467$).
   - Researchers should report performance metrics broken down by channel (`email` vs. `sms`) and by `evaluation_origin` to isolate channel effects from fraud detection capabilities.
4. **Reproducibility Guarantee:**
   - Every inclusion, exclusion, and annotation decision is deterministically tracked in `external_scam_annotation_audit.csv` and `external_scam_exclusion_log.csv`, ensuring full third-party academic reproducibility.

---

## 8. Directory Artifact Inventory

All generated artifacts are preserved in: `data/external_evaluation/`

1. **`external_fin_scam_curated.csv`** (792 rows, 35 columns, ~1.5 MB)  
   *Curated, verified external financial scam records only.*
2. **`expanded_binary_external_test.csv`** (7,025 rows, 35 columns, ~14.1 MB)  
   *Expanded test set combining 792 external scams with 6,233 held-out legitimate controls.*
3. **`balanced_binary_external_test.csv`** (1,584 rows, 36 columns, ~3.2 MB)  
   *Balanced evaluation dataset (792 scam, 792 legitimate sampled reproducibly with seed 42).*
4. **`external_scam_annotation_audit.csv`** (12,776 rows, 13 columns, ~2.8 MB)  
   *Record-level annotation audit across all candidate corpora (792 included, 11,984 excluded).*
5. **`external_scam_exclusion_log.csv`** (11,984 rows, 13 columns, ~2.6 MB)  
   *Full audit log of excluded records with specific rejection reason codes.*
6. **`external_evaluation_dataset_audit.md`**  
   *This comprehensive dataset construction and quality report.*
7. **Experimental Evaluation Report & Prediction Outputs:**  
   - Comprehensive Research Report: [`reports/dataset_audits/external_source_generalization_evaluation_report.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/external_source_generalization_evaluation_report.md)  
   - Prediction Outputs: [`output/external_evaluation/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/) (`primary_test_predictions.csv`, `balanced_test_predictions.csv`, `external_scam_predictions.csv`)
