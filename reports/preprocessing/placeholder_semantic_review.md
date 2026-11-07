# Placeholder Ontology Semantic Review & Correction Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Investigation Date:** 2026-11-07  
**Artifact Referenced:** [`reports/preprocessing/placeholder_normalization_stats.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/placeholder_normalization_stats.csv)

---

## 1. Executive Summary & Review Scope

Following Task 03, a semantic review of the placeholder normalization ontology was conducted across the four suspect mappings:
1. `<NAMED_ENTITY>` (1,778 occurrences in `real_fin_scam.csv`).
2. `[You]` (1,911 occurrences in `synthetic_financial_scams.csv`).
3. `[PASSWORD]` (117 occurrences in `real_fin_legit.csv`).
4. `<NRP>` (181 occurrences in `real_fin_scam.csv`).

This audit inspected the underlying raw text contexts, upstream curation methodology, and NLP entity definitions. All four mappings contained semantic inaccuracies that have now been corrected.

---

## 2. In-Depth Investigation of Suspect Mappings

### 2.1 `<NAMED_ENTITY>`: From `[PERSON_NAME]` to `[NAMED_ENTITY]`
- **Upstream Origin:** 100% of the 1,468 records containing `<NAMED_ENTITY>` originate from the *Smishing Dataset IMC25*.
- **Empirical Text Contexts:**
  - Bank / Financial Institutions: `"<NAMED_ENTITY>: We've placed a hold on your debit/atm card due to some unusual activity..."`
  - Commercial Payment Services: `"WELLSFARGO: Your <NAMED_ENTITY> pay of $1250 to <EMAIL_ADDRESS> is on Hold..."`
  - Merchants & Platforms: `"Your <NAMED_ENTITY> account has been locked. We recently received multiple failed login attempts..."`
  - Persons: `"Hello, I'm <NAMED_ENTITY> from OPN Architects Inc..."`
  - Action / Status Words: `"EBT-Card is currently <NAMED_ENTITY>! MessageID for <PHONE_NUMBER>!"`
- **Audit Assessment:** The upstream annotator in IMC25 utilized `<NAMED_ENTITY>` as an umbrella catch-all placeholder for organizations, products, services, and persons alike. Mapping `<NAMED_ENTITY>` to `[PERSON_NAME]` falsely converted banks, apps, and statuses into fake person names.
- **Correction:** Harmonized to canonical square-bracket token **`[NAMED_ENTITY]`**. This eliminates bracket syntax leakage (`<...>` $\rightarrow$ `[...]`) while accurately preserving entity type generality without fabricating person identities.

### 2.2 `[You]`: Preserved as Conversational Speaker Turn Marker
- **Upstream Origin:** 100% of the 1,911 occurrences originate from `synthetic_financial_scams.csv` in records where `scam_channel == 'chat'`.
- **Empirical Text Contexts:**
  - `"[Fictional Contact]: A quiet review has been placed on the account. Confirm the requested details through [LINK REDACTED]. ... [You]: Can you provide the official verification desk number before I proceed?"`
  - `"[Fictional Contact]: ... Pay the [AMOUNT REDACTED] handling charge before the next review. ... [You]: Which payment method is considered official?"`
- **Audit Assessment:** `[You]` is not an anonymized person name redacted to protect PII; it is the dialogue speaker label representing the recipient's turn in a synthetic two-party instant messaging script (`[Attacker]: ... [Recipient/You]: ...`). Replacing `[You]` with `[PERSON_NAME]` corrupted conversational dialogue transcripts into artificial person entities.
- **Correction:** **`[You]` is retained as `[You]`**. Dialogue conversational structure is preserved intact.

### 2.3 `[PASSWORD]`: From `[SYSTEM_ARTIFACT]` to `[CREDENTIAL]` (Ontology Extension)
- **Upstream Origin:** 74 records (117 occurrences) in `real_fin_legit.csv` from MeAJOR (`trec5`, `trec6`, `trec7`).
- **Empirical Text Contexts:**
  - `"User ID: [USERNAME] PW: [PASSWORD] July 18 -- [ORGANIZATION]'s Corporate Counsel Weekly"`
  - `"[ORGANIZATION] User Id and Password: [NAME], Please find below your new [ORGANIZATION] User Id and Password."`
  - `"Your temporary password is [PASSWORD]. Please login at [URL] to change it."`
- **Audit Assessment:** In financial fraud and cybercrime research, passwords, PINs, and authentication secrets are **credentials**—the primary target of credential harvesting and authentication bypass attacks. Collapsing `[PASSWORD]` into `[SYSTEM_ARTIFACT]` (alongside file paths and HTML tags) stripped critical cybersecurity semantics from the feature space.
- **Correction:** Introduced the targeted canonical ontology extension **`[CREDENTIAL]`**. Maps `[PASSWORD]`, `[password]`, and `<password>` directly to `[CREDENTIAL]`.

### 2.4 `<NRP>`: From `[ORGANIZATION]` to `[NRP]`
- **Upstream Origin:** 170 records (181 occurrences) in `real_fin_scam.csv` from the *Smishing Dataset IMC25*.
- **Empirical Text Contexts:**
  - `"...The mission of the IRS is to help <NRP> taxpayers understand and meet their tax responsibilities..."`
  - `"...The team will publish how to make a profit in the <NRP> market. Reply..."`
  - `"...NEWS: <DATE_TIME> for a <NRP> house in your area No credit needed..."`
- **Audit Assessment:** In official United States government documentation, the IRS mission statement reads: *"The mission of the IRS is to help America’s taxpayers..."* (or *American taxpayers*). In standard NLP NER libraries (such as SpaCy and Stanford CoreNLP), nationalities, religious groups, and political affiliations are classified under the **NORP** entity label. Upstream annotators truncated `NORP` to `<NRP>`. Mapping `<NRP>` to `[ORGANIZATION]` falsely converted nationalities (e.g. "American") into companies or institutions.
- **Correction:** Harmonized to canonical square-bracket token **`[NRP]`**. This eliminates bracket syntax leakage while preserving the original SpaCy nationality/demographic annotation.

### 2.5 `[PRODUCT]`: Maintained as Distinct Domain Entity
- **Total Occurrences:** 139,758 occurrences across 14,732 records in `real_fin_legit.csv` (MeAJOR).
- **Assessment:** Represents commercial and commodity products (software products, energy trading contracts, etc.). Preserved as **`[PRODUCT]`** to prevent misleadingly converting commercial products into organizations or generic system artifacts.

---

## 3. Corrected Canonical Ontology Summary

| Canonical Target Token | Category Meaning | Raw Placeholder Inputs |
| :--- | :--- | :--- |
| **`[URL]`** | URLs & Hyperlinks | `<URL>`, `[URL]`, `[LINK REDACTED]`, `<url>`, `[url]` |
| **`[PHONE_NUMBER]`** | Telephony & Voice/SMS Contact | `<PHONE>`, `<PHONE_NUMBER>`, `[PHONE_NUMBER]`, `[PHONE]`, `[FAX_NUMBER]` |
| **`[EMAIL_ADDRESS]`** | Email Communication Endpoints | `<EMAIL>`, `<EMAIL_ADDRESS>`, `[EMAIL_ADDRESS]`, `[EMAIL]` |
| **`[PERSON_NAME]`** | Individual Personal Names & Usernames | `[NAME]`, `[Name]`, `<name>`, `[USERNAME]`, `[INITIALS]`, `[Fictional Contact]` |
| **`[ORGANIZATION]`** | Corporate Entities & Fictional Desks | `[ORGANIZATION]`, `[FICTIONAL ORGANIZATION]`, `[FICTITIOUS SERVICE DESK]`, `[FICTIONAL SERVICE]` |
| **`[FINANCIAL_DATA]`** | Account Numbers & Monetary Amounts | `<US_BANK_NUMBER>`, `[FINANCIAL_INFO]`, `[AMOUNT REDACTED]`, `[ACCOUNT_NUMBER]`, `<CREDIT_CARD>` |
| **`[IDENTIFIER]`** | Government IDs & Case Reference Numbers | `<US_DRIVER_LICENSE>`, `<US_SSN>`, `<US_PASSPORT>`, `<UK_NHS>`, `<MEDICAL_LICENSE>`, `[REFERENCE_NUMBER]`, `[CASE REDACTED]` |
| **`[DATE_TIME]`** | Temporal Timestamps & Dates | `<DATE_TIME>`, `[DATE]`, `[TIME]`, `[date]` |
| **`[LOCATION]`** | Physical Addresses & Locations | `<LOCATION>`, `[ADDRESS]` |
| **`[CREDENTIAL]`** *(Extension)*| Passwords & Authentication Secrets | `[PASSWORD]`, `[password]`, `<password>` |
| **`[NAMED_ENTITY]`** *(Preserved)*| Generic / Unspecified Named Entities | `<NAMED_ENTITY>` |
| **`[NRP]`** *(Preserved)* | Nationalities / Demographics (SpaCy NORP)| `<NRP>` |
| **`[SYSTEM_ARTIFACT]`** | File Paths & Markup Metadata | `<IP_ADDRESS>`, `[IP_ADDRESS]`, `[FILE_NAME]`, `[FILE_PATH]`, `[SYMBOL]`, `[VERSION]`, `[alternative HTML version deleted]` |
| **`[PRODUCT]`** *(Preserved)* | Commercial & Commodity Products | `[PRODUCT]` |
| **`[You]`** *(Preserved)* | Dialogue Conversational Speaker Turn | `[You]` |

---

## 4. Verification & Testing

All updated mappings were implemented in [`src/preprocessing/harmonizer.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/harmonizer.py) and verified with dedicated regression unit tests in [`tests/test_preprocessing.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/tests/test_preprocessing.py) (`test_targeted_placeholder_corrections`), with 100% passing tests.
