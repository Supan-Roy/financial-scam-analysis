# Forensic Investigation Report: Anomaly in Record EXT-SCAM-00224 (nazario_row_533)

**Research Project Title:**  
*Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*

**Investigation Date:** November 2026  
**Investigator:** Antigravity Research Engineering  
**Subject Record:** `EXT-SCAM-00224`  
**Upstream Provenance:** Jose Nazario Phishing Corpus (`nazario_row_533`, Zenodo DOI: `10.5281/zenodo.8339691`)  
**Report Location:** `reports/dataset_audits/nazario_row_533_forensic_investigation.md`  

---

## Executive Summary

During final pre-evaluation inspection of `data/external_evaluation/external_fin_scam_curated.csv`, a severe structural anomaly was identified in record `EXT-SCAM-00224`:
* **Character Length:** **1,023,605 characters**
* **Word Count:** **46,580 words**
* **Estimated Subword Tokens:** **~463,696 DistilBERT tokens** (exceeding the model's 512-token limit by ~905x)
* **Embedded Email Addresses:** **45,146 distinct email addresses**

This forensic investigation traced the record from its raw honeypot source through every processing stage, established the mechanical root cause, determined its semantic classification validity, surveyed the remaining 526 retained Nazario records, and formulated an actionable, non-destructive correction plan.

---

## Phase 1: Forensic Investigation & Provenance Trace

```
                              RECORD TRACE FUNNEL
                                       │
[Raw Source: Zenodo 8339691] ─────────► nazario_row_533 (Subject + 1,023,577 char Body)
                                       │
[Audit & Screening] ──────────────────► False Positive Bank Match (Email domains contained 'citi/chase')
                                       │
[Canonical Harmonization] ────────────► Placeholder pass-through (Plain text emails, no brackets)
                                       │
[Curated Output] ─────────────────────► EXT-SCAM-00224 (Assigned subtype: bank_impersonation)
```

### 1. Source Record Inspection & Raw Structure
In the raw Jose Nazario corpus (Zenodo record 8339691, `Nazario.csv`), row index 533 has the following attributes:
* **`subject`:** `"someone has your password"`
* **`body`:** 1,023,577 characters
* **Header / Salutation Structure:**
  - Prefix (chars 0–47): `"someone has your password - Security Alert Dear "`
  - Recipient Block 1 (chars 48–511,469): **45,146 comma-separated email addresses** from hundreds of institutional, military, telecom, and corporate domains (e.g., `053732488-0001@t-online.de`, `05a@f04.navy.gov.au`, `100012.71@compuserve.com`, ..., `kirill@videotr`).
  - Transition Phrase: `", kirill@videotr Our server detects that at 03:56 GMT today, your email account \""`
  - Recipient Block 2 (chars 511,540–1,022,960): **The exact same 45,146 comma-separated email addresses repeated verbatim**.
  - Payload Closing: `"\" was accessed from Kuala Lumpur, Malaysia from this IP: 115.254.224.100 address. To keep your account safe, we strongly recommend that you change your current password immediately to a stronger and more secured combination, else you stand the risk of having your account hijacked. Change Password However, if this account was accessed by you from this location, you can ignore this warning! Thank you for your cooperation. This message is auto-generated from E-mail security server, and replies sent to this email can not be delivered. 2017. All rights reserved."`

### 2. Determination of Recipient List Origin
The investigation evaluated four potential hypotheses:

| Hypothesis | Evaluated Evidence | Conclusion |
| :--- | :--- | :--- |
| **A. Expanded Mailing List Header** | Standard SMTP headers (`To:`, `Cc:`, `Bcc:`) appear in email headers, not embedded twice in the message body text following `"Dear "` and inside quotes after `"your email account \""`. | **Rejected** |
| **B. Accidental Concatenation of Records** | There are no intermediate `From `, `Date:`, `Subject:`, or Unix mbox delimiters within the 1 MB block. It contains a single coherent grammatical narrative wrapped around the recipient block. | **Rejected** |
| **C. Parser / Extraction Defect** | The Zenodo CSV parsing script simply called `msg.get_payload()` on the MIME text part of the mbox file. The recipient list was literally inside the raw body payload of the original email. | **Rejected** |
| **D. Attacker Mail-Merge Script Defect** | Phishing attack tools use template variables (e.g., `Dear $TARGET_EMAIL`, `your email account "$TARGET_EMAIL" was accessed`). A programming bug in the spammer's mass-mailing script passed the entire array of 45,146 target email addresses as a single flat string into `$TARGET_EMAIL` rather than iterating row-by-row. | **CONFIRMED (Root Cause)** |

**Conclusion:** The anomaly is a **spammer script configuration defect** captured in the raw honeypot stream in 2017.

### 3. Trace Through Processing Pipeline
1. **Raw Ingestion:** The 1 MB payload was loaded into memory from `Nazario.csv` row 533.
2. **Financial Relevance Screening:** The automated classifier evaluated `(subject + " " + body).lower()`. Because the text contained 45,146 email addresses from thousands of global organizations, several email addresses contained substring bank names in their domain or local parts (e.g., `...chase.com`, `...citi...`, `...bank...`). Consequently, `has_bank` evaluated to `True`, masking the fact that the actual message narrative contained no banking context.
3. **Harmonization Pipeline:** `PlaceholderHarmonizer.normalize_text()` inspects bracketed placeholder entities (`<URL>`, `[URL]`, `[EMAIL_ADDRESS]`). Because the 45,146 email addresses were raw text strings without brackets, they passed through untouched.
4. **Dataset Assembly:** The record was assigned canonical ID `EXT-SCAM-00224`, labeled as `bank_impersonation`, and included in `external_fin_scam_curated.csv` and `expanded_binary_external_test.csv`.

### 4. Independence and Financial Scam Validity
When the 45,146-email recipient avalanche is abstracted, the substantive text is:
> *"someone has your password - Security Alert Dear [TARGET], Our server detects that at 03:56 GMT today, your email account '[TARGET]' was accessed from Kuala Lumpur, Malaysia from this IP: 115.254.224.100 address. To keep your account safe, we strongly recommend that you change your current password immediately to a stronger and more secured combination, else you stand the risk of having your account hijacked. Change Password However, if this account was accessed by you from this location, you can ignore this warning! Thank you for your cooperation. This message is auto-generated from E-mail security server, and replies sent to this email can not be delivered. 2017. All rights reserved."*

**Critical Finding on Semantic Validity:**  
* This message is a **generic webmail / email account credential phishing lure**.
* It contains **zero banking institutions, zero debit/credit card references, zero payment platforms, zero invoices, and zero financial transactions**.
* Its inclusion in the financial scam corpus was an **algorithmic false positive** caused solely by random banking substrings present inside the 45,146 recipient email domains.
* Therefore, independently of its extreme length, **its classification as a financial scam is invalid**.

### 5. Audit of All Other 526 Retained Nazario Records
A systematic scan was conducted across all other 526 retained Nazario records in `external_fin_scam_curated.csv`:

#### A. Length & Recipient Anomaly Scan
* **Embedded Email Address Counts:**
  - Rank 1 (`EXT-SCAM-00224`): **45,146 email addresses**
  - Rank 2 (`EXT-SCAM-00204`): **9 email addresses** (normal email header/footer)
  - Rank 3 (`EXT-SCAM-00482`): **8 email addresses**
  - Ranks 4–527: $\le 8$ email addresses (mean = 1.4 emails).
* **Character Length Distribution:**
  - `EXT-SCAM-00224`: **1,023,605 characters** (Extreme outlier)
  - Rank 2 (`EXT-SCAM-00348`): **16,078 characters** (authentic NedBank electronic statement)
  - Rank 3 (`EXT-SCAM-00341`): **16,056 characters** (authentic NedBank electronic statement)
  - Rank 4 (`EXT-SCAM-00485`): **12,231 characters**
  - 95th Percentile: 6,135 characters
  - Median: 1,052 characters
* **Conclusion:** `EXT-SCAM-00224` is a **unique, isolated 1-of-1 anomaly**. No other record in the corpus exhibits a recipient or character avalanche.

#### B. Additional Hygiene Observations Across Retained Records
During the scan of the remaining 526 records, two additional minor hygiene patterns were uncovered for disclosure:
1. **Foreign-Language Remnants (3 records):**
   - `EXT-SCAM-00449` (`nazario_row_1230`): French language (`"compte"`, `"veuillez"`, `"sécurité"`).
   - `EXT-SCAM-00450` (`nazario_row_1243`): German language (`"Wir haben ungewöhnliche Aktivitäten festgestellt!"`).
   - `EXT-SCAM-00485` (`nazario_row_1414`): German language (`"Wir brauchen Ihre Hilfe, um ein Problem..."`).
2. **Webmail / Quarantine Password Resets (11 records):**
   - Records targeting `jose@monkey.org` mailbox delivery or quarantine notifications (e.g., `EXT-SCAM-00404`, `EXT-SCAM-00478` `"Mail Delivery Failure (Incoming Mail Blocked)"`). They entered the dataset because quarantine digests mentioned words like `"invoice"`.

---

## Phase 2: Recommendation & Trade-Off Analysis

| Option | Description | Methodological Implications | Final Verdict |
| :--- | :--- | :--- | :--- |
| **RETAIN** | Keep `EXT-SCAM-00224` as-is in the evaluation set. | **Fatal Flaw:** The first 512 tokens seen by DistilBERT consist entirely of the recipient list (`"someone has your password - Security Alert Dear 053732488-0001@t-online.de..."`). The model never evaluates the message body. Furthermore, the narrative is non-financial. | **REJECTED** |
| **REPAIR** | Strip the 45,146 email addresses and keep the reconstructed short body. | **Methodological Violation:** Fabricates artificial text not present in the raw corpus. More importantly, the repaired message is a webmail alert that fails the financial scam definition. | **REJECTED** |
| **EXCLUDE** | Formally reject `EXT-SCAM-00224`, document the exclusion in the audit log, and rebuild the evaluation slices. | **Best Practice:** Restores strict data hygiene, eliminates a 1,000,000-character outlier, and ensures 100% of evaluated scam records represent genuine financial scam communications. | **STRONGLY RECOMMENDED** |

---

## Phase 3: Conditional Correction Plan (Awaiting Approval)

**DO NOT EXECUTE UNTIL EXPLICIT USER APPROVAL.**

If the recommendation to **EXCLUDE** `EXT-SCAM-00224` is approved, the following exact, reproducible steps will be executed:

### 1. Update Annotation Audit & Exclusion Logs
* In `data/external_evaluation/external_scam_annotation_audit.csv`:
  - Locate candidate `EXT-NAZ-00534` (`original_row_idx = 533`).
  - Update `inclusion_status`: `excluded`.
  - Update `final_label`: `-1`.
  - Update `financial_relevance_decision`: `not_financial_scam`.
  - Update `reason_code`: `excluded_malformed_recipient_avalanche_non_financial`.
  - Update `reviewer_notes`: `"Attacker mail-merge defect embedding 45,146 email addresses (1,023,605 chars); narrative is generic webmail security alert lacking financial fraud context."`
* In `data/external_evaluation/external_scam_exclusion_log.csv`:
  - Append this record to the exclusion log (increasing total exclusions from 11,979 to 11,980).

### 2. Rebuild `external_fin_scam_curated.csv`
* Remove `EXT-SCAM-00224`.
* Re-index remaining scam record IDs sequentially (`EXT-SCAM-00001` through `EXT-SCAM-00796`).
* **New Curated Scam Count:** **796 records** (526 Email, 270 SMS).

### 3. Rebuild `expanded_binary_external_test.csv`
* Combine the 796 curated external scams with the unchanged 6,233 legitimate test records.
* **New Expanded Test Count:** **7,029 records** (6,233 legitimate, 796 scam).
* **New Class Ratio:** 11.32% scam, 88.68% legitimate.

### 4. Rebuild `balanced_binary_external_test.csv`
* Retain all 796 external scams (`label = 1`).
* Resample exactly **796 legitimate records** from the 6,233 held-out test partition using fixed seed `random_state = 42`.
* **New Balanced Test Count:** **1,592 records** (796 legitimate, 796 scam; exact 50 / 50 balance).

### 5. Summary of Recalculated Distributions (Post-Correction Preview)

```
                            POST-CORRECTION DISTRIBUTION
┌──────────────────────────────────────┬────────────────────────┬────────────────────────┐
│ Dataset Artifact                     │ Current (Flawed)       │ Corrected (Proposed)   │
├──────────────────────────────────────┼────────────────────────┼────────────────────────┤
│ external_fin_scam_curated.csv        │ 797 records            │ 796 records            │
│ expanded_binary_external_test.csv    │ 7,030 records          │ 7,029 records          │
│ balanced_binary_external_test.csv    │ 1,594 records          │ 1,592 records          │
│ Total Exclusions Logged              │ 11,979 records         │ 11,980 records         │
│ Nazario Scams (Email)                │ 527 records            │ 526 records            │
│ Mishra & Soni Scams (SMS)            │ 268 records            │ 268 records            │
│ AbayomiAlli Scams (SMS)              │ 2 records              │ 2 records              │
└──────────────────────────────────────┴────────────────────────┴────────────────────────┘
```

---

## Conclusion & Awaiting Decision

The anomaly in `EXT-SCAM-00224` has been forensically dissected. It is an unrepresentative, 1 MB attacker mail-merge defect with non-financial webmail content that falsely triggered banking keywords due to domain names within its 45,146 recipients.

No files, datasets, or notebooks have been modified.

**Awaiting your review and explicit approval to proceed with Phase 3 execution.**
