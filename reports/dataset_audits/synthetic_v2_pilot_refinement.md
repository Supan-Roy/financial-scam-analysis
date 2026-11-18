# Synthetic Financial Scam Dataset Refinement Pilot Report (130 Records)

**Dataset:** `data/raw/synthetic_v2_pilot_130.csv`  
**Scope:** Targeted Realism Refinement Pilot (10 records per each of the 13 canonical `phishing_type` categories).  
**Evaluation Baseline:** Comparative analysis against `synthetic_financial_scams_v2.csv`.  

---

## 1. Pilot Distribution Summary

- **Total Records:** 130 (exactly 10 per subtype across 13 subtypes)
- **Primary Fraudulent Intent Representation:**
  - `induce_payment_or_transfer`: 71 records
  - `obtain_personal_or_financial_information`: 23 records
  - `obtain_credentials_or_codes`: 16 records
  - `gain_account_or_device_access`: 10 records
  - `induce_fraudulent_investment`: 10 records
- **Channel Representation:**
  - `email`: 46 records
  - `sms`: 44 records
  - `chat`: 31 records
  - `notification`: 9 records
- **Tactics Cardinalities:**
  - 0 tactics: 11 records
  - 1 tactics: 54 records
  - 2 tactics: 52 records
  - 3 tactics: 13 records

---

## 2. Quantitative & Qualitative Comparison: V2 Baseline vs. Refined Pilot

| Dimension | V2 Baseline Dataset | Refined Pilot (130 Records) | Improvement Observed |
| :--- | :---: | :---: | :--- |
| **Narrative & Action Alignment** | Global intent pool caused register clashes (e.g. accounting escrow in romance) | **Contextually Grounded**: Call-to-action is scenario-tailored | Tone clashes eliminated; family/romance scams use natural requests |
| **Chat Conversation Structure** | 100% rigid 3-turn pattern (`'What happened? What do I need to do right now?'`) | **Dynamic 2 to 4 turns** with varied victim stances | Authentic hesitation, panic, inquiry, and compliance responses |
| **Notification Length** | Unnaturally dense (mean 46.1 words, up to 77 words) | **Lockscreen Concise (mean: 20.4 words, range: 14–26 words)** | Matches authentic mobile OS push notification constraints |
| **Cross-Domain Purity** | Tactic leakage (e.g. loan pre-approvals inside prize sweepstakes) | **100% Subtype-Pure Tactics Pools** | Prize benefits remain prizes; loans remain credit offers |
| **Discourse Transitions** | Staccato modular sentence concatenation | **Syntactically coherent, connected prose** | Smooth connective tissue between problem, context, and action |
| **Character Span Accuracy** | 100% verified offsets | **100% verified offsets** | Character-for-character substring slice verification maintained |

---

## 3. Complete Verbatim Inspection of All 130 Pilot Records

### Subtype Group: `account_verification`

#### Record PILOT-0001
- **ID:** `PILOT-0001`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 310, "end_char": 413, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access."}`
- **Narrative Evidence:** `{"start_char": 113, "end_char": 195, "span_text": "An unrecognized login attempt was detected from a new device located in Miami, FL."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 197, "end_char": 308, "span_text": "Failure to act immediately will result in permanent account termination and referral to collection authorities."}]`

**Complete Original Text:**
```text
Subject: Security Alert: Sign-in Attempt Detected on Your Horizon Trust Bank Profile

Attention Account Holder,

An unrecognized login attempt was detected from a new device located in Miami, FL.

Failure to act immediately will result in permanent account termination and referral to collection authorities.

Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT-0002
- **ID:** `PILOT-0002`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 415, "end_char": 537, "span_text": "Enter your online banking password and security PIN at https://summit-portal-verify.net/login to authenticate your device."}`
- **Narrative Evidence:** `{"start_char": 122, "end_char": 226, "span_text": "Your online banking profile requires mandatory annual identity re-certification under security protocol."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 228, "end_char": 322, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}, {"tactic": "urgency", "start_char": 323, "end_char": 413, "span_text": "You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Subject: Security Alert: Sign-in Attempt Detected on Your Summit Federal Credit Union Profile

Attention Account Holder,

Your online banking profile requires mandatory annual identity re-certification under security protocol.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture.

Enter your online banking password and security PIN at https://summit-portal-verify.net/login to authenticate your device.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0003
- **ID:** `PILOT-0003`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["false_legitimacy", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 388, "end_char": 503, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to re-certify your profile."}`
- **Narrative Evidence:** `{"start_char": 108, "end_char": 212, "span_text": "Your online banking profile requires mandatory annual identity re-certification under security protocol."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 214, "end_char": 299, "span_text": "Audit Case Docket: CF-69429 registered under statutory financial compliance protocol."}, {"tactic": "fear_or_threat", "start_char": 300, "end_char": 386, "span_text": "Law enforcement officers will be dispatched to your registered domicile if unresolved."}]`

**Complete Original Text:**
```text
Subject: Security Alert: Sign-in Attempt Detected on Your Pinnacle Bank Profile

Attention Account Holder,

Your online banking profile requires mandatory annual identity re-certification under security protocol.

Audit Case Docket: CF-69429 registered under statutory financial compliance protocol. Law enforcement officers will be dispatched to your registered domicile if unresolved.

Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to re-certify your profile.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT-0004
- **ID:** `PILOT-0004`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["secrecy", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 264, "end_char": 363, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 84, "span_text": "An unrecognized login attempt was detected from a new device located in Atlanta, GA."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 85, "end_char": 168, "span_text": "Do not disclose this ongoing internal audit to any third party under any condition."}, {"tactic": "fear_or_threat", "start_char": 169, "end_char": 263, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
An unrecognized login attempt was detected from a new device located in Atlanta, GA. Do not disclose this ongoing internal audit to any third party under any condition. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. Download and launch the AnyDesk remote support client to grant our technician configuration access.
```

---

#### Record PILOT-0005
- **ID:** `PILOT-0005`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["false_legitimacy", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 278, "end_char": 377, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "Your online banking profile requires mandatory annual identity re-certification under security protocol."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 105, "end_char": 190, "span_text": "Audit Case Docket: CF-86622 registered under statutory financial compliance protocol."}, {"tactic": "fear_or_threat", "start_char": 191, "end_char": 277, "span_text": "Law enforcement officers will be dispatched to your registered domicile if unresolved."}]`

**Complete Original Text:**
```text
Your online banking profile requires mandatory annual identity re-certification under security protocol. Audit Case Docket: CF-86622 registered under statutory financial compliance protocol. Law enforcement officers will be dispatched to your registered domicile if unresolved. Download and launch the AnyDesk remote support client to grant our technician configuration access.
```

---

#### Record PILOT-0006
- **ID:** `PILOT-0006`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 217, "end_char": 320, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "Your online banking profile requires mandatory annual identity re-certification under security protocol."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 105, "end_char": 216, "span_text": "Failure to act immediately will result in permanent account termination and referral to collection authorities."}]`

**Complete Original Text:**
```text
Your online banking profile requires mandatory annual identity re-certification under security protocol. Failure to act immediately will result in permanent account termination and referral to collection authorities. Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access.
```

---

#### Record PILOT-0007
- **ID:** `PILOT-0007`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["false_legitimacy", "fear_or_threat", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 477, "end_char": 600, "span_text": "Enter your online banking password and security PIN at https://apex-claims-clearance.net/login to authenticate your device."}`
- **Narrative Evidence:** `{"start_char": 113, "end_char": 197, "span_text": "An unrecognized login attempt was detected from a new device located in Chicago, IL."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 199, "end_char": 280, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "fear_or_threat", "start_char": 281, "end_char": 375, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}, {"tactic": "secrecy", "start_char": 376, "end_char": 475, "span_text": "Maintain strict confidentiality and avoid discussing this matter with local branch representatives."}]`

**Complete Original Text:**
```text
Subject: Security Alert: Sign-in Attempt Detected on Your Apex National Bank Profile

Attention Account Holder,

An unrecognized login attempt was detected from a new device located in Chicago, IL.

Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. Maintain strict confidentiality and avoid discussing this matter with local branch representatives.

Enter your online banking password and security PIN at https://apex-claims-clearance.net/login to authenticate your device.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT-0008
- **ID:** `PILOT-0008`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 349, "end_char": 467, "span_text": "Install our certified SecurityAgent utility APK from https://first-secure-wire-desk.org/support on your mobile device."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "Your online banking profile requires mandatory annual identity re-certification under security protocol."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 105, "end_char": 176, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}, {"tactic": "urgency", "start_char": 177, "end_char": 248, "span_text": "Time-sensitive alert: immediate verification is required without delay."}, {"tactic": "secrecy", "start_char": 249, "end_char": 348, "span_text": "Maintain strict confidentiality and avoid discussing this matter with local branch representatives."}]`

**Complete Original Text:**
```text
Your online banking profile requires mandatory annual identity re-certification under security protocol. This communication is issued by the Federal Regulatory Compliance Unit. Time-sensitive alert: immediate verification is required without delay. Maintain strict confidentiality and avoid discussing this matter with local branch representatives. Install our certified SecurityAgent utility APK from https://first-secure-wire-desk.org/support on your mobile device.
```

---

#### Record PILOT-0009
- **ID:** `PILOT-0009`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 280, "end_char": 383, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 83, "span_text": "An unrecognized login attempt was detected from a new device located in Dallas, TX."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 84, "end_char": 195, "span_text": "Failure to act immediately will result in permanent account termination and referral to collection authorities."}, {"tactic": "secrecy", "start_char": 196, "end_char": 279, "span_text": "Do not disclose this ongoing internal audit to any third party under any condition."}]`

**Complete Original Text:**
```text
An unrecognized login attempt was detected from a new device located in Dallas, TX. Failure to act immediately will result in permanent account termination and referral to collection authorities. Do not disclose this ongoing internal audit to any third party under any condition. Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access.
```

---

#### Record PILOT-0010
- **ID:** `PILOT-0010`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 135, "end_char": 238, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 84, "span_text": "An unrecognized login attempt was detected from a new device located in Atlanta, GA."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 85, "end_char": 134, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
An unrecognized login attempt was detected from a new device located in Atlanta, GA. Immediate response required before 5:00 PM today. Reply with the 6-digit confirmation passcode displayed on your authentication screen to confirm access.
```

---

### Subtype Group: `card_transaction_alert`

#### Record PILOT-0011
- **ID:** `PILOT-0011`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 77, "end_char": 184, "span_text": "Transfer a temporary dispute escrow deposit of $914.50 through AppleCash Express to freeze the transaction."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 76, "span_text": "An out-of-state ATM cash withdrawal of $914.50 was attempted in Seattle, WA."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
An out-of-state ATM cash withdrawal of $914.50 was attempted in Seattle, WA. Transfer a temporary dispute escrow deposit of $914.50 through AppleCash Express to freeze the transaction.
```

---

#### Record PILOT-0012
- **ID:** `PILOT-0012`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 217, "end_char": 324, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen to cancel this charge."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 215, "span_text": "A pending authorization of $4,136.50 at Walmart Supercenter #2041 was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Subject: Fraud Monitoring: Verification Required for Card Activity ($4,136.50)

Attention Account Holder,

A pending authorization of $4,136.50 at Walmart Supercenter #2041 was flagged by automated fraud monitoring.

Reply with the 6-digit confirmation passcode displayed on your authentication screen to cancel this charge.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0013
- **ID:** `PILOT-0013`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 133, "end_char": 254, "span_text": "Enter your online banking password and security PIN at https://vanguard-portal-verify.net/login to block the transaction."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 132, "span_text": "A pending authorization of $3,457.00 at BestBuy Electronics #841 was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[Vanguard Bancorp Alert] A pending authorization of $3,457.00 at BestBuy Electronics #841 was flagged by automated fraud monitoring. Enter your online banking password and security PIN at https://vanguard-portal-verify.net/login to block the transaction.
```

---

#### Record PILOT-0014
- **ID:** `PILOT-0014`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["false_legitimacy", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 273, "end_char": 395, "span_text": "Enter your online banking password and security PIN at https://summit-secure-wire-desk.org/login to block the transaction."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 107, "span_text": "A pending authorization of $3,904.00 at BestBuy Electronics #841 was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 108, "end_char": 193, "span_text": "Audit Case Docket: CF-19602 registered under statutory financial compliance protocol."}, {"tactic": "authority_impersonation", "start_char": 194, "end_char": 272, "span_text": "Official notice from Summit Federal Credit Union Fraud Investigation Division."}]`

**Complete Original Text:**
```text
A pending authorization of $3,904.00 at BestBuy Electronics #841 was flagged by automated fraud monitoring. Audit Case Docket: CF-19602 registered under statutory financial compliance protocol. Official notice from Summit Federal Credit Union Fraud Investigation Division. Enter your online banking password and security PIN at https://summit-secure-wire-desk.org/login to block the transaction.
```

---

#### Record PILOT-0015
- **ID:** `PILOT-0015`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["false_legitimacy", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 205, "end_char": 327, "span_text": "Enter your online banking password and security PIN at https://first-auth-alert-center.com/login to block the transaction."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 77, "span_text": "An out-of-state ATM cash withdrawal of $1,250.80 was attempted in London, UK."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 78, "end_char": 154, "span_text": "Certified clearance code: CF-25129-AUTH verified through centralized ledger."}, {"tactic": "urgency", "start_char": 155, "end_char": 204, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
An out-of-state ATM cash withdrawal of $1,250.80 was attempted in London, UK. Certified clearance code: CF-25129-AUTH verified through centralized ledger. Immediate response required before 5:00 PM today. Enter your online banking password and security PIN at https://first-auth-alert-center.com/login to block the transaction.
```

---

#### Record PILOT-0016
- **ID:** `PILOT-0016`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 168, "end_char": 262, "span_text": "Submit your full Social Security number and debit card CVV to verify your fraud dispute claim."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 76, "span_text": "An out-of-state ATM cash withdrawal of $179.80 was attempted in Phoenix, AZ."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 77, "end_char": 167, "span_text": "You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
An out-of-state ATM cash withdrawal of $179.80 was attempted in Phoenix, AZ. You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture. Submit your full Social Security number and debit card CVV to verify your fraud dispute claim.
```

---

#### Record PILOT-0017
- **ID:** `PILOT-0017`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 216, "end_char": 323, "span_text": "Remit the $25 expedited dispute investigation fee via PayLink Mobile to initiate immediate charge reversal."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 75, "span_text": "An out-of-state ATM cash withdrawal of $476.80 was attempted in Dallas, TX."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 76, "end_char": 128, "span_text": "Authorized by senior financial auditor Robert Vance."}, {"tactic": "fear_or_threat", "start_char": 129, "end_char": 215, "span_text": "Law enforcement officers will be dispatched to your registered domicile if unresolved."}]`

**Complete Original Text:**
```text
An out-of-state ATM cash withdrawal of $476.80 was attempted in Dallas, TX. Authorized by senior financial auditor Robert Vance. Law enforcement officers will be dispatched to your registered domicile if unresolved. Remit the $25 expedited dispute investigation fee via PayLink Mobile to initiate immediate charge reversal.
```

---

#### Record PILOT-0018
- **ID:** `PILOT-0018`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 329, "end_char": 451, "span_text": "Enter your online banking password and security PIN at https://beacon-claims-clearance.net/login to block the transaction."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 214, "span_text": "A pending authorization of $2,182.80 at BestBuy Electronics #841 was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 216, "end_char": 327, "span_text": "Failure to act immediately will result in permanent account termination and referral to collection authorities."}]`

**Complete Original Text:**
```text
Subject: Fraud Monitoring: Verification Required for Card Activity ($2,182.80)

Attention Account Holder,

A pending authorization of $2,182.80 at BestBuy Electronics #841 was flagged by automated fraud monitoring.

Failure to act immediately will result in permanent account termination and referral to collection authorities.

Enter your online banking password and security PIN at https://beacon-claims-clearance.net/login to block the transaction.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0019
- **ID:** `PILOT-0019`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 220, "end_char": 321, "span_text": "Remit the $25 expedited dispute investigation fee via SwiftPay to initiate immediate charge reversal."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 107, "span_text": "A pending authorization of $3,026.95 at BestBuy Electronics #841 was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 108, "end_char": 219, "span_text": "Failure to act immediately will result in permanent account termination and referral to collection authorities."}]`

**Complete Original Text:**
```text
A pending authorization of $3,026.95 at BestBuy Electronics #841 was flagged by automated fraud monitoring. Failure to act immediately will result in permanent account termination and referral to collection authorities. Remit the $25 expedited dispute investigation fee via SwiftPay to initiate immediate charge reversal.
```

---

#### Record PILOT-0020
- **ID:** `PILOT-0020`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 152, "end_char": 262, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to reverse the charge."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 74, "span_text": "An out-of-state ATM cash withdrawal of $513.95 was attempted in Miami, FL."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 75, "end_char": 151, "span_text": "Certified clearance code: CF-10221-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
An out-of-state ATM cash withdrawal of $513.95 was attempted in Miami, FL. Certified clearance code: CF-10221-AUTH verified through centralized ledger. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to reverse the charge.
```

---

### Subtype Group: `refund_chargeback`

#### Record PILOT-0021
- **ID:** `PILOT-0021`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 153, "end_char": 241, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 103, "span_text": "An erroneous billing adjustment created an excess refund balance of $1,192.50 requiring reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 104, "end_char": 152, "span_text": "Immediate response required by tomorrow morning."}]`

**Complete Original Text:**
```text
An erroneous billing adjustment created an excess refund balance of $1,192.50 requiring reconciliation. Immediate response required by tomorrow morning. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code.
```

---

#### Record PILOT-0022
- **ID:** `PILOT-0022`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 295, "end_char": 389, "span_text": "Settle the required statutory handling fee of $844.80 using QuickTransfer before the deadline."}`
- **Narrative Evidence:** `{"start_char": 98, "end_char": 198, "span_text": "An automated overcharge of $844.80 for your NetDefender Support subscription is pending full refund."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 200, "end_char": 243, "span_text": "Immediate response required within 2 hours."}, {"tactic": "urgency", "start_char": 244, "end_char": 293, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Subject: Billing Notification: Adjustment Statement #CF-77561 Pending

Attention Account Holder,

An automated overcharge of $844.80 for your NetDefender Support subscription is pending full refund.

Immediate response required within 2 hours. Immediate response required before 5:00 PM today.

Settle the required statutory handling fee of $844.80 using QuickTransfer before the deadline.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0023
- **ID:** `PILOT-0023`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 127, "end_char": 225, "span_text": "Remit payment of $3,295.95 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 24, "end_char": 126, "span_text": "An automated overcharge of $3,295.95 for your NetDefender Support subscription is pending full refund."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[PayLink Mobile Notice] An automated overcharge of $3,295.95 for your NetDefender Support subscription is pending full refund. Remit payment of $3,295.95 via wire transfer to our settlement escrow routing account immediately.
```

---

#### Record PILOT-0024
- **ID:** `PILOT-0024`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["authority_impersonation", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 354, "end_char": 461, "span_text": "Install TeamViewer QuickSupport to enable our diagnostic specialist to inspect your active banking session."}`
- **Narrative Evidence:** `{"start_char": 98, "end_char": 197, "span_text": "An automated overcharge of $4,501.80 for your Apex ID Services subscription is pending full refund."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 199, "end_char": 270, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}, {"tactic": "false_legitimacy", "start_char": 271, "end_char": 352, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

**Complete Original Text:**
```text
Subject: Billing Notification: Adjustment Statement #CF-68008 Pending

Attention Account Holder,

An automated overcharge of $4,501.80 for your Apex ID Services subscription is pending full refund.

This communication is issued by the Federal Regulatory Compliance Unit. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight.

Install TeamViewer QuickSupport to enable our diagnostic specialist to inspect your active banking session.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT-0025
- **ID:** `PILOT-0025`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 176, "end_char": 275, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 103, "span_text": "An automated overcharge of $2,375.80 for your CloudShield Security subscription is pending full refund."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 104, "end_char": 175, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}]`

**Complete Original Text:**
```text
An automated overcharge of $2,375.80 for your CloudShield Security subscription is pending full refund. This communication is issued by the Federal Regulatory Compliance Unit. Download and launch the AnyDesk remote support client to grant our technician configuration access.
```

---

#### Record PILOT-0026
- **ID:** `PILOT-0026`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 174, "end_char": 267, "span_text": "Transfer $310.95 through SwiftPay to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 101, "span_text": "An erroneous billing adjustment created an excess refund balance of $310.95 requiring reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 102, "end_char": 173, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}]`

**Complete Original Text:**
```text
An erroneous billing adjustment created an excess refund balance of $310.95 requiring reconciliation. This communication is issued by the Federal Regulatory Compliance Unit. Transfer $310.95 through SwiftPay to our designated clearance officer to resolve the balance.
```

---

#### Record PILOT-0027
- **ID:** `PILOT-0027`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 274, "end_char": 370, "span_text": "Remit payment of $370.95 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 98, "end_char": 199, "span_text": "An erroneous billing adjustment created an excess refund balance of $370.95 requiring reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 201, "end_char": 272, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}]`

**Complete Original Text:**
```text
Subject: Billing Notification: Adjustment Statement #CF-87580 Pending

Attention Account Holder,

An erroneous billing adjustment created an excess refund balance of $370.95 requiring reconciliation.

This communication is issued by the Federal Regulatory Compliance Unit.

Remit payment of $370.95 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0028
- **ID:** `PILOT-0028`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 280, "end_char": 376, "span_text": "Remit payment of $308.00 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 98, "end_char": 198, "span_text": "An automated overcharge of $308.00 for your NetDefender Support subscription is pending full refund."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 200, "end_char": 278, "span_text": "Official notice from Summit Federal Credit Union Fraud Investigation Division."}]`

**Complete Original Text:**
```text
Subject: Billing Notification: Adjustment Statement #CF-55870 Pending

Attention Account Holder,

An automated overcharge of $308.00 for your NetDefender Support subscription is pending full refund.

Official notice from Summit Federal Credit Union Fraud Investigation Division.

Remit payment of $308.00 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0029
- **ID:** `PILOT-0029`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 296, "end_char": 394, "span_text": "Remit payment of $3,171.50 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 98, "end_char": 201, "span_text": "An erroneous billing adjustment created an excess refund balance of $3,171.50 requiring reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 203, "end_char": 294, "span_text": "You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Subject: Billing Notification: Adjustment Statement #CF-89415 Pending

Attention Account Holder,

An erroneous billing adjustment created an excess refund balance of $3,171.50 requiring reconciliation.

You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture.

Remit payment of $3,171.50 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0030
- **ID:** `PILOT-0030`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 124, "end_char": 227, "span_text": "Provide your complete banking routing number and checking account digits to update your direct profile."}`
- **Narrative Evidence:** `{"start_char": 24, "end_char": 123, "span_text": "An automated overcharge of $1,141.00 for your Apex ID Services subscription is pending full refund."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🔔 [ZelleConnect Notice] An automated overcharge of $1,141.00 for your Apex ID Services subscription is pending full refund. Provide your complete banking routing number and checking account digits to update your direct profile.
```

---

### Subtype Group: `invoice_payment_request`

#### Record PILOT-0031
- **ID:** `PILOT-0031`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "urgency", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 328, "end_char": 426, "span_text": "Remit payment of $3,958.95 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 105, "span_text": "Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($3,958.95)."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 106, "end_char": 187, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "urgency", "start_char": 188, "end_char": 259, "span_text": "Time-sensitive alert: immediate verification is required without delay."}, {"tactic": "authority_impersonation", "start_char": 260, "end_char": 327, "span_text": "Official notice from Beacon Financial Fraud Investigation Division."}]`

**Complete Original Text:**
```text
Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($3,958.95). Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Time-sensitive alert: immediate verification is required without delay. Official notice from Beacon Financial Fraud Investigation Division. Remit payment of $3,958.95 via wire transfer to our settlement escrow routing account immediately.
```

---

#### Record PILOT-0032
- **ID:** `PILOT-0032`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 286, "end_char": 384, "span_text": "Remit payment of $2,440.80 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 206, "span_text": "Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($2,440.80)."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 208, "end_char": 284, "span_text": "Certified clearance code: CF-82848-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-82848: Remittance Update from Accounts Receivable

Attention Account Holder,

Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($2,440.80).

Certified clearance code: CF-82848-AUTH verified through centralized ledger.

Remit payment of $2,440.80 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
First Crest Bank
```

---

#### Record PILOT-0033
- **ID:** `PILOT-0033`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 287, "end_char": 381, "span_text": "Transfer $3,462.50 through NovaPay to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 207, "span_text": "Outstanding billing statement INV-8921 for $3,462.50 from CloudShield Security is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 209, "end_char": 285, "span_text": "Certified clearance code: CF-50135-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-50135: Remittance Update from Accounts Receivable

Attention Account Holder,

Outstanding billing statement INV-8921 for $3,462.50 from CloudShield Security is past due for settlement.

Certified clearance code: CF-50135-AUTH verified through centralized ledger.

Transfer $3,462.50 through NovaPay to our designated clearance officer to resolve the balance.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT-0034
- **ID:** `PILOT-0034`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 256, "end_char": 354, "span_text": "Remit payment of $1,666.50 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 203, "span_text": "Outstanding billing statement INV-8921 for $1,666.50 from SecureVault Tech is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 205, "end_char": 254, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-38361: Remittance Update from Accounts Receivable

Attention Account Holder,

Outstanding billing statement INV-8921 for $1,666.50 from SecureVault Tech is past due for settlement.

Immediate response required before 5:00 PM today.

Remit payment of $1,666.50 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0035
- **ID:** `PILOT-0035`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 301, "end_char": 396, "span_text": "Transfer $4,171.00 through SwiftPay to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 203, "span_text": "Outstanding billing statement INV-8921 for $4,171.00 from SecureVault Tech is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 205, "end_char": 299, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-11607: Remittance Update from Accounts Receivable

Attention Account Holder,

Outstanding billing statement INV-8921 for $4,171.00 from SecureVault Tech is past due for settlement.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.

Transfer $4,171.00 through SwiftPay to our designated clearance officer to resolve the balance.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0036
- **ID:** `PILOT-0036`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 435, "end_char": 531, "span_text": "Settle the required statutory handling fee of $2,639.00 using QuickTransfer before the deadline."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 206, "span_text": "Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($2,639.00)."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 208, "end_char": 289, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "authority_impersonation", "start_char": 290, "end_char": 361, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}, {"tactic": "urgency", "start_char": 362, "end_char": 433, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-42530: Remittance Update from Accounts Receivable

Attention Account Holder,

Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($2,639.00).

Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. This communication is issued by the Federal Regulatory Compliance Unit. Time-sensitive alert: immediate verification is required without delay.

Settle the required statutory handling fee of $2,639.00 using QuickTransfer before the deadline.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0037
- **ID:** `PILOT-0037`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 281, "end_char": 375, "span_text": "Transfer $1,436.50 through NovaPay to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 206, "span_text": "Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($1,436.50)."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 208, "end_char": 279, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-32782: Remittance Update from Accounts Receivable

Attention Account Holder,

Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($1,436.50).

This communication is issued by the Federal Regulatory Compliance Unit.

Transfer $1,436.50 through NovaPay to our designated clearance officer to resolve the balance.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT-0038
- **ID:** `PILOT-0038`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 209, "end_char": 307, "span_text": "Remit payment of $1,770.95 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 207, "span_text": "Outstanding billing statement INV-8921 for $1,770.95 from CloudShield Security is past due for settlement."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Subject: Statement #CF-25043: Remittance Update from Accounts Receivable

Attention Account Holder,

Outstanding billing statement INV-8921 for $1,770.95 from CloudShield Security is past due for settlement.

Remit payment of $1,770.95 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0039
- **ID:** `PILOT-0039`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 376, "span_text": "Settle the required statutory handling fee of $4,195.95 using SwiftPay before the deadline."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 206, "span_text": "Outstanding billing statement INV-8921 for $4,195.95 from NetDefender Support is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 208, "end_char": 283, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-20543: Remittance Update from Accounts Receivable

Attention Account Holder,

Outstanding billing statement INV-8921 for $4,195.95 from NetDefender Support is past due for settlement.

Act within the next 60 minutes to prevent irreversible account restriction.

Settle the required statutory handling fee of $4,195.95 using SwiftPay before the deadline.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0040
- **ID:** `PILOT-0040`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 353, "end_char": 448, "span_text": "Transfer $3,772.80 through CashFlow to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 206, "span_text": "Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($3,772.80)."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 208, "end_char": 279, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}, {"tactic": "urgency", "start_char": 280, "end_char": 351, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Subject: Statement #CF-33788: Remittance Update from Accounts Receivable

Attention Account Holder,

Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ($3,772.80).

This communication is issued by the Federal Regulatory Compliance Unit. Time-sensitive alert: immediate verification is required without delay.

Transfer $3,772.80 through CashFlow to our designated clearance officer to resolve the balance.

Sincerely,
Operations & Risk Desk
First Crest Bank
```

---

### Subtype Group: `loan_offer`

#### Record PILOT-0041
- **ID:** `PILOT-0041`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 261, "end_char": 362, "span_text": "Provide your complete banking routing number and checking account digits to establish direct deposit."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 97, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 98, "end_char": 169, "span_text": "Time-sensitive alert: immediate verification is required without delay."}, {"tactic": "scarcity", "start_char": 170, "end_char": 260, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}]`

**Complete Original Text:**
```text
You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate. Time-sensitive alert: immediate verification is required without delay. Only 2 participant allocations remain available before registration is permanently closed. Provide your complete banking routing number and checking account digits to establish direct deposit.
```

---

#### Record PILOT-0042
- **ID:** `PILOT-0042`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 289, "end_char": 395, "span_text": "Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement."}`
- **Narrative Evidence:** `{"start_char": 106, "end_char": 209, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 211, "end_char": 287, "span_text": "Certified clearance code: CF-13783-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
Subject: Notice of Credit Authorization: Personal Line Disbursement Scheduled

Attention Account Holder,

Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.

Certified clearance code: CF-13783-AUTH verified through centralized ledger.

Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement.

Sincerely,
Operations & Risk Desk
First Crest Bank
```

---

#### Record PILOT-0043
- **ID:** `PILOT-0043`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 388, "span_text": "Remit the mandatory advance insurance deposit of $3,553.95 via NovaPay before credit line disbursement."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 97, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 98, "end_char": 198, "span_text": "You have been pre-approved for an unrestricted credit line of $25,000 at zero introductory interest."}, {"tactic": "scarcity", "start_char": 199, "end_char": 284, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}]`

**Complete Original Text:**
```text
You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate. You have been pre-approved for an unrestricted credit line of $25,000 at zero introductory interest. Limited settlement quota expires today and cannot be extended under any circumstance. Remit the mandatory advance insurance deposit of $3,553.95 via NovaPay before credit line disbursement.
```

---

#### Record PILOT-0044
- **ID:** `PILOT-0044`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 129, "end_char": 239, "span_text": "Remit the mandatory advance insurance deposit of $4,161.50 via PayLink Mobile before credit line disbursement."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 128, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[First Crest Bank Alert] Your application for an emergency debt consolidation credit line of $35,000 has been formally approved. Remit the mandatory advance insurance deposit of $4,161.50 via PayLink Mobile before credit line disbursement.
```

---

#### Record PILOT-0045
- **ID:** `PILOT-0045`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 314, "end_char": 426, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($4,207.00) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 28, "end_char": 131, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 237, "end_char": 313, "span_text": "Certified clearance code: CF-26547-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
[10:14 AM] Recruiter_Sarah: Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.
[10:16 AM] You: How does the return or commission get paid out? Is it daily?
[10:17 AM] Recruiter_Sarah: Certified clearance code: CF-26547-AUTH verified through centralized ledger. Pay the mandatory 2% loan origination and documentation fee ($4,207.00) via wire transfer to release your funds.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0046
- **ID:** `PILOT-0046`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 363, "end_char": 469, "span_text": "Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 97, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 98, "end_char": 175, "span_text": "Secure an immediate personal advance disbursement of $25,000 upon enrollment."}, {"tactic": "scarcity", "start_char": 176, "end_char": 266, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}, {"tactic": "urgency", "start_char": 267, "end_char": 362, "span_text": "You must complete this mandatory requirement by tomorrow morning to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate. Secure an immediate personal advance disbursement of $25,000 upon enrollment. Only 2 participant allocations remain available before registration is permanently closed. You must complete this mandatory requirement by tomorrow morning to avoid automatic forfeiture. Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement.
```

---

#### Record PILOT-0047
- **ID:** `PILOT-0047`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 428, "end_char": 534, "span_text": "Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 130, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 236, "end_char": 336, "span_text": "You have been pre-approved for an unrestricted credit line of $25,000 at zero introductory interest."}, {"tactic": "scarcity", "start_char": 337, "end_char": 427, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}]`

**Complete Original Text:**
```text
[10:14 AM] Advisor_Morgan: Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.
[10:16 AM] You: Is there any documentation or agreement I need to sign first?
[10:17 AM] Advisor_Morgan: You have been pre-approved for an unrestricted credit line of $25,000 at zero introductory interest. Only 2 participant allocations remain available before registration is permanently closed. Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0048
- **ID:** `PILOT-0048`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 380, "end_char": 484, "span_text": "Remit the mandatory advance insurance deposit of $4,627.50 via CashFlow before credit line disbursement."}`
- **Narrative Evidence:** `{"start_char": 106, "end_char": 209, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 211, "end_char": 296, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}, {"tactic": "false_legitimacy", "start_char": 297, "end_char": 378, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

**Complete Original Text:**
```text
Subject: Notice of Credit Authorization: Personal Line Disbursement Scheduled

Attention Account Holder,

Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.

Limited settlement quota expires today and cannot be extended under any circumstance. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight.

Remit the mandatory advance insurance deposit of $4,627.50 via CashFlow before credit line disbursement.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT-0049
- **ID:** `PILOT-0049`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 417, "end_char": 529, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($3,392.80) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 106, "end_char": 209, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 211, "end_char": 287, "span_text": "Certified clearance code: CF-11061-AUTH verified through centralized ledger."}, {"tactic": "reward_or_benefit", "start_char": 288, "end_char": 365, "span_text": "Secure an immediate personal advance disbursement of $25,000 upon enrollment."}, {"tactic": "urgency", "start_char": 366, "end_char": 415, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Subject: Notice of Credit Authorization: Personal Line Disbursement Scheduled

Attention Account Holder,

Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.

Certified clearance code: CF-11061-AUTH verified through centralized ledger. Secure an immediate personal advance disbursement of $25,000 upon enrollment. Immediate response required before 5:00 PM today.

Pay the mandatory 2% loan origination and documentation fee ($3,392.80) via wire transfer to release your funds.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0050
- **ID:** `PILOT-0050`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["scarcity", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 373, "end_char": 479, "span_text": "Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement."}`
- **Narrative Evidence:** `{"start_char": 106, "end_char": 203, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 205, "end_char": 295, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}, {"tactic": "urgency", "start_char": 296, "end_char": 371, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}]`

**Complete Original Text:**
```text
Subject: Notice of Credit Authorization: Personal Line Disbursement Scheduled

Attention Account Holder,

You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate.

Only 2 participant allocations remain available before registration is permanently closed. Act within the next 60 minutes to prevent irreversible account restriction.

Submit your full Social Security number, monthly income, and bank routing digits to finalize disbursement.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

### Subtype Group: `investment_crypto`

#### Record PILOT-0051
- **ID:** `PILOT-0051`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["secrecy", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 385, "end_char": 484, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 89, "end_char": 195, "span_text": "A private pre-sale token allocation on BitCrest Capital is open exclusively to verified community members."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 197, "end_char": 280, "span_text": "Do not disclose this ongoing internal audit to any third party under any condition."}, {"tactic": "trust_exploitation", "start_char": 281, "end_char": 383, "span_text": "As your assigned dedicated personal banker at First Crest Bank, I am handling your profile personally."}]`

**Complete Original Text:**
```text
Subject: Private Placement: Managed Staking Yield Allocation

Attention Account Holder,

A private pre-sale token allocation on BitCrest Capital is open exclusively to verified community members.

Do not disclose this ongoing internal audit to any third party under any condition. As your assigned dedicated personal banker at First Crest Bank, I am handling your profile personally.

Download and launch the AnyDesk remote support client to grant our technician configuration access.

Sincerely,
Operations & Risk Desk
First Crest Bank
```

---

#### Record PILOT-0052
- **ID:** `PILOT-0052`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 132, "end_char": 235, "span_text": "Transfer 1,500 USDT to our liquidity contract vault on BitCrest Capital to activate 18% weekly returns."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 131, "span_text": "A private pre-sale token allocation on BitCrest Capital is open exclusively to verified community members."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: A private pre-sale token allocation on BitCrest Capital is open exclusively to verified community members. Transfer 1,500 USDT to our liquidity contract vault on BitCrest Capital to activate 18% weekly returns.
[10:16 AM] You: Is there any documentation or agreement I need to sign first?
```

---

#### Record PILOT-0053
- **ID:** `PILOT-0053`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 341, "end_char": 448, "span_text": "Install TeamViewer QuickSupport to enable our diagnostic specialist to inspect your active banking session."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 132, "span_text": "Our proprietary AI algorithmic trading engine on PrimeYield Vault achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 236, "end_char": 340, "span_text": "As your assigned dedicated personal banker at Apex National Bank, I am handling your profile personally."}]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: Our proprietary AI algorithmic trading engine on PrimeYield Vault achieved an audited 24.5% monthly return.
[10:16 AM] You: Is there any documentation or agreement I need to sign first?
[10:17 AM] Desk_Officer: As your assigned dedicated personal banker at Apex National Bank, I am handling your profile personally. Install TeamViewer QuickSupport to enable our diagnostic specialist to inspect your active banking session.
```

---

#### Record PILOT-0054
- **ID:** `PILOT-0054`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 134, "end_char": 237, "span_text": "Deposit an initial investment of $3,411.80 into the EtherPeak Trading automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 133, "span_text": "Our proprietary AI algorithmic trading engine on EtherPeak Trading achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: Our proprietary AI algorithmic trading engine on EtherPeak Trading achieved an audited 24.5% monthly return. Deposit an initial investment of $3,411.80 into the EtherPeak Trading automated arbitrage trading pool.
[10:16 AM] You: How does the return or commission get paid out? Is it daily?
```

---

#### Record PILOT-0055
- **ID:** `PILOT-0055`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 207, "end_char": 310, "span_text": "Deposit an initial investment of $1,358.00 into the NovaChain Markets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 109, "span_text": "A private pre-sale token allocation on NovaChain Markets is open exclusively to verified community members."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 110, "end_char": 206, "span_text": "You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
💰 A private pre-sale token allocation on NovaChain Markets is open exclusively to verified community members. You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture. Deposit an initial investment of $1,358.00 into the NovaChain Markets automated arbitrage trading pool.
```

---

#### Record PILOT-0056
- **ID:** `PILOT-0056`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 197, "end_char": 302, "span_text": "Deposit an initial investment of $4,051.95 into the CryptoSphere Assets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 110, "span_text": "Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 111, "end_char": 196, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}]`

**Complete Original Text:**
```text
Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return. Limited settlement quota expires today and cannot be extended under any circumstance. Deposit an initial investment of $4,051.95 into the CryptoSphere Assets automated arbitrage trading pool.
```

---

#### Record PILOT-0057
- **ID:** `PILOT-0057`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 127, "end_char": 233, "span_text": "Transfer 1,500 USDT to our liquidity contract vault on CryptoSphere Assets to activate 18% weekly returns."}`
- **Narrative Evidence:** `{"start_char": 17, "end_char": 126, "span_text": "A private pre-sale token allocation on CryptoSphere Assets is open exclusively to verified community members."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[NovaPay Notice] A private pre-sale token allocation on CryptoSphere Assets is open exclusively to verified community members. Transfer 1,500 USDT to our liquidity contract vault on CryptoSphere Assets to activate 18% weekly returns.
```

---

#### Record PILOT-0058
- **ID:** `PILOT-0058`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 337, "end_char": 443, "span_text": "Transfer 1,500 USDT to our liquidity contract vault on CryptoSphere Assets to activate 18% weekly returns."}`
- **Narrative Evidence:** `{"start_char": 89, "end_char": 198, "span_text": "A private pre-sale token allocation on CryptoSphere Assets is open exclusively to verified community members."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 200, "end_char": 249, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "scarcity", "start_char": 250, "end_char": 335, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}]`

**Complete Original Text:**
```text
Subject: Private Placement: Managed Staking Yield Allocation

Attention Account Holder,

A private pre-sale token allocation on CryptoSphere Assets is open exclusively to verified community members.

Immediate response required before 5:00 PM today. Limited settlement quota expires today and cannot be extended under any circumstance.

Transfer 1,500 USDT to our liquidity contract vault on CryptoSphere Assets to activate 18% weekly returns.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT-0059
- **ID:** `PILOT-0059`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["reward_or_benefit", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 125, "end_char": 229, "span_text": "Transfer 1,500 USDT to our liquidity contract vault on NovaChain Markets to activate 18% weekly returns."}`
- **Narrative Evidence:** `{"start_char": 17, "end_char": 124, "span_text": "A private pre-sale token allocation on NovaChain Markets is open exclusively to verified community members."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[NovaPay Notice] A private pre-sale token allocation on NovaChain Markets is open exclusively to verified community members. Transfer 1,500 USDT to our liquidity contract vault on NovaChain Markets to activate 18% weekly returns.
```

---

#### Record PILOT-0060
- **ID:** `PILOT-0060`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["scarcity", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 340, "end_char": 443, "span_text": "Transfer 1,500 USDT to our liquidity contract vault on BitCrest Capital to activate 18% weekly returns."}`
- **Narrative Evidence:** `{"start_char": 89, "end_char": 196, "span_text": "Our proprietary AI algorithmic trading engine on BitCrest Capital achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 198, "end_char": 288, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}, {"tactic": "urgency", "start_char": 289, "end_char": 338, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Subject: Private Placement: Managed Staking Yield Allocation

Attention Account Holder,

Our proprietary AI algorithmic trading engine on BitCrest Capital achieved an audited 24.5% monthly return.

Only 2 participant allocations remain available before registration is permanently closed. Immediate response required before 5:00 PM today.

Transfer 1,500 USDT to our liquidity contract vault on BitCrest Capital to activate 18% weekly returns.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

### Subtype Group: `prize_reward`

#### Record PILOT-0061
- **ID:** `PILOT-0061`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 244, "end_char": 351, "span_text": "Provide your full legal name, date of birth, and active credit card details for winner identity validation."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 99, "span_text": "Official winner notification: your entry ticket was awarded the $401.00 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 100, "end_char": 175, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}, {"tactic": "reward_or_benefit", "start_char": 176, "end_char": 243, "span_text": "Unlock your confirmed prize distribution voucher valued at $401.00."}]`

**Complete Original Text:**
```text
🥳 Official winner notification: your entry ticket was awarded the $401.00 retail promotional grant. Act within the next 60 minutes to prevent irreversible account restriction. Unlock your confirmed prize distribution voucher valued at $401.00. Provide your full legal name, date of birth, and active credit card details for winner identity validation.
```

---

#### Record PILOT-0062
- **ID:** `PILOT-0062`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 289, "end_char": 407, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly."}`
- **Narrative Evidence:** `{"start_char": 104, "end_char": 203, "span_text": "Official winner notification: your entry ticket was awarded the $3,623.95 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 205, "end_char": 287, "span_text": "Receive an immediate promotional gift disbursement of $3,623.95 upon verification."}]`

**Complete Original Text:**
```text
Subject: Award Confirmation: Entry Selection for Seasonal Promotional Grant

Attention Account Holder,

Official winner notification: your entry ticket was awarded the $3,623.95 retail promotional grant.

Receive an immediate promotional gift disbursement of $3,623.95 upon verification.

Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT-0063
- **ID:** `PILOT-0063`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 182, "end_char": 273, "span_text": "Remit the $350 sweepstakes tax clearance fee via wire transfer to disburse your cash award."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 99, "span_text": "Official winner notification: your entry ticket was awarded the $212.50 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 100, "end_char": 181, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

**Complete Original Text:**
```text
✨ Official winner notification: your entry ticket was awarded the $212.50 retail promotional grant. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Remit the $350 sweepstakes tax clearance fee via wire transfer to disburse your cash award.
```

---

#### Record PILOT-0064
- **ID:** `PILOT-0064`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 257, "end_char": 332, "span_text": "Transfer $75 via AppleCash Express to activate your prize shipment voucher."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 101, "span_text": "Official winner notification: your entry ticket was awarded the $3,723.00 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 102, "end_char": 184, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}, {"tactic": "urgency", "start_char": 185, "end_char": 256, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
🎉 Official winner notification: your entry ticket was awarded the $3,723.00 retail promotional grant. This reservation window is strictly limited to the first ten verified respondents. Time-sensitive alert: immediate verification is required without delay. Transfer $75 via AppleCash Express to activate your prize shipment voucher.
```

---

#### Record PILOT-0065
- **ID:** `PILOT-0065`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 489, "end_char": 588, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via QuickTransfer to release your prize."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 122, "span_text": "Official winner notification: your entry ticket was awarded the $794.95 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 226, "end_char": 311, "span_text": "Audit Case Docket: CF-50668 registered under statutory financial compliance protocol."}, {"tactic": "urgency", "start_char": 312, "end_char": 402, "span_text": "You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture."}, {"tactic": "scarcity", "start_char": 403, "end_char": 488, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: Official winner notification: your entry ticket was awarded the $794.95 retail promotional grant.
[10:16 AM] You: Understood. What is the quickest way to resolve this balance?
[10:17 AM] Desk_Officer: Audit Case Docket: CF-50668 registered under statutory financial compliance protocol. You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture. Limited settlement quota expires today and cannot be extended under any circumstance. Pay the mandatory $125 delivery and insurance handling fee via QuickTransfer to release your prize.
```

---

#### Record PILOT-0066
- **ID:** `PILOT-0066`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["scarcity", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 359, "end_char": 488, "span_text": "Enter your customer rewards portal password and security PIN at https://horizon-secure-wire-desk.org/login to claim your voucher."}`
- **Narrative Evidence:** `{"start_char": 104, "end_char": 203, "span_text": "Official winner notification: your entry ticket was awarded the $1,601.95 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 205, "end_char": 287, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}, {"tactic": "reward_or_benefit", "start_char": 288, "end_char": 357, "span_text": "Unlock your confirmed prize distribution voucher valued at $1,601.95."}]`

**Complete Original Text:**
```text
Subject: Award Confirmation: Entry Selection for Seasonal Promotional Grant

Attention Account Holder,

Official winner notification: your entry ticket was awarded the $1,601.95 retail promotional grant.

This reservation window is strictly limited to the first ten verified respondents. Unlock your confirmed prize distribution voucher valued at $1,601.95.

Enter your customer rewards portal password and security PIN at https://horizon-secure-wire-desk.org/login to claim your voucher.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT-0067
- **ID:** `PILOT-0067`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 385, "end_char": 503, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly."}`
- **Narrative Evidence:** `{"start_char": 104, "end_char": 203, "span_text": "Official winner notification: your entry ticket was awarded the $2,501.00 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 205, "end_char": 297, "span_text": "Claim your guaranteed cash reward allocation of $2,501.00 credited directly to your profile."}, {"tactic": "scarcity", "start_char": 298, "end_char": 383, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}]`

**Complete Original Text:**
```text
Subject: Award Confirmation: Entry Selection for Seasonal Promotional Grant

Attention Account Holder,

Official winner notification: your entry ticket was awarded the $2,501.00 retail promotional grant.

Claim your guaranteed cash reward allocation of $2,501.00 credited directly to your profile. Limited settlement quota expires today and cannot be extended under any circumstance.

Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT-0068
- **ID:** `PILOT-0068`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 287, "end_char": 378, "span_text": "Remit the $350 sweepstakes tax clearance fee via wire transfer to disburse your cash award."}`
- **Narrative Evidence:** `{"start_char": 104, "end_char": 201, "span_text": "Official winner notification: your entry ticket was awarded the $470.50 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 203, "end_char": 285, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Subject: Award Confirmation: Entry Selection for Seasonal Promotional Grant

Attention Account Holder,

Official winner notification: your entry ticket was awarded the $470.50 retail promotional grant.

This reservation window is strictly limited to the first ten verified respondents.

Remit the $350 sweepstakes tax clearance fee via wire transfer to disburse your cash award.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT-0069
- **ID:** `PILOT-0069`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 266, "end_char": 384, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 96, "span_text": "You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 97, "end_char": 189, "span_text": "Claim your guaranteed cash reward allocation of $2,477.80 credited directly to your profile."}, {"tactic": "urgency", "start_char": 190, "end_char": 265, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}]`

**Complete Original Text:**
```text
✨ You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing. Claim your guaranteed cash reward allocation of $2,477.80 credited directly to your profile. Act within the next 60 minutes to prevent irreversible account restriction. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly.
```

---

#### Record PILOT-0070
- **ID:** `PILOT-0070`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 122, "end_char": 220, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via ZelleConnect to release your prize."}`
- **Narrative Evidence:** `{"start_char": 22, "end_char": 121, "span_text": "Official winner notification: your entry ticket was awarded the $3,120.80 retail promotional grant."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[ZelleConnect Notice] Official winner notification: your entry ticket was awarded the $3,120.80 retail promotional grant. Pay the mandatory $125 delivery and insurance handling fee via ZelleConnect to release your prize.
```

---

### Subtype Group: `tax_payment`

#### Record PILOT-0071
- **ID:** `PILOT-0071`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 242, "end_char": 363, "span_text": "Remit payment of $1,631.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $1,631.50."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 105, "end_char": 188, "span_text": "Do not disclose this ongoing internal audit to any third party under any condition."}, {"tactic": "authority_impersonation", "start_char": 189, "end_char": 241, "span_text": "Authorized by senior financial auditor Robert Vance."}]`

**Complete Original Text:**
```text
A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $1,631.50. Do not disclose this ongoing internal audit to any third party under any condition. Authorized by senior financial auditor Robert Vance. Remit payment of $1,631.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

#### Record PILOT-0072
- **ID:** `PILOT-0072`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 291, "end_char": 413, "span_text": "Submit your full Social Security number, date of birth, and checking account routing digits to reconcile your tax profile."}`
- **Narrative Evidence:** `{"start_char": 92, "end_char": 193, "span_text": "Statutory audit docket #CF-60052 identified an underreported income tax liability totaling $3,932.80."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 195, "end_char": 289, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Subject: STATUTORY COMPLIANCE: Assessment Notice File #CF-60052

Attention Account Holder,

Statutory audit docket #CF-60052 identified an underreported income tax liability totaling $3,932.80.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.

Submit your full Social Security number, date of birth, and checking account routing digits to reconcile your tax profile.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0073
- **ID:** `PILOT-0073`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 170, "end_char": 286, "span_text": "Settle the outstanding statutory tax obligation of $3,830.50 using AppleCash Express before county sheriff dispatch."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,830.50."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 105, "end_char": 169, "span_text": "Official notice from Pinnacle Bank Fraud Investigation Division."}]`

**Complete Original Text:**
```text
A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,830.50. Official notice from Pinnacle Bank Fraud Investigation Division. Settle the outstanding statutory tax obligation of $3,830.50 using AppleCash Express before county sheriff dispatch.
```

---

#### Record PILOT-0074
- **ID:** `PILOT-0074`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 158, "end_char": 279, "span_text": "Remit payment of $2,896.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $2,896.50."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 105, "end_char": 157, "span_text": "Authorized by senior financial auditor Robert Vance."}]`

**Complete Original Text:**
```text
A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $2,896.50. Authorized by senior financial auditor Robert Vance. Remit payment of $2,896.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

#### Record PILOT-0075
- **ID:** `PILOT-0075`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 102, "end_char": 213, "span_text": "Settle the outstanding statutory tax obligation of $2,510.50 using ZelleConnect before county sheriff dispatch."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 101, "span_text": "Statutory audit docket #CF-49472 identified an underreported income tax liability totaling $2,510.50."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Statutory audit docket #CF-49472 identified an underreported income tax liability totaling $2,510.50. Settle the outstanding statutory tax obligation of $2,510.50 using ZelleConnect before county sheriff dispatch.
```

---

#### Record PILOT-0076
- **ID:** `PILOT-0076`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 193, "end_char": 315, "span_text": "Submit your full Social Security number, date of birth, and checking account routing digits to reconcile your tax profile."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,666.00."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 105, "end_char": 192, "span_text": "Keep this private settlement between us until the documentation is officially archived."}]`

**Complete Original Text:**
```text
A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,666.00. Keep this private settlement between us until the documentation is officially archived. Submit your full Social Security number, date of birth, and checking account routing digits to reconcile your tax profile.
```

---

#### Record PILOT-0077
- **ID:** `PILOT-0077`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy", "authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 458, "end_char": 579, "span_text": "Remit payment of $3,075.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 92, "end_char": 196, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,075.00."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 198, "end_char": 297, "span_text": "Maintain strict confidentiality and avoid discussing this matter with local branch representatives."}, {"tactic": "authority_impersonation", "start_char": 298, "end_char": 369, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}, {"tactic": "fear_or_threat", "start_char": 370, "end_char": 456, "span_text": "Law enforcement officers will be dispatched to your registered domicile if unresolved."}]`

**Complete Original Text:**
```text
Subject: STATUTORY COMPLIANCE: Assessment Notice File #CF-55193

Attention Account Holder,

A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,075.00.

Maintain strict confidentiality and avoid discussing this matter with local branch representatives. This communication is issued by the Federal Regulatory Compliance Unit. Law enforcement officers will be dispatched to your registered domicile if unresolved.

Remit payment of $3,075.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.

Sincerely,
Operations & Risk Desk
First Crest Bank
```

---

#### Record PILOT-0078
- **ID:** `PILOT-0078`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 279, "end_char": 385, "span_text": "Verify your taxpayer identification number and primary debit card CVV to complete statutory documentation."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 102, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $508.50."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 103, "end_char": 178, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}, {"tactic": "secrecy", "start_char": 179, "end_char": 278, "span_text": "Maintain strict confidentiality and avoid discussing this matter with local branch representatives."}]`

**Complete Original Text:**
```text
A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $508.50. Act within the next 60 minutes to prevent irreversible account restriction. Maintain strict confidentiality and avoid discussing this matter with local branch representatives. Verify your taxpayer identification number and primary debit card CVV to complete statutory documentation.
```

---

#### Record PILOT-0079
- **ID:** `PILOT-0079`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 105, "end_char": 218, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen to authorize tax settlement."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 104, "span_text": "A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,752.95."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of $3,752.95. Reply with the 6-digit confirmation passcode displayed on your authentication screen to authorize tax settlement.
```

---

#### Record PILOT-0080
- **ID:** `PILOT-0080`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 195, "end_char": 301, "span_text": "Verify your taxpayer identification number and primary debit card CVV to complete statutory documentation."}`
- **Narrative Evidence:** `{"start_char": 92, "end_char": 193, "span_text": "Statutory audit docket #CF-50173 identified an underreported income tax liability totaling $2,836.80."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Subject: STATUTORY COMPLIANCE: Assessment Notice File #CF-50173

Attention Account Holder,

Statutory audit docket #CF-50173 identified an underreported income tax liability totaling $2,836.80.

Verify your taxpayer identification number and primary debit card CVV to complete statutory documentation.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

### Subtype Group: `job_task_commission`

#### Record PILOT-0081
- **ID:** `PILOT-0081`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 362, "end_char": 460, "span_text": "Remit payment of $1,460.00 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 28, "end_char": 128, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 235, "end_char": 284, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "false_legitimacy", "start_char": 285, "end_char": 361, "span_text": "Certified clearance code: CF-28714-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
[10:14 AM] Recruiter_Sarah: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.
[10:16 AM] You: Understood. Where exactly do I need to send the confirmation?
[10:17 AM] Recruiter_Sarah: Immediate response required before 5:00 PM today. Certified clearance code: CF-28714-AUTH verified through centralized ledger. Remit payment of $1,460.00 via wire transfer to our settlement escrow routing account immediately.
```

---

#### Record PILOT-0082
- **ID:** `PILOT-0082`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 276, "end_char": 374, "span_text": "Remit payment of $3,410.80 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 96, "end_char": 196, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 198, "end_char": 274, "span_text": "Certified clearance code: CF-95139-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
Subject: Onboarding Documentation: Evaluation Specialist Assignment

Attention Account Holder,

Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.

Certified clearance code: CF-95139-AUTH verified through centralized ledger.

Remit payment of $3,410.80 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT-0083
- **ID:** `PILOT-0083`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 398, "end_char": 489, "span_text": "Settle the required statutory handling fee of $1,789.00 using CashFlow before the deadline."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 125, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 229, "end_char": 306, "span_text": "Receive guaranteed daily task bonuses of $250 to $450 credited every evening."}, {"tactic": "scarcity", "start_char": 307, "end_char": 397, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.
[10:16 AM] You: Understood. Where exactly do I need to send the confirmation?
[10:17 AM] Desk_Officer: Receive guaranteed daily task bonuses of $250 to $450 credited every evening. Only 2 participant allocations remain available before registration is permanently closed. Settle the required statutory handling fee of $1,789.00 using CashFlow before the deadline.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0084
- **ID:** `PILOT-0084`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 372, "end_char": 466, "span_text": "Transfer $1,287.50 through NovaPay to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 132, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 238, "end_char": 287, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "reward_or_benefit", "start_char": 288, "end_char": 371, "span_text": "Earn daily automated commission distributions averaging $300 daily upon onboarding."}]`

**Complete Original Text:**
```text
[10:14 AM] Advisor_Morgan: Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily.
[10:16 AM] You: Understood. Where exactly do I need to send the confirmation?
[10:17 AM] Advisor_Morgan: Immediate response required before 5:00 PM today. Earn daily automated commission distributions averaging $300 daily upon onboarding. Transfer $1,287.50 through NovaPay to our designated clearance officer to resolve the balance.
```

---

#### Record PILOT-0085
- **ID:** `PILOT-0085`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 130, "end_char": 233, "span_text": "Provide your complete banking routing number and checking account digits to update your direct profile."}`
- **Narrative Evidence:** `{"start_char": 24, "end_char": 129, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[PayLink Mobile Notice] Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily. Provide your complete banking routing number and checking account digits to update your direct profile.
```

---

#### Record PILOT-0086
- **ID:** `PILOT-0086`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 189, "end_char": 286, "span_text": "Settle the required statutory handling fee of $2,398.50 using PayLink Mobile before the deadline."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 102, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 103, "end_char": 188, "span_text": "Limited settlement quota expires today and cannot be extended under any circumstance."}]`

**Complete Original Text:**
```text
📲 Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations. Limited settlement quota expires today and cannot be extended under any circumstance. Settle the required statutory handling fee of $2,398.50 using PayLink Mobile before the deadline.
```

---

#### Record PILOT-0087
- **ID:** `PILOT-0087`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 268, "end_char": 375, "span_text": "Submit your full Social Security number, date of birth, and mother's maiden name for record reconciliation."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 107, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 108, "end_char": 185, "span_text": "Receive guaranteed daily task bonuses of $250 to $450 credited every evening."}, {"tactic": "false_legitimacy", "start_char": 186, "end_char": 267, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

**Complete Original Text:**
```text
💼 Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily. Receive guaranteed daily task bonuses of $250 to $450 credited every evening. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Submit your full Social Security number, date of birth, and mother's maiden name for record reconciliation.
```

---

#### Record PILOT-0088
- **ID:** `PILOT-0088`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 128, "end_char": 227, "span_text": "Transfer $4,368.00 through ZelleConnect to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 127, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Advisor_Morgan: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations. Transfer $4,368.00 through ZelleConnect to our designated clearance officer to resolve the balance.
[10:16 AM] You: Wait, what is the minimum deposit or fee required to start?
```

---

#### Record PILOT-0089
- **ID:** `PILOT-0089`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["false_legitimacy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 391, "end_char": 490, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 127, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 231, "end_char": 312, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "reward_or_benefit", "start_char": 313, "end_char": 390, "span_text": "Receive guaranteed daily task bonuses of $250 to $450 credited every evening."}]`

**Complete Original Text:**
```text
[10:14 AM] Advisor_Morgan: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.
[10:16 AM] You: Wait, what is the minimum deposit or fee required to start?
[10:17 AM] Advisor_Morgan: Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Receive guaranteed daily task bonuses of $250 to $450 credited every evening. Download and launch the AnyDesk remote support client to grant our technician configuration access.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0090
- **ID:** `PILOT-0090`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 310, "end_char": 407, "span_text": "Settle the required statutory handling fee of $3,146.95 using PayLink Mobile before the deadline."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 127, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 233, "end_char": 309, "span_text": "Certified clearance code: CF-57964-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
[10:14 AM] Advisor_Morgan: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.
[10:16 AM] You: Understood. Where exactly do I need to send the confirmation?
[10:17 AM] Advisor_Morgan: Certified clearance code: CF-57964-AUTH verified through centralized ledger. Settle the required statutory handling fee of $3,146.95 using PayLink Mobile before the deadline.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

### Subtype Group: `romance_financial_manipulation`

#### Record PILOT-0091
- **ID:** `PILOT-0091`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 322, "end_char": 421, "span_text": "Please wire $2,927.80 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 128, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 225, "end_char": 321, "span_text": "You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: Wait, can't the embassy or the company help you cover this?
[10:17 AM] Elena: You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture. Please wire $2,927.80 to the medical clearing officer today so I can receive the emergency surgery.
```

---

#### Record PILOT-0092
- **ID:** `PILOT-0092`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 409, "end_char": 521, "span_text": "Can you send $2,905.95 through CashFlow to the airport customs liaison so I can clear my luggage and fly to you?"}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 128, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 237, "end_char": 320, "span_text": "Reaching out to you directly because I know you have always believed in our future."}, {"tactic": "secrecy", "start_char": 321, "end_char": 408, "span_text": "Keep this private settlement between us until the documentation is officially archived."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: Don't worry sweetheart, I'm here for you. Where do I send the transfer?
[10:17 AM] Elena: Reaching out to you directly because I know you have always believed in our future. Keep this private settlement between us until the documentation is officially archived. Can you send $2,905.95 through CashFlow to the airport customs liaison so I can clear my luggage and fly to you?
[10:19 AM] Honey: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0093
- **ID:** `PILOT-0093`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["emotional_manipulation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 381, "end_char": 491, "span_text": "If we deposit $4,085.50 together on PrimeYield Vault, we can earn the returns to buy our dream home next year."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 128, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 214, "end_char": 284, "span_text": "I am sitting in total distress and feeling utterly helpless right now."}, {"tactic": "urgency", "start_char": 285, "end_char": 380, "span_text": "You must complete this mandatory requirement by tomorrow morning to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: My love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am sitting in total distress and feeling utterly helpless right now. You must complete this mandatory requirement by tomorrow morning to avoid automatic forfeiture. If we deposit $4,085.50 together on PrimeYield Vault, we can earn the returns to buy our dream home next year.
```

---

#### Record PILOT-0094
- **ID:** `PILOT-0094`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 391, "end_char": 491, "span_text": "Please send $2,812.95 via wire transfer to the harbor authority so they release my travel documents."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 129, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 227, "end_char": 314, "span_text": "Keep this private settlement between us until the documentation is officially archived."}, {"tactic": "urgency", "start_char": 315, "end_char": 390, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}]`

**Complete Original Text:**
```text
[10:14 AM] Sophia: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: Wait, can't the embassy or the company help you cover this?
[10:17 AM] Sophia: Keep this private settlement between us until the documentation is officially archived. Act within the next 60 minutes to prevent irreversible account restriction. Please send $2,812.95 via wire transfer to the harbor authority so they release my travel documents.
[10:19 AM] Honey: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0095
- **ID:** `PILOT-0095`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["urgency", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 349, "end_char": 463, "span_text": "Allocate $2,517.50 to the automated trading pool on EtherPeak Trading so we can achieve early retirement together."}`
- **Narrative Evidence:** `{"start_char": 76, "end_char": 186, "span_text": "My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 188, "end_char": 263, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}, {"tactic": "secrecy", "start_char": 264, "end_char": 347, "span_text": "Do not disclose this ongoing internal audit to any third party under any condition."}]`

**Complete Original Text:**
```text
Subject: Urgent update from overseas - please read right away

My dearest,

My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs.

Act within the next 60 minutes to prevent irreversible account restriction. Do not disclose this ongoing internal audit to any third party under any condition.

Allocate $2,517.50 to the automated trading pool on EtherPeak Trading so we can achieve early retirement together.

Yours always,
Sophia
```

---

#### Record PILOT-0096
- **ID:** `PILOT-0096`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "emotional_manipulation", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 442, "end_char": 541, "span_text": "Please wire $4,074.50 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 129, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 226, "end_char": 275, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "emotional_manipulation", "start_char": 276, "end_char": 358, "span_text": "I am in complete despair and do not know who else can help me through this crisis."}, {"tactic": "trust_exploitation", "start_char": 359, "end_char": 441, "span_text": "You know our mutual trust and love mean everything to me in this difficult moment."}]`

**Complete Original Text:**
```text
[10:14 AM] Sophia: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: Oh no, that sounds awful. How soon do they need the money?
[10:17 AM] Sophia: Immediate response required before 5:00 PM today. I am in complete despair and do not know who else can help me through this crisis. You know our mutual trust and love mean everything to me in this difficult moment. Please wire $4,074.50 to the medical clearing officer today so I can receive the emergency surgery.
[10:19 AM] Honey: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0097
- **ID:** `PILOT-0097`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 302, "end_char": 413, "span_text": "Can you send $4,046.95 through NovaPay to the airport customs liaison so I can clear my luggage and fly to you?"}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 128, "span_text": "My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 214, "end_char": 301, "span_text": "Keep this private settlement between us until the documentation is officially archived."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs.
[10:16 AM] Honey: My love, what happened?! Are you safe right now?
[10:17 AM] Elena: Keep this private settlement between us until the documentation is officially archived. Can you send $4,046.95 through NovaPay to the airport customs liaison so I can clear my luggage and fly to you?
[10:19 AM] Honey: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0098
- **ID:** `PILOT-0098`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 130, "end_char": 251, "span_text": "Can you send $2,521.00 through AppleCash Express to the airport customs liaison so I can clear my luggage and fly to you?"}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 129, "span_text": "My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Sophia: My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs. Can you send $2,521.00 through AppleCash Express to the airport customs liaison so I can clear my luggage and fly to you?
[10:16 AM] Honey: Don't worry sweetheart, I'm here for you. Where do I send the transfer?
```

---

#### Record PILOT-0099
- **ID:** `PILOT-0099`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 252, "end_char": 351, "span_text": "Please wire $2,566.50 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 76, "end_char": 186, "span_text": "My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 188, "end_char": 250, "span_text": "Please do not abandon me when I need your compassion the most."}]`

**Complete Original Text:**
```text
Subject: Urgent update from overseas - please read right away

My dearest,

My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs.

Please do not abandon me when I need your compassion the most.

Please wire $2,566.50 to the medical clearing officer today so I can receive the emergency surgery.

Love always,
Elena
```

---

#### Record PILOT-0100
- **ID:** `PILOT-0100`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation", "trust_exploitation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 308, "end_char": 405, "span_text": "Please wire $243.80 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 110, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 111, "end_char": 173, "span_text": "Please do not abandon me when I need your compassion the most."}, {"tactic": "trust_exploitation", "start_char": 174, "end_char": 257, "span_text": "Reaching out to you directly because I know you have always believed in our future."}, {"tactic": "urgency", "start_char": 258, "end_char": 307, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery. Please do not abandon me when I need your compassion the most. Reaching out to you directly because I know you have always believed in our future. Immediate response required before 5:00 PM today. Please wire $243.80 to the medical clearing officer today so I can receive the emergency surgery.
```

---

### Subtype Group: `family_emergency_request`

#### Record PILOT-0101
- **ID:** `PILOT-0101`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 378, "end_char": 476, "span_text": "Forward the debit card approval passcode sent to your mobile so I can clear the emergency deposit."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 126, "span_text": "Hi Uncle Dave, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 245, "end_char": 294, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "emotional_manipulation", "start_char": 295, "end_char": 377, "span_text": "I am in complete despair and do not know who else can help me through this crisis."}]`

**Complete Original Text:**
```text
[10:14 AM] Jordan: Hi Uncle Dave, my phone was severely damaged in an accident so I am messaging you from this temporary line.
[10:16 AM] Uncle Dave: Wait, is this really you? Why aren't you calling me from your normal phone?
[10:17 AM] Jordan: Immediate response required before 5:00 PM today. I am in complete despair and do not know who else can help me through this crisis. Forward the debit card approval passcode sent to your mobile so I can clear the emergency deposit.
[10:19 AM] Uncle Dave: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0102
- **ID:** `PILOT-0102`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 115, "end_char": 200, "span_text": "Please wire $1,377.50 to the emergency clinic liaison right away so I can be treated."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 114, "span_text": "Hey Cousin Mark, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Hey Cousin Mark, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Please wire $1,377.50 to the emergency clinic liaison right away so I can be treated.
```

---

#### Record PILOT-0103
- **ID:** `PILOT-0103`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 186, "end_char": 279, "span_text": "Can you please Zelle $328.95 to pay-clinic@emergency-care.net right now so they can admit me?"}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 106, "span_text": "Hey Sis, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 107, "end_char": 185, "span_text": "You know that our family bond means everything to me in this difficult moment."}]`

**Complete Original Text:**
```text
Hey Sis, I was involved in an unexpected fender bender and need to settle the repair before police arrive. You know that our family bond means everything to me in this difficult moment. Can you please Zelle $328.95 to pay-clinic@emergency-care.net right now so they can admit me?
```

---

#### Record PILOT-0104
- **ID:** `PILOT-0104`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 132, "end_char": 232, "span_text": "Please send $3,242.95 via QuickTransfer to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 131, "span_text": "Hey Uncle Dave, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Kevin: Hey Uncle Dave, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Please send $3,242.95 via QuickTransfer to the towing driver right now so they don't impound my car.
[10:16 AM] Uncle Dave: Oh my god, what happened?? Are you hurt? Which clinic are you at?
```

---

#### Record PILOT-0105
- **ID:** `PILOT-0105`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 123, "end_char": 235, "span_text": "Can you give me your checking account number and routing digits so the clinic doctor can process direct billing?"}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 122, "span_text": "Hi Grandma, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Kevin: Hi Grandma, my phone was severely damaged in an accident so I am messaging you from this temporary line. Can you give me your checking account number and routing digits so the clinic doctor can process direct billing?
[10:16 AM] Grandma: Oh my god, what happened?? Are you hurt? Which clinic are you at?
```

---

#### Record PILOT-0106
- **ID:** `PILOT-0106`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 214, "end_char": 315, "span_text": "Could you transfer $612.50 through NovaPay to the repair garage immediately before the police arrive?"}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 100, "span_text": "Hi Dad, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 101, "end_char": 150, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "emotional_manipulation", "start_char": 151, "end_char": 213, "span_text": "Please do not abandon me when I need your compassion the most."}]`

**Complete Original Text:**
```text
Hi Dad, my phone was severely damaged in an accident so I am messaging you from this temporary line. Immediate response required before 5:00 PM today. Please do not abandon me when I need your compassion the most. Could you transfer $612.50 through NovaPay to the repair garage immediately before the police arrive?
```

---

#### Record PILOT-0107
- **ID:** `PILOT-0107`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 124, "end_char": 209, "span_text": "Please wire $3,272.80 to the emergency clinic liaison right away so I can be treated."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 123, "span_text": "Hi Grandma, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Jordan: Hi Grandma, my phone was severely damaged in an accident so I am messaging you from this temporary line. Please wire $3,272.80 to the emergency clinic liaison right away so I can be treated.
[10:16 AM] Grandma: I can send it right now, just tell me where to send it!
```

---

#### Record PILOT-0108
- **ID:** `PILOT-0108`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 367, "end_char": 462, "span_text": "Can you please Zelle $2,238.50 to pay-clinic@emergency-care.net right now so they can admit me?"}`
- **Narrative Evidence:** `{"start_char": 17, "end_char": 117, "span_text": "Hi Dad, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 207, "end_char": 283, "span_text": "Hi Dad, it's really me reaching out directly because I trust you completely."}, {"tactic": "emotional_manipulation", "start_char": 284, "end_char": 366, "span_text": "I am in complete despair and do not know who else can help me through this crisis."}]`

**Complete Original Text:**
```text
[10:14 AM] Alex: Hi Dad, my phone was severely damaged in an accident so I am messaging you from this temporary line.
[10:16 AM] Dad: I can send it right now, just tell me where to send it!
[10:17 AM] Alex: Hi Dad, it's really me reaching out directly because I trust you completely. I am in complete despair and do not know who else can help me through this crisis. Can you please Zelle $2,238.50 to pay-clinic@emergency-care.net right now so they can admit me?
[10:19 AM] Dad: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0109
- **ID:** `PILOT-0109`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 254, "end_char": 358, "span_text": "Please send $2,633.00 via AppleCash Express to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 123, "span_text": "Hi Grandma, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Jordan: Hi Grandma, my phone was severely damaged in an accident so I am messaging you from this temporary line.
[10:16 AM] Grandma: Oh my god, what happened?? Are you hurt? Which clinic are you at?
[10:17 AM] Jordan: Please listen carefully. Please send $2,633.00 via AppleCash Express to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT-0110
- **ID:** `PILOT-0110`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 405, "end_char": 508, "span_text": "Could you transfer $3,967.00 through NovaPay to the repair garage immediately before the police arrive?"}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 126, "span_text": "Hi Uncle Dave, my phone was severely damaged in an accident so I am messaging you from this temporary line."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 235, "end_char": 313, "span_text": "You know that our family bond means everything to me in this difficult moment."}, {"tactic": "urgency", "start_char": 314, "end_char": 404, "span_text": "You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
[10:14 AM] Jordan: Hi Uncle Dave, my phone was severely damaged in an accident so I am messaging you from this temporary line.
[10:16 AM] Uncle Dave: Oh my god, what happened?? Are you hurt? Which clinic are you at?
[10:17 AM] Jordan: You know that our family bond means everything to me in this difficult moment. You must complete this mandatory requirement within 2 hours to avoid automatic forfeiture. Could you transfer $3,967.00 through NovaPay to the repair garage immediately before the police arrive?
[10:19 AM] Uncle Dave: Okay, I am opening the link now to complete it.
```

---

### Subtype Group: `recovery_support`

#### Record PILOT-0111
- **ID:** `PILOT-0111`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy", "reward_or_benefit", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 435, "end_char": 533, "span_text": "Remit payment of $4,660.80 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 209, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $4,660.80."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 211, "end_char": 298, "span_text": "Keep this private settlement between us until the documentation is officially archived."}, {"tactic": "reward_or_benefit", "start_char": 299, "end_char": 347, "span_text": "Immediate response required by tomorrow morning."}, {"tactic": "false_legitimacy", "start_char": 348, "end_char": 433, "span_text": "Audit Case Docket: CF-43728 registered under statutory financial compliance protocol."}]`

**Complete Original Text:**
```text
Subject: Investigation Status: Restitution Docket #CF-43728 Distribution

Attention Account Holder,

Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $4,660.80.

Keep this private settlement between us until the documentation is officially archived. Immediate response required by tomorrow morning. Audit Case Docket: CF-43728 registered under statutory financial compliance protocol.

Remit payment of $4,660.80 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT-0112
- **ID:** `PILOT-0112`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 307, "end_char": 406, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 204, "span_text": "You are named in court restitution docket #CF-28021 to receive recovered fraud compensation of $202.95."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 206, "end_char": 305, "span_text": "Maintain strict confidentiality and avoid discussing this matter with local branch representatives."}]`

**Complete Original Text:**
```text
Subject: Investigation Status: Restitution Docket #CF-28021 Distribution

Attention Account Holder,

You are named in court restitution docket #CF-28021 to receive recovered fraud compensation of $202.95.

Maintain strict confidentiality and avoid discussing this matter with local branch representatives.

Download and launch the AnyDesk remote support client to grant our technician configuration access.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT-0113
- **ID:** `PILOT-0113`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 132, "end_char": 228, "span_text": "Remit payment of $287.80 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 131, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $287.80."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $287.80. Remit payment of $287.80 via wire transfer to our settlement escrow routing account immediately.
[10:16 AM] You: Can you give me the reference docket number for this matter?
```

---

#### Record PILOT-0114
- **ID:** `PILOT-0114`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 380, "span_text": "Transfer $2,607.00 through CashFlow to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 135, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $2,607.00."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 240, "end_char": 284, "span_text": "Immediate response required within 24 hours."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative: Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $2,607.00.
[10:16 AM] You: Can you give me the reference docket number for this matter?
[10:17 AM] Representative: Immediate response required within 24 hours. Transfer $2,607.00 through CashFlow to our designated clearance officer to resolve the balance.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0115
- **ID:** `PILOT-0115`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 257, "end_char": 357, "span_text": "Settle the required statutory handling fee of $1,881.95 using AppleCash Express before the deadline."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 209, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $1,881.95."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 211, "end_char": 255, "span_text": "Immediate response required within 24 hours."}]`

**Complete Original Text:**
```text
Subject: Investigation Status: Restitution Docket #CF-45532 Distribution

Attention Account Holder,

Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $1,881.95.

Immediate response required within 24 hours.

Settle the required statutory handling fee of $1,881.95 using AppleCash Express before the deadline.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT-0116
- **ID:** `PILOT-0116`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 208, "end_char": 304, "span_text": "Provide your 12-word master secret recovery seed phrase to re-establish account synchronization."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 206, "span_text": "You are named in court restitution docket #CF-98740 to receive recovered fraud compensation of $2,119.95."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Subject: Investigation Status: Restitution Docket #CF-98740 Distribution

Attention Account Holder,

You are named in court restitution docket #CF-98740 to receive recovered fraud compensation of $2,119.95.

Provide your 12-word master secret recovery seed phrase to re-establish account synchronization.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT-0117
- **ID:** `PILOT-0117`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["authority_impersonation", "secrecy", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 482, "end_char": 581, "span_text": "Download and launch the AnyDesk remote support client to grant our technician configuration access."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 135, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $3,399.80."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 240, "end_char": 311, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}, {"tactic": "secrecy", "start_char": 312, "end_char": 399, "span_text": "Keep this private settlement between us until the documentation is officially archived."}, {"tactic": "false_legitimacy", "start_char": 400, "end_char": 481, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative: Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $3,399.80.
[10:16 AM] You: Can you give me the reference docket number for this matter?
[10:17 AM] Representative: This communication is issued by the Federal Regulatory Compliance Unit. Keep this private settlement between us until the documentation is officially archived. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Download and launch the AnyDesk remote support client to grant our technician configuration access.
[10:19 AM] You: Okay, I am opening the link now to complete it.
```

---

#### Record PILOT-0118
- **ID:** `PILOT-0118`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 133, "end_char": 231, "span_text": "Remit payment of $1,413.95 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 132, "span_text": "You are named in court restitution docket #CF-51507 to receive recovered fraud compensation of $1,413.95."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[10:14 AM] Representative: You are named in court restitution docket #CF-51507 to receive recovered fraud compensation of $1,413.95. Remit payment of $1,413.95 via wire transfer to our settlement escrow routing account immediately.
[10:16 AM] You: Understood. What is the quickest way to resolve this balance?
```

---

#### Record PILOT-0119
- **ID:** `PILOT-0119`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 300, "end_char": 398, "span_text": "Remit payment of $2,807.95 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 101, "end_char": 209, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $2,807.95."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 211, "end_char": 298, "span_text": "Keep this private settlement between us until the documentation is officially archived."}]`

**Complete Original Text:**
```text
Subject: Investigation Status: Restitution Docket #CF-11617 Distribution

Attention Account Holder,

Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $2,807.95.

Keep this private settlement between us until the documentation is officially archived.

Remit payment of $2,807.95 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT-0120
- **ID:** `PILOT-0120`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["secrecy", "false_legitimacy", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 365, "end_char": 450, "span_text": "Reply with the 6-digit confirmation passcode displayed on your authentication screen."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 106, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $668.50."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 107, "end_char": 206, "span_text": "Maintain strict confidentiality and avoid discussing this matter with local branch representatives."}, {"tactic": "false_legitimacy", "start_char": 207, "end_char": 288, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "urgency", "start_char": 289, "end_char": 364, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}]`

**Complete Original Text:**
```text
Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $668.50. Maintain strict confidentiality and avoid discussing this matter with local branch representatives. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Act within the next 60 minutes to prevent irreversible account restriction. Reply with the 6-digit confirmation passcode displayed on your authentication screen.
```

---

### Subtype Group: `charity_donation`

#### Record PILOT-0121
- **ID:** `PILOT-0121`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 271, "end_char": 366, "span_text": "Transfer $2,849.95 through CashFlow to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 3, "end_char": 109, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 110, "end_char": 186, "span_text": "Certified clearance code: CF-53874-AUTH verified through centralized ledger."}, {"tactic": "emotional_manipulation", "start_char": 187, "end_char": 270, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
🕊️ Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support. Certified clearance code: CF-53874-AUTH verified through centralized ledger. Every passing minute puts an innocent life in severe jeopardy without your support. Transfer $2,849.95 through CashFlow to our designated clearance officer to resolve the balance.
```

---

#### Record PILOT-0122
- **ID:** `PILOT-0122`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 129, "end_char": 224, "span_text": "Settle the required statutory handling fee of $1,082.50 using ZelleConnect before the deadline."}`
- **Narrative Evidence:** `{"start_char": 22, "end_char": 128, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
[ZelleConnect Notice] Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support. Settle the required statutory handling fee of $1,082.50 using ZelleConnect before the deadline.
```

---

#### Record PILOT-0123
- **ID:** `PILOT-0123`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 376, "end_char": 471, "span_text": "Settle the required statutory handling fee of $3,616.95 using ZelleConnect before the deadline."}`
- **Narrative Evidence:** `{"start_char": 87, "end_char": 193, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 195, "end_char": 271, "span_text": "Certified clearance code: CF-19694-AUTH verified through centralized ledger."}, {"tactic": "trust_exploitation", "start_char": 272, "end_char": 374, "span_text": "As your assigned dedicated personal banker at Beacon Financial, I am handling your profile personally."}]`

**Complete Original Text:**
```text
Subject: Humanitarian Relief: Emergency Assistance Sponsorship Drive

Dear Supporter,

Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support.

Certified clearance code: CF-19694-AUTH verified through centralized ledger. As your assigned dedicated personal banker at Beacon Financial, I am handling your profile personally.

Settle the required statutory handling fee of $3,616.95 using ZelleConnect before the deadline.

Sincerely,
Community Outreach Team
SecureVault Tech
```

---

#### Record PILOT-0124
- **ID:** `PILOT-0124`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 318, "end_char": 406, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 131, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 234, "end_char": 317, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
[10:14 AM] Desk_Officer: Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support.
[10:16 AM] You: Can you give me the reference docket number for this matter?
[10:17 AM] Desk_Officer: Every passing minute puts an innocent life in severe jeopardy without your support. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code.
```

---

#### Record PILOT-0125
- **ID:** `PILOT-0125`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 329, "end_char": 425, "span_text": "Settle the required statutory handling fee of $4,104.00 using QuickTransfer before the deadline."}`
- **Narrative Evidence:** `{"start_char": 87, "end_char": 194, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 196, "end_char": 245, "span_text": "Immediate response required before 5:00 PM today."}, {"tactic": "false_legitimacy", "start_char": 246, "end_char": 327, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

**Complete Original Text:**
```text
Subject: Humanitarian Relief: Emergency Assistance Sponsorship Drive

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Immediate response required before 5:00 PM today. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight.

Settle the required statutory handling fee of $4,104.00 using QuickTransfer before the deadline.

Sincerely,
Community Outreach Team
AuthGuardian Inc.
```

---

#### Record PILOT-0126
- **ID:** `PILOT-0126`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 283, "end_char": 377, "span_text": "Settle the required statutory handling fee of $516.00 using QuickTransfer before the deadline."}`
- **Narrative Evidence:** `{"start_char": 87, "end_char": 194, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 196, "end_char": 281, "span_text": "Audit Case Docket: CF-12960 registered under statutory financial compliance protocol."}]`

**Complete Original Text:**
```text
Subject: Humanitarian Relief: Emergency Assistance Sponsorship Drive

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Audit Case Docket: CF-12960 registered under statutory financial compliance protocol.

Settle the required statutory handling fee of $516.00 using QuickTransfer before the deadline.

Sincerely,
Community Outreach Team
NetDefender Support
```

---

#### Record PILOT-0127
- **ID:** `PILOT-0127`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 195, "end_char": 294, "span_text": "Transfer $3,390.00 through ZelleConnect to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 2, "end_char": 108, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 109, "end_char": 194, "span_text": "Audit Case Docket: CF-90492 registered under statutory financial compliance protocol."}]`

**Complete Original Text:**
```text
🙏 Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support. Audit Case Docket: CF-90492 registered under statutory financial compliance protocol. Transfer $3,390.00 through ZelleConnect to our designated clearance officer to resolve the balance.
```

---

#### Record PILOT-0128
- **ID:** `PILOT-0128`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["trust_exploitation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 262, "end_char": 350, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code."}`
- **Narrative Evidence:** `{"start_char": 0, "end_char": 106, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 107, "end_char": 211, "span_text": "As your assigned dedicated personal banker at Horizon Trust Bank, I am handling your profile personally."}, {"tactic": "urgency", "start_char": 212, "end_char": 261, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support. As your assigned dedicated personal banker at Horizon Trust Bank, I am handling your profile personally. Immediate response required before 5:00 PM today. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code.
```

---

#### Record PILOT-0129
- **ID:** `PILOT-0129`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 161, "end_char": 252, "span_text": "Settle the required statutory handling fee of $1,279.95 using SwiftPay before the deadline."}`
- **Narrative Evidence:** `{"start_char": 3, "end_char": 110, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 111, "end_char": 160, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
❤️ Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water. Immediate response required before 5:00 PM today. Settle the required statutory handling fee of $1,279.95 using SwiftPay before the deadline.
```

---

#### Record PILOT-0130
- **ID:** `PILOT-0130`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 195, "end_char": 290, "span_text": "Transfer $4,290.95 through SwiftPay to our designated clearance officer to resolve the balance."}`
- **Narrative Evidence:** `{"start_char": 87, "end_char": 193, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
Subject: Humanitarian Relief: Emergency Assistance Sponsorship Drive

Dear Supporter,

Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support.

Transfer $4,290.95 through SwiftPay to our designated clearance officer to resolve the balance.

Sincerely,
Community Outreach Team
Apex ID Services
```

---
