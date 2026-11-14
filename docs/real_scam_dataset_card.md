# Real-World Financial Scam Dataset Card

## 1. Overview & Provenance

`real_fin_scam.csv` is an aggregated, audited corpus of **13,861 English-language real-world financial scam messages** collected across multiple digital communication channels. It serves as the primary positive class (`label=1`, `is_synthetic=false`) for the real-world financial fraud detection and social engineering research benchmark.

### Raw Dataset Provenance
The corpus compiles four prominent public research datasets and threat feeds:

| Collection Source | Raw Channel | Canonical Channel | Record Count | Share (%) | Description & Threat Context |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Smishing Dataset IMC25 (public user reports)** | `sms/email` | `sms` | 9,600 | 69.26% | Crowd-sourced user reports of cellular mobile smishing, bank impersonation, package delivery lures, and fake fraud alerts. |
| **Nigerian_Fraud.csv** | `email` | `email` | 3,265 | 23.56% | Long-form advance-fee fraud (419 scams), fraudulent inheritance, bank transfer proposals, and contractual fund release scams. |
| **Phishing and Legitimate Emails (Kaggle)** | `email` | `email` | 500 | 3.61% | Enterprise credential harvesting emails, banking account lock warnings, and malicious invoice notifications. |
| **smishtank.csv** | `sms` | `sms` | 496 | 3.58% | Verified smishing messages captured from active spam feeds, carrier gateways, and banking alert spoofs. |
| **Total Real-World Scams** | | | **13,861** | **100.00%** | |

---

## 2. Channel Distribution & Carrier Gateway Transport

- **SMS (Smishing):** 10,096 records (72.84%)
- **Email:** 3,765 records (27.16%)

### Email-to-SMS Gateway Disambiguation
Following the forensic audit in Task 03.1, carrier email-to-SMS gateway transport was decoupled from the raw collection label:
- **Verified Gateway Transport (`is_email_gateway = True`):** **46 records** exhibit verifiable carrier routing headers (`FRM:...`, `FROM:...`, `SUBJ:...`, `MSG:...`):
  - **24 records in IMC25:** `FIN-07897`, `FIN-07921`, `FIN-08034`, `FIN-08053`, `FIN-08101`, `FIN-08106`, `FIN-08127`, `FIN-08147`, `FIN-08173`, `FIN-08207`, `FIN-08236`, `FIN-08240`, `FIN-08253`, `FIN-08282`, `FIN-08304`, `FIN-08332`, `FIN-08447`, `FIN-08481`, `FIN-08485`, `FIN-08571`, `FIN-08575`, `FIN-08587`, `FIN-10497`, `FIN-10544`.
  - **22 records in smishtank:** `FIN-00049`, `FIN-00055`, `FIN-00057`, `FIN-00063`, `FIN-00085`, `FIN-00100`, `FIN-00109`, `FIN-00114`, `FIN-00116`, `FIN-00119`, `FIN-00138`, `FIN-00147`, `FIN-00159`, `FIN-00164`, `FIN-00165`, `FIN-00185`, `FIN-00187`, `FIN-00196`, `FIN-00213`, `FIN-00234`, `FIN-00361`, `FIN-00366`.
- **Standard Mobile SMS (`is_email_gateway = False`):** **10,050 records** (9,576 in IMC25 and 474 in smishtank) represent ordinary cellular SMS communications without email transport artifacts.

---

## 3. Duplicate Cluster Structure & Leakage Prevention

MinHash LSH deduplication (Jaccard similarity threshold $\ge 0.85$) identified significant template reuse across scam campaigns:
- **Clustered Records:** 3,206 records (23.13%) belong to **1,217 distinct multi-record clusters** (`REAL_FIN_SCAM_C0001` through `REAL_FIN_SCAM_C1217`).
- **Singletons:** 10,655 records (76.87%) are unique singleton messages.
- **Cluster Size Distribution:** Mean size is 2.63 records; maximum size is 18 records (e.g., repeated IRS tax refund smishing templates and 419 inheritance email variants).
- **Cross-Source Leakage:** **61 duplicate clusters span multiple raw sources** (e.g. identical smishing templates appearing in both IMC25 and smishtank). In the benchmark splits, these clusters are treated as atomic units to eliminate cross-split data leakage.

---

## 4. Anonymization & Placeholder Standardization

All identifiable entities, phone numbers, phishing URLs, and credentials have been normalized into canonical square-bracket tokens while preserving raw text verbatim in `original_text`:

| Token Category | Canonical Token | Upstream Raw Mappings | Semantic Justification |
| :--- | :--- | :--- | :--- |
| **Named Entities** | `[NAMED_ENTITY]` | `<NAMED_ENTITY>` | Catch-all for institutions, banks, payment apps, and persons in IMC25. |
| **Credentials** | `[CREDENTIAL]` | `[PASSWORD]`, `[password]`, `<password>` | Authentication secrets targeted in phishing. |
| **Demographics** | `[NRP]` | `<NRP>` | SpaCy NORP demographic, nationality, and political entities. |
| **URLs / Links** | `[URL]` | `[LINK REDACTED]`, `[URL]`, `<URL>` | Hyperlinks and domain destinations. |
| **Phone Numbers** | `[PHONE_NUMBER]` | `[PHONE_NUMBER]`, `<PHONE_NUMBER>` | Cellular numbers and call-back targets. |
| **Financial Values** | `[AMOUNT]` | `[AMOUNT]`, `[FINANCIAL_DATA]`, `<AMOUNT>` | Currency values, transfer sums, and fee requests. |

---

## 5. Ethical Considerations & Safety Constraints

- **Threat Mitigation:** The dataset contains malicious linguistic lures (advance-fee fraud, banking smishing, cryptocurrency investment fraud). Live malicious URLs and phone numbers are redacted.
- **Dual-Use Safeguard:** This dataset is provided exclusively for academic defense research, spam/phishing filter development, and Explainable AI (XAI) security analytics.
- **Licensing:** Individual components retain their upstream public domain or CC-BY academic research terms. Derived canonical schemas and audit metadata are licensed under Apache 2.0.
