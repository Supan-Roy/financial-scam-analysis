# Task 04.1 Completion Report: Leakage-Resistant Group-Aware Dataset Splitter

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Implementation Date:** 2026-11-08  
**Pipeline Status:** Verified, Validated & Reproducible  
**Referenced Deliverables:**
- Summary Report: [`reports/splitting/split_summary.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_summary.md)
- Feasibility Analysis: [`reports/splitting/split_feasibility_report.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_feasibility_report.md)
- Split Assignments: [`data/splits/split_assignments.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/split_assignments.csv)
- Distribution Table: [`reports/splitting/split_distribution.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_distribution.csv)
- Group Integrity Table: [`reports/splitting/split_group_integrity.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_group_integrity.csv)
- Splitting Configuration: [`configs/splitting_config.yaml`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/configs/splitting_config.yaml)

---

## 1. Executive Summary & Objective

In Task 04.1, we implemented, verified, and executed a deterministic, leakage-resistant dataset splitting pipeline for the real-world binary scam classification benchmark.

The pipeline processes all **76,193 real-world records** (`13,861` scam messages from `real_fin_scam_processed.csv` and `62,332` legitimate communications from `real_fin_legit_processed.csv`), strictly excluding synthetic data (`synthetic_financial_scams_processed.csv`).

Every known near-duplicate cluster (MinHash LSH Jaccard $\ge 0.85$) was treated as an atomic, indivisible block. Unclustered records were constructed as independent singleton groups. The resulting **71,533 unique groups** were partitioned into Train (80%), Validation (10%), and Test (10%) sets using **Stratified Group-Aware Greedy Partitioning (SGGP)**.

All 12 mandatory validation checks passed, verifying **0% duplicate cluster leakage**, **0 duplicate records**, **100% record conservation**, and **< 0.004% deviation** from target proportions.

---

## 2. Implementation Overview & Architecture

The splitting architecture was organized into modular components under `src/data/` adhering to the research framework's software standards:

```
Pipeline Modular Organization
├── configs/splitting_config.yaml       # Declarative experiment configuration (ratios, paths, seed)
├── src/data/splitter.py                # GroupAwareSplitter & GroupMetadata (SGGP allocation algorithm)
├── src/data/split_validator.py         # SplitValidator (12 mandatory integrity & leakage checks)
├── src/data/split_reporter.py          # SplitReporter (markdown summary, distribution & integrity CSVs)
├── scripts/run_split.py                # Standalone orchestration CLI script
├── main.py (--split)                   # Top-level framework CLI integration
└── tests/test_splitter.py              # Automated test suite (8 dedicated tests, 29 total in suite)
```

---

## 3. Allocation Algorithm: Stratified Group-Aware Greedy Partitioning (SGGP)

### 3.1 Indivisible Group Construction
To prevent near-duplicate template leakage between train and test splits, group identifiers are assigned by:
$$\text{group\_id} = \begin{cases} \text{duplicate\_cluster\_id}, & \text{if } \text{duplicate\_cluster\_id is not null and non-empty} \\ \text{"singleton\_" } + \text{record\_id}, & \text{otherwise} \end{cases}$$

- **Duplicate Clusters:** 2,551 multi-record clusters containing 7,211 records.
- **Singleton Groups:** 68,982 records, each assigned a unique `singleton_{record_id}` group.
- **Null Safety:** Unclustered records are never lumped into a single null group, preserving maximum degrees of freedom for balanced partitioning.
- **Purity Guarantee:** All 2,551 duplicate clusters were verified to be 100% homogeneous in label and channel.

### 3.2 Stratified Multi-Capacity Bin-Packing
1. **Primary Strata Partitioning:** Groups are partitioned into 4 mutually exclusive strata based on joint `(label, channel)`:
   - *Legit Email:* 55,001 groups (57,662 records)
   - *Legit SMS:* 4,660 groups (4,670 records)
   - *Scam Email:* 3,189 groups (3,765 records)
   - *Scam SMS:* 8,683 groups (10,096 records)
2. **Deterministic Group Ordering:** Within each stratum, groups are sorted descending by cluster size (`size`), with a secondary deterministic sort on `group_id` (alphabetical ascending). This places large clusters first (bin-packing heuristic), preventing late-stage proportion distortion.
3. **Greedy Allocation:** For each group of size $s$, the algorithm assigns it to the split $k \in \{\text{train}, \text{validation}, \text{test}\}$ that minimizes its relative target quota fill:
$$\arg\min_{k} \frac{C_k + s}{T_k}$$
where $C_k$ is the current count of records in split $k$, and $T_k = N_{\text{stratum}} \times r_k$ is the target record quota ($r_{\text{train}} = 0.8, r_{\text{val}} = 0.1, r_{\text{test}} = 0.1$).
4. **Idempotence & Determinism:** No stochastic random number generators are required during bin-packing; identical inputs guarantee 100% bitwise identical assignments on every execution.

---

## 4. Final Split Record & Group Counts

| Split Name | Target % | Actual Records | Actual % | Absolute Deviation | Total Groups | Multi-Record Clusters | Clustered Records | Singleton Groups / Records |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Train** | 80.00% | 60,957 | **80.0034%** | **+0.0034%** (+3 recs) | 57,221 | 2,037 | 5,773 | 55,184 |
| **Validation** | 10.00% | 7,618 | **9.9983%** | **-0.0017%** (-1 rec) | 7,156 | 257 | 719 | 6,899 |
| **Test** | 10.00% | 7,618 | **9.9983%** | **-0.0017%** (-1 rec) | 7,156 | 257 | 719 | 6,899 |
| **Total Corpus** | **100.00%** | **76,193** | **100.0000%** | **0.0000%** | **71,533** | **2,551** | **7,211** | **68,982** |

---

## 5. Multi-Attribute Distribution Analysis

### 5.1 Binary Class Balance Across Splits

| Split | Scam Count (Label 1) | Scam Share | Legit Count (Label 0) | Legit Share |
| :--- | :---: | :---: | :---: | :---: |
| **Train** | 11,091 | 18.19% | 49,866 | 81.81% |
| **Validation** | 1,385 | 18.18% | 6,233 | 81.82% |
| **Test** | 1,385 | 18.18% | 6,233 | 81.82% |
| **Total Real Corpus** | **13,861** | **18.19%** | **62,332** | **81.81%** |

*Class balance is preserved with less than 0.01% deviation across all three partitions.*

### 5.2 Communication Channel Distribution Across Splits

| Split | Email Records | Email Share | SMS Records | SMS Share |
| :--- | :---: | :---: | :---: | :---: |
| **Train** | 49,143 | 80.62% | 11,814 | 19.38% |
| **Validation** | 6,142 | 80.62% | 1,476 | 19.38% |
| **Test** | 6,142 | 80.62% | 1,476 | 19.38% |
| **Total Real Corpus** | **61,427** | **80.62%** | **14,766** | **19.38%** |

*Channel proportions are identical to the fourth decimal place across Train, Validation, and Test.*

### 5.3 Joint Strata Matrix `(Split x [Label, Channel])`

$$\begin{array}{l|cc|cc|c}
\textbf{Split} & \textbf{Legit Email} & \textbf{Legit SMS} & \textbf{Scam Email} & \textbf{Scam SMS} & \textbf{Total} \\
\hline
\text{Train (80\%)} & 46,130 & 3,736 & 3,013 & 8,078 & 60,957 \\
\text{Validation (10\%)} & 5,766 & 467 & 376 & 1,009 & 7,618 \\
\text{Test (10\%)} & 5,766 & 467 & 376 & 1,009 & 7,618 \\
\hline
\textbf{Total} & \mathbf{57,662} & \mathbf{4,670} & \mathbf{3,765} & \mathbf{10,096} & \mathbf{76,193}
\end{array}$$

### 5.4 Legitimate Category Distribution

In `real_fin_legit_processed.csv`:
- `general_legitimate`: 43,131 records (69.20% of legit)
  - Train: 34,506 (69.20%)
  - Validation: 4,312 (69.18%)
  - Test: 4,313 (69.20%)
- `financial_legitimate`: 19,201 records (30.80% of legit)
  - Train: 15,360 (30.80%)
  - Validation: 1,921 (30.82%)
  - Test: 1,920 (30.80%)

### 5.5 Source Representation Across Splits

| Dataset | Underlying Source | Corpus Total | Train Count (80%) | Val Count (10%) | Test Count (10%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `real_fin_scam` | Smishing Dataset IMC25 | 9,600 | 7,680 (80.00%) | 957 (9.97%) | 963 (10.03%) |
| `real_fin_scam` | Nigerian_Fraud.csv | 3,265 | 2,613 (80.03%) | 326 (9.98%) | 326 (9.98%) |
| `real_fin_scam` | Kaggle Phishing & Legit | 500 | 400 (80.00%) | 50 (10.00%) | 50 (10.00%) |
| `real_fin_scam` | smishtank.csv | 496 | 398 (80.24%) | 52 (10.48%) | 46 (9.27%) |
| `real_fin_legit` | MeAJOR (trec5) | 27,291 | 21,833 (79.99%) | 2,731 (10.01%) | 2,727 (9.99%) |
| `real_fin_legit` | MeAJOR (trec7) | 19,244 | 15,394 (79.99%) | 1,924 (10.00%) | 1,926 (10.01%) |
| `real_fin_legit` | MeAJOR (trec6) | 11,127 | 8,903 (80.01%) | 1,111 (9.98%) | 1,113 (10.00%) |
| `real_fin_legit` | UCI SMS Spam Collection | 4,500 | 3,600 (80.00%) | 449 (9.98%) | 451 (10.02%) |
| `real_fin_legit` | Mendeley Financial Scams V2 | 170 | 136 (80.00%) | 18 (10.59%) | 16 (9.41%) |

*Every single collection source is preserved in near-perfect 80/10/10 proportions.*

---

## 6. Mandatory Validation Results (12 Checks)

All 12 mandatory checks executed via [`src/data/split_validator.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/data/split_validator.py) returned **PASSED**:

1. **Total Record Count:** Exactly 76,193 records verified ($60,957 + 7,618 + 7,618 = 76,193$).
2. **No Record Missing:** 0 missing records; all 76,193 raw IDs present.
3. **No Record Duplicated:** 0 duplicate record IDs ($76,193$ unique).
4. **Single-Split Assignment:** Every record ID appears in exactly one split file.
5. **Duplicate Cluster Integrity:** All 2,551 duplicate clusters belong to exactly one split (**0 leaked clusters**).
6. **Group ID Isolation:** All 71,533 group IDs appear in exactly one split (**0 leaked groups**).
7. **Label Preservation:** All original labels (0 and 1) verified identical to processed inputs.
8. **Synthetic Scams Excluded:** 0 synthetic records detected (`synthetic_financial_scams` strictly absent).
9. **Processed Datasets Untouched:** Baseline SHA-256 hashes of processed datasets verified unchanged:
   - `real_fin_scam_processed.csv`: `ca5982d24190e542c5089d1de9d0af670b066beada1f0bf1e5daa4e58b853e6b` (MATCH)
   - `real_fin_legit_processed.csv`: `e4a4c323bded643d1986c00003dd02e592f27695db17cde7fabafc43d82321a4` (MATCH)
10. **Proportions Verified:** Train 80.0034%, Val 9.9983%, Test 9.9983% (all deviations < 0.004%).
11. **Distribution Integrity:** Source, channel, and legitimate categories validated.
12. **Idempotence & Reproducibility:** Repeated execution verified bitwise identical.

---

## 7. Automated Test Suite Results

A comprehensive test suite of **29 tests** was executed via the project virtual environment:
```text
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

**Results:**
- `tests/test_audit.py`: 5 passed
- `tests/test_validation.py`: 5 passed
- `tests/test_preprocessing.py`: 11 passed
- `tests/test_splitter.py`: 8 passed
  - `test_singleton_group_construction` PASSED
  - `test_global_group_id_uniqueness` PASSED
  - `test_duplicate_cluster_integrity_no_split_leakage` PASSED
  - `test_deterministic_reproducibility` PASSED
  - `test_mixed_stratum_group_detection` PASSED
  - `test_synthetic_dataset_exclusion` PASSED
  - `test_record_preservation_and_duplicate_detection` PASSED
  - `test_invalid_target_ratios` PASSED

**Total: 29 passed, 0 failed in 7.34 seconds.**

---

## 8. Cryptographic Hashes of Generated Split Artifacts

| File Path | Description | Records | Size | SHA-256 Hash |
| :--- | :--- | :---: | :---: | :--- |
| [`data/splits/train.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/train.csv) | Training partition (80%) | 60,957 | 188.60 MB | `44f0009aac5b47ddf64c8483df27007170800cb6bf67fba4b562d2ce8b675cce` |
| [`data/splits/validation.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/validation.csv) | Validation partition (10%) | 7,618 | 23.72 MB | `da9cbf17bd47d7f1df3d2dc6f4b2d0517274092a654f55b3af1a7e07fc776a5c` |
| [`data/splits/test.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/test.csv) | Held-out test partition (10%) | 7,618 | 23.34 MB | `01ac0c3e8c2788ba4bf3a27f73d10b84ed2fc5e12ac5a993cf23d3020b4021f0` |
| [`data/splits/split_assignments.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/split_assignments.csv) | Fast reproducibility mapping | 76,193 | 5.80 MB | `17db4df33e956cc1b82e88e176d81a5e11e07dcde8007b8fb27cc7447a91ecbe` |

---

## 9. Limitations & Research Methodology Disclosures

1. **Legitimate Near-Duplicate Sampling:** As documented in Task 02, near-duplicate analysis for `real_fin_legit` was evaluated on a representative 25,000-record sample. Consequently, 58,327 legitimate communications remain unclustered singletons. While scam duplicates were 100% audited and clustered across all 13,861 scam records (preventing scam template leakage), some undetected duplicate relationships may remain among unclustered legitimate emails.
2. **Channel-Class Confounding:** In the real-world benchmark, scams are 72.84% SMS while legitimate messages are 92.51% Email. Although SGGP enforces identical joint $P(\text{channel}, \text{class})$ distributions across splits, model evaluation should report channel-disaggregated metrics (SMS F1 and Email F1) to ensure models are not relying on surface channel features.
3. **Synthetic Scam Benchmark Isolation:** `synthetic_financial_scams_processed.csv` (7,643 records) was strictly excluded from these splits to preserve an unpolluted real-world benchmark. It remains available for zero-shot testing, domain adaptation, and synthetic data augmentation experiments in subsequent phases.

---

## 10. Reproduction Commands

To deterministically reproduce the exact splits and audit reports:

```powershell
# Using the top-level main driver
.\.venv\Scripts\python.exe main.py --split

# Or using the standalone script directly
.\.venv\Scripts\python.exe scripts/run_split.py --config configs/splitting_config.yaml

# To run the complete regression test suite
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

---

## 11. Index of Created & Modified Files

### Created Files
1. [`configs/splitting_config.yaml`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/configs/splitting_config.yaml) — Declarative configuration for data splitting.
2. [`src/data/splitter.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/data/splitter.py) — GroupAwareSplitter and SGGP allocation engine.
3. [`src/data/split_validator.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/data/split_validator.py) — Validation suite for record conservation and leakage prevention.
4. [`src/data/split_reporter.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/data/split_reporter.py) — Generator for split summaries, distributions, and integrity tables.
5. [`scripts/run_split.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/scripts/run_split.py) — CLI splitting pipeline driver.
6. [`tests/test_splitter.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/tests/test_splitter.py) — 8 automated tests for splitting and validation logic.
7. [`data/splits/split_assignments.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/split_assignments.csv) — 76,193-row reproducibility mapping artifact (tracked in git).
8. [`reports/splitting/split_summary.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_summary.md) — Summary markdown report.
9. [`reports/splitting/split_distribution.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_distribution.csv) — Detailed strata distribution table.
10. [`reports/splitting/split_group_integrity.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/split_group_integrity.csv) — Group-level integrity statistics.
11. [`reports/splitting/task_04_1_completion_report.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/splitting/task_04_1_completion_report.md) — Comprehensive completion synthesis report (this document).
*(Note: Generated partitions `train.csv` (188 MB), `validation.csv` (24 MB), and `test.csv` (23 MB) reside locally in `data/splits/` and are safely gitignored in accordance with GitHub's 100MB file limit).*

### Modified Files
1. [`.gitignore`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/.gitignore) — Explicitly unignored `!data/splits/split_assignments.csv` to ensure fast 1-click reproducibility in git.
2. [`main.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/main.py) — Added `--split` CLI option and execution binding.
3. [`requirements.txt`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/requirements.txt) — Added `pyyaml>=6.0` dependency.

