# Email-to-SMS Gateway Classification Forensic Verification Report

**Project Title:** An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications  
**Investigation Date:** 2026-11-07  
**Artifact Referenced:** [`reports/preprocessing/channel_harmonization_stats.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/channel_harmonization_stats.csv)

---

## 1. Context & Motivation for Investigation

In Task 02, the channel audit reported:
- 9,600 IMC25 records originally labelled `sms/email`.
- 9,580 were standard mobile SMS messages.
- Only 20 were identified with carrier email-to-SMS gateway transport headers (`^FRM:`).

However, Task 03's preliminary report showed:
- `is_email_gateway = True` for all **9,600** `sms/email` records.
- 22 gateway headers in `sms/email` and 20 in `sms`.

This forensic audit investigates the discrepancy, identifies the root cause, establishes the exact record IDs with gateway evidence, and documents the corrected pipeline logic.

---

## 2. Root Cause Analysis

### 2.1 Why Task 03 Set `is_email_gateway = True` for All 9,600 Records
In Task 03, [`src/preprocessing/channel_mapper.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/channel_mapper.py) implemented:
```python
if raw_clean == "sms/email":
    canonical_channel = "sms"
    is_gateway = True  # <-- FLAW: Equated raw label with empirical gateway transport
```
The upstream curator of the *Smishing Dataset IMC25* (user reports of smishing) used the compound label `sms/email` to signify that mobile smishing reports *could* arrive either directly over cellular SMS or via carrier email-to-SMS gateways (e.g. `number@vtext.com`, `number@txt.att.net`).

However, treating the upstream label as proof that all 9,600 messages were gateway-delivered was a semantic error. 9,576 of these records have standard SMS character lengths (median 22 words / 132 chars) and exhibit **zero** email routing headers or email originating addresses. Ordinary mobile SMS messages must not be classified as email gateways.

---

## 3. The 20-versus-22-versus-24 Gateway Header Discrepancy

We audited the exact regex patterns used across Task 02 and Task 03:

### 3.1 Task 02 Baseline (20 Records)
In [`src/data/validation.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/data/validation.py) (line 475), the code tested:
`src_sub["text"].str.contains(r"^FRM:", regex=True).sum()`
Because of the strict start-of-string anchor (`^`), this counted only records where `FRM:` appeared at character position 0. This matched **exactly 20 records** in IMC25.

### 3.2 Task 03 Regex (22 Records)
In Task 03, the regex checked:
`RE_GATEWAY_HEADERS = re.compile(r"(?:^FRM:|\bFRM:\s*.*?\b(?:SUBJ:|MSG:))", re.IGNORECASE | re.DOTALL)`
This matched the 20 records starting with `^FRM:` PLUS **2 additional records** where carrier prefixes preceded `FRM:`:
- `FIN-07921`: Prepended with SMS pagination: `1 of 2\nFRM:InfoPaypal # <URL>\n*%^@$^$%\nSUBJ:Account Closed\nMSG:Urgently You need to update your details...`
- `FIN-10544`: Prepended with carrier alert tag: `(Alert)FRM: M&T BNK MSG: TEMPORAL HOLD HAS BEEN PLACED ON YOUR PROFILE...`

### 3.3 Unified Forensic Pattern (24 Verified Records in IMC25)
A comprehensive audit of carrier gateway transmission signatures reveals **2 additional records** that use the spelled-out header `FROM:` accompanied by `SUBJ:` and `MSG:`:
- `FIN-08173`: `FROM: Savings Bank ACC LOCKED\nSUBJ: Go to <LOCATION>\nMSG: ACCOUNT-ID: agioitneop !`
- `FIN-08447`: `FROM: Savings Bank ACC LOCKED\nSUBJ: Go to <URL>\nMSG: ACCOUNT-ID: <NRP> !`

---

## 4. Complete Inventory of Verified Gateway Records

### 4.1 IMC25 (`real_fin_scam.csv`, 24 Records)

| Record ID | Gateway Header Pattern | Sender / Origin Preview | Text Snippet |
| :--- | :--- | :--- | :--- |
| `FIN-03762` | `^FRM:... SUBJ:... MSG:` | `<US_DRIVER_LICENSE>` | `FRM:<US_DRIVER_LICENSE> SUBJ:-<US_DRIVER_LICENSE> MSG: -<US_DRIVER_LICENSE>.WellsFARGO. <URL>` |
| `FIN-03811` | `^FRM:... MSG:` | `Altura CU.` | `FRM:Altura CU.\nMSG:Security Alert\nVerify your account to avoid permanent lock` |
| `FIN-03848` | `^FRM:... MSG:` | `WA COVID-19 Information` | `FRM:WA COVID-19 Information MSG:You have $1087 unclaimed covid-19Support payment money : <URL>` |
| `FIN-03875` | `^FRM:... SUBJ:... MSG:` | `AMEX@Message` | `FRM:AMEX@Message\nSUBJ:<NAMED_ENTITY>\nMSG:Card Alert;Card Alert` |
| `FIN-03904` | `^FRM:... SUBJ:... MSG:` | `Navy Federal Credit` | `FRM:Navy Federal Credit <URL>BIT LOCKED\nSUBJ:Contact <US_BANK_NUMBER>\nMSG<IP_ADDRESS>` |
| `FIN-04064` | `^FRM:... SUBJ:... MSG:` | `ChaseBanking-Alert-3887` | `FRM:ChaseBanking-Alert-3887\nSUBJ:CALL: <PHONE_NUMBER> Now!\nMSG:MSG 17001 Account.Locked!` |
| `FIN-07003` | `^FRM:... MSG:` | `wellsfargo-Service Terminated!` | `FRM:[wellsfargo-Service Terminated!]" MSG:Account Suspended. Please read this: <URL>` |
| `FIN-07014` | `^FRM:... MSG:` | `Important-wellsfargo^MSG` | `FRM:***Important-wellsfargo^MSG***" MSG:Card-Locked! Read the complete message now:` |
| `FIN-07021` | `^FRM:... MSG:` | `wellsfargo-Service Terminated!` | `FRM:[wellsfargo-Service Terminated!]\nMSG:Account Suspended.\nPlease read this: <URL>` |
| `FIN-07701` | `^FRM:... MSG:` | `WellsFargo` | `FRM:WellsFargo . Call <PHONE_NUMBER> NOW MSG:4472 Urgent Account Notification` |
| `FIN-07921` | `Pagination + FRM:... SUBJ:... MSG:` | `InfoPaypal` | `1 of 2\nFRM:InfoPaypal # <URL>\n*%^@$^$%\nSUBJ:Account Closed\nMSG:Urgently You need to update your details...` |
| `FIN-08164` | `^FRM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FRM: Savings Bank ACC LOCKED\nSUBJ: Go to <URL>\nMSG: ACCOUNT-ID: agioitneop !` |
| `FIN-08173` | `FROM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FROM: Savings Bank ACC LOCKED\nSUBJ: Go to <LOCATION>\nMSG: ACCOUNT-ID: agioitneop !` |
| `FIN-08227` | `^FRM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FRM: Savings Bank ACC LOCKED\nSUBJ: Go to <LOCATION>\nMSG: ACCOUNT-ID: agiоitneop !` |
| `FIN-08295` | `^FRM:... SUBJ:... MSG:` | `M&T BANK Security` | `FRM:M&T BANK Security\nSUBJ:HIGH TICKET:qt9\nCONFIRM ACCOUNT!\nMSG:<US_DRIVER_LICENSE> <URL>` |
| `FIN-08387` | `^FRM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FRM: Savings Bank ACC LOCKED\nSUBJ: Go to <LOCATION>\nMSG: ACCOUNT-ID: <NRP> !` |
| `FIN-08447` | `FROM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FROM: Savings Bank ACC LOCKED\nSUBJ: Go to <URL>\nMSG: ACCOUNT-ID: <NRP> !` |
| `FIN-08558` | `^FRM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FRM: Savings Bank ACC LOCKED\nSUBJ: Go to <LOCATION>\nMSG: ACCOUNT-ID:agoiitneop !` |
| `FIN-08897` | `^FRM:... SUBJ:... MSG:` | `Savings Bank ACC LOCKED` | `FRM: Savings Bank ACC LOCKED\nSUBJ: Go to <LOCATION>\nMSG: ACCOUNT-ID:agioitneop !` |
| `FIN-09491` | `^FRM:... SUBJ:... MSG:` | `W Fargo Alert 7610` | `FRM:W Fargo Alert 7610 SUBJ:Please-Call <PHONE_NUMBER> id* MSG: VGQQWMWIPNMGGONFGHTIYR...` |
| `FIN-09734` | `^FRM:... SUBJ:... MSG:` | `JPMchase2284` | `FRM:JPMchase2284\nSUBJ:Please-contact <PHONE_NUMBER> ID*\nMSG:\nVOUHKYYJOFRHLEFTTNRDX...` |
| `FIN-10544` | `(Alert) + FRM:... MSG:` | `M&T BNK` | `(Alert)FRM: M&T BNK MSG: TEMPORAL HOLD HAS BEEN PLACED ON YOUR PROFILE Credible...` |
| `FIN-11149` | `^FRM:... SUBJ:... MSG:` | `BoAmerica-Alert2385` | `FRM:BoAmerica-Alert2385 SUBJ:Please-call <PHONE_NUMBER> UID* MSG: QFBEPUZHQRVTPXXERMORTZPUJWEJWOENZRN` |
| `FIN-13043` | `^FRM:... SUBJ:... MSG:` | `AT&T` | `FRM:AT&T\nSUBJ:Payment on hold. Call <PHONE_NUMBER> .\nMSG:2914` |

### 4.2 smishtank.csv (`real_fin_scam.csv`, 22 Records)
`FIN-03277`, `FIN-03288`, `FIN-03305`, `FIN-03323`, `FIN-03330`, `FIN-03350`, `FIN-03371`, `FIN-03372`, `FIN-03412`, `FIN-03413`, `FIN-03421`, `FIN-03423`, `FIN-03426`, `FIN-03427`, `FIN-03431`, `FIN-03514`, `FIN-03516`, `FIN-03604`, `FIN-03661`, `FIN-03712`, `FIN-03741`, `FIN-03742`.

---

## 5. Corrected Semantics & Pipeline Verification

The pipeline has been updated in [`src/preprocessing/channel_mapper.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/channel_mapper.py) to implement the required semantics:

- **`channel`**: Canonical medium. For all 9,600 IMC25 records, `channel = "sms"`.
- **`original_channel`**: Preserved raw source string: `"sms/email"`.
- **`has_gateway_headers`**: `True` if and only if message text contains verified carrier gateway headers.
- **`is_email_gateway`**: `True` if and only if gateway transport is supported by empirical source evidence (`has_gateway_headers == True`). Ordinary mobile SMS records receive `is_email_gateway = False`.

### Updated Distribution in `real_fin_scam_processed.csv`:
- `channel == 'sms'` & `original_channel == 'sms/email'`: **9,600 records**
  - `is_email_gateway == True` & `has_gateway_headers == True`: **24 records** (0.25%)
  - `is_email_gateway == False` & `has_gateway_headers == False`: **9,576 records** (99.75%)
- `channel == 'sms'` & `original_channel == 'sms'` (smishtank): **496 records**
  - `is_email_gateway == True` & `has_gateway_headers == True`: **22 records** (4.44%)
  - `is_email_gateway == False` & `has_gateway_headers == False`: **474 records** (95.56%)
- `channel == 'email'`: **3,765 records** (`is_email_gateway == False`)

### Documented Limitation:
For the remaining 9,576 records in IMC25, users reported receiving these messages as SMS on cellular phones. Because upstream collectors did not archive carrier routing metadata, we preserve empirical truth: without transport headers, gateway delivery cannot be proven, and these messages are correctly classified as ordinary mobile SMS.

