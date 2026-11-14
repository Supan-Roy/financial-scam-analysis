# Legitimate Dataset Audit Baseline

## 1. Verified Record Counts & Ingestion Audit

- **Raw Dataset Filename:** `data/raw/real_fin_legit.csv`
- **Total Validated Records:** **62,332**
- **Binary Labels:** 100% `label=0` (Legitimate)
- **Synthetic Flags:** 100% `is_synthetic=false`
- **Missing / Null Text Records:** **0** (100% complete)
- **SHA-256 Hash:** `6810244c341b8f484e19b16a6e13482b38877f5608debfb829874e145adac6bc` (Verified Intact)

---

## 2. Ingestion Composition by Source & Track

| Release Source | Track / Sub-Collection | Original Channel | Canonical Channel | Record Count | Share (%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **MeAJOR** | TREC 2005 Benign Email (`trec5`) | `email` | `email` | 27,291 | 43.78% |
| **MeAJOR** | TREC 2007 Benign Email (`trec7`) | `email` | `email` | 19,244 | 30.87% |
| **MeAJOR** | TREC 2006 Benign Email (`trec6`) | `email` | `email` | 11,127 | 17.85% |
| **UCI Repository** | SMS Spam Collection (Benign) | `sms` | `sms` | 4,500 | 7.22% |
| **Mendeley Data** | Financial Scams Detection (V2 Benign) | `sms` | `sms` | 170 | 0.27% |
| **Total Corpus** | | | | **62,332** | **100.00%** |

---

## 3. Category Breakdown

- **`general_legitimate`:** **43,131 records (69.20%)**
- **`financial_legitimate`:** **19,201 records (30.80%)**

---

## 4. Near-Duplicate Cluster Structure

- **Sample Size Audited:** 25,000 representative records (LSH MinHash 100 permutations, Jaccard threshold $\ge 0.85$).
- **Multi-Record Clusters:** **1,334 clusters** containing **4,005 records** (6.43%).
- **Singletons:** **58,327 records** (93.57%).
- **Maximum Cluster Size:** 166 records (`REAL_FIN_LEGIT_C0001`, stock quote alerts).
