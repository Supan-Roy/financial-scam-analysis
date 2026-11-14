# Leakage-Resistant Group-Aware Data Splitting Methodology

## 1. Context & Motivation

In NLP-based financial fraud detection, traditional random record-level train/test splitting causes severe **data leakage**. Phishing campaigns and enterprise mailing lists frequently reuse identical or near-identical templates (e.g. repeated IRS refund notices, Enron stock alerts). 

If near-duplicate messages are split between training and test sets, machine learning and Transformer models can memorize boilerplate phrasing, achieving artificially inflated test performance that fails to generalize to unseen real-world attacks.

---

## 2. Experimental Benchmark Scope

The initial benchmark is strictly restricted to **real-world empirical communications**:
- **Included:** `real_fin_scam_processed.csv` (13,861 records) + `real_fin_legit_processed.csv` (62,332 records) = **76,193 total records**.
- **Strictly Excluded:** `synthetic_financial_scams_processed.csv` (7,643 records) is held out to preserve clean in-distribution evaluation, reserved for zero-shot generalization testing and synthetic-to-real transfer studies in subsequent phases.

---

## 3. Group Construction & Singleton Rule

To eliminate template leakage, records are partitioned at the **group level**, where every group is treated as an indivisible atomic block:

$$\text{group\_id} = \begin{cases} \text{duplicate\_cluster\_id}, & \text{if } \text{duplicate\_cluster\_id is not null and non-empty} \\ \text{"singleton\_" } + \text{record\_id}, & \text{otherwise} \end{cases}$$

- **Duplicate Clusters:** 2,551 multi-record clusters (7,211 records) discovered via MinHash LSH (Jaccard similarity threshold $\ge 0.85$).
- **Singleton Groups:** 68,982 records without near-duplicates, each assigned an independent `singleton_{record_id}` group.
- **Null Safety:** Unclustered records are **never** grouped into a monolithic null group, preserving maximal degrees of freedom for balanced allocation.
- **Total Groups:** Exactly **71,533 globally unique, class-pure, channel-pure groups**.

---

## 4. Stratified Group-Aware Greedy Partitioning (SGGP)

Groups are allocated into Train (80%), Validation (10%), and Test (10%) splits using deterministic multi-capacity bin-packing:

1. **Stratum Partitioning:** Groups are divided into 4 mutually exclusive strata based on joint `(label, channel)`:
   - *Legit Email:* 55,001 groups (57,662 records)
   - *Legit SMS:* 4,660 groups (4,670 records)
   - *Scam Email:* 3,189 groups (3,765 records)
   - *Scam SMS:* 8,683 groups (10,096 records)
2. **Deterministic Group Ordering:** Within each stratum, groups are sorted descending by size (`size`), with a secondary deterministic sort on `group_id` (alphabetical ascending). This packs large clusters first (e.g. `REAL_FIN_LEGIT_C0001` with 166 records), preventing late-stage proportion skew.
3. **Greedy Allocation:** Each group of size $s$ is assigned to the split $k \in \{\text{train}, \text{validation}, \text{test}\}$ that minimizes relative target quota fill:
   $$\arg\min_{k} \frac{C_k + s}{T_k}$$
   where $C_k$ is the current record count in split $k$, and $T_k = N_{\text{stratum}} \times r_k$ is the target record quota ($r_{\text{train}} = 0.8, r_{\text{val}} = 0.1, r_{\text{test}} = 0.1$).

---

## 5. Quantitative Split Verification

| Split Name | Target % | Actual Records | Actual % | Deviation | Scam (Label 1) | Legit (Label 0) | Email Records | SMS Records | Leaked Groups |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Train** | 80.00% | 60,957 | **80.0034%** | **+0.0034%** | 11,091 (18.19%) | 49,866 (81.81%) | 49,143 (80.62%) | 11,814 (19.38%) | **0** |
| **Validation** | 10.00% | 7,618 | **9.9983%** | **-0.0017%** | 1,385 (18.18%) | 6,233 (81.82%) | 6,142 (80.62%) | 1,476 (19.38%) | **0** |
| **Test** | 10.00% | 7,618 | **9.9983%** | **-0.0017%** | 1,385 (18.18%) | 6,233 (81.82%) | 6,142 (80.62%) | 1,476 (19.38%) | **0** |
| **Total Real Corpus**| **100.00%** | **76,193** | **100.0000%** | **0.0000%** | **13,861 (18.19%)**| **62,332 (81.81%)**| **61,427 (80.62%)**| **14,766 (19.38%)**| **0** |

- **Duplicate Cluster Leakage:** Exactly **0 duplicate clusters** divided between splits.
- **Class & Channel Stratification:** Every split preserves the corpus baseline ($18.18\% - 18.19\%$ scam, $80.62\%$ email, $19.38\%$ SMS).

---

## 6. How to Load and Reproduce Splits

### Fast Reproducibility via `split_assignments.csv`
The mapping artifact [`data/splits/split_assignments.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/split_assignments.csv) (5.80 MB, 76,193 rows) is tracked in Git. It can be merged directly with the processed datasets:

```python
import pandas as pd

# Load processed data
scam_df = pd.read_csv("data/processed/real_fin_scam_processed.csv")
legit_df = pd.read_csv("data/processed/real_fin_legit_processed.csv")
full_df = pd.concat([scam_df, legit_df], ignore_index=True)

# Load tracked split assignments
assignments_df = pd.read_csv("data/splits/split_assignments.csv")
full_df = full_df.merge(assignments_df[["record_id", "split", "group_id"]], on="record_id")

train_df = full_df[full_df["split"] == "train"]
val_df = full_df[full_df["split"] == "validation"]
test_df = full_df[full_df["split"] == "test"]
```

### Full Pipeline Re-Execution
To deterministically regenerate all split partitions on disk:
```powershell
.\.venv\Scripts\python.exe main.py --split
```
