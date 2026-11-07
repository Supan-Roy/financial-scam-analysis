# Leakage-Resistant Group-Aware Dataset Splitting Summary Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Execution Date:** 2026-11-08  
**Scope:** Real-world benchmark (`real_fin_scam` + `real_fin_legit`), 76,193 total records.  
**Synthetic Scam Status:** Strictly excluded from initial benchmark splits.

---

## 1. Executive Summary & Split Proportions

The dataset was partitioned using **Stratified Group-Aware Greedy Partitioning (SGGP)**. The algorithm preserves every duplicate cluster within a single partition while maintaining exact joint stratification across binary labels and communication channels.

| Split Name | Target % | Actual Records | Actual % | Deviation | Scam (Label 1) | Legit (Label 0) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `train` | 80.0% | 60,957 | 80.0034% | +0.0034% | 11,091 (18.19%) | 49,866 (81.81%) |
| `validation` | 10.0% | 7,618 | 9.9983% | -0.0017% | 1,385 (18.18%) | 6,233 (81.82%) |
| `test` | 10.0% | 7,618 | 9.9983% | -0.0017% | 1,385 (18.18%) | 6,233 (81.82%) |
| **Total Real Corpus** | **100.0%** | **76,193** | **100.0000%** | **0.0000%** | **13,861 (18.19%)** | **62,332 (81.81%)** |

---

## 2. Channel Distribution by Split

| Split Name | Total Records | Email Records (%) | SMS Records (%) |
| :--- | :---: | :---: | :---: |
| `train` | 60,957 | 49,143 (80.62%) | 11,814 (19.38%) |
| `validation` | 7,618 | 6,142 (80.62%) | 1,476 (19.38%) |
| `test` | 7,618 | 6,142 (80.62%) | 1,476 (19.38%) |
| **Total Real Corpus** | **76,193** | **61,427 (80.62%)** | **14,766 (19.38%)** |

---

## 3. Joint Strata Preservation Matrix

$$\begin{array}{l|cc|cc|c}
\textbf{Split} & \textbf{Legit Email} & \textbf{Legit SMS} & \textbf{Scam Email} & \textbf{Scam SMS} & \textbf{Total} \\
\hline
\text{Train (80\%)} & 46,130 & 3,736 & 3,013 & 8,078 & 60,957 \\
\text{Validation (10\%)} & 5,766 & 467 & 376 & 1,009 & 7,618 \\
\text{Test (10\%)} & 5,766 & 467 & 376 & 1,009 & 7,618 \\
\hline
\textbf{Total} & \mathbf{57,662} & \mathbf{4,670} & \mathbf{3,765} & \mathbf{10,096} & \mathbf{76,193}
\end{array}$$

---

## 4. Group & Duplicate Cluster Leakage Audit

- **Total Distinct Groups:** 71,533
- **Multi-Record Duplicate Clusters:** 2,551 (7,211 records)
- **Singleton Groups:** 68,982 (68,982 records)
- **Groups Leaked Across Splits:** **0 (0.0% leakage)**
- **Duplicate Clusters Divided Between Splits:** **0 (0.0% leakage)**
- **Integrity Status:** **VERIFIED INTACT & LEAKAGE-FREE**

---

## 5. Generated Split Artifacts & Cryptographic Hashes

| Artifact File | Split Role | File Size | SHA-256 Hash |
| :--- | :--- | :---: | :--- |
| `train.csv` | `train` | 188.60 MB | `44f0009aac5b47ddf64c8483df27007170800cb6bf67fba4b562d2ce8b675cce` |
| `validation.csv` | `validation` | 23.72 MB | `da9cbf17bd47d7f1df3d2dc6f4b2d0517274092a654f55b3af1a7e07fc776a5c` |
| `test.csv` | `test` | 23.34 MB | `01ac0c3e8c2788ba4bf3a27f73d10b84ed2fc5e12ac5a993cf23d3020b4021f0` |
| `split_assignments.csv` | `assignments` | 5.80 MB | `17db4df33e956cc1b82e88e176d81a5e11e07dcde8007b8fb27cc7447a91ecbe` |

*Full assignments mapped in [`data/splits/split_assignments.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/split_assignments.csv).*
