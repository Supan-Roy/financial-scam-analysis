# Task 04.0: Group-Aware Data Splitting Feasibility Analysis Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Investigation Date:** 2026-11-07  
**Status:** Completed & Validated  
**Referenced Deliverables:**
- Group Distribution Analysis: [`reports/splitting/group_distribution_analysis.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/group_distribution_analysis.csv)
- Source & Channel Distribution: [`reports/splitting/source_channel_distribution.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/source_channel_distribution.csv)
- Cluster Size Analysis: [`reports/splitting/cluster_size_analysis.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/cluster_size_analysis.csv)
- Processed Scam Dataset: [`data/processed/real_fin_scam_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/real_fin_scam_processed.csv)
- Processed Legit Dataset: [`data/processed/real_fin_legit_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/real_fin_legit_processed.csv)

---

## 1. Executive Summary & Feasibility Verdict

### Feasibility Verdict: **FULLY FEASIBLE**
Creating leakage-resistant, group-aware train (80%), validation (10%), and test (10%) splits for real-world binary scam classification is **fully feasible and mathematically stable**, provided that:
1. **Grouping Unit is defined by Near-Duplicate Clusters:** Groups are formed strictly by `duplicate_cluster_id` for clustered records, while each unclustered record is treated as an independent singleton group (`singleton_{record_id}`). Under no circumstances should unclustered records be grouped into a monolithic null group.
2. **Splitting Strategy is Stratified Group-Aware Partitioning:** Splitting must stratify jointly across `(label, channel)` while treating each group as an atomic, indivisible block.
3. **Synthetic Scam Data is Strictly Isolated:** `synthetic_financial_scams_processed.csv` (7,643 records) is held out entirely from the baseline splits and preserved for out-of-distribution robustness evaluation and domain transfer testing in later tasks.

### Empirical Validation Highlights:
- **Total Real-World Corpus:** 76,193 records (13,861 scam + 62,332 legitimate).
- **Total Indivisible Groups:** 71,533 groups (11,872 scam groups + 59,661 legitimate groups).
- **Cluster Integrity:** 2,551 multi-record duplicate clusters (7,211 records) are preserved intact with **0% cross-split leakage**.
- **Algorithmic Simulation:** A greedy group-aware stratified partitioner achieved an allocation of **80.00% Train (60,957 records), 10.00% Validation (7,618 records), and 10.00% Test (7,618 records)** with an absolute deviation of less than **0.004%** (< 4 records) and **zero cluster leakage**.

---

## 2. Dataset Scope & Schema Inspection

The analysis scope is strictly limited to real-world communications. All inputs conform to the 30-column canonical schema established in Task 03 and corrected in Task 03.1:

| Dataset | Scope Role | Row Count | Distinct Record IDs | Canonical Schema Columns | Label Definition |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `real_fin_scam_processed.csv` | Positive Class | 13,861 | 13,861 (100% unique) | 30 columns | Binary `1` (scam) |
| `real_fin_legit_processed.csv` | Negative Class | 62,332 | 62,332 (100% unique) | 30 columns | Binary `0` (legitimate) |
| **Combined Real Corpus** | **Baseline Scope** | **76,193** | **76,193 (100% unique)** | **30 columns** | **Binary `0` / `1`** |
| `synthetic_financial_scams_processed.csv` | *Isolated (Held Out)* | 7,643 | 7,643 (100% unique) | 30 columns | *Excluded from Task 04* |

---

## 3. Duplicate Cluster Availability & Group Construction

### 3.1 Cluster Availability by Dataset

Duplicate cluster IDs were audited in Task 02 and persisted in Task 03/03.1. Clustered records represent near-duplicate message templates (MinHash LSH Jaccard similarity $\ge 0.85$):

| Dataset | Total Records | Clustered Records | Clustered Share | Singletons (Unclustered) | Singleton Share | Distinct Clusters |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `real_fin_scam` | 13,861 | 3,206 | 23.13% | 10,655 | 76.87% | 1,217 |
| `real_fin_legit` | 62,332 | 4,005 | 6.43% | 58,327 | 93.57% | 1,334 |
| **Total Real Corpus** | **76,193** | **7,211** | **9.46%** | **68,982** | **90.54%** | **2,551** |

### 3.2 Singleton Group Handling Rule
A critical methodological requirement is that **unclustered records must become individual singleton groups**:
$$\text{group\_id} = \begin{cases} \text{duplicate\_cluster\_id}, & \text{if } \text{duplicate\_cluster\_id is not null} \\ \text{"singleton\_" } + \text{record\_id}, & \text{if } \text{duplicate\_cluster\_id is null} \end{cases}$$

> [!CAUTION]
> If records with null cluster IDs were treated as a single "null" group, 58,327 legitimate records (93.57% of all legitimate data) would be forced into a single indivisible split, completely destroying any train/val/test partitioning. Treating each unclustered record as its own singleton group yields 68,982 independent single-record groups, providing maximal flexibility for stratification.

### 3.3 Global Uniqueness of Cluster IDs
An inspection of cluster ID naming conventions confirmed:
- Scam cluster IDs follow: `REAL_FIN_SCAM_C0001` through `REAL_FIN_SCAM_C1217`.
- Legit cluster IDs follow: `REAL_FIN_LEGIT_C0001` through `REAL_FIN_LEGIT_C1334`.
- **Overlap between scam and legit cluster IDs:** **0 (disjoint sets)**.
- Every cluster ID is globally unique. Combining cluster IDs with `singleton_{record_id}` yields **71,533 globally unique groups** across the 76,193 real records.

---

## 4. Class Distribution at Record vs. Group Level

Because near-duplicate density is substantially higher in scam messages (23.13%) than in legitimate messages (6.43%), the class balance shifts slightly between record and group levels:

| Level | Scam Count | Legit Count | Total | Scam Share | Legit Share | Imbalance Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Record Level** | 13,861 | 62,332 | 76,193 | **18.19%** | **81.81%** | 1 : 4.50 |
| **Group Level** | 11,872 | 59,661 | 71,533 | **16.60%** | **83.40%** | 1 : 5.03 |

### Cluster Purity:
- **Cross-class duplicate clusters:** **0**.
- Every single duplicate cluster is 100% pure (contains either only scam records or only legitimate records).
- Mean records per group: **1.168** for scam, **1.045** for legitimate.

---

## 5. Source, Channel & Legitimate Category Distributions

### 5.1 Source Distribution & Severe Skew
Each dataset is composed of distinct underlying collection sources with significant size skew:

| Dataset | Source Name | Channel | Records | Dataset Share | Corpus Share | Distinct Groups |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `real_fin_scam` | Smishing Dataset IMC25 | SMS | 9,600 | 69.26% | 12.60% | 8,308 |
| `real_fin_scam` | Nigerian_Fraud.csv | Email | 3,265 | 23.56% | 4.29% | 2,689 |
| `real_fin_scam` | Kaggle Phishing & Legit | Email | 500 | 3.61% | 0.66% | 500 |
| `real_fin_scam` | smishtank.csv | SMS | 496 | 3.58% | 0.65% | 436 |
| `real_fin_legit` | MeAJOR (trec5) | Email | 27,291 | 43.78% | 35.82% | 25,586 |
| `real_fin_legit` | MeAJOR (trec7) | Email | 19,244 | 30.87% | 25.26% | 18,443 |
| `real_fin_legit` | MeAJOR (trec6) | Email | 11,127 | 17.85% | 14.60% | 10,972 |
| `real_fin_legit` | UCI SMS Spam Collection | SMS | 4,500 | 7.22% | 5.91% | 4,491 |
| `real_fin_legit` | Mendeley Financial Scams V2 | SMS | 170 | 0.27% | 0.22% | 170 |

### 5.2 Channel Confounding
Cross-tabulation reveals that communication channel is strongly correlated with class:

| Channel | Scam Records | Scam % | Legit Records | Legit % | Total Records | Total Share |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Email** | 3,765 | 27.16% | 57,662 | 92.51% | 61,427 | **80.62%** |
| **SMS** | 10,096 | 72.84% | 4,670 | 7.49% | 14,766 | **19.38%** |
| **Total** | 13,861 | 100.00% | 62,332 | 100.00% | 76,193 | 100.00% |

> [!IMPORTANT]
> - 72.84% of real scam messages are SMS, whereas 92.51% of legitimate messages are Email.
> - To prevent splits from having arbitrary channel shifts, **stratification must be performed jointly across `(label, channel)`**. Every split (train, validation, test) must contain the exact same joint proportions.

### 5.3 Legitimate Subcategories
In `real_fin_legit_processed.csv`:
- `general_legitimate`: 43,131 records (69.20% of legit)
- `financial_legitimate`: 19,201 records (30.80% of legit)
All financial legitimate messages are concentrated in MeAJOR emails (18,979) and Mendeley SMS (76) / UCI SMS (146).

---

## 6. Feasibility Assessment of Source-Aware Grouping

The feasibility of grouping by `source` (i.e., holding out entire sources for validation or testing, such as Leave-One-Source-Out) was evaluated.

### Verdict: **SOURCE-LEVEL GROUPING IS INFEASIBLE AND METHODOLOGICALLY FLAWED**

#### Reasons:
1. **Zero Source Overlap:** The intersection of sources between scam and legitimate data is empty ($\emptyset$). No single source contains both scam and legitimate communications. If an entire source were assigned to a split, that split would suffer catastrophic class imbalance (e.g., holding out a source produces an evaluation set with 0% scam or 0% legitimate).
2. **Extreme Source Skew:** IMC25 represents 69.26% of all scams. Assigning IMC25 to one split would place nearly 70% of all scam examples into that single split, completely violating any target 80/10/10 ratio. Similarly, MeAJOR trec5 represents 43.78% of all legitimate records.
3. **Cross-Source Near-Duplicate Leakage:** Forensic analysis revealed that **61 duplicate clusters in `real_fin_scam` span multiple raw sources** (e.g. repeated smishing templates shared between `Smishing Dataset IMC25` and `smishtank.csv`). Grouping by source would place source A in train and source B in test, directly leaking identical scam templates across splits!
4. **Channel-Source Entanglement:** Every source is strictly single-channel (e.g., IMC25 is 100% SMS; Nigerian_Fraud is 100% Email). Splitting by source would simultaneously destabilize channel distributions.

**Conclusion:** Groups must be defined by **near-duplicate clusters**, while **stratification** must be applied across joint `(label, channel)` strata.

---

## 7. Cluster Size Outlier Analysis

Cluster sizes were audited to determine whether unusually large clusters could distort split proportions:

### 7.1 Scam Clusters (1,217 clusters, 3,206 records)
- **Minimum:** 2 records
- **Median:** 2 records
- **Mean:** 2.63 records
- **75th Percentile:** 3 records
- **Maximum:** 18 records (Clusters `REAL_FIN_SCAM_C0001`, `C0002`, `C0003`)
- **Assessment:** Scam clusters are compact and uniform. The largest cluster (18 records) represents only 0.13% of the scam dataset and 0.02% of the corpus. It introduces zero stratification difficulty.

### 7.2 Legitimate Clusters (1,334 clusters, 4,005 records)
- **Minimum:** 2 records
- **Median:** 2 records
- **Mean:** 3.00 records
- **75th Percentile:** 2 records
- **Maximum:** 166 records (`REAL_FIN_LEGIT_C0001`)
- **Next Largest Clusters:**
  - `REAL_FIN_LEGIT_C0002`: 72 records
  - `REAL_FIN_LEGIT_C0003`: 51 records
  - `REAL_FIN_LEGIT_C0004`: 50 records
  - `REAL_FIN_LEGIT_C0005`: 50 records
  - `REAL_FIN_LEGIT_C0006`: 47 records
  - `REAL_FIN_LEGIT_C0007`: 47 records
  - `REAL_FIN_LEGIT_C0008`: 46 records

### 7.3 Impact of `REAL_FIN_LEGIT_C0001` (166 Records)
- **Content:** Automated stock quote email notification templates from Enron/MeAJOR (`"Stock Notification for [ORGANIZATION] ... ONEOK Inc. Stock Quote Notification..."`).
- **Relative Size:** 166 records represent:
  - 0.27% of the legitimate dataset (62,332 records)
  - 0.22% of the total real corpus (76,193 records)
  - 2.18% of a 10% test split (~7,619 records)
- **Feasibility:** Because 166 records is only 2.18% of the test partition, a greedy group-aware partitioner that sorts clusters descending by size easily packs `REAL_FIN_LEGIT_C0001` into the training split (or validation/test split) while maintaining split proportions within < 0.01% of the target.
- **Leakage Prevention Necessity:** Keeping `REAL_FIN_LEGIT_C0001` intact is essential; if these 166 near-identical boilerplate templates were split between train and test, the model would simply memorize the corporate disclaimer text and artificially inflate evaluation metrics.

---

## 8. Splitting Strategy & Simulation Validation

### 8.1 Recommended Strategy: Stratified Group-Aware Greedy Partitioning (SGGP)
To achieve leakage prevention while maintaining exact joint distributions:

1. **Atomic Group Construction:**
   - Assign `group_id = duplicate_cluster_id` for clustered records.
   - Assign `group_id = f"singleton_{record_id}"` for unclustered records.
2. **Stratum Definition:**
   - Partition the 71,533 groups into 4 mutually exclusive joint strata based on `(label, channel)`:
     - Stratum 0: Legit Email (55,001 groups, 57,662 records)
     - Stratum 1: Legit SMS (4,660 groups, 4,670 records)
     - Stratum 2: Scam Email (3,189 groups, 3,765 records)
     - Stratum 3: Scam SMS (8,683 groups, 10,096 records)
3. **Deterministic Bin-Packing Allocation:**
   - Target ratios: $80\%$ Train, $10\%$ Validation, $10\%$ Test.
   - Within each stratum, sort groups descending by size (`size`, secondary deterministic key `group_id`).
   - For each group, greedily allocate it to the split that minimizes deviation from its target quota.

### 8.2 Simulation Results (80/10/10 Target)

A full simulation was executed across all 76,193 records and 71,533 groups:

| Split | Target % | Actual Records | Actual % | Absolute Deviation | Scam Records | Scam % | Email Records | SMS Records | Leaked Groups |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Train** | 80.00% | 60,957 | **80.0034%** | **+0.0034%** (+3 recs) | 11,091 | 18.19% | 49,143 | 11,814 | **0** |
| **Validation** | 10.00% | 7,618 | **9.9983%** | **-0.0017%** (-1 rec) | 1,385 | 18.18% | 6,142 | 1,476 | **0** |
| **Test** | 10.00% | 7,618 | **9.9983%** | **-0.0017%** (-1 rec) | 1,385 | 18.18% | 6,142 | 1,476 | **0** |
| **Total** | 100.00% | 76,193 | 100.0000% | 0.0000% | 13,861 | 18.19% | 61,427 | 14,766 | **0** |

### Joint Strata Preservation Matrix:

$$\begin{array}{l|cc|cc|c}
\textbf{Split} & \textbf{Legit Email} & \textbf{Legit SMS} & \textbf{Scam Email} & \textbf{Scam SMS} & \textbf{Total} \\
\hline
\text{Train (80\%)} & 46,130 & 3,736 & 3,013 & 8,078 & 60,957 \\
\text{Validation (10\%)} & 5,766 & 467 & 376 & 1,009 & 7,618 \\
\text{Test (10\%)} & 5,766 & 467 & 376 & 1,009 & 7,618 \\
\hline
\textbf{Total} & \mathbf{57,662} & \mathbf{4,670} & \mathbf{3,765} & \mathbf{10,096} & \mathbf{76,193}
\end{array}$$

- **Class distribution across every split:** Identical to the corpus baseline ($18.18\% - 18.19\%$ scam).
- **Channel distribution across every split:** Identical to the corpus baseline ($80.62\%$ email, $19.38\%$ SMS).
- **Group Leakage:** Exactly **0 groups leaked** across splits.

---

## 9. Research Methodology Disclosures & Limitations

The following methodological characteristics must be explicitly disclosed in publication:
1. **Partial Clustering of Legitimate Communications:** In Task 02, near-duplicate clustering for `real_fin_legit` was conducted on a representative 25,000-record sample due to the $O(N^2)$ pairwise comparison complexity of 62,332 emails. Consequently, 58,327 legitimate records remain unclustered singletons. While scam duplicates were 100% audited and clustered across all 13,861 scam records (preventing scam template leakage), some undetected legitimate duplicate pairs may exist across splits.
2. **Class-Channel Confounding:** In real-world data, scam communications are predominantly mobile SMS (72.84%), whereas legitimate communications are predominantly enterprise email (92.51%). While our splitting stratifies channel to ensure train, validation, and test share the identical joint distribution, models evaluated on this benchmark could potentially learn spurious channel-correlated cues (such as text length). Transformer evaluation should report channel-disaggregated metrics (e.g. SMS-only F1 and Email-only F1).
3. **Source Distribution Imbalance:** Over 69% of real scams come from the IMC25 smishing repository, and over 43% of legitimate messages come from MeAJOR trec5. Source-aware grouping is unfeasible due to source-class confounding and multi-source scam clusters.
4. **Strict Isolation of Synthetic Scams:** `synthetic_financial_scams` (7,643 records) is deliberately excluded from these initial splits to preserve clean experimental control. It will be utilized in subsequent tasks for zero-shot generalization testing and synthetic-to-real transfer evaluation.

---

## 10. Recommendations for Task 04.1 (Implementation)

1. **Target Proportions:** Adopt **80% Train, 10% Validation, 10% Test**.
2. **Pipeline Module:** Implement `src/data/splitter.py` featuring `GroupAwareStratifiedSplitter` that applies deterministic greedy bin-packing over joint `(label, channel)` strata.
3. **Artifact Generation:** Output:
   - `data/splits/train.csv` (60,957 records)
   - `data/splits/val.csv` (7,618 records)
   - `data/splits/test.csv` (7,618 records)
   - `data/splits/split_manifest.json` (SHA-256 hashes, record counts, and leakage verification flags)
4. **Automated Verification:** Add unit tests verifying:
   - Zero duplicate cluster leakage ($\text{clusters}(\text{train}) \cap \text{clusters}(\text{test}) = \emptyset$).
   - Exact conservation of all 76,193 records ($\text{train} \cup \text{val} \cup \text{test} = \text{corpus}$).
   - Class and channel ratio stability within $\pm 0.1\%$.

---

## 11. Regression Test Suite Status

All 21 unit and integration tests continue to pass seamlessly in the Python 3.13 virtual environment (`.\.venv\Scripts\python.exe -m pytest tests/ -v`):
```text
tests/test_audit.py::test_detect_column_helpers PASSED                   [  4%]
tests/test_audit.py::test_data_quality_audit PASSED                      [  9%]
tests/test_audit.py::test_composition_audit PASSED                       [ 14%]
tests/test_audit.py::test_text_profiler PASSED                           [ 19%]
tests/test_audit.py::test_duplicate_and_lsh_detection PASSED             [ 23%]
tests/test_preprocessing.py::test_raw_dataset_hash_preservation PASSED   [ 28%]
tests/test_preprocessing.py::test_placeholder_normalization_categories PASSED [ 33%]
tests/test_preprocessing.py::test_targeted_placeholder_corrections PASSED [ 38%]
tests/test_preprocessing.py::test_nested_and_malformed_placeholders PASSED [ 42%]
tests/test_preprocessing.py::test_nested_cleanup_preserves_words PASSED  [ 47%]
tests/test_preprocessing.py::test_placeholder_idempotency PASSED         [ 52%]
tests/test_preprocessing.py::test_unknown_placeholder_preservation PASSED [ 57%]
tests/test_preprocessing.py::test_channel_harmonization_rules PASSED     [ 61%]
tests/test_preprocessing.py::test_schema_mapping_and_columns PASSED      [ 66%]
tests/test_preprocessing.py::test_cluster_mapping_loader PASSED          [ 71%]
tests/test_preprocessing.py::test_synthetic_and_legit_processing_mock PASSED [ 76%]
tests/test_validation.py::test_lsh_theoretical_probabilities PASSED      [ 80%]
tests/test_validation.py::test_word_shingles PASSED                      [ 85%]
tests/test_validation.py::test_connected_component_clustering PASSED     [ 90%]
tests/test_validation.py::test_placeholder_investigation PASSED          [ 95%]
tests/test_validation.py::test_extreme_message_investigation PASSED      [100%]
============================= 21 passed in 4.85s ==============================
```

Raw datasets remain completely untouched with verified SHA-256 hashes.

