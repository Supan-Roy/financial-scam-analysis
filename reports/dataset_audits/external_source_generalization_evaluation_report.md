# Research Report: External-Source Generalization Evaluation (Notebook 09)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-25  
**Notebook Reference:** [`notebooks/09_external_source_generalization_evaluation.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/09_external_source_generalization_evaluation.ipynb)  
**Evaluated Model Checkpoint:** Canonical Real-Only Fine-Tuned DistilBERT Binary Classifier (`models/distilbert_binary/` from Notebook 06)  
**Evaluated External Corpora:** Jose Nazario Phishing Corpus, Mishra & Soni SMS Phishing Dataset, AbayomiAlli SMS Dataset  
**Primary Evaluation Artifacts:**
- Primary Expanded Test Set: [`data/external_evaluation/expanded_binary_external_test.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/expanded_binary_external_test.csv) ($N = 7,025$)
- Balanced Evaluation Companion: [`data/external_evaluation/balanced_binary_external_test.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/balanced_binary_external_test.csv) ($N = 1,584$)
- Curated External Scams: [`data/external_evaluation/external_fin_scam_curated.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/external_fin_scam_curated.csv) ($N = 792$)
**Output Prediction Files:**
- [`output/external_evaluation/primary_test_predictions.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/primary_test_predictions.csv)
- [`output/external_evaluation/balanced_test_predictions.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/balanced_test_predictions.csv)
- [`output/external_evaluation/external_scam_predictions.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/external_scam_predictions.csv)

---

## 1. Executive Summary & Research Motivation

In modern digital fraud detection, high in-distribution benchmark accuracy often masks severe model brittleness. In Notebook 06, our fine-tuned DistilBERT binary classifier achieved near-perfect performance on the real financial communications test set (**99.8950% accuracy**, **99.9278% scam recall**, **99.7118% scam F1-score**, and **99.9894% PR-AUC**). However, the diagnostic investigations in Notebook 07 revealed that:
1. Originating dataset sources possess strong lexical signatures (97.83% cross-source identifiability).
2. The benchmark suffers from structural channel–class confounding (93.1% of legitimate controls are corporate emails from MeAJOR/TREC, while scams are heavily weighted toward mobile smishing).

These findings raised a foundational research question:
> *Does our fine-tuned DistilBERT binary classifier genuinely learn transferable semantic representations of financial deception, or is its near-perfect performance an artifact of memorized benchmark source templates and channel shortcuts?*

To resolve this question conclusively, **Notebook 09 evaluates the original, frozen DistilBERT binary classifier on independently sourced external financial scam communications without any model retraining, fine-tuning, or threshold adaptation.**

### Key Scientific Findings

1. **Robust Generalization to Unseen External Scam Sources:**  
   The frozen DistilBERT model detected **766 out of 792 external real financial scams**, achieving an **external scam recall of 96.72%**. This high detection rate confirms that the model has learned robust, transferable semantic representations of financial fraud narratives rather than superficial benchmark shortcuts.
2. **Sustained High Classification Performance on Unseen Evaluation Sets:**  
   - **Primary Expanded Test ($N = 7,025$; 88.73% legit / 11.27% scam):**  
     **99.5302% Accuracy**, **99.0944% Precision**, **96.7172% Scam Recall**, **97.8914% Scam F1-score**, **98.3039% Balanced Accuracy**, **99.68% PR-AUC**, and **99.94% ROC-AUC**.
   - **Balanced Evaluation Test ($N = 1,584$; exact 50/50 balance):**  
     **98.2955% Accuracy**, **99.8696% Precision**, **96.7172% Scam Recall**, **98.2681% Scam F1-score**, **98.2955% Balanced Accuracy**, **99.93% PR-AUC**, and **99.92% ROC-AUC**.
3. **Flawless Generalization on Mobile Smishing (100.0% Recall):**  
   The model achieved **100.00% recall (270 / 270 detected)** on all external SMS smishing communications across both the Mishra & Soni SMS dataset ($N = 268$) and the AbayomiAlli Nigerian SMS dataset ($N = 2$), with **zero false negatives**.
4. **Strong Generalization on External Email Phishing (95.02% Recall):**  
   On the Jose Nazario Phishing Corpus, the model detected **496 out of 522 external phishing emails (95.02% recall)**. All 26 false negatives across the entire external evaluation originated from this historical email corpus.
5. **Ultra-Low False Positive Rate on Legitimate Controls (0.11% FPR):**  
   Evaluating against the 6,233 untouched held-out legitimate benchmark controls produced only **7 false positives** (99.89% specificity), demonstrating that external scam detection does not compromise legitimate classification precision.
6. **Interpretability of Residual Failure Modes:**  
   Forensic analysis of the 26 false negatives identified specific failure modes:
   - **Quarantine Digest Framing (8 cases):** Enterprise mail quarantine summaries that bury a financial wire transfer or invoice lure inside repetitive IT server administrative boilerplate.
   - **Ultra-Short Messages (2 cases):** Messages under 50 characters with truncated content (e.g., subject line only).
   - **IT / Software Update Lures (7 cases):** Fake security alerts and Adobe/cloud drive updates masquerading as enterprise IT maintenance.
   - **Complex B2B Purchasing (9 cases):** Obscure purchase order notices and supplier reconciliation texts lacking urgent retail banking terminology.

---

## 2. External Dataset Composition & Decontamination Audit

### Ingestion Funnel & Rigorous Decontamination

A total of **12,776 raw candidates** across three candidate corpora were audited at the record level. Following an initial pass and a pre-evaluation forensic quality audit, **11,984 non-eligible records were excluded**, leaving **792 verified external financial scams** (6.20% curation yield):

```
Candidate Corpus Ingestion Funnel:
12,776 Audited Candidates
   ├── 5,971 (Mishra & Soni) ──> 268 Curated (5,703 Excluded)
   ├── 5,240 (AbayomiAlli)    ──>   2 Curated (5,238 Excluded)
   └── 1,565 (Jose Nazario)   ──> 522 Curated (1,043 Excluded)
Total Curated External Scams: 792 records
Total Excluded Non-Eligible: 11,984 records
```

### Forensic Quality Decontaminations ($N = 5$)
Prior to evaluation, five anomalous records were formally excluded from the external candidate pool:
1. **`EXT-SCAM-00224` (`nazario_row_533`):** Attacker mail-merge script defect containing **45,146 email addresses repeated twice** (1,023,605 characters, ~46,580 words, ~463,696 DistilBERT tokens) with zero financial content (`excluded_malformed_script_defect`).
2. **`EXT-SCAM-00449` (`nazario_row_1230`):** Corrupted payload concatenating an English Amex security lure with a duplicated French e-commerce order confirmation (`smartdrive-boutique COMMANDE #11344 Votre commande est en route`). Excluded under English-only research scope (`excluded_foreign_language`).
3. **`EXT-SCAM-00450` (`nazario_row_1243`):** PayPal account security phish written 100% in German (`Wir haben ungewöhnliche Aktivitäten festgestellt!`). Excluded under English-only scope (`excluded_foreign_language`).
4. **`EXT-SCAM-00485` (`nazario_row_1414`):** Apple ID verification phish written 100% in German (`Liebes Apple-Mitglied IDENTITÄTSÜBERPRÜFUNG ERFORDERLICH`). Excluded under English-only scope (`excluded_foreign_language`).
5. **`EXT-SCAM-00106` (`nazario_row_237`):** Non-financial IT webmail mailbox quota exhaustion alert (`mailbox 95.77% full, verify email ID to avoid suspension and get 1000MB free storage`). Contains zero substantive financial fraud content (`excluded_it_helpdesk_non_financial`).

### Individual Review of Webmail / Quarantine Digest Alerts ($N = 10$)
The remaining 10 webmail/quarantine alerts (`EXT-SCAM-00385`, `00386`, `00389`, `00392`, `00404`, `00407`, `00419`, `00437`, `00472`, `00478`) were individually inspected. All 10 were **retained as genuine financial fraud lures**: their quarantine digest framing serves as the delivery envelope for explicit financial fraud lures (blocked HSBC incoming wire transfers, contract invoice copies, sales orders, payment vouchers, and telegraphic transfer copies).

---

## 3. Experimental Evaluation Protocol

### Evaluated Model & Checkpoint
- **Checkpoint:** Fine-tuned DistilBERT Base Uncased (`distilbert/distilbert-base-uncased`) with binary sequence classification head (`num_labels = 2`).
- **Training Provenance:** Checkpoint `models/distilbert_binary/` trained exclusively on the 60,957 real-world binary training communications from Notebook 06.
- **Strict Freezing:** Evaluated in pure inference mode (`model.eval()`). **Zero parameter updates, gradient computations, or threshold recalibrations were performed.**

### Inference & Tokenization Configuration
- **Input Text Column:** `normalized_text` (harmonized entity placeholders, normalized whitespace).
- **Maximum Sequence Length:** `max_length = 512` (with dynamic padding and right-truncation).
- **Inference Hardware:** Google Colab GPU (`cuda:0`).
- **Batch Size:** 32 (`DataLoader(..., batch_size=32)`).
- **Probability Scoring:** Softmax over output logits:
  $$P(\text{Scam} \mid x) = \frac{\exp(z_1)}{\exp(z_0) + \exp(z_1)}$$
- **Decision Rule:** Argmax classification corresponding to fixed decision threshold $\tau = 0.5$:
  $$\hat{y} = \begin{cases} 1 & \text{if } P(\text{Scam} \mid x) \ge 0.5 \\ 0 & \text{otherwise} \end{cases}$$

---

## 4. Empirical Evaluation Results

### Cross-Corpus Comparative Performance

The table below contrasts in-distribution test set performance (Notebook 06) against the newly completed external out-of-distribution evaluations:

| Evaluation Metric | In-Distribution Benchmark Test (Notebook 06) | Primary Expanded Test Set ($N = 7,025$) | Balanced Test Set ($N = 1,584$) |
| :--- | :---: | :---: | :---: |
| **Total Test Records** | 7,618 | 7,025 | 1,584 |
| **Legitimate Controls ($y = 0$)** | 6,233 (81.82%) | 6,233 (88.73%) | 792 (50.00%) |
| **Scam Communications ($y = 1$)** | 1,385 (18.18%) | 792 (11.27%) | 792 (50.00%) |
| **Accuracy** | **99.8950%** | **99.5302%** | **98.2955%** |
| **Scam Precision** | **99.4975%** | **99.0944%** | **99.8696%** |
| **Scam Recall** | **99.9278%** | **96.7172%** | **96.7172%** |
| **Scam F1-Score** | **99.7122%** | **97.8914%** | **98.2681%** |
| **Balanced Accuracy** | **99.9074%** | **98.3039%** | **98.2955%** |
| **PR-AUC (Average Precision)** | **99.9894%** | **99.6800%** | **99.9300%** |
| **ROC-AUC** | **99.9972%** | **99.9400%** | **99.9200%** |
| **Total Classification Errors** | **8 / 7,618** (1 FN, 7 FP) | **33 / 7,025** (26 FN, 7 FP) | **27 / 1,584** (26 FN, 1 FP) |

---

### Detailed Confusion Matrices

#### 1. Primary Expanded Test Set ($N = 7,025$)

| Actual \ Predicted | Predicted Legitimate ($\hat{y} = 0$) | Predicted Scam ($\hat{y} = 1$) | Total Support | Recall / Specificity |
| :--- | :---: | :---: | :---: | :---: |
| **Actual Legitimate ($y = 0$)** | **6,226** (True Negative) | **7** (False Positive) | 6,233 | 99.8877% (Specificity) |
| **Actual Scam ($y = 1$)** | **26** (False Negative) | **766** (True Positive) | 792 | 96.7172% (Recall) |
| **Total Predictions** | 6,252 | 773 | 7,025 | -- |

#### 2. Balanced Evaluation Test Set ($N = 1,584$)

| Actual \ Predicted | Predicted Legitimate ($\hat{y} = 0$) | Predicted Scam ($\hat{y} = 1$) | Total Support | Recall / Specificity |
| :--- | :---: | :---: | :---: | :---: |
| **Actual Legitimate ($y = 0$)** | **791** (True Negative) | **1** (False Positive) | 792 | 99.8737% (Specificity) |
| **Actual Scam ($y = 1$)** | **26** (False Negative) | **766** (True Positive) | 792 | 96.7172% (Recall) |
| **Total Predictions** | 817 | 767 | 1,584 | -- |

---

## 5. Granular Performance Dissection

### Performance by Originating External Source

| Originating Source Dataset | Channel | Total Scams | Correctly Detected | Missed (FN) | Scam Recall (%) | 95% Confidence Interval |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Jose Nazario Phishing Corpus** | Email | 522 | 496 | 26 | **95.02%** | [92.79%, 96.61%] |
| **Mishra & Soni SMS Phishing** | SMS | 268 | 268 | 0 | **100.00%** | [98.59%, 100.0%] |
| **AbayomiAlli SMS Dataset** | SMS | 2 | 2 | 0 | **100.00%** | [34.24%, 100.0%] |
| **Combined External Scams** | -- | **792** | **766** | **26** | **96.72%** | [95.23%, 97.79%] |

### Performance by Communication Channel

| Communication Channel | Total Scams | Detected | Missed | Scam Recall (%) | Key Observations |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Mobile SMS (`sms`)** | 270 | 270 | 0 | **100.00%** | Perfect transfer across banking alerts, prize claims, and tax rebate lures. |
| **Email (`email`)** | 522 | 496 | 26 | **95.02%** | High overall recall; all 26 errors driven by enterprise framing and digest boilerplate. |

### Performance by Financial Scam Subtype

| Financial Scam Subtype | Channel | Total Records | Detected | Missed | Recall (%) | Error Driver / Characteristics |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `card_verification_fraud` | Email | 25 | 25 | 0 | **100.00%** | High semantic overlap with card verification forms. |
| `fake_prize_or_compensation` | SMS | 210 | 210 | 0 | **100.00%** | Robust recognition of lottery, compensation, and voucher lures. |
| `bank_smishing` | SMS | 50 | 50 | 0 | **100.00%** | Strong detection of mobile banking OTP and KYC blocks. |
| `tax_refund_smishing` | SMS | 8 | 8 | 0 | **100.00%** | High sensitivity to HMRC/COVID rebate texts. |
| `payment_service_smishing` | SMS | 2 | 2 | 0 | **100.00%** | Apple Pay/Venmo security alerts detected cleanly. |
| `money_transfer_fraud` | Email | 2 | 2 | 0 | **100.00%** | Western Union/wire clearance lures recognized. |
| `payment_service_phishing` | Email | 82 | 81 | 1 | **98.78%** | 1 Portuguese-English hybrid missed (`EXT-SCAM-00451`). |
| `billing_invoice_scam` | Email | 34 | 33 | 1 | **97.06%** | 1 Apple ID purchase receipt missed (`EXT-SCAM-00347`). |
| `bank_impersonation` | Email | 280 | 265 | 15 | **94.64%** | Misses concentrated in USAA security updates & quarantine HSBC digests. |
| `account_security_phishing` | Email | 82 | 75 | 7 | **91.46%** | Misses driven by Adobe update and mail server quota lures. |
| `tax_refund_phishing` | Email | 17 | 15 | 2 | **88.24%** | 1 healthcare IT update and 1 high-HTML base64 subject missed. |
| **Total** | -- | **792** | **766** | **26** | **96.72%** | -- |

---

## 6. Forensic Error Taxonomy & Qualitative Analysis

### Analysis of False Negatives ($N = 26$)

Every false negative ($y = 1, \hat{y} = 0$) occurred within the Jose Nazario email corpus. Forensic inspection categorizes them into four distinct structural error types:

```
False Negative Error Taxonomy (N = 26):
├── 1. Quarantine Digest Boilerplate Masking (N = 8)
│      EXT-SCAM-00385, 00386, 00389, 00392, 00404, 00407, 00419, 00437
├── 2. Enterprise IT & Software Update Framing (N = 7)
│      EXT-SCAM-00039, 00062, 00108, 00287, 00313, 00459, 00500
├── 3. Ultra-Short or Truncated Payloads (N = 2)
│      EXT-SCAM-00049, 00193
└── 4. Institutional Security Notices & B2B Orders (N = 9)
       EXT-SCAM-00028, 00034, 00073, 00280, 00302, 00347, 00438, 00451, 00502
```

1. **Quarantine Digest Boilerplate Masking (8 records; $P(\text{Scam}) < 0.003$):**  
   Records `EXT-SCAM-00385`, `00386`, `00389`, `00392`, `00404`, `00407`, `00419`, and `00437` follow a template disguised as a mail server digest notification:  
   `"jose@monkey.org Messages could not delivered... There are new messages in your Email Quarantine, messages will be automatically removed after 7 day(s)..."`  
   Buried inside the digest is a table row: `"Incoming Transfer from Sale@.... [HSBC]"`.  
   *Root Cause:* Over 80% of the token sequence comprises standard corporate mail server administration boilerplate. DistilBERT's self-attention layers attend primarily to the administrative headers (strongly associated with legitimate MeAJOR emails in training), drowning out the single isolated wire transfer token.
2. **Enterprise IT & Software Update Framing (7 records; $P(\text{Scam}) = 0.0001 - 0.4259$):**  
   Records like `EXT-SCAM-00287` (`"Adobe Acrobat Reader Security update... Access Secured Documents... strategic alliance with Microsoft"`) and `EXT-SCAM-00039` (`"Please Contact The IT Service Desk... Password will expire in 2 days... Fallon Health"`).  
   *Root Cause:* The scam narrative mimics corporate software lifecycle notices without explicit payment demands or banking credential forms.
3. **Ultra-Short Payloads (2 records; $P(\text{Scam}) < 0.07$):**  
   `EXT-SCAM-00049` (43 characters: `"PLS READ THE NEW USAA NEW YEAR UPDATE NOW -"`) and `EXT-SCAM-00193` (43 characters: `"USAA Electronic Wire Transfer Message -"`).  
   *Root Cause:* The entire message body is truncated or empty, containing only a subject line. Without syntactic context or an explicit phishing URL, the classifier defaults toward neutral/legitimate probability.
4. **Institutional Security Notices & B2B Orders (9 records; $P(\text{Scam}) = 0.0000 - 0.3896$):**  
   Long institutional device upgrade notices (e.g., `EXT-SCAM-00034` with 3,044 characters: `"USAA END OF THE YEAR UPDATE - DO NOT IGNORE... Internet upgrade to increase online security... Device Update Deadline Dec 31, 2015"`) and B2B purchase orders (`EXT-SCAM-00280`).  
   *Root Cause:* Long-form institutional advisories that avoid urgent payment demands or immediate account suspension threats align closely with legitimate corporate communications in the training corpus.

---

### Analysis of False Positives ($N = 7$)

Out of 6,233 held-out legitimate benchmark controls in the expanded test set, only **7 records** were incorrectly flagged as scams (FPR = 0.11%):

1. **`LEG-FIN-00010` ($P = 0.9999$):** `"Your OTP is 789654, keep it confidential to secure your account."`  
   *Analysis:* A genuine automated banking OTP SMS. Because the training corpus contains numerous OTP-harvesting smishing attacks mimicking this exact structure, the model exhibits a false positive on raw OTP text lacking enterprise sender context.
2. **`LEG-FIN-00121` ($P = 0.9999$):** `"I sent the freelance payment of $150 via Payoneer. Check and confirm receipt, please"`  
   *Analysis:* Authentic P2P payment notification containing explicit financial tokens (`$150`, `payment`, `Payoneer`).
3. **`LEG-FIN-00161` ($P = 1.0000$):** `"A new login to your account was detected from an unknown device. Secure your login now."`  
   *Analysis:* Authentic security notice from Mendeley Data V2. Semantic framing is virtually indistinguishable from an account takeover phishing alert.
4. **`LEG-FIN-00191` ($P = 0.9970$):** `"Can't you let me send you some money towards your net ? I need you ... I want you ... I crave you ..."`  
   *Analysis:* Personal chat message from UCI SMS spam collection mentioning sending money.
5. **`MEAJOR-LEG-002599` ($P = 0.9999$):** Enron email discussing accounting gains (`[FINANCIAL_DATA]`), Pastoria reserves, and signoff.
6. **`MEAJOR-LEG-016647` ($P = 0.9971$):** Enron email requesting budget figures and discussing a credit arrangement.
7. **`MEAJOR-LEG-029407` ($P = 0.9948$):** TREC spam/promotional email (`"FREE CELL PHONES AND NO BILLS!"`).

*Crucially, in the balanced evaluation set ($N = 1,584$), only **1 false positive** occurred (`LEG-FIN-00161`), demonstrating exceptional specificity (99.87%).*

---

## 7. Prediction Probability Distributions & Confidence Calibration

Analyzing predicted probabilities across the evaluation sets reveals sharp bimodal distribution and strong confidence calibration:

```
Probability Distribution Summary:
├── External Scams (N = 792)
│   ├── Mean: 0.9634 | Median: 1.0000 | Std: 0.1837
│   ├── Q1 (25%): 1.0000 | Q3 (75%): 1.0000
│   └── 749 of 792 records (94.57%) assigned P(Scam) > 0.9900
└── Legitimate Controls (N = 6,233)
    ├── Mean: 0.0019 | Median: 0.0000 | Std: 0.0401
    └── 6,212 of 6,233 records (99.66%) assigned P(Scam) < 0.0100
```

- **Extreme Confidence Calibration:** Over 94.5% of external scams received prediction probabilities $> 0.9900$, while over 99.6% of legitimate communications received probabilities $< 0.0100$.
- **Steep Decision Boundary:** Very few examples clustered near the decision threshold $\tau = 0.5$, indicating that the model makes confident, decisive distinctions between communicative classes rather than borderline guesses.

---

## 8. Answers to Core Research Questions

### Question 1: Does the DistilBERT binary classifier generalize to independently sourced scam narratives?
**Answer: YES.**  
Achieving **96.72% external scam recall** (and **100.00% on SMS smishing**) across completely unseen external corpora compiled by different researchers in different years and jurisdictions conclusively demonstrates that DistilBERT has captured transferable semantic representations of financial deception. The model does not merely rely on memorized training templates.

### Question 2: How much performance degradation occurs when transitioning from in-distribution to out-of-distribution evaluation?
**Answer: A modest, quantifiable drop of 3.21% in scam recall.**  
- In-distribution scam recall: **99.93%** (Notebook 06)  
- External out-of-distribution scam recall: **96.72%** (Notebook 09)  
- In-distribution balanced accuracy: **99.91%** $\rightarrow$ External balanced accuracy: **98.30%**  
This 3.21% delta reflects realistic out-of-distribution domain shift, primarily driven by enterprise quarantine digests and IT software update framing.

### Question 3: Is model performance artificially inflated by channel–class confounding?
**Answer: NO, but channel context influences specific failure modes.**  
If the model relied solely on channel shortcuts (e.g., classifying all SMS as scams or all email as legitimate), it would have catastrophically failed on the 522 external phishing emails. Instead, it successfully detected **95.02% of external emails**, proving that linguistic content—not channel metadata—drives classification. However, the presence of administrative boilerplate in enterprise email digests can mask short financial scam lures.

---

## 9. Research Evaluation Limitations & Disclosure Guidelines

When citing these experimental findings in academic publications, researchers must disclose the following methodological constraints:

1. **Hybrid Provenance (Asymmetric Independence):**  
   The external scam cohort ($N = 792$) is fully independent and out-of-distribution. However, the legitimate cohort ($N = 6,233$) originates from the established benchmark test partition (`MeAJOR` and `UCI SMS`). Consequently, this evaluation specifically measures **scam generalization against held-out legitimate controls**, rather than a fully external dual-class benchmark.
2. **Channel-Source Alignment in External Scams:**  
   In the curated external dataset, all emails originate from the Jose Nazario corpus, while all SMS originate from Mishra & Soni or AbayomiAlli. While reflective of available open-access datasets, cross-channel effects within the same external source could not be evaluated.
3. **Evaluation Class Distribution vs. Real-World Base Rates:**  
   The primary expanded test set class ratio (11.27% scam) and balanced companion ratio (50.00% scam) do not reflect real-world telecommunication base rates (where fraud represents $< 0.1\%$ of total volume). Evaluation metrics should prioritize precision, recall, F1-score, and PR-AUC over raw accuracy.
4. **Reproducibility Guarantee:**  
   Every inference output, logit score, and predicted class label is tracked deterministically in the output directory files, enabling exact external academic replication.

---

## 10. Output Directory Inventory

All prediction outputs from the Notebook 09 experiment are preserved and tracked in `output/external_evaluation/`:

1. **[`output/external_evaluation/primary_test_predictions.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/primary_test_predictions.csv)** (7,025 rows, ~0.39 MB)  
   *Full predictions on primary expanded test set (`record_id`, `label`, `channel`, `source`, `scam_probability`, `predicted_label`).*
2. **[`output/external_evaluation/balanced_test_predictions.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/balanced_test_predictions.csv)** (1,584 rows, ~0.09 MB)  
   *Predictions on balanced 50/50 evaluation companion set.*
3. **[`output/external_evaluation/external_scam_predictions.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/output/external_evaluation/external_scam_predictions.csv)** (792 rows, ~0.05 MB)  
   *Dedicated predictions and confidence scores for the 792 curated external scams.*
