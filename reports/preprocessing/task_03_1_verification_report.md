# Task 03.1 Forensic Verification & Semantic Validation Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Investigation Date:** 2026-11-07  
**Status:** Completed & Fully Verified  
**Referenced Deliverables:**
- Gateway Verification: [`reports/preprocessing/gateway_classification_verification.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/gateway_classification_verification.md)
- Semantic Review: [`reports/preprocessing/placeholder_semantic_review.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/placeholder_semantic_review.md)
- Text Reduction Analysis: [`reports/preprocessing/text_reduction_investigation.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/text_reduction_investigation.md)
- Reduction Audit Data: [`reports/preprocessing/text_reduction_investigation.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/text_reduction_investigation.csv)
- Channel Harmonization Stats: [`reports/preprocessing/channel_harmonization_stats.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/channel_harmonization_stats.csv)
- Placeholder Stats: [`reports/preprocessing/placeholder_normalization_stats.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/placeholder_normalization_stats.csv)

---

## 1. Executive Summary

This forensic audit and verification report resolves the three concerns identified in the preliminary Task 03 preprocessing outputs:
1. **Email-to-SMS Gateway Classification:** A logic flaw in `channel_mapper.py` had incorrectly marked all 9,600 IMC25 messages as `is_email_gateway = True`. The empirical evidence was audited at the individual record level. Exactly **24 IMC25 records** and **22 smishtank records** exhibit carrier email-to-SMS transport headers. `channel_mapper.py` has been corrected so that only records with verifiable gateway routing evidence receive `is_email_gateway = True`, while the remaining 9,576 mobile SMS messages in IMC25 are correctly assigned `is_email_gateway = False`.
2. **Placeholder Ontology Semantic Review:** Four suspect placeholder mappings were investigated against their original text contexts and source annotation definitions:
   - `<NAMED_ENTITY>` (previously mapped to `[PERSON_NAME]`): Converted to canonical `[NAMED_ENTITY]` to avoid falsely labeling banks, payment networks, and services as personal names.
   - `[You]` (previously mapped to `[PERSON_NAME]`): Retained verbatim as `[You]` because it represents the dialogue recipient turn in synthetic chat transcripts, not a redacted personal name.
   - `[PASSWORD]` (previously mapped to `[SYSTEM_ARTIFACT]`): Mapped to a dedicated cybersecurity credential token `[CREDENTIAL]` (along with `[password]` and `<password>`).
   - `<NRP>` (previously mapped to `[ORGANIZATION]`): Mapped to canonical `[NRP]` to preserve SpaCy's NORP (Nationalities, Religious, or Political groups) entity category without fabricating organizational affiliations.
   - `[PRODUCT]`: Verified and retained as a distinct financial product/service token.
3. **Unexpected Text Reduction Investigation:** The 12,345-character reduction in record `MEAJOR-LEG-054248` (30,893 $\rightarrow$ 18,548 characters) was verified. The audit established that **zero natural language words, numbers, or punctuation were lost** (word count remained exactly 448 words). The 12,345 characters removed consisted entirely of 12,345 redundant bracket characters (`6,174` opening brackets and `6,171` closing brackets) caused by upstream MeAJOR regex concatenation loops. A dataset-wide audit of all 11,511 records with character reductions confirmed that reductions stem solely from malformed bracket un-nesting and placeholder canonicalization.

---

## 2. Investigation Findings & Root Cause Analysis

### 2.1 Email-to-SMS Gateway Classification

#### Preliminary Task 03 Inconsistency
Task 02 established that out of 9,600 IMC25 records originally labeled `sms/email`, 9,580 were standard mobile SMS messages and only 20 contained carrier email-to-SMS gateway transport headers (`^FRM:`). However, Task 03 reported:
- `sms/email`: 9,600 records, all 9,600 marked `is_email_gateway = True`.
- `sms`: 496 records, 0 marked `is_email_gateway = True`.
- Gateway header counts reported: 22 in `sms/email` and 20 in `sms`.

#### Root Cause
In [`src/preprocessing/channel_mapper.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/channel_mapper.py), the mapping rule was implemented as:
```python
if raw_clean == "sms/email":
    canonical_channel = "sms"
    is_gateway = True  # <-- FLAW: Assumed raw label was empirical proof of gateway transport
```
The upstream creators of the *Smishing Dataset IMC25* applied the label `sms/email` broadly to indicate that mobile smishing reports were collected through channels that could receive SMS originating from both mobile numbers and email addresses. Equating this collection label with physical carrier email-to-SMS gateway transport corrupted the semantics for 9,576 ordinary SMS messages.

#### Forensic Analysis of the Header Discrepancy (20 vs. 22 vs. 24)
Comparing the regex patterns across tasks revealed why previous counts diverged:
1. **Task 02 strictly anchored regex (`^FRM:`):**
   - Matched only messages where `FRM:` appeared at string index 0.
   - Captured **20 records** in IMC25 and **14 records** in smishtank.
2. **Task 03 unanchored compound regex:**
   - Permitted leading text or multi-part carrier segmentation (`1 of 2\nFRM:...` or `(Alert)FRM:...`).
   - Captured **22 records** in IMC25 and **20 records** in smishtank.
3. **Task 03.1 unified regex audit (`(?:^|\s)(?:FRM|FROM):.*?(?:SUBJ|MSG):`):**
   - Captured two additional records in IMC25 that use the full word `FROM:` instead of the abbreviation `FRM:`: `FIN-08173` and `FIN-08447`.
   - Captured two additional multi-part messages in smishtank (`FIN-00164` and `FIN-00165`).
   - Total verified gateway header records: **24 in IMC25** and **22 in smishtank**.

#### Exact Verified Record IDs
- **IMC25 Gateway Records (24 records):**
  `FIN-07897`, `FIN-07921`, `FIN-08034`, `FIN-08053`, `FIN-08101`, `FIN-08106`, `FIN-08127`, `FIN-08147`, `FIN-08173`, `FIN-08207`, `FIN-08236`, `FIN-08240`, `FIN-08253`, `FIN-08282`, `FIN-08304`, `FIN-08332`, `FIN-08447`, `FIN-08481`, `FIN-08485`, `FIN-08571`, `FIN-08575`, `FIN-08587`, `FIN-10497`, `FIN-10544`.
- **Smishtank Gateway Records (22 records):**
  `FIN-00049`, `FIN-00055`, `FIN-00057`, `FIN-00063`, `FIN-00085`, `FIN-00100`, `FIN-00109`, `FIN-00114`, `FIN-00116`, `FIN-00119`, `FIN-00138`, `FIN-00147`, `FIN-00159`, `FIN-00164`, `FIN-00165`, `FIN-00185`, `FIN-00187`, `FIN-00196`, `FIN-00213`, `FIN-00234`, `FIN-00361`, `FIN-00366`.

---

### 2.2 Placeholder Ontology Semantic Review

The audit inspected all four suspect mappings against source text records and upstream documentation.

#### 1. `<NAMED_ENTITY>` (1,468 records, 1,778 occurrences in `real_fin_scam.csv`)
- **Previous Mapping:** `[PERSON_NAME]`
- **Root Cause of Error:** Presumed that entities are personal names.
- **Empirical Context:** Upstream IMC25 annotators used `<NAMED_ENTITY>` as an umbrella catch-all for institutions (e.g. `"<NAMED_ENTITY>: We've placed a hold on your debit/atm card..."`), payment apps (e.g. `"WELLSFARGO: Your <NAMED_ENTITY> pay of $1250..."`), and platforms. Less than 15% of contexts were personal names.
- **Correction:** Standardized to canonical square-bracket token **`[NAMED_ENTITY]`**. Eliminates delimiter leakage while preserving entity generality without fabricating personal identities.

#### 2. `[You]` (1,911 records, 1,911 occurrences in `synthetic_financial_scams.csv`)
- **Previous Mapping:** `[PERSON_NAME]`
- **Root Cause of Error:** Heuristic assumed bracketed words denote anonymized PII names.
- **Empirical Context:** Synthetic chat messages simulate two-party dialogue scripts:
  `"[Fictional Contact]: A quiet review has been placed on the account. Confirm through [LINK REDACTED]. ... [You]: Can you provide the official verification desk number before I proceed?"`
  Here `[You]` represents the victim's conversational dialogue turn.
- **Correction:** **Retained verbatim as `[You]`**. Preserves conversational dialogue structure.

#### 3. `[PASSWORD]` (74 records, 117 occurrences in `real_fin_legit.csv`)
- **Previous Mapping:** `[SYSTEM_ARTIFACT]`
- **Root Cause of Error:** Overly broad categorization of technical tokens.
- **Empirical Context:** Legitimate IT notifications concerning account credentials (e.g. `"Your temporary [PASSWORD] is expired"`, `"Never share your [PASSWORD] with anyone"`). In financial scam analysis, credentials are a primary target of social engineering attacks.
- **Correction:** Established dedicated canonical token **`[CREDENTIAL]`** (covering `[PASSWORD]`, `[password]`, and `<password>`).

#### 4. `<NRP>` (170 records, 181 occurrences in `real_fin_scam.csv`)
- **Previous Mapping:** `[ORGANIZATION]`
- **Root Cause of Error:** Unverified assumption of abbreviation meaning.
- **Empirical Context:** Originates from SpaCy NER tagging for `NORP` (Nationalities, Religious, or Political groups, e.g. "American taxpayers", "Federal Christian assistance").
- **Correction:** Standardized to canonical square-bracket token **`[NRP]`**. Preserves demographic entity scope without fabricating corporate organizations.

#### 5. `[PRODUCT]` (7,842 records, 24,082 occurrences in `real_fin_legit.csv`)
- **Assessment:** Refers specifically to commercial banking products, credit cards, and loan packages in MeAJOR financial emails. Retained as a distinct canonical token **`[PRODUCT]`**.

---

### 2.3 Unexpected Text Reduction Investigation

#### Forensic Audit of `MEAJOR-LEG-054248`
In Task 03, `MEAJOR-LEG-054248` decreased from 30,893 to 18,548 characters ($\Delta = -12,345$, -39.96%). A character-level comparison between raw and processed text confirmed:
- **Raw character count:** 30,893
- **Processed character count:** 18,548
- **Character difference:** -12,345 (-39.96%)
- **Raw word count:** 448 words
- **Processed word count:** 448 words ($\Delta = 0$ words, **100% identical**)
- **Raw opening brackets `[`:** 7,926
- **Processed opening brackets `[`:** 1,752 ($\Delta = -6,174$)
- **Raw closing brackets `]`:** 7,926
- **Processed closing brackets `]`:** 1,755 ($\Delta = -6,171$)
- **Total bracket reduction:** $-6,174 + (-6,171) = -12,345$ brackets exactly.

$$\Delta_{\text{characters}} = \Delta_{\text{brackets}} = -12,345$$

Every single deleted character was a redundant bracket generated by recursive upstream regex replacements in MeAJOR (e.g., `[[[[[[[[[[PRODUCT]]]]]]]]]]`). **Zero natural language content was lost.**

#### Dataset-Wide Ranked Analysis
Across all 83,836 records, 11,511 records exhibited character reductions:
- Top 10 reductions were all MeAJOR records containing malformed nested bracket cascades around `[PRODUCT]`.
- All other reductions resulted strictly from:
  1. Multi-word placeholder canonicalization (e.g., `[LINK REDACTED]` (15 chars) $\rightarrow$ `[URL]` (5 chars)).
  2. Canonical length standardization (e.g., `[REFERENCE_NUMBER]` (18 chars) $\rightarrow$ `[IDENTIFIER]` (12 chars)).
  3. Whitespace normalization (collapsing redundant internal spacing).
- **Accidental deletion of meaningful text across the corpus: 0 occurrences.**

---

## 3. Exact Corrections Implemented

### 3.1 Codebase Modifications

1. **[`src/preprocessing/channel_mapper.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/channel_mapper.py):**
   - Decoupled `canonical_channel`, `original_channel`, `is_email_gateway`, and `has_gateway_headers`.
   - Updated regex pattern to capture all carrier gateway signatures:
     ```python
     GATEWAY_HEADER_REGEX = re.compile(
         r'(?:^|\s)(?:FRM|FROM):.*?(?:SUBJ|MSG):|'
         r'(?:^|\s)FRM:\s*[\w\.\-\+]+@[\w\.\-]+\.[a-zA-Z]{2,}|'
         r'\(Alert\)\s*FRM:|'
         r'^\d+\s*of\s*\d+\s*\nFRM:',
         re.IGNORECASE | re.DOTALL
     )
     ```
   - Assigned `is_email_gateway = True` **only** when `has_gateway_headers == True`.
   - Labeled ordinary mobile SMS records (9,576 in IMC25 and 474 in smishtank) as `is_email_gateway = False`.

2. **[`src/preprocessing/harmonizer.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/harmonizer.py):**
   - Added canonical tokens `[CREDENTIAL]`, `[NAMED_ENTITY]`, `[NRP]`, `[PRODUCT]`, and `[You]`.
   - Updated mapping dictionaries:
     - `"<NAMED_ENTITY>"` $\rightarrow$ `"[NAMED_ENTITY]"`
     - `"NAMED_ENTITY"` $\rightarrow$ `"[NAMED_ENTITY]"`
     - `"[You]"` $\rightarrow$ `"[You]"` (preserved verbatim)
     - `"[PASSWORD]"`, `"[password]"`, `"<password>"` $\rightarrow$ `"[CREDENTIAL]"`
     - `"<NRP>"` $\rightarrow$ `"[NRP]"`
   - Maintained deterministic, idempotent multi-pass bracket normalizer with protection against stripping natural words in brackets.

3. **[`tests/test_preprocessing.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/tests/test_preprocessing.py):**
   - Added regression test `test_targeted_placeholder_corrections` covering `<NAMED_ENTITY>`, `[You]`, `[PASSWORD]`, and `<NRP>`.
   - Added regression test `test_nested_cleanup_preserves_words` ensuring nested bracket cleanup does not delete words or valid text.
   - Updated gateway classification assertions to reflect evidence-based transport tagging.

4. **Regeneration of Processed Datasets & Reports:**
   - Executed [`scripts/run_preprocessing.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/scripts/run_preprocessing.py) to regenerate all processed datasets in `data/processed/` and statistical audit tables in `reports/preprocessing/`.

---

## 4. Quantitative Before vs. After Summary

### 4.1 Record Counts & Dataset Integrity

Row counts and record IDs are 100% conserved across raw, interim, and processed representations:

| Dataset Name | Raw Rows | Processed Rows | Preservation Rate | Original Text Verbatim Match | Record IDs Unique |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `real_fin_scam` | 13,861 | 13,861 | 100.0% | Yes | Yes (100%) |
| `synthetic_financial_scams` | 7,643 | 7,643 | 100.0% | Yes | Yes (100%) |
| `real_fin_legit` | 62,332 | 62,332 | 100.0% | Yes | Yes (100%) |
| **Total Corpus** | **83,836** | **83,836** | **100.0%** | **Yes** | **Yes (100%)** |

### 4.2 Channel Classification Statistics Before vs. After

| Dataset Name | Original Channel | Canonical Channel | Record Count | Pre-Correction `is_email_gateway` | Post-Correction `is_email_gateway` | Net Correction |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| `real_fin_scam` | `sms/email` | `sms` | 9,600 | 9,600 | **24** | **-9,576** (false positives eliminated) |
| `real_fin_scam` | `sms` | `sms` | 496 | 0 | **22** | **+22** (verified headers recognized) |
| `real_fin_scam` | `email` | `email` | 3,765 | 0 | 0 | 0 |
| `synthetic_financial_scams` | `chat` | `chat` | 1,911 | 0 | 0 | 0 |
| `synthetic_financial_scams` | `email` | `email` | 1,911 | 0 | 0 | 0 |
| `synthetic_financial_scams` | `notification` | `notification` | 1,910 | 0 | 0 | 0 |
| `synthetic_financial_scams` | `sms` | `sms` | 1,911 | 0 | 0 | 0 |
| `real_fin_legit` | `email` | `email` | 57,662 | 0 | 0 | 0 |
| `real_fin_legit` | `sms` | `sms` | 4,670 | 0 | 0 | 0 |
| **Total** | | | **83,836** | **9,600** | **46** | **-9,554** |

### 4.3 Placeholder Ontology Mapping Summary

| Placeholder Pattern | Previous Mapping | Corrected Mapping | Justification / Semantic Basis | Occurrences |
| :--- | :--- | :--- | :--- | :---: |
| `<NAMED_ENTITY>` | `[PERSON_NAME]` | `[NAMED_ENTITY]` | Upstream IMC25 catch-all for banks, apps, and merchants; avoids fabricating person names | 1,778 |
| `[You]` | `[PERSON_NAME]` | `[You]` | Synthetic dialogue recipient turn marker; retains conversation flow | 1,911 |
| `[PASSWORD]` | `[SYSTEM_ARTIFACT]` | `[CREDENTIAL]` | Specific authentication secret critical to financial credential theft | 117 |
| `<NRP>` | `[ORGANIZATION]` | `[NRP]` | SpaCy NORP demographic/national category; avoids fabricating corporate entities | 181 |
| `[PRODUCT]` | `[PRODUCT]` | `[PRODUCT]` | Retained as distinct category for commercial financial banking products | 24,082 |

### 4.4 Dataset-Wide Placeholder Normalization Statistics

| Dataset Name | Total Records | Records with Original Placeholders | Records with Normalized Placeholders | Total Original Placeholders | Total Normalized Placeholders | Distinct Unresolved Tokens | Total Unresolved Occurrences |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `real_fin_scam` | 13,861 | 11,070 | 11,070 | 22,957 | 22,957 | 241 | 497 |
| `synthetic_financial_scams` | 7,643 | 6,855 | 6,855 | 14,705 | 14,705 | 13 | 155 |
| `real_fin_legit` | 62,332 | 56,065 | 56,065 | 949,145 | 949,145 | 2,784 | 35,251 |
| **Total** | **83,836** | **73,990** | **73,990** | **986,807** | **986,807** | **3,038** | **35,903** |

---

## 5. Raw Dataset Hash Integrity Verification

All three raw CSV files in `data/raw/` were verified before and after pipeline execution. Their SHA-256 hashes are identical to the initial audit baseline:

| Raw Dataset File | SHA-256 Hash | Integrity Status |
| :--- | :--- | :---: |
| `data/raw/real_fin_scam.csv` | `e00822c1e6469ea7e35fe7f2339c3fc557bdc13d13545cca4bda47385d3b4021` | **Verified Intact** |
| `data/raw/synthetic_financial_scams.csv` | `8e708fa30aeaed63067db56c9b5c10e1cbb90b6fb8574c53882e32b3654240d7` | **Verified Intact** |
| `data/raw/real_fin_legit.csv` | `6810244c341b8f484e19b16a6e13482b38877f5608debfb829874e145adac6bc` | **Verified Intact** |

---

## 6. Complete Test Results

The full regression test suite was executed across all components:
```text
pytest tests/ -v
```
**Results:**
- `tests/test_audit.py`: 5 passed
  - `test_detect_column_helpers` PASSED
  - `test_data_quality_audit` PASSED
  - `test_composition_audit` PASSED
  - `test_text_profiler` PASSED
  - `test_duplicate_and_lsh_detection` PASSED
- `tests/test_preprocessing.py`: 11 passed
  - `test_raw_dataset_hash_preservation` PASSED
  - `test_placeholder_normalization_categories` PASSED
  - `test_targeted_placeholder_corrections` PASSED
  - `test_nested_and_malformed_placeholders` PASSED
  - `test_nested_cleanup_preserves_words` PASSED
  - `test_placeholder_idempotency` PASSED
  - `test_unknown_placeholder_preservation` PASSED
  - `test_channel_harmonization_rules` PASSED
  - `test_schema_mapping_and_columns` PASSED
  - `test_cluster_mapping_loader` PASSED
  - `test_synthetic_and_legit_processing_mock` PASSED
- `tests/test_validation.py`: 5 passed
  - `test_lsh_theoretical_probabilities` PASSED
  - `test_word_shingles` PASSED
  - `test_connected_component_clustering` PASSED
  - `test_placeholder_investigation` PASSED
  - `test_extreme_message_investigation` PASSED

**Total: 21 passed, 0 failed in 4.15 seconds.**

---

## 7. Remaining Uncertainties & Research Limitations

1. **Upstream Anonymization Inherent Ambiguity:** In `real_fin_scam.csv` (IMC25), `<NAMED_ENTITY>` was used indiscriminately by the original collectors for bank names, platforms, and personal names. Because raw un-anonymized strings are unavailable, downstream Transformer models cannot determine the exact entity type from the token alone. However, preserving the token as `[NAMED_ENTITY]` accurately conveys to attention layers that an entity was present without biasing predictions towards person-based narratives.
2. **Carrier Email Gateway Headers:** Mobile carriers format email-to-SMS gateway gateways differently (e.g., `FRM:`, `FROM:`, `MSG:`, or carrier-specific headers). While 46 messages have unmistakable gateway header artifacts, it remains possible that some carrier gateways stripped routing headers before delivery. We have strictly limited `is_email_gateway = True` to cases with verifiable evidence, ensuring no ungrounded assumptions enter the feature space.
3. **Legitimate Bracketed Text in MeAJOR:** In `real_fin_legit.csv`, bracketed abbreviations like `[R]`, `[1]`, and `[DMDX]` were retained verbatim under `unresolved_placeholders`. These represent scientific/technical mailing list tags and survey notations rather than PII placeholders. They are preserved intact in `text_normalized`.

---

## 8. Index of Created & Modified Artifacts

### Created Files
1. [`reports/preprocessing/task_03_1_verification_report.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/task_03_1_verification_report.md) — Comprehensive synthesis report (this file).
2. [`reports/preprocessing/gateway_classification_verification.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/gateway_classification_verification.md) — Detailed forensic investigation of carrier gateway routing and header regex discrepancies.
3. [`reports/preprocessing/placeholder_semantic_review.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/placeholder_semantic_review.md) — Semantic evaluation and correction analysis of `<NAMED_ENTITY>`, `[You]`, `[PASSWORD]`, `<NRP>`, and `[PRODUCT]`.
4. [`reports/preprocessing/text_reduction_investigation.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/text_reduction_investigation.md) — Forensic audit and mathematical proof of character conservation for `MEAJOR-LEG-054248`.
5. [`reports/preprocessing/text_reduction_investigation.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/text_reduction_investigation.csv) — Ranked dataset-wide audit of all 11,511 records with character reductions.

### Modified Files
1. [`src/preprocessing/channel_mapper.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/channel_mapper.py) — Fixed gateway assignment logic and updated multi-part gateway regex.
2. [`src/preprocessing/harmonizer.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/harmonizer.py) — Corrected placeholder mappings, added `[CREDENTIAL]`, and preserved `[You]`.
3. [`src/preprocessing/pipeline.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/pipeline.py) — Updated schema documentation and summary statistics generation.
4. [`tests/test_preprocessing.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/tests/test_preprocessing.py) — Added targeted tests for gateway rules, placeholder corrections, and bracket safety.
5. [`reports/preprocessing/channel_harmonization_stats.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/channel_harmonization_stats.csv) — Updated channel mapping distribution counts.
6. [`reports/preprocessing/placeholder_normalization_stats.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/placeholder_normalization_stats.csv) — Updated placeholder token frequencies and mappings.
7. [`reports/preprocessing/preprocessing_summary.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/preprocessing_summary.md) — Regenerated pipeline summary markdown.
8. [`reports/preprocessing/integrity_verification.json`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/integrity_verification.json) — Integrity audit verification status.
9. [`data/processed/real_fin_scam_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/real_fin_scam_processed.csv) — Regenerated processed canonical dataset.
10. [`data/processed/synthetic_financial_scams_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_processed.csv) — Regenerated processed canonical dataset.
11. [`data/processed/real_fin_legit_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/real_fin_legit_processed.csv) — Regenerated processed canonical dataset.

