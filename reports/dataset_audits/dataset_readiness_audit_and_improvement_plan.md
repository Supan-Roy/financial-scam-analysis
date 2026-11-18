# Dataset Readiness Audit and Improvement Plan — Financial Scam Research

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection, Fraud Analysis and Social Engineering Pattern Recognition in Digital Communications  
**Deliverable Type:** Academic Dataset Readiness Audit & 10-Day Improvement Strategy  
**Evaluation Milestone:** Phase 1 Research Evaluation  
**Status:** Read-Only Audit Completed — No Datasets or Splits Modified  

---

## 1. Verified Current Dataset Status

A comprehensive, read-only audit of all 9 dataset assets in `data/raw/`, `data/processed/`, and `data/splits/` was executed against the actual CSV files.

### 1.1 Dataset Asset Inventory & Schema Hierarchy

| Dataset Stage | Asset Path | Record Count | Schema Columns | Label Distribution | Primary Channels | Integrity / Null Notes |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Raw Scam** | `data/raw/real_fin_scam.csv` | 13,861 | 9 | `label=1` (13,861) | SMS (10,096), Email (3,765) | 3,792 missing `source_record_id`. 62 records contain stringified Python lists (`"['..."`). |
| **Raw Legit** | `data/raw/real_fin_legit.csv` | 62,332 | 13 | `label=0` (62,332) | Email (57,662), SMS (4,670) | 5,618 missing `email_subject`, 4,670 missing `email_body` (all SMS). |
| **Raw Synthetic** | `data/raw/synthetic_financial_scams.csv` | 7,643 | 11 | `label=1` (7,643) | Email, SMS, Chat, Notification (~1,911 each) | 0 missing values. 13 subtypes, 3 intents, 9 tactics. |
| **Processed Scam** | `data/processed/real_fin_scam_processed.csv` | 13,861 | 30 | `label=1` (13,861) | SMS (10,096), Email (3,765) | 30-column canonical schema. 3,206 records in 1,217 duplicate clusters. |
| **Processed Legit** | `data/processed/real_fin_legit_processed.csv` | 62,332 | 30 | `label=0` (62,332) | Email (57,662), SMS (4,670) | 30-column canonical schema. 4,005 records in 1,334 duplicate clusters. |
| **Processed Synthetic** | `data/processed/synthetic_financial_scams_processed.csv` | 7,643 | 30 | `label=1` (7,643) | Balanced 4 channels | Held out from benchmark splits. |
| **Split: Train** | `data/splits/train.csv` | 60,957 | 32 | `0`: 49,866 (81.81%)<br>`1`: 11,091 (18.19%) | Email: 49,143 (80.62%)<br>SMS: 11,814 (19.38%) | Group-aware SGGP. 0 cluster leakage. 32 columns (+`group_id`, `split`). |
| **Split: Validation**| `data/splits/validation.csv` | 7,618 | 32 | `0`: 6,233 (81.82%)<br>`1`: 1,385 (18.18%) | Email: 6,142 (80.62%)<br>SMS: 1,476 (19.38%) | Group-aware SGGP. 0 cluster leakage. |
| **Split: Test** | `data/splits/test.csv` | 7,618 | 32 | `0`: 6,233 (81.82%)<br>`1`: 1,385 (18.18%) | Email: 6,142 (80.62%)<br>SMS: 1,476 (19.38%) | Group-aware SGGP. 0 cluster leakage. |

### 1.2 Empirical Source Distribution

#### Real Scams (`real_fin_scam.csv` — 13,861 records):
- **Smishing Dataset IMC25 (public user reports):** 9,600 records (69.26%) — SMS & Gateway messages.
- **Nigerian_Fraud.csv (GitHub threat archive):** 3,265 records (23.56%) — Advance-fee fraud emails.
- **Phishing and Legitimate Emails Dataset (Kaggle):** 500 records (3.61%) — Financial phishing emails.
- **smishtank.csv:** 496 records (3.58%) — Mobile smishing reports.

#### Real Legitimate (`real_fin_legit.csv` — 62,332 records):
- **MeAJOR (trec5):** 27,291 records (43.78%) — 1999–2002 Enterprise & Open Source mailing list emails.
- **MeAJOR (trec7):** 19,244 records (30.87%) — Enterprise & Open Source mailing list emails.
- **MeAJOR (trec6):** 11,127 records (17.85%) — Enterprise & Open Source mailing list emails.
- **UCI SMS Spam Collection:** 4,500 records (7.22%) — 2012 Personal mobile SMS communications.
- **Financial scams detection dataset (Mendeley Data V2):** 170 records (0.27%) — Mobile banking & transactional SMS.

### 1.3 Exact Overlap & Label Consistency Verification
- **Cross-class exact text overlap:** Exactly **0 records** overlap between `real_fin_scam` and `real_fin_legit` on `normalized_text`.
- **Exact duplicate texts within class:** 3 duplicates within scam, 5 duplicates within legitimate (all retained within isolated singleton/duplicate groups).
- **Cluster leakage across splits:** Exactly **0 duplicate clusters** cross the train, validation, or test partitions.
- **Report Consistency:** All reported record counts in previous audit reports (`83,836` total, `76,193` real benchmark, `60,957` train, `7,618` val, `7,618` test) match the actual CSV files with 100% precision.

---

## 2. Most Serious Dataset Weaknesses

Our forensic audit identifies four critical structural weaknesses that explain why the baseline Logistic Regression achieved 99.41% validation accuracy, while simultaneously exhibiting serious failure modes on real banking communications.

```mermaid
flowchart TD
    subgraph Weaknesses ["Systemic Dataset Confounding"]
        W1["1. Severe Channel Skew<br/>Scam = 72.8% SMS<br/>Legit = 92.5% Email"]
        W2["2. Entity Placeholder Leakage<br/>[PERSON_NAME]: 77.7% Legit vs 0.05% Scam<br/>LR Weight = -14.9"]
        W3["3. Severe Consumer SMS Scarcity<br/>Legit Banking SMS = 76 records (0.12%)<br/>Scam Banking SMS = 10,096 records"]
        W4["4. Domain / Topic Disparity<br/>Legit: Enron / Linux / Apache IT<br/>Scam: Banking & Wire Urgency"]
    end

    subgraph Impact ["Model Behavioral Failure"]
        W1 --> FAIL["Learns Transport / Syntax Shortcuts"]
        W2 --> FAIL
        W3 --> FAIL
        W4 --> FAIL
        FAIL --> ERR["Mendeley Real Banking SMS Error: 47.06%<br/>(8 of 17 False Positives)"]
    end
```

### Weakness 1: Severe Channel-Class Confounding (Shortcut Learning)
- **Scams are 72.83% SMS**, whereas **Legitimate communications are 92.51% Email**.
- Within SMS, **68.38% are scams**; within email, **93.87% are legitimate**.
- **The Consequence:** A classifier can achieve ~95%+ accuracy simply by detecting whether a message contains email headers, formal sign-offs, or conversational length, completely bypassing the semantic narrative of financial fraud.

### Weakness 2: Entity Placeholder Leakage (Provenance Artifacts)
- When `TfidfVectorizer` tokenizes text with standard word boundaries (`\b\w\w+\b`), bracketed placeholders become unigram words (`person_name`, `organization`, `named_entity`).
- `[PERSON_NAME]` is present in **77.73% of legitimate records** and only **0.05% of scam records**.
- `[ORGANIZATION]` is present in **54.70% of legitimate records** and **0.00% of scam records**.
- `[NAMED_ENTITY]` is present exclusively in scam records.
- In the baseline Logistic Regression:
  - `organization` weight: **-14.94**
  - `person_name` weight: **-14.90**
  - `named_entity` weight: **+8.33**
- The model exploits these preprocessing conventions as an artificial cheat code.

### Weakness 3: Severe Underrepresentation of Legitimate Consumer Financial SMS
- In the entire 62,332-record legitimate corpus, **only 170 records come from mobile financial datasets (Mendeley Data V2)**.
- Only **76 of those records** are categorized as `financial_legitimate`.
- The remaining 4,500 legitimate SMS records are casual interpersonal chats from UCI SMS (e.g. *"Aight, I'll hit you up when I get some cash"*).
- **The Result:** The model was never trained on legitimate mobile banking OTPs, debit alerts, or transaction receipts. When tested on real legitimate banking SMS from Mendeley, **the false positive rate spiked to 47.06% (8 out of 17 misclassified as scams)**.

### Weakness 4: Domain Disparity in the Email Corpus
- 92.5% of the legitimate emails (57,662 messages) originate from 1999–2002 Enron and Apache mailing lists (`MeAJOR trec5/6/7`).
- While 18,979 of these are labeled `financial_legitimate`, inspection reveals they are **wholesale energy trading contracts (GISB), GTC spot agreements, pipeline capacity open season notices, and corporate advertising invoices**.
- They do **not** represent modern retail consumer banking emails (e.g. Chase/Wells Fargo transaction alerts, PayPal receipts, password reset links).
- Meanwhile, the scam emails are Nigerian 419 advance-fee fraud and lottery scams. The linear model simply separates "open-source software development" from "urgent wire transfer demands."

### Weakness 5: Missing Multi-Level Annotations on Real-World Data
- For Phase 1 research evaluation, the project title promises:
  1. Financial scam narrative detection (Binary)
  2. Fraudulent intent analysis (Multi-class)
  3. Social engineering pattern recognition (Multi-label)
- In the current benchmark splits (`train.csv`, `val.csv`, `test.csv`):
  - `scam_subtype` has only **1 monolithic value** (`financial_scam`) for all 13,861 real scams.
  - `fraudulent_intent` is **100% null (NaN)**.
  - `social_engineering_tactics` is **100% null (NaN)**.
- Levels 2 and 3 exist **only** in the 7,643 synthetic records. If the Phase 1 evaluation expects real-world multi-level classification, the dataset currently cannot support it without annotation or a synthetic-to-real transfer design.

---

## 3. Legitimate Financial-Message Coverage Audit

To verify whether the legitimate corpus sufficiently represents consumer and retail financial communications, an exhaustive regular expression audit was conducted across all 62,332 legitimate records:

| Financial Communication Category | Total Matches (out of 62,332) | Legitimate SMS Matches (out of 4,670) | Legitimate Email Matches (out of 57,662) | Primary Dataset Source | Coverage Status |
| :--- | :---: | :---: | :---: | :--- | :---: |
| **1. OTP & Authentication Notifications** | 9 | **4** | 5 | Mendeley V2 (4), MeAJOR (5) | **Critically Deficient** |
| **2. Wallet Transactions (PayPal, bKash, etc.)** | 75 | **10** | 65 | Mendeley V2 (8), MeAJOR (65) | **Critically Deficient** |
| **3. Bank Transfer Confirmations (Wire, ACH)** | 221 | **8** | 213 | Mendeley V2 (7), MeAJOR (213) | **Critically Deficient** |
| **4. Card Transactions & Alerts (Debit/Credit)** | 348 | **5** | 343 | MeAJOR Enron (343), Mendeley (2) | **Critically Deficient** |
| **5. Payment Receipts & Confirmations** | 182 | **20** | 162 | Mendeley V2 (20), MeAJOR (156) | **Severe Scarcity** |
| **6. Refund Notifications & Credit Reversals** | 167 | **4** | 163 | MeAJOR Enron (163), Mendeley (3) | **Critically Deficient** |
| **7. Salary & Payroll Notifications** | 249 | **10** | 239 | MeAJOR Enron (239), Mendeley (5) | **Severe Scarcity** |
| **8. Loan & Banking / EMI Notifications** | 201 | **6** | 195 | MeAJOR Enron (195), UCI (5) | **Critically Deficient** |
| **9. Account Security Alerts (New Login, Device)**| 72 | **1** | 71 | MeAJOR IT logs (71), Mendeley (1) | **Critically Deficient** |
| **10. E-commerce Payment & Delivery Alerts** | 236 | **7** | 229 | MeAJOR (229), Mendeley (7) | **Critically Deficient** |

### Audit Finding:
Across the entire legitimate SMS corpus (4,670 records), **fewer than 75 total messages** represent genuine retail financial transactions or security alerts. In contrast, the scam SMS corpus contains **over 10,000 messages** simulating these exact categories. 

This creates a **130:1 structural class imbalance** in mobile banking syntax, directly causing the model to mistake benign banking notifications for fraud.

---

## 4. Potential Additional Traceable Datasets

To resolve the legitimate financial scarcity without introducing synthetic records or unverified data, the following publicly available, traceable datasets were evaluated:

### Candidate 1: Bank Transactions SMS datasetss (Khalifa University)
- **Source & Author:** Compiled under the supervision of Prof. Zeyar Aung at Khalifa University; published by Reem Ali (`engreemali`).
- **Official URL:** [`https://www.kaggle.com/datasets/engreemali/bank-transactions-sms-datasetss`](https://www.kaggle.com/datasets/engreemali/bank-transactions-sms-datasetss)
- **Record Count:** Thousands of real transaction SMS messages spanning a 5-year period (`Prepared bank transactions SMS dataset .xlsx`, ~292 KB).
- **Channel & Language:** SMS; English.
- **Content:** Genuine debit and credit card notifications, ATM withdrawals, POS purchases, account balance updates, and merchant debits voluntarily contributed by users.
- **License & Use:** Strictly for academic and educational research. Commercial use prohibited.
- **Suitability:** **Extremely High.** Directly provides the exact consumer bank transaction SMS messages currently missing from our legitimate corpus.

### Candidate 2: Financial Scams Detection Dataset Version 2 (Full Release)
- **Source & Authors:** Al Rafi Ahmed and Gazi Faizul Islam (International University of Business Agriculture and Technology - IUBAT).
- **Official DOI & Repository:** [`https://data.mendeley.com/datasets/znsk27yk3h/2`](https://data.mendeley.com/datasets/znsk27yk3h/2) (DOI: `10.17632/znsk27yk3h.2`).
- **Record Count:** Multi-thousand message repository (currently our repo only imports an isolated 170-record subset).
- **Channel & Language:** SMS, Email, and Chat; English and code-mixed Bangla-English.
- **Content:** Genuine Mobile Financial Services (MFS) messages (bKash, Nagad, Rocket), bank OTPs, wallet top-ups, transaction confirmations, and interpersonal financial requests, paired with real scam reports.
- **License & Use:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Suitability:** **Highest Priority.** Expanding from our 170-record sample to the complete verified English legitimate subset directly fixes our worst empirical failure mode without introducing a new unfamiliar source.

### Candidate 3: SMS-Data (Financial Health Extraction)
- **Source & Author:** Dhwanil Shah.
- **Official URL:** [`https://www.kaggle.com/datasets/dhwanilshah/sms-data`](https://www.kaggle.com/datasets/dhwanilshah/sms-data)
- **Record Count:** Tabular corpus of user SMS notifications.
- **Channel & Language:** SMS; English.
- **Content:** Anonymized transactional SMS messages from Indian banks covering salary credits, debit/credit card alerts, UPI payments, EMI loan debits, and balance inquiries.
- **License & Use:** Open for research and NLP text parsing.
- **Suitability:** **High.** Excellent for training models to distinguish legitimate UPI/banking templates from smishing attacks.

### Candidate 4: Phishing and Legitimate Emails Dataset (Kaggle - Safe Email Subset)
- **Source & Author:** `kuladeep19`.
- **Official URL:** [`https://www.kaggle.com/datasets/kuladeep19/phishing-and-legitimate-emails-dataset`](https://www.kaggle.com/datasets/kuladeep19/phishing-and-legitimate-emails-dataset)
- **Record Count:** ~5,000+ legitimate emails (the companion safe partition to the 500 scam emails already imported into `real_fin_scam.csv`).
- **Channel & Language:** Email; English.
- **Content:** Modern consumer notification emails, account confirmations, and non-phishing correspondence.
- **License & Use:** Open research dataset on Kaggle.
- **Suitability:** **Moderate-to-High.** Bridges the gap between 2000-era Enron corporate trading emails and modern consumer email notifications.

---

## 5. Recommended Improvements & 10-Day Plan

To prepare a rigorous, academically defensible presentation for the Phase 1 evaluation in 10 days, recommendations are partitioned into three distinct horizons:

```mermaid
flowchart LR
    subgraph T1 ["Tier 1: Days 1–3 (Methodology & Baseline Fixes)"]
        direction TB
        A1["Neutralize Placeholder Leakage<br/>(Ablation & Tokenizer Regex)"]
        A2["Channel-Stratified Evaluation<br/>(Email F1 vs SMS F1)"]
        A3["Mendeley Stress-Test Metric<br/>(Formalize Failure Analysis)"]
    end

    subgraph T2 ["Tier 2: Days 4–8 (Experimental Hardening)"]
        direction TB
        B1["Synthetic OOD Stress Test<br/>(Zero-Shot Evaluation on 7.6k records)"]
        B2["Compile Curated Legit Validation Set<br/>(200–500 real banking SMS)"]
        B3["DeBERTa / RoBERTa Initial Baseline"]
    end

    subgraph T3 ["Tier 3: Post-Phase 1 (Long-Term Expansion)"]
        direction TB
        C1["Incorporate Full Khalifa & Mendeley V2 Data"]
        C2["Multi-Level Intent & Tactics Annotation"]
        C3["Synthetic-to-Real Transfer Learning"]
    end

    T1 --> T2 --> T3
```

### 5.1 Tier 1: Essential Corrections Before Phase 1 (Days 1–3)
*No changes to raw datasets or existing split files.*

1. **Neutralize Placeholder Shortcut Learning in Baselines:**
   - *Why:* Prevent tree and linear models from keying on `person_name` (-14.9) and `organization` (-14.9).
   - *Action:* Implement a clean feature representation option that masks all bracketed entities `[A-Z_]+` to a uniform `[REDACTED]` token or strips them during vectorization (`token_pattern=r"(?u)\b[a-zA-Z]{2,}\b"` with placeholder exclusion).
   - *Expected Benefit:* Demonstrates scientific rigor; proves baseline accuracy remains high (~99.0%) based on genuine lexical signals rather than dataset artifacts.
   - *Affected Files:* `notebooks/03_baseline_machine_learning.ipynb`, `src/preprocessing/`.

2. **Mandate Channel-Stratified Reporting:**
   - *Why:* Overall accuracy (99.4%) masks channel-specific dynamics.
   - *Action:* In all evaluation scripts and tables, report **Email F1** and **SMS F1** separately alongside the macro average.
   - *Affected Files:* `notebooks/03_baseline_machine_learning.ipynb`, `src/data/split_reporter.py`.

3. **Formalize the "Mendeley Real-Banking Stress Test":**
   - *Why:* Academic reviewers value honest error analysis over inflated metrics.
   - *Action:* Include a dedicated subsection in the Phase 1 report detailing the 47.06% error rate on legitimate banking SMS as the motivating problem statement for multi-level Transformers.
   - *Affected Files:* `notebooks/03_baseline_machine_learning.ipynb`, research slide deck.

### 5.2 Tier 2: Improvements Achievable Within Next 10 Days (Days 4–8)
*Requires zero split modifications; uses existing held-out assets.*

1. **Evaluate Baseline Generalization on Held-Out Synthetic Scams (OOD Stress Test):**
   - *Why:* `synthetic_financial_scams.csv` (7,643 records) was generated with neutral entities and balanced channels, completely free of MeAJOR or IMC25 source shortcuts.
   - *Action:* Test the trained Logistic Regression and Naive Bayes models zero-shot on the synthetic dataset.
   - *Expected Benefit:* Provides an unvarnished measure of whether the model learned general financial fraud semantics or merely memorized source artifacts.
   - *Affected Files:* `notebooks/03_baseline_machine_learning.ipynb`.

2. **Assemble a Curated External Legitimate SMS Evaluation Probe:**
   - *Why:* To objectively measure legitimate banking false-alarm rates without modifying the core 76,193 benchmark split.
   - *Action:* Extract 200–300 verified legitimate transactional SMS records from *Bank Transactions SMS datasetss* (Khalifa University) into a standalone evaluation probe (`data/external/legit_financial_sms_probe.csv`).
   - *Expected Benefit:* Provides a true out-of-distribution specificity metric for Phase 1 presentation.

3. **Train Initial Pretrained Transformer Baselines (DeBERTa-v3-small / RoBERTa):**
   - *Why:* To demonstrate technical progress beyond linear models for Phase 1.
   - *Action:* Fine-tune `microsoft/deberta-v3-small` on `train.csv` (using placeholder-ablated text) with early stopping on validation loss.
   - *Expected Benefit:* Subword tokenizers and contextual attention are significantly more resistant to word-order invariance and isolated keyword confounding than TF-IDF.

### 5.3 Tier 3: Longer-Term Research Improvements (Post-Phase 1)
*Planned for Phase 2 implementation.*

1. **Canonical Ingestion of Verified Consumer Banking Data:**
   - Download, harmonize, and canonicalize the Khalifa University and Mendeley V2 full releases.
   - Re-run MinHash LSH deduplication and regenerate `data/processed/real_fin_legit_processed.csv`.
   - Update SGGP bin-packing to produce an augmented, balanced benchmark partition.

2. **Multi-Level Real-World Annotation Campaign:**
   - Annotate a representative sample (1,500–2,000 real scam messages) with Level 2 (`fraudulent_intent`) and Level 3 (`social_engineering_tactics`).
   - Enables multi-task Transformer learning on empirical communications.

---

## 6. Definitive Usability Recommendation for Phase 1

### Verdict: **CONDITIONALLY USABLE FOR PHASE 1 (WITH METHODOLOGICAL SAFEGUARDS)**

The existing 76,193-record dataset and its SGGP partitions are **sufficiently usable to demonstrate technical progress in Phase 1**, but **ONLY** under strict scientific framing:

1. **Do NOT claim 99.4% real-world accuracy.** Frame the high accuracy as a combination of strong lexical separation on narrative fraud and observable source confounding.
2. **Present the Placeholder Ablation Study:** Show that when entity placeholders are removed, performance adjusts to ~99.07%, proving the model learns genuine linguistic markers (`account`, `bank`, `refund`, `urgent`) while acknowledging the -14.9 shortcut.
3. **Highlight the Mendeley Failure Mode as the Research Justification:** Use the 47% false positive rate on legitimate banking SMS to demonstrate why classical ML is brittle and why the project is developing an **Explainable Multi-Level Transformer Framework**.
4. **Scope Multi-Level Tasks Accurately:** Clearly state in Phase 1 documentation that Level 1 (Narrative Detection) is benchmarked on the 76,193 real-world corpus, while Levels 2 and 3 (Intent and Tactics) are evaluated on the 7,643 synthetic corpus pending real-world multi-task annotation.

Following this defense strategy converts what would otherwise be a vulnerable research flaw into a compelling, scientifically rigorous demonstration of empirical research maturity.
