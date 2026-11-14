# Legitimate Communication Dataset Card

## 1. Overview & Provenance

`real_fin_legit.csv` provides the negative baseline (`label=0`, `is_synthetic=false`) for the financial scam detection research framework. It comprises **62,332 verified legitimate English-language digital communications** spanning mobile SMS messages and workplace/enterprise emails.

### Composition & Sourcing

| Collection Source | Channel | Record Count | Share (%) | Financial Legitimate | General Legitimate |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **MeAJOR (trec5)** | Email | 27,291 | 43.78% | 13,124 | 14,167 |
| **MeAJOR (trec7)** | Email | 19,244 | 30.87% | 3,350 | 15,894 |
| **MeAJOR (trec6)** | Email | 11,127 | 17.85% | 2,505 | 8,622 |
| **UCI SMS Spam Collection** | SMS | 4,500 | 7.22% | 146 | 4,354 |
| **Mendeley Financial Scams Dataset (V2)** | SMS | 170 | 0.27% | 76 | 94 |
| **Total Legitimate Corpus** | | **62,332** | **100.00%** | **19,201 (30.80%)** | **43,131 (69.20%)** |

- **Email Communications:** 57,662 records (92.51%)
- **SMS Communications:** 4,670 records (7.49%)

---

## 2. Legitimate Category Taxonomy

Legitimate communications are categorized into two primary analytical classes:
1. **`financial_legitimate` (19,201 records, 30.80%):** Benign transactional, banking, credit, invoice, energy trading, dividend, account summary, and business-finance communications. Essential for teaching models to distinguish benign financial terminology from fraudulent lures.
2. **`general_legitimate` (43,131 records, 69.20%):** General workplace, administrative, technical mailing list, scheduling, and personal interpersonal communications.

---

## 3. Duplicate Cluster Structure & Cluster Outlier Analysis

Near-duplicate analysis via MinHash LSH (Jaccard similarity threshold $\ge 0.85$) identified:
- **Clustered Records:** 4,005 records (6.43%) participating in **1,334 multi-record clusters** (`REAL_FIN_LEGIT_C0001` through `REAL_FIN_LEGIT_C1334`).
- **Singletons:** 58,327 records (93.57%) are independent singleton messages.
- **Cluster Outlier:** The largest cluster, **`REAL_FIN_LEGIT_C0001` (166 records)**, consists of automated stock quote email notifications from Enron/MeAJOR. These repeated templates are kept strictly within a single partition in the benchmark splits to eliminate data leakage.

---

## 4. Upstream Provenance & Data Sanitization

- **MeAJOR Provenance:** Released on Zenodo (DOI: [10.5281/zenodo.18471483](https://zenodo.org/records/18471483)) under CC BY 4.0. Incorporates Enron enterprise communications and TREC 2005/2006/2007 legitimate email corpuses with entity anonymization.
- **Mobile SMS Provenance:** Derived from the academic UCI SMS Spam Collection (Almeida et al.) and Mendeley Financial Communications (V2).
- **Text Reduction Verification (Task 03.1):** Forensic character-level audits proved that large character reductions in MeAJOR records (such as `MEAJOR-LEG-054248`, -12,345 characters) resulted strictly from stripping malformed recursive regex bracket cascades (`[[[[PRODUCT]]]]`). Zero natural language words or punctuation marks were removed.

---

## 5. Methodological Limitations

1. **Sampling of Legitimate Near-Duplicates:** Duplicate clustering for `real_fin_legit` was evaluated on a representative 25,000-record sample during Task 02. Undetected legitimate near-duplicates may remain among unclustered singletons.
2. **Channel-Class Confounding:** Legitimate data is 92.51% email, whereas scam data is 72.84% SMS. All experimental splits must stratify channel jointly with class to prevent spurious correlation artifacts.
