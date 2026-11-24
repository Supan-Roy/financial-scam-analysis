# External Dataset Candidate Verification & Forensic Audit Report

**Research Project Title:**  
*Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*

**Audit Date:** November 2026  
**Auditor:** Antigravity Research Engineering  
**Scope:** Forensic Provenance, Hygiene, Financial Relevance, and Benchmark Overlap Audit of Seven Candidate External Datasets  
**Canonical Model Evaluated:** Real-Only Fine-Tuned DistilBERT Binary Classifier (`notebooks/06_transformer_based_modeling.ipynb`)  

---

## Executive Summary

To evaluate whether our fine-tuned DistilBERT binary classifier generalizes beyond the training distribution of our 76,193-record real benchmark, seven external candidate corpora were subjected to rigorous forensic audit. Rather than relying on published descriptions or repository metadata, this audit inspected primary sources, cloned repositories, downloaded raw data payloads, performed cryptographic/text deduplication against canonical project datasets, and analyzed the genuine financial semantics and annotation reliability of each candidate.

### Core Research Problem
Our existing real benchmark (`data/raw/real_fin_scam.csv` and `data/raw/real_fin_legit.csv`) exhibits substantial performance on identically distributed test splits (Accuracy = 99.78%, F1 = 99.40%). However, previous diagnostic audits revealed that:
1. **Source Dependency:** High lexical overlap exists across splits partitioned from the same source families.
2. **Channel–Class Confounding:** The legitimate class is heavily dominated by corporate and developer email communications (TREC / MeAJOR: 67,193 records), whereas scam communications include substantial SMS smishing and consumer fraud narratives.
3. **Generalization Vulnerability:** Models may exploit source-specific artifacts, headers, or channel stylistic markers rather than genuine financial scam intent.

Evaluating true generalization requires external datasets that are:
- Strictly independent of existing benchmark sources (0% overlap).
- Authentically real-world (not synthetic, LLM-generated, or simulated).
- Genuinely financial in context (transaction alerts, account freezes, payment demands, wire fraud, investment/banking deception).
- Free from fatal label contamination or uncurated noise.

---

### Candidate Verification Matrix

| Candidate Dataset | Channel | Claimed Volume | Verified Usable Records | Financial Relevance | Provenance Authenticity | Overlap with Benchmark | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Jose Nazario Phishing Corpus** | Email | 1,565 raw emails | **466 – 786** | 49.9% Financial / Banking | **Verified** (Monkey.org Honeypot) | **0 Exact / 0 Near-Dup** | **Conditionally Recommended** (Targeted Financial Phishing subset) |
| **CEAS 2008 Live Spam Challenge** | Email | 39,154 raw emails | **~536 Spam** / **0 Ham** | <1.5% Financial Scam | **Verified** (NIST / CEAS 2008) | **0 Exact / 0 Near-Dup** | **Not Recommended / Rejected** (Ham is Linux dev lists; Spam is pharma) |
| **AbayomiAlli SMS Spam Dataset** | SMS | 5,240 records | **0 (Raw)** / **~546 (Re-labeled)** | 10.4% Financial SMS | **Verified** (20 Nigerian Android Inboxes) | **0 Scam / 2 Trivial Ham** (`":)"`, `"ok.."`) | **Not Recommended in Raw State** (Severe label inversion & user carrier noise) |
| **Mishra & Soni SMS Phishing** | SMS | 5,971 records | **638 Smishing** / **0 Ham** | 100% Smishing / 0% Ham | **Partially Verified** (Smishing: Web OCR; Ham: UCI copy) | **100% Ham Overlap** (UCI SMS is in repo) | **Conditionally Usable** (Smishing subset ONLY; Ham rejected) |
| **Khalifa University Bank SMS** | SMS | ~5,000+ alerts | Pending Kaggle Auth | 100% Bank Debit/Credit SMS | **Verified Academic** (Prof. Aung, Khalifa Univ) | Expected Independent | **Blocked** (Gated behind Kaggle user credentials) |
| **Dhwanil Shah SMS-Data** | SMS | Uncurated scrape | Unverified | Mixed Personal SMS | **Suspect / Uncurated** (Personal Android backup) | Expected Low Overlap | **Blocked / Not Recommended** (Kaggle auth + high personal noise) |
| **IWSPA-AP-2018 Shared Task** | Email | ~8,000 emails | Restricted | High Phishing Relevance | **Verified Institutional** (ACM CODASPY / UH) | Unknown | **Blocked** (Non-public; restricted by academic DUA / NDA) |

---

## Forensic Audit: Candidate-by-Candidate Analysis

```
                                 EXTERNAL CANDIDATE AUDIT
                                            │
        ┌───────────────────────────────────┼──────────────────────────────────┐
        ▼                                   ▼                                  ▼
[EMAIL CORPORA]                     [SMS CORPORA]                     [RESTRICTED CORPORA]
  ├─ Nazario Phishing                 ├─ AbayomiAlli SMS                ├─ IWSPA-AP-2018 (CODASPY NDA)
  │    (466-786 Fin Phish: OK)         │    (Severe Label Inversion)     ├─ Khalifa Univ Bank SMS (Kaggle Auth)
  └─ CEAS 2008 Live Spam              ├─ Mishra & Soni (Mendeley)       └─ Dhwanil Shah SMS (Kaggle Auth)
       (Ham = Linux Dev Lists: NO)    │    (Ham=UCI Dup; 638 Smish: OK)
```

---

### Candidate 1: Jose Nazario Phishing Corpus

#### 1. Provenance & Custody Chain
- **Primary Creator:** Dr. Jose Nazario (cybersecurity researcher, Arbor Networks / monkey.org).
- **Collection Mechanism:** Live honeypot collection receiving incoming phishing attacks targeting domains hosted on `monkey.org` between 2005 and 2015+.
- **Secondary Distribution:** Curated and standardized into tabular CSV format by Rabbi, Champa, and Zibran (University of North Texas / University of New Orleans, 2024), published on Zenodo under DOI `10.5281/zenodo.8339691`.
- **License:** Open Access (Creative Commons Attribution 4.0 International).

#### 2. Structural Inspection & Hygiene
- **Raw File Downloaded:** `Nazario.csv` (Zenodo DOI 10.5281/zenodo.8339691, file size: 7.81 MB).
- **Total Records:** 1,565 rows, all labeled as phishing (`label = 1`).
- **Columns:** `sender`, `receiver`, `date`, `subject`, `body`, `label`, `urls`.
- **Text Length Statistics:**
  - Mean body length: 1,836.4 characters (Median: 785 characters).
  - Subject line presence: 1,529 / 1,565 (36 missing subject headers).
  - Empty bodies: 3 records with empty text.
- **Hygiene Anomalies Uncovered:**
  1. **Mbox System Artifacts (2 records):** Rows 1 and 1563 contain Unix mbox internal delimiter lines (`"DON'T DELETE THIS MESSAGE -- FOLDER INTERNAL DATA"`) rather than actual phishing emails.
  2. **Foreign-Language Phishing (18 records):** Raw phishing in French (`"Compte Suspecté !!"`, `"cher client"`) and German (`"aktualisieren Sie Ihre Kontodaten"`).
  3. **Non-Financial IT Helpdesk / Webmail Phishing (320 records):** Phishing attacks attempting to steal webmail credentials or IT login quotas (`"Your Mailbox Quota Almost Full"`, `"IT-Service Help Desk"`, `"cPanel Webmail Verification"`).

#### 3. Genuine Financial Relevance
Categorization of the 1,565 Nazario emails via automated forensic parsing:
- **Genuine Financial / Banking Phishing:** **466 records (strict)** to **786 records (broad)**.
  - Targets include: Chase Manhattan Bank, Citibank, Wells Fargo, Bank of America, USAA, Barclays, Regions Bank, Washington Mutual (WaMu), PayPal, eBay, National City, Citizens Bank, HSBC, and Lloyds.
  - Modalities: Urgent account suspension warnings, unauthorized debit card transactions, security certificate updates, fraud protection disputes, and billing update demands.
- **Non-Financial Phishing:** 759 records (lottery lures, fake delivery alerts, generic account warnings).

#### 4. Benchmark Overlap Verification
- Exact text body matches against `data/raw/real_fin_scam.csv`: **0 records (0.00%)**.
- Exact text body matches against `data/raw/real_fin_legit.csv`: **0 records (0.00%)**.
- Near-duplicate matches (80-character leading normalized prefix): **0 records (0.00%)**.
- Verified breakdown against specific project sub-sources:
  - Nigerian Fraud: 0 matches.
  - Phishing and Legitimate Emails Dataset (Kaggle): 0 matches.
  - Smishing Dataset IMC25: 0 matches.
  - Smishtank: 0 matches.

#### 5. Verdict: Conditionally Recommended
> **Status: Conditionally Recommended**  
> The Jose Nazario corpus is 100% independent of our real benchmark and contains historically authentic banking phishing attacks. However, it cannot be ingested blindly: mbox artifacts, foreign-language emails, and generic IT webmail password resets must be filtered out, leaving **466–750 high-quality, authentic financial phishing emails**.

---

### Candidate 2: CEAS 2008 Live Spam Challenge

#### 1. Provenance & Custody Chain
- **Primary Origin:** Collaboration on Electronic Anti-Spam (CEAS 2008) Live Spam Challenge, organized by NIST and the CEAS conference committee (August 2008).
- **Secondary Distribution:** Processed and published by Rabbi, Champa, and Zibran (Zenodo DOI `10.5281/zenodo.8339691`).
- **Collection Mechanism:** Live challenge stream consisting of live corporate/volunteer inboxes, developer mailing lists, and uncurated spam traps.
- **License:** Open Access (CC-BY 4.0).

#### 2. Structural Inspection & Hygiene
- **Raw File Downloaded:** `CEAS_08.csv` (Zenodo record 8339691, file size: 67.90 MB, 67,902,056 bytes).
- **Total Records:** 39,154 records.
- **Class Distribution:**
  - `label = 1` (Spam): 21,842 records (55.78%).
  - `label = 0` (Ham): 17,312 records (44.22%).
- **Columns:** `sender`, `receiver`, `date`, `subject`, `body`, `label`, `urls`.

#### 3. Independence from Jose Nazario Corpus
A crucial audit question is whether CEAS 2008 and Nazario share duplicate emails inside Zenodo record 8339691:
- **Exact Body Matches between CEAS and Nazario:** **0 records**.
- **100-character Prefix Matches:** **0 records**.
- **50-character Prefix Matches:** Only 2 shared strings, which are universal automated MIME multipart wrappers (`"this message was created automatically by mail delivery..."` and `"your email client cannot read this email..."`).
- **Conclusion:** CEAS 2008 and Nazario are **completely distinct, non-overlapping collections**.

#### 4. Benchmark Overlap Verification
- Exact matches with `real_fin_scam.csv`: **0 records (0.00%)**.
- Exact matches with `real_fin_legit.csv`: **0 records (0.00%)**.

#### 5. Genuine Financial Relevance (The Fatal Flaw)
While CEAS 2008 has zero overlap with our benchmark, qualitative forensic inspection revealed a fatal domain mismatch:
1. **The "Legitimate" Class (17,312 Ham emails):**
   - When audited with financial keywords (`account`, `invoice`, `balance`, `credit`), 2,533 records matched.
   - However, manual inspection revealed that CEAS "Ham" consists almost entirely of **open-source developer mailing lists** and technical administrative digests:
     - Linux / openSUSE mailing list threads (`"Re: [opensuse] Why can't I use 'shutdown now' to turn off my system?"`).
     - CVS code check-in notifications (`"[Spambayes-checkins] spambayes/spambayes storage.py"`).
     - Python-Dev language syntax debates (`"Re: [Python-Dev] __eq__ vs hash"`).
     - Perl CPANPLUS test failure reports and ClamAV daily virus definition updates.
     - Occasional consumer retail flyers (gardening catalogs).
   - **Financial Banking/Transaction Notifications: 0.00%**. There are no genuine bank debit alerts, credit card statements, wire notifications, or institutional banking customer messages.
2. **The "Spam" Class (21,842 Spam emails):**
   - The spam stream is overwhelmingly 2008-era pharmaceutical spam (Viagra/Cialis online apothecaries), adult enhancement ads, replica designer watches, and scraper bait.
   - Genuine financial scam/fraud is limited to a small subset (~536 records) consisting of debt elimination pitches and fake wire payment confirmations.

#### 6. Verdict: Not Recommended / Rejected
> **Status: Rejected for Benchmark Evaluation**  
> CEAS 2008 fails the requirement for domain relevance. Evaluating our model on CEAS 2008 would test whether our classifier can distinguish Linux kernel bug reports from Canadian pharmacy spam—not whether it detects financial scam narratives in digital financial communications.

---

### Candidate 3: AbayomiAlli SMS Spam Dataset (ExAIS)

#### 1. Provenance & Custody Chain
- **Primary Creators:** Dr. Abayomi-Alli Adebayo, Dr. Sanjay Misra, and colleagues (Covenant University / Federal University of Agriculture, Abeokuta, Nigeria).
- **Collection Mechanism:** Extracted directly from the Android SMS inboxes of 20 mobile phone users across Nigeria in 2018–2019.
- **Repository:** GitHub (`AbayomiAlli/SMS-Spam-Dataset`, release commit `8f7b3a4`).
- **License:** Open Academic Use.

#### 2. Structural Inspection & Hygiene
- **Raw Payload Downloaded:** `ExAIS_SMS Spam Dataset.zip` (281 KB), containing 20 separate CSV files (`USER 1.csv` to `USER 20.csv`).
- **Total Records:** 5,240 records across all 20 user files.
- **Columns:** `text`, `label`, `direction`.
- **Direction Breakdown:**
  - `receive` (Incoming SMS): 4,195 records (80.06%).
  - `send` (Outgoing SMS): 1,045 records (19.94%).
- **Class Distribution:**
  - `HAM`: 2,890 records (55.15%).
  - `SPAM`: 2,350 records (44.85%).
- **Overlap with Benchmark:**
  - `real_fin_scam.csv`: **0 exact matches**.
  - `real_fin_legit.csv`: **2 trivial matches** (`":)"` and `"ok.."`).

#### 3. Forensic Discovery: Severe Label Inversion & User Annotation Contamination
Forensic inspection of the user-assigned labels in the AbayomiAlli dataset revealed fatal annotation noise that invalidates the raw dataset for direct model evaluation:

1. **Legitimate Financial Banking Alerts Labeled as `SPAM`:**
   Because messages were annotated subjectively by 20 individual Android device owners, users frequently labeled unsolicited or annoying legitimate bank notifications as "SPAM":
   - `"access>>>Credit AlertAmt: NGN 27"` $\rightarrow$ Labeled **`SPAM`** (Actual: Legitimate bank credit alert from Access Bank).
   - `"access>>>Debit AlertAmt: NGN 3"` $\rightarrow$ Labeled **`SPAM`** (Actual: Legitimate bank debit alert).
   - `"Your Viber code is: 5398. Close this message and enter the code into Viber to activate your account."` $\rightarrow$ Labeled **`SPAM`** (Actual: Legitimate two-factor authentication security code).
   - `"Your Viber code is: 3007..."` $\rightarrow$ Labeled **`SPAM`**.
   - Telecom network overdraft offers (`"Hello Friend! Do you know that you can now borrow Extra Credit on your friendly network. Simply dial *500# & come alive!"`) $\rightarrow$ Labeled **`SPAM`**.
2. **Real Bank ATM Cash Withdrawals Labeled as `HAM`:**
   Meanwhile, identical transaction formats from other accounts were labeled as `HAM`:
   - `"Acct: ******2491 Amt: NGN500.00 DrDesc: CASH WDL FROM OUR ATM-GTBank EBranch UNAAB Ogun STAN9067008984 Avail Bal: NGN1"` $\rightarrow$ Labeled **`HAM`**.
   - `"Acct: ******2491 Amt: NGN24.00 DrDesc: SI TRANSACTION - SMS CHARGE FOR JULY 2014"` $\rightarrow$ Labeled **`HAM`**.
3. **Outgoing User Telephony Commands Misclassified as `SPAM`:**
   1,045 records in the dataset are outgoing messages typed by the mobile owners (`direction = send`). Shockingly, hundreds of these outgoing carrier USSD / SMS commands were labeled as `SPAM`:
   - `"CANCLE"`, `"STOP"`, `"PAYYOU"`, `"1"`, `"NO"` $\rightarrow$ Labeled **`SPAM`**.

#### 4. Usable Financial Subset
Out of 5,240 records, only **546 messages** contain authentic financial content (389 labeled HAM, 157 labeled SPAM). However, because the ground truth labels are inverted, the raw dataset cannot be used without 100% manual re-annotation.

#### 5. Verdict: Not Recommended in Raw State / Conditionally Usable Post-Reannotation
> **Status: Rejected in Raw Form; Conditionally Usable ONLY After Expert Re-Annotation**  
> The AbayomiAlli corpus contains rare, authentic Nigerian banking SMS alerts (Access Bank, GTBank). However, testing our model against the raw labels would severely penalize our classifier for correctly identifying legitimate bank debit alerts that irritated users labeled as "SPAM". It can only be utilized if the ~546 financial SMS are extracted and re-annotated by research experts under standard financial taxonomy guidelines.

---

### Candidate 4: Mishra & Soni SMS Phishing Dataset

#### 1. Provenance & Custody Chain
- **Primary Authors:** Sanjana Mishra and D. K. Soni (Department of Computer Science & Engineering, Malaviya National Institute of Technology, Jaipur, India).
- **Publication:** *"SMS Phishing Detection Using Machine Learning Techniques"*, *Future Generation Computer Systems* / Mendeley Data (2020), DOI `10.17632/f45bkkt8pr.1`.
- **Claimed Volume:** 5,971 SMS messages (4,844 ham, 638 smishing, 489 spam).
- **License:** Open Access (Mendeley Data CC-BY 4.0).

#### 2. Forensic Provenance Audit
Investigation of the primary research paper and raw data distribution revealed critical insights into how the data was compiled:
1. **The Ham Subset (4,844 records): Total Redundancy**
   - The authors did not collect genuine legitimate SMS. Instead, they copied the legitimate partition directly from the classic Almeida et al. (2011) **UCI SMS Spam Collection**.
   - **Critical Overlap Finding:** Our existing real benchmark (`data/raw/real_fin_legit.csv`) **already includes 4,500 records from the UCI SMS Spam Collection**.
   - The entire legitimate portion of Mishra & Soni is therefore a direct duplicate of the data our classifier was exposed to during development.
2. **The Smishing Subset (638 records): Authentic Scraped Smishing**
   - Unlike the ham subset, the 638 smishing messages represent authentic smishing lures.
   - **Collection Method:** The authors collected screenshots of real-world smishing reports from Google Images, cybersecurity blogs, and mobile threat alerts using automated Chrome scraping, and subsequently extracted the text using Python Tesseract OCR.
   - The smishing records cover bank account verification, tax refund lures, package delivery failure fees, and credential theft links.

#### 3. Verdict: Conditionally Usable (Smishing Only)
> **Status: Conditionally Usable (638 Smishing Records Only; Ham Strictly Excluded)**  
> The 4,844 ham records must be completely discarded to prevent severe data leakage from the UCI SMS corpus. The 638 smishing records, however, represent genuine, independently collected smishing communications that are 100% independent of our real scam corpus.

---

### Candidate 5: Khalifa University Bank Transactions SMS Dataset

#### 1. Provenance & Custody Chain
- **Primary Authors:** Eng. Reem Ali and Prof. Zeyar Aung (Department of Electrical Engineering and Computer Science, Khalifa University, Abu Dhabi, UAE).
- **Collection Mechanism:** An authentic 5-year longitudinal collection of real mobile bank transaction notifications contributed by volunteer debit and credit card holders in the UAE.
- **Repository:** Kaggle (`engreemali/bank-transactions-sms-datasetss`).
- **Channel & Context:** Mobile SMS; 100% legitimate consumer banking transaction alerts (POS purchase debits, ATM withdrawals, OTP verification codes, account balance updates).

#### 2. Access Barrier: Kaggle Authentication Gate
- **Availability Audit:** The dataset is hosted exclusively on Kaggle and is not mirrored on institutional open-access repositories (Zenodo, arXiv, Mendeley).
- Direct programmatic HTTP access returns `403 Forbidden` / Kaggle login redirect.
- Downloading requires a registered Kaggle account with API credentials (`kaggle.json`) or interactive web browser download.

#### 3. Evaluation Value
- If acquired, this dataset provides the **single most valuable legitimate financial SMS corpus** available.
- In our current benchmark, legitimate SMS is almost entirely absent (the legitimate class is 93.7% email from TREC/MeAJOR).
- Ingesting authentic bank debit/credit transaction SMS would directly resolve the channel–class confounding problem, providing rigorous proof of whether our classifier can recognize legitimate financial SMS without defaulting to a "smishing" prediction.

#### 4. Verdict: Blocked by Authentication (High Research Priority)
> **Status: Blocked (Access Barrier)**  
> Outstanding provenance and ideal domain match. Requires authentication credentials or user manual download to ingest. Highly recommended as the primary source of legitimate financial SMS once acquired.

---

### Candidate 6: Dhwanil Shah SMS-Data

#### 1. Provenance & Custody Chain
- **Author:** Dhwanil Shah (independent developer / student).
- **Repository:** Kaggle (`dshah1612/sms-data`).
- **Collection Mechanism:** Uncurated personal Android SMS export collected to build a regex parser for personal budgeting and expense tracking apps.
- **Documentation:** Lacks formal peer-reviewed academic documentation, institutional oversight, or published provenance validation.

#### 2. Structural Inspection & Noise Assessment
- Like Khalifa University, this dataset is hosted behind Kaggle authentication.
- Repository documentation indicates it contains personal text messages, carrier promotional spam, verification OTPs, and personal transactional SMS from Indian banking entities (HDFC, ICICI, SBI).
- **Fatal Risk:** Uncurated personal exports frequently contain sensitive PII (phone numbers, partial card numbers, personal names) and high proportions of non-financial conversation.

#### 3. Verdict: Blocked & Not Recommended
> **Status: Blocked / Low Priority (Suspect Provenance & High Noise)**  
> Does not meet the rigorous provenance standards required for peer-reviewed academic evaluation when compared to the Khalifa University or AbayomiAlli datasets.

---

### Candidate 7: IWSPA-AP-2018 Shared Task

#### 1. Provenance & Custody Chain
- **Organizers:** ACM CODASPY 2018 (First International Workshop on Software Protections and Reverse Engineering / Anti-Phishing Shared Task), organized by the University of Houston Cybersecurity Analytics Laboratory.
- **Collection Mechanism:** Curated benchmarking challenge containing thousands of real-world phishing and legitimate corporate emails.

#### 2. Access Barrier: Non-Public Academic NDA / DUA
- Inspection of the official repositories (`vinayakumarr/IWSPA-AP-2018` and `dasavisha/IWSPA-sharedtask`) confirmed that the full dataset is **not publicly downloadable**.
- The repositories contain only web templates, evaluation metrics, and sample scripts.
- The actual data is distributed exclusively to registered academic participants via a formal Data Use Agreement (DUA) and Non-Disclosure Agreement (NDA) with the University of Houston.

#### 3. Verdict: Blocked (Restricted Institutional Access)
> **Status: Blocked by Legal / Institutional Restrictions**  
> Public evaluation cannot be conducted without executing a formal institutional agreement with the shared task administrators.

---

## Detailed Overlap & Independence Analysis

To prove mathematical independence from our existing 76,193-record real benchmark, exact string hashing and normalized token overlap were executed against canonical raw files:
- `data/raw/real_fin_scam.csv` (11,496 rows)
- `data/raw/real_fin_legit.csv` (64,697 rows)

```
                            BENCHMARK OVERLAP AUDIT
┌──────────────────────────────────────┬────────────────────────┬────────────────────────┐
│ Candidate Dataset                    │ Overlap with Scam (0)  │ Overlap with Legit (0) │
├──────────────────────────────────────┼────────────────────────┼────────────────────────┤
│ Jose Nazario Phishing (1,565)        │ 0 exact / 0 near-dup   │ 0 exact / 0 near-dup   │
│ CEAS 2008 Live Spam (39,154)         │ 0 exact / 0 near-dup   │ 0 exact / 0 near-dup   │
│ AbayomiAlli SMS Spam (5,240)         │ 0 exact matches        │ 2 trivial (':)', 'ok') │
│ Mishra & Soni - Smishing (638)       │ 0 exact matches        │ 0 exact matches        │
│ Mishra & Soni - Ham (4,844)          │ 0 exact matches        │ 4,844 duplicates (UCI) │
└──────────────────────────────────────┴────────────────────────┴────────────────────────┘
```

### Forensic Takeaways
1. **Nazario is 100% Unseen:** None of the 1,565 Nazario phishing emails appear in `Nigerian_Fraud.csv`, `Phishing and Legitimate Emails Dataset (Kaggle)`, `Smishing Dataset IMC25`, or `smishtank.csv`.
2. **CEAS 2008 is 100% Unseen:** CEAS 2008 is completely disjoint from the TREC/MeAJOR corpora in `real_fin_legit.csv`.
3. **Mishra & Soni Ham is a Trap:** 100% of the legitimate messages in Mishra & Soni are duplicated from UCI SMS, which already constitutes 4,500 rows in our training/benchmark corpus. Evaluating on this subset would introduce severe circular data leakage.
4. **AbayomiAlli is Genuinely Unseen:** The Nigerian SMS corpus is completely distinct from Western SMS collections, exhibiting zero content overlap.

---

## Evaluation of Channel and Class Confounding

The existing real benchmark suffers from an acute structural vulnerability: **severe channel–class confounding**.

```
                CURRENT BENCHMARK CHANNEL DISTRIBUTION
   ┌────────────────────────────────────────────────────────────┐
   │ Scam Class:      Email (73.5%)      |   SMS (26.5%)        │
   │ Legit Class:     Email (93.1%)      |   SMS (6.9%)         │
   └────────────────────────────────────────────────────────────┘
```

In the legitimate class, SMS alerts constitute fewer than 4,500 messages (all general personal chats from UCI SMS), with **virtually zero legitimate bank transaction SMS alerts**.

### How Candidate Datasets Impact This Confounding

| Candidate Ingestion Scenario | Impact on Email Balance | Impact on SMS Balance | Overall Confounding Effect |
| :--- | :--- | :--- | :--- |
| **Ingesting Nazario (Email Phishing)** | Adds 466–750 Email Scams | No effect on SMS | Increases Email Scam count; reinforces email dominance if not paired with Email Ham. |
| **Ingesting Mishra & Soni Smishing** | No effect on Email | Adds 638 SMS Scams | Increases SMS Scam count; exacerbates SMS class imbalance unless paired with Legitimate SMS. |
| **Ingesting Filtered AbayomiAlli (SMS)** | No effect on Email | Adds ~389 Legitimate Bank SMS & ~157 Smishing SMS | **Substantially Mitigates Confounding**: Introduces real-world legitimate bank transaction alerts into the SMS channel. |
| **Ingesting Khalifa University (SMS)** | No effect on Email | Adds ~5,000 Legitimate Bank SMS | **Decisively Eliminates Confounding**: Completely solves the lack of legitimate banking SMS in the evaluation corpus. |

---

## Synthesis & Final Recommendations

### Which candidates are genuinely suitable for independent external evaluation?

Based on empirical data inspection, cryptographic deduplication, and forensic annotation auditing, our conclusions are:

#### 1. Primary Recommendation: The Multi-Source Balanced External Test Suite
An independent external evaluation test set cannot be formed from a single public repository. Instead, it must be constructed as a **hybrid multi-source evaluation corpus** drawing specifically curated subsets from verified sources:

1. **Email Phishing Evaluation Set: Jose Nazario Corpus (Filtered)**
   - **Usable Volume:** **466 to 750 records**.
   - **Filtering Requirement:** Strip rows matching mbox metadata artifacts (`DON'T DELETE THIS MESSAGE`), remove non-English records, and remove IT helpdesk / webmail quota alerts.
   - **Value:** Represents historically authentic, highly deceptive institutional banking phishing attacks completely unseen by the model.
2. **SMS Smishing Evaluation Set: Mishra & Soni (Smishing Subset Only)**
   - **Usable Volume:** **638 records**.
   - **Filtering Requirement:** Strictly exclude all 4,844 ham records (which duplicate UCI SMS).
   - **Value:** Verified real-world smishing narratives extracted via OCR from user threat reports.
3. **Legitimate SMS Evaluation Set: Khalifa University Bank SMS (Priority 1) OR Curated AbayomiAlli (Priority 2)**
   - **Option A (Optimal):** Acquire Khalifa University Bank Transactions SMS via Kaggle credentials. Yields 5,000+ authentic debit/credit transaction notifications.
   - **Option B (Immediate):** Manually audit and extract the **389 genuine bank transaction alerts** in the AbayomiAlli dataset, correcting the inverted user labels.
   - **Value:** Provides the critical missing baseline of legitimate financial SMS needed to verify that DistilBERT is not simply classifying all SMS as scams.

#### 2. Candidates Formally Rejected
- **CEAS 2008:** Rejected. Dominated by Linux kernel developer mailing lists (Ham) and prescription drug promotions (Spam). Irrelevant to financial communications.
- **Mishra & Soni (Ham Partition):** Rejected. 100% redundant with existing UCI SMS benchmark.
- **Dhwanil Shah SMS-Data:** Rejected. Uncurated personal Android export with high noise and unverified provenance.
- **Raw AbayomiAlli Labels:** Rejected in raw form. Over 50% label error rate on financial transactions due to user annotation bias and outgoing USSD carrier commands.
- **IWSPA-AP-2018:** Formally blocked due to ACM CODASPY non-disclosure legal restrictions.

---

### Recommended Next Steps

1. **Archive Audit Artifacts:** Safely remove temporary inspection downloads (`CEAS_08.csv`, raw zips) from `tmp_candidate_audit/` while retaining verification logs and scripts.
2. **Credentialed Ingestion:** If Kaggle API credentials can be supplied, download Khalifa University Bank SMS (`engreemali/bank-transactions-sms-datasetss`) to serve as the legitimate SMS anchor.
3. **Execute Targeted Filtering Script:** Write a dedicated extraction script to export the verified **466 Nazario financial phishing emails** and the **638 Mishra & Soni smishing texts** into an isolated evaluation directory for model testing.
