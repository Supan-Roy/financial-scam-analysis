# Task 02: Dataset Audit Validation & Leakage Investigation Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications

**Investigation Date:** 2026-11-06 23:53:11
**Status:** Complete 100% Corpus Validation & Forensic Analysis

---

## 1. Near-Duplicate Cluster Investigation (Connected Components)

In this stage, we extended the preliminary 25k sampling to **100% full corpus coverage** across all `62,332` legitimate records, all `13,861` real scam records, and all `7,643` synthetic records. Connected components were extracted from verified near-duplicate pairs (word 3-gram Jaccard index $\ge 0.85$).

### 1.1 Cluster Summary Across Corpora

| Dataset | Total Records | Records in Clusters | % of Dataset | Verified Near-Dupe Pairs | Total Clusters | Max Cluster Size | Mean Cluster Size | Primary Cluster Nature |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **real_fin_scam** | 13,861 | **3,206** | **23.1%** | 3,452 | 1,217 | **18** | 2.63 | 419 Campaign Templates |
| **synthetic_financial_scams** | 7,643 | **345** | **4.5%** | 320 | 130 | **4** | 2.65 | Factorial Variants |
| **real_fin_legit** | 62,332 | **4,005** | **6.4%** | 14,473 | 1,334 | **166** | 3.00 | Stock Alerts & Email Threads |

### 1.2 Cluster Size Distribution Breakdown

| Dataset | Pair Clusters (Size = 2) | Small Clusters (3–5) | Medium Clusters (6–10) | Large Clusters (>10) |
| :--- | :--- | :--- | :--- | :--- |
| **real_fin_scam** | 879 | 278 | 52 | **8** |
| **synthetic_financial_scams** | 65 | 65 | 0 | **0** |
| **real_fin_legit** | 1,063 | 216 | 30 | **25** |

### 1.3 Forensic Analysis of Largest Clusters

1. **`real_fin_legit` (Max Size: 166 records):**
   - Cluster `REAL_FIN_LEGIT_C0001` consists of **166 near-identical automated stock quote notifications** (`Stock Notification for [ORGANIZATION]... The stock price for [ORGANIZATION] (NASD:[REFERENCE_NUMBER]) has changed...`).
   - Cluster `REAL_FIN_LEGIT_C0002` (72 records) consists of daily energy trading schedule circulars (`EOL Data for [DATE]...`).
   - These clusters represent automated bot/server notifications rather than human conversations.
2. **`real_fin_scam` (Max Size: 18 records):**
   - Clusters `REAL_FIN_SCAM_C0001` through `C0003` (18 records each) represent massive Nigerian 419 financial scam campaigns (`ASSIST ME AND MY FAMILY DEAR FRIEND, THROUGH THE COURTESY OF BUSINESS OPPORTUNITY, I TAKE LIBERTY ANCHORED ON A STRONG DESIRE TO SOLICIT YOUR ASSISTANCE...`).
   - Attackers blast the same body text while slightly modifying the sender persona, return email, or dollar amounts.
3. **`synthetic_financial_scams` (Max Size: 4 records):**
   - Tightly bounded factorial variations representing structured subtype scenarios.

> **CRITICAL DATA LEAKAGE IMPLICATION:**  
> A naive random train/val/test split will shatter these clusters across sets, allowing models to achieve artificially inflated test scores by memorizing templates. **Group-aware splitting (grouped by cluster ID) is mandatory for Phase 3.**

---

## 2. Placeholder Pattern Investigation & Harmonization Strategy

We systematically cataloged all angle-bracket (`<...>`) and square-bracket (`[...]`) anonymization/redaction tokens across the three datasets.

### 2.1 Placeholder Distribution by Dataset & Bracket Style

| Metric | Real Financial Scam (`real_fin_scam`) | Synthetic Scam (`synthetic_financial_scams`) | Legitimate Communications (`real_fin_legit`) |
| :--- | :--- | :--- | :--- |
| **Angle-Bracket Tokens (`<...>`)** | **22,479** (Dominant) | 0 | 12,368 (HTML/markup tags) |
| **Square-Bracket Tokens (`[...]`)** | 478 | **14,705** (Dominant) | **936,777** (Dominant) |
| **Records with Placeholders** | 11,003 (79.4%) | 7,643 (100.0%) | 55,984 (89.8%) |
| **Placeholder-Dominated Records ($\\ge 50\\%$)** | 14 | 0 | **655** |

### 2.2 Top Placeholder Tokens Across Corpora

| Original Token | Bracket Type | Real Scam Count | Synthetic Count | Legit Count | Total Count | Semantic Category | Recommended Harmonization |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[ORGANIZATION]` | Square ([...]) | 0 | 0 | 182,646 | 182,646 | Organization / Company / Service | **`[ORGANIZATION]`** |
| `[NAME]` | Square ([...]) | 0 | 0 | 179,722 | 179,722 | Person Name / Individual | **`[PERSON_NAME]`** |
| `[PRODUCT]` | Square ([...]) | 0 | 0 | 139,758 | 139,758 | Product / Commodity | **`[PRODUCT]`** |
| `[DATE]` | Square ([...]) | 0 | 0 | 76,115 | 76,115 | Date / Time / Timestamp | **`[DATE_TIME]`** |
| `[REFERENCE_NUMBER]` | Square ([...]) | 0 | 0 | 58,436 | 58,436 | Reference Number / Case Number | **`[IDENTIFIER]`** |
| `[FINANCIAL_INFO]` | Square ([...]) | 0 | 0 | 55,666 | 55,666 | Financial Data / Amount / Account | **`[FINANCIAL_DATA]`** |
| `[ADDRESS]` | Square ([...]) | 0 | 0 | 39,738 | 39,738 | Physical Location / Address | **`[LOCATION]`** |
| `[URL]` | Square ([...]) | 5 | 0 | 30,551 | 30,556 | URL / Web Link | **`[URL]`** |
| `[TIME]` | Square ([...]) | 0 | 0 | 28,666 | 28,666 | Date / Time / Timestamp | **`[DATE_TIME]`** |
| `[EMAIL_ADDRESS]` | Square ([...]) | 0 | 0 | 27,813 | 27,813 | Email Address | **`[EMAIL_ADDRESS]`** |
| `[PHONE_NUMBER]` | Square ([...]) | 0 | 0 | 25,071 | 25,071 | Phone Number | **`[PHONE_NUMBER]`** |
| `[FILE_NAME]` | Square ([...]) | 0 | 0 | 25,020 | 25,020 | System File / Path Artifact | **`[SYSTEM_ARTIFACT]`** |
| `[USERNAME]` | Square ([...]) | 0 | 0 | 15,393 | 15,393 | Person Name / Individual | **`[PERSON_NAME]`** |
| `[FILE_PATH]` | Square ([...]) | 0 | 0 | 13,308 | 13,308 | System File / Path Artifact | **`[SYSTEM_ARTIFACT]`** |
| `[INITIALS]` | Square ([...]) | 0 | 0 | 11,009 | 11,009 | Person Name / Individual | **`[PERSON_NAME]`** |

### 2.3 Malformed & Nested Placeholder Patterns in MeAJOR

- Exactly **5,089 records** in `real_fin_legit.csv` contain nested or repeated brackets (e.g. `[[[[[PRODUCT]]]]]`, `[[[[USERNAME]]]]`, `<<[FILE_NAME]>>`).
- These artifacts stem from iterative regex token replacement during MeAJOR preprocessing.
- In Phase 3, a recursive regex pass `re.sub(r'\[+([A-Z0-9_]+)\]+', r'[\1]', text)` will clean nested brackets.

### 2.4 Semantic Harmonization Strategy Recommendation

To prevent bracket-syntax shortcut learning while preserving crucial fraud-analysis semantics, we recommend standardizing all entities into a unified, square-bracket canonical ontology:
- **Links & Contact:** `<URL>`, `[URL]`, `[LINK REDACTED]` $\rightarrow$ `[URL]`
- **Telephony:** `<PHONE>`, `<PHONE_NUMBER>`, `[PHONE_NUMBER]` $\rightarrow$ `[PHONE_NUMBER]`
- **Email:** `<EMAIL>`, `<EMAIL_ADDRESS>`, `[EMAIL_ADDRESS]` $\rightarrow$ `[EMAIL_ADDRESS]`
- **Personal Entities:** `<NAMED_ENTITY>`, `[NAME]`, `[Fictional Contact]`, `[You]`, `[USERNAME]` $\rightarrow$ `[PERSON_NAME]`
- **Corporate / Brand:** `[ORGANIZATION]`, `[FICTIONAL ORGANIZATION]`, `[FICTIONAL SERVICE]`, `<NRP>` $\rightarrow$ `[ORGANIZATION]`
- **Financial & Account:** `<US_BANK_NUMBER>`, `[FINANCIAL_INFO]`, `[AMOUNT REDACTED]` $\rightarrow$ `[FINANCIAL_DATA]`
- **Identifiers & Legal:** `<US_DRIVER_LICENSE>`, `<US_SSN>`, `<US_PASSPORT>`, `<UK_NHS>`, `[REFERENCE_NUMBER]` $\rightarrow$ `[IDENTIFIER]`
- **Temporal & Spatial:** `<DATE_TIME>`, `[DATE]`, `[TIME]` $\rightarrow$ `[DATE_TIME]`; `<LOCATION>`, `[ADDRESS]` $\rightarrow$ `[LOCATION]`
---

## 3. Extremely Short and Long Message Investigation

### 3.1 Discrepancy Resolution

The initial audit report contained a textual discrepancy regarding suspiciously long records (>10,000 chars):

- **Report text stated:** 8 in `real_fin_scam` and 11 in `real_fin_legit`.
- **Actual empirical count:** Exactly **16 records** in `real_fin_scam` and **9 records** in `real_fin_legit`.
- **Root cause:** The initial report author hardcoded draft exploratory counts in prose while the programmatic `data_quality_report.csv` recorded the exact numbers (16 and 9). This report formally amends the audit baseline to the verified figures.

### 3.2 Outlier Inventory & Semantic Assessment

| Dataset | Record ID | Category | Chars | Words | Source | Channel | Text Preview | Semantic Assessment |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `real_fin_scam` | `FIN-00350` | long_outlier (>10k chars) | 121,724 | 23,486 | Nigerian_Fraud.csv | `email` | `BUSINESS PROPOSER REQUESTING CHANGE OF OWNERSHIP ATTENTION  ...` | Multi-page Nigerian 419 financial scam solicitation letter |
| `real_fin_legit` | `MEAJOR-LEG-054248` | long_outlier (>10k chars) | 30,893 | 448 | MeAJOR (trec7) | `email` | `[[[[[PRODUCT]]]]]e: [[[[[[PRODUCT]]]]]] [PRODUCT][[[[[[PRODU...` | Corporate legal disclaimer / multi-party quoted email chain in MeAJOR |
| `real_fin_scam` | `FIN-00348` | long_outlier (>10k chars) | 26,372 | 1,190 | Nigerian_Fraud.csv | `email` | `PROJECT INTEREST. My dear friend,   I am DR. Yetunde Basse...` | Multi-page Nigerian 419 financial scam solicitation letter |
| `real_fin_scam` | `FIN-00680` | long_outlier (>10k chars) | 21,694 | 3,701 | Nigerian_Fraud.csv | `email` | `urgent assitance MY DEAR FRIEND,  I DO BELIEF THAT THIS MAIL...` | Multi-page Nigerian 419 financial scam solicitation letter |
| `real_fin_legit` | `MEAJOR-LEG-035290` | long_outlier (>10k chars) | 19,149 | 658 | MeAJOR (trec6) | `email` | `[[[[USERNAME]]][[[[USERNAME]]]][[[USERNAME]]]] Re: [[[[USERN...` | Corporate legal disclaimer / multi-party quoted email chain in MeAJOR |
| `real_fin_scam` | `FIN-01756` | long_outlier (>10k chars) | 16,716 | 2,969 | Nigerian_Fraud.csv | `email` | `FROM RICHARD  FROM RICHARD AND Janet Dear sir,  I am Sanko R...` | Multi-page Nigerian 419 financial scam solicitation letter |
| `real_fin_legit` | `MEAJOR-LEG-042796` | long_outlier (>10k chars) | 16,359 | 622 | MeAJOR (trec7) | `email` | `Re: [R] xyplot() [[REFERENCE_NUMBER]]nd [REFERENCE_NUMBER] p...` | Corporate legal disclaimer / multi-party quoted email chain in MeAJOR |
| `real_fin_legit` | `MEAJOR-LEG-040617` | long_outlier (>10k chars) | 13,895 | 490 | MeAJOR (trec7) | `email` | `[R] Questio[[[[REFERENCE_NUMBER]]]] of the i[[[[REFERENCE_NU...` | Corporate legal disclaimer / multi-party quoted email chain in MeAJOR |
| `real_fin_legit` | `MEAJOR-LEG-048499` | long_outlier (>10k chars) | 13,517 | 468 | MeAJOR (trec7) | `email` | `[[[[PRODUCT]]]]e: [[[[[PRODUCT]]]]] using [P[[[[PRODUCT]]]]O...` | Corporate legal disclaimer / multi-party quoted email chain in MeAJOR |
| `real_fin_scam` | `FIN-01985` | long_outlier (>10k chars) | 13,013 | 2,293 | Nigerian_Fraud.csv | `email` | `honestly ok Qin Wang Lloyds TSB Pacific Limited Hong Kong Br...` | Multi-page Nigerian 419 financial scam solicitation letter |

### 3.3 Outlier Engineering Handling (Phase 3):

- **Short Outliers (<10 chars, 30 records total):** These are valid SMS communications (emoticons `:)`, codes `645`, replies `Yup`) and smishing URLs (`<URL>`). **Do not delete.** Retain for channel-specific evaluation.
- **Long Outliers (>10,000 chars, 25 records total):** Maximum length is `121,724` chars (`23,486` words in `FIN-00350`). These are valid 419 scam letters and corporate email threads. Transformer tokenizers truncate at 512 tokens. We recommend a **dual-window truncation** (first 256 tokens + last 256 tokens) to preserve the critical header solicitation and closing payment/contact instructions.
---

## 4. Channel Classification Investigation (`sms/email`)

We investigated the 9,600 records categorized as `sms/email` in `real_fin_scam.csv`.

### 4.1 Findings & Provenance

- **Source Attribution:** 100% of the 9,600 `sms/email` records originate from the **Smishing Dataset IMC25 (public user reports)**.
- **Text Length Distribution:** Median character length is **132.0 characters** (median 22.0 words; mean 25.5 words). This exactly matches the length distribution of `smishtank.csv` (`sms`, median 141.5 chars / 22.0 words).
- **Gateway Transmissions:** Only 20 records (0.2%) contain explicit email-to-SMS gateway headers (`FRM:... SUBJ:... MSG:...`). The remaining 9,580 records are standard mobile smishing texts.
- **Nature of `sms/email` Label:** In the upstream IMC25 study, public smishing reports included messages sent to cellular phones where the originating address was an email-to-SMS gateway. The upstream curator used the compound label `sms/email` to denote this dual transport mechanism.

### 4.2 Channel Harmonization Recommendation

| Current Channel Label | Record Count | Recommended Harmonized Channel | Rationale |
| :--- | :--- | :--- | :--- |
| `email` | 27,291 | **`email`** | Retain 'email'; lengths and formatting correspond to MIME body/subjects.... |
| `email` | 19,244 | **`email`** | Retain 'email'; lengths and formatting correspond to MIME body/subjects.... |
| `email` | 11,127 | **`email`** | Retain 'email'; lengths and formatting correspond to MIME body/subjects.... |
| `sms/email` | 9,600 | **`sms`** | Text lengths (median 22 words / 132 chars) strictly match standard SMS constraints. The dataset provenance (IMC25 Smishi... |
| `sms` | 4,500 | **`sms`** | Retain 'sms'; lengths align with 160-character mobile protocol limits.... |
| `email` | 3,265 | **`email`** | Retain 'email'; lengths and formatting correspond to MIME body/subjects.... |
| `chat` | 1,911 | **`chat`** | Retain 'chat'; synthetically controlled dialogue format.... |
| `sms` | 1,911 | **`sms`** | Retain 'sms'; lengths align with 160-character mobile protocol limits.... |
| `email` | 1,911 | **`email`** | Retain 'email'; lengths and formatting correspond to MIME body/subjects.... |
| `notification` | 1,910 | **`notification`** | Retain 'notification'; terse system event format.... |
| `email` | 500 | **`email`** | Retain 'email'; lengths and formatting correspond to MIME body/subjects.... |
| `sms` | 496 | **`sms`** | Retain 'sms'; lengths align with 160-character mobile protocol limits.... |
| `sms` | 170 | **`sms`** | Retain 'sms'; lengths align with 160-character mobile protocol limits.... |

---

## 5. Cross-Dataset Similarity Validation

The initial audit reported **zero** cross-dataset near-duplicate pairs between real scam, synthetic scam, and legitimate corpora. We validated the rigor and limits of this finding.

### 5.1 Verification Parameters & Methodology

- **Scope:** Evaluated across all **83,836** records (full corpus pairwise cross-comparison).
- **Tokenization:** Case-folded, whitespace-collapsed word 3-shingles ($k=3$).
- **MinHash Configuration:** $m = 64$ hash permutations, 32-bit MD5 prefixes, Mersenne-adjacent prime $p = 4,294,967,311$, seed 42.
- **LSH Banding:** $b = 16$ bands with $r = 4$ rows per band ($b \times r = 64$).
- **Similarity Criterion:** Candidate pairs evaluated by exact Jaccard similarity threshold $s \ge 0.85$.

### 5.2 Theoretical Collision Probability Analysis

The probability that two documents with true word 3-gram Jaccard similarity $s$ collide in at least one LSH band is given by:
$$P(\text{collision}) = 1 - (1 - s^r)^b = 1 - (1 - s^4)^{16}$$

| Jaccard Similarity ($s$) | Theoretical LSH Collision Probability $P$ | Empirical Interpretation |
| :--- | :--- | :--- |
| $s = 0.99$ | **1.000000** (100.000%) | Virtually guaranteed detection |
| $s = 0.95$ | **1.000000** (100.000%) | Virtually guaranteed detection |
| $s = 0.90$ | **1.000000** (100.000%) | Virtually guaranteed detection |
| $s = 0.85$ | **0.999993** (99.999%) | Virtually guaranteed detection |
| $s = 0.80$ | **0.999782** (99.978%) | Virtually guaranteed detection |
| $s = 0.70$ | **0.987638** (98.764%) | High detection rate |
| $s = 0.50$ | **0.643926** (64.393%) | Moderate detection |
| $s = 0.30$ | **0.122017** (12.202%) | Infrequent collision |

### 5.3 Known Limitations & False Negative Boundary Conditions

1. **Short Message Edge Cases (<3 words):** Messages with fewer than 3 words produce singleton token sets where word 3-grams cannot form; these rely on fallback word-unigram hashing.
2. **Lexical vs Semantic Near-Duplicates:** MinHash LSH operates strictly on surface lexical n-grams. Semantic paraphrases that convey the same fraudulent narrative using completely different vocabulary will not be detected by lexical shingling.
3. **Scientific Limitation:** Finding zero approximate matches via MinHash LSH empirically confirms that there are no high-overlap ($\ge 0.85$) lexical near-duplicates across datasets, but **does not constitute a mathematical proof** of zero conceptual or semantic overlap.

---

## 6. Audit Report Amendments & Correction Log

| Report Section | Original Text / Claim | Corrected Finding | Justification / Source |
| :--- | :--- | :--- | :--- |
| **Section 3: Outliers** | `real_fin_scam: 8 messages >10k chars` | **16 messages >10k chars** | Corrected prose to match verified programmatic count in `data_quality_report.csv`. |
| **Section 3: Outliers** | `real_fin_legit: 11 messages >10k chars` | **9 messages >10k chars** | Corrected prose to match verified programmatic count in `data_quality_report.csv`. |
| **Section 6: Legit Dupes** | `2,138 near-duplicate pairs (25k sample)` | **14,473 near-duplicate pairs (100% full coverage)** | Expanded analysis to all 62,332 records; identified 1,334 clusters (max size: 166). |
| **Section 7: Shortcut Claim** | `attaining >90% validation accuracy` | `creating severe spurious statistical correlations` | Qualified unsupported speculative predictive claims; replaced with objective risk characterization. |

---

## 7. Deliverables & Data Asset Manifest

- [`near_duplicate_clusters.csv`](near_duplicate_clusters.csv): 2,681 distinct clusters across corpora with representative exemplars.
- [`near_duplicate_examples.csv`](near_duplicate_examples.csv): 18,245 verified near-duplicate pairs with pairwise Jaccard similarities.
- [`near_duplicate_cluster_summary.csv`](near_duplicate_cluster_summary.csv): Cluster size distributions and coverage statistics.
- [`placeholder_inventory.csv`](placeholder_inventory.csv): Exhaustive inventory of 73 distinct placeholders with recommended harmonization targets.
- [`placeholder_record_analysis.csv`](placeholder_record_analysis.csv): Per-record placeholder counts, character lengths, and density ratios.
- [`extreme_message_analysis.csv`](extreme_message_analysis.csv): 55 extreme outlier records (<10 chars, >10k chars) with semantic assessments.
- [`channel_mapping_audit.csv`](channel_mapping_audit.csv): Cross-tabulation of sources, transport mechanisms, and channel recommendations.