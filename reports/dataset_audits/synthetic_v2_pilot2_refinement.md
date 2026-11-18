# Synthetic Financial Scam Dataset Refinement Report: Pilot 2 (130 Records)

**Dataset:** `data/raw/synthetic_v2_pilot2_130.csv`  
**Scope:** Final Qualitative Refinement Pilot (10 records per each of the 13 canonical `phishing_type` categories).  
**Evaluation Baseline:** Comparative analysis against `synthetic_v2_pilot_130.csv` and `synthetic_financial_scams_v2.csv`.  

---

## 1. Pilot 2 Distribution Summary

- **Total Records:** 130 (exactly 10 per subtype across 13 subtypes)
- **Primary Fraudulent Intent Representation:**
  - `induce_payment_or_transfer`: 59 records
  - `obtain_personal_or_financial_information`: 26 records
  - `obtain_credentials_or_codes`: 19 records
  - `gain_account_or_device_access`: 13 records
  - `induce_fraudulent_investment`: 13 records
- **Channel Representation:**
  - `email`: 51 records
  - `sms`: 43 records
  - `chat`: 25 records
  - `notification`: 11 records
- **Tactics Cardinalities:**
  - 1 tactics: 63 records
  - 2 tactics: 67 records

---

## 2. Quantitative & Qualitative Comparison: Pilot 1 vs. Pilot 2

| Dimension | Pilot 1 (Previous) | Pilot 2 (Revised Refinement) | Defect Eradication |
| :--- | :---: | :---: | :--- |
| **Narrative-Intent Coherence** | Disconnected pairings (e.g. romance customs story ending in crypto trading pool) | **100% Scenario-Paired Coherence**: Narrative premise directly dictates the requested action | Resolved: Romance medical emergencies ask for clinic wires; crypto investment narratives ask for crypto deposits |
| **Conversational Progression** | Skeptical victim abruptly complied without scammer explanation | **Believable Multi-Turn Exchange**: Scammer offers plausible excuse to skepticism before victim agrees | Resolved: Realistic progression (Scammer hook -> Victim doubt -> Scammer explanation -> Compliance) |
| **Safe Synthetic Entities** | Used functional-looking `.net`/`.com` domains and emails | **RFC 2606 Reserved `.example` Domains**: Safe, non-routable synthetic endpoints (`auth.apexbank.example`) | Resolved: Zero usable credentials, safe non-functional domains |
| **Scenario Internal Consistency** | Inconsistent destinations (e.g. fender bender asking for clinic liaison) | **100% Destination-Reason Alignment**: Fender benders pay towing drivers; clinic visits pay clinic desks | Resolved: Zero contradictory explanations |
| **Notification Length** | 29–34 words | **Concise Lockscreen Push Alerts (18–26 words)** | Resolved: Matches authentic mobile OS lockscreen display limits |
| **Span Offset Integrity** | 100% verified | **100% verified substring matches** | Preserved |

---

## 3. Complete Verbatim Inspection of All 130 Pilot 2 Records

### Subtype Group: `account_verification`

#### Record PILOT2-0001
- **ID:** `PILOT2-0001`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 200, "end_char": 341, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.pinnaclebank.example/login."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 134, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 135, "end_char": 199, "span_text": "Official notice from Pinnacle Bank Fraud Investigation Division."}]`

**Complete Original Text:**
```text
Urgent alert: We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL. Official notice from Pinnacle Bank Fraud Investigation Division. To secure your account and block this device, enter your online banking password and security PIN at https://auth.pinnaclebank.example/login.
```

---

#### Record PILOT2-0002
- **ID:** `PILOT2-0002`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 202, "end_char": 343, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.horizontrust.example/login."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 131, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Atlanta, GA."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 132, "end_char": 201, "span_text": "Official notice from Horizon Trust Bank Fraud Investigation Division."}]`

**Complete Original Text:**
```text
Important: We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Atlanta, GA. Official notice from Horizon Trust Bank Fraud Investigation Division. To secure your account and block this device, enter your online banking password and security PIN at https://auth.horizontrust.example/login.
```

---

#### Record PILOT2-0003
- **ID:** `PILOT2-0003`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["fear_or_threat", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 144, "end_char": 305, "span_text": "To verify you are the legitimate account holder, confirm your full Social Security number and primary debit card CVV at https://verify.apexbank.example/identity."}`
- **Narrative Evidence:** `{"start_char": 29, "end_char": 143, "span_text": "Your online profile requires mandatory annual identity re-certification under federal banking compliance protocol."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [Apex National Bank Alert] Your online profile requires mandatory annual identity re-certification under federal banking compliance protocol. To verify you are the legitimate account holder, confirm your full Social Security number and primary debit card CVV at https://verify.apexbank.example/identity.
```

---

#### Record PILOT2-0004
- **ID:** `PILOT2-0004`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 288, "end_char": 425, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.apexbank.example/login."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 213, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 215, "end_char": 286, "span_text": "Act within the next 60 minutes to prevent permanent account suspension."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-95320 - Verification Required

Attention Account Holder,

We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL.

Act within the next 60 minutes to prevent permanent account suspension.

To secure your account and block this device, enter your online banking password and security PIN at https://auth.apexbank.example/login.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0005
- **ID:** `PILOT2-0005`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 260, "end_char": 422, "span_text": "To verify you are the legitimate account holder, confirm your full Social Security number and primary debit card CVV at https://verify.summitfcu.example/identity."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 207, "span_text": "Your online profile requires mandatory annual identity re-certification under federal banking compliance protocol."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 209, "end_char": 258, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-54504 - Verification Required

Attention Account Holder,

Your online profile requires mandatory annual identity re-certification under federal banking compliance protocol.

Immediate response required before 5:00 PM today.

To verify you are the legitimate account holder, confirm your full Social Security number and primary debit card CVV at https://verify.summitfcu.example/identity.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0006
- **ID:** `PILOT2-0006`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 157, "end_char": 295, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.summitfcu.example/login."}`
- **Narrative Evidence:** `{"start_char": 38, "end_char": 156, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Miami, FL."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [Summit Federal Credit Union Alert] We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Miami, FL. To secure your account and block this device, enter your online banking password and security PIN at https://auth.summitfcu.example/login.
```

---

#### Record PILOT2-0007
- **ID:** `PILOT2-0007`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 197, "end_char": 338, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.pinnaclebank.example/login."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 131, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 132, "end_char": 196, "span_text": "Official notice from Pinnacle Bank Fraud Investigation Division."}]`

**Complete Original Text:**
```text
Important: We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL. Official notice from Pinnacle Bank Fraud Investigation Division. To secure your account and block this device, enter your online banking password and security PIN at https://auth.pinnaclebank.example/login.
```

---

#### Record PILOT2-0008
- **ID:** `PILOT2-0008`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 148, "end_char": 292, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.vanguardbancorp.example/login."}`
- **Narrative Evidence:** `{"start_char": 27, "end_char": 147, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Seattle, WA."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [Vanguard Bancorp Alert] We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Seattle, WA. To secure your account and block this device, enter your online banking password and security PIN at https://auth.vanguardbancorp.example/login.
```

---

#### Record PILOT2-0009
- **ID:** `PILOT2-0009`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 150, "end_char": 287, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.apexbank.example/login."}`
- **Narrative Evidence:** `{"start_char": 29, "end_char": 149, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [Apex National Bank Alert] We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Chicago, IL. To secure your account and block this device, enter your online banking password and security PIN at https://auth.apexbank.example/login.
```

---

#### Record PILOT2-0010
- **ID:** `PILOT2-0010`
- **Subtype (`phishing_type`):** `account_verification`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 287, "end_char": 424, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.apexbank.example/login."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 212, "span_text": "We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Dallas, TX."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 214, "end_char": 285, "span_text": "Act within the next 60 minutes to prevent permanent account suspension."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-74296 - Verification Required

Attention Account Holder,

We detected an unauthorized sign-in attempt to your checking profile from an unrecognized Chrome session in Dallas, TX.

Act within the next 60 minutes to prevent permanent account suspension.

To secure your account and block this device, enter your online banking password and security PIN at https://auth.apexbank.example/login.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

### Subtype Group: `card_transaction_alert`

#### Record PILOT2-0011
- **ID:** `PILOT2-0011`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 194, "end_char": 307, "span_text": "If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 121, "span_text": "A pending authorization of $1,171.00 at BestBuy Electronics #841 was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 122, "end_char": 193, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Urgent alert: A pending authorization of $1,171.00 at BestBuy Electronics #841 was flagged by automated fraud monitoring. Time-sensitive alert: immediate verification is required without delay. If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately.
```

---

#### Record PILOT2-0012
- **ID:** `PILOT2-0012`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 130, "end_char": 243, "span_text": "If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately."}`
- **Narrative Evidence:** `{"start_char": 29, "end_char": 129, "span_text": "A pending authorization of $4,391.00 at PrimeStore Online was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [Apex National Bank Alert] A pending authorization of $4,391.00 at PrimeStore Online was flagged by automated fraud monitoring. If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately.
```

---

#### Record PILOT2-0013
- **ID:** `PILOT2-0013`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 185, "end_char": 306, "span_text": "A temporary dispute processing deposit of $50.00 is required via QuickTransfer to process immediate transaction reversal."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 109, "span_text": "A disputed international retail transaction of $3,711.50 has triggered an automated card freeze."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 110, "end_char": 184, "span_text": "Resolve this pending matter within 2 hours of receiving this notification."}]`

**Complete Original Text:**
```text
Please note: A disputed international retail transaction of $3,711.50 has triggered an automated card freeze. Resolve this pending matter within 2 hours of receiving this notification. A temporary dispute processing deposit of $50.00 is required via QuickTransfer to process immediate transaction reversal.
```

---

#### Record PILOT2-0014
- **ID:** `PILOT2-0014`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 180, "end_char": 299, "span_text": "To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 101, "span_text": "An out-of-state ATM cash withdrawal attempt of $3,855.00 was intercepted in Chicago, IL."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 102, "end_char": 179, "span_text": "Issued by the Central Fraud and Loss Prevention Bureau of Apex National Bank."}]`

**Complete Original Text:**
```text
Please note: An out-of-state ATM cash withdrawal attempt of $3,855.00 was intercepted in Chicago, IL. Issued by the Central Fraud and Loss Prevention Bureau of Apex National Bank. To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code.
```

---

#### Record PILOT2-0015
- **ID:** `PILOT2-0015`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 192, "end_char": 305, "span_text": "If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 119, "span_text": "A pending authorization of $1,931.50 at PrimeStore Online was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 120, "end_char": 191, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
For your security: A pending authorization of $1,931.50 at PrimeStore Online was flagged by automated fraud monitoring. Time-sensitive alert: immediate verification is required without delay. If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately.
```

---

#### Record PILOT2-0016
- **ID:** `PILOT2-0016`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 178, "end_char": 297, "span_text": "To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 101, "span_text": "An out-of-state ATM cash withdrawal attempt of $4,621.00 was intercepted in Chicago, IL."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 102, "end_char": 177, "span_text": "Issued by the Central Fraud and Loss Prevention Bureau of Beacon Financial."}]`

**Complete Original Text:**
```text
Please note: An out-of-state ATM cash withdrawal attempt of $4,621.00 was intercepted in Chicago, IL. Issued by the Central Fraud and Loss Prevention Bureau of Beacon Financial. To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code.
```

---

#### Record PILOT2-0017
- **ID:** `PILOT2-0017`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["fear_or_threat", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 183, "end_char": 302, "span_text": "To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 104, "span_text": "An out-of-state ATM cash withdrawal attempt of $505.80 was intercepted in Dallas, TX."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 105, "end_char": 182, "span_text": "Issued by the Central Fraud and Loss Prevention Bureau of Horizon Trust Bank."}]`

**Complete Original Text:**
```text
For your security: An out-of-state ATM cash withdrawal attempt of $505.80 was intercepted in Dallas, TX. Issued by the Central Fraud and Loss Prevention Bureau of Horizon Trust Bank. To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code.
```

---

#### Record PILOT2-0018
- **ID:** `PILOT2-0018`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 339, "end_char": 455, "span_text": "A temporary dispute processing deposit of $50.00 is required via CashFlow to process immediate transaction reversal."}`
- **Narrative Evidence:** `{"start_char": 35, "end_char": 129, "span_text": "A disputed international retail transaction of $256.50 has triggered an automated card freeze."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 264, "end_char": 338, "span_text": "Resolve this pending matter within 2 hours of receiving this notification."}]`

**Complete Original Text:**
```text
[10:14 AM] Fraud_Prevention_Agent: A disputed international retail transaction of $256.50 has triggered an automated card freeze.
[10:15 AM] You: Wait, I didn't authorize this! What card or account was used?
[10:16 AM] Fraud_Prevention_Agent: Card ending in 4102. Resolve this pending matter within 2 hours of receiving this notification. A temporary dispute processing deposit of $50.00 is required via CashFlow to process immediate transaction reversal.
```

---

#### Record PILOT2-0019
- **ID:** `PILOT2-0019`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 118, "end_char": 237, "span_text": "To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code."}`
- **Narrative Evidence:** `{"start_char": 29, "end_char": 117, "span_text": "An out-of-state ATM cash withdrawal attempt of $1,472.50 was intercepted in Chicago, IL."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [Horizon Trust Bank Alert] An out-of-state ATM cash withdrawal attempt of $1,472.50 was intercepted in Chicago, IL. To dispute this unauthorized charge, please confirm your 16-digit debit card number and 3-digit card verification code.
```

---

#### Record PILOT2-0020
- **ID:** `PILOT2-0020`
- **Subtype (`phishing_type`):** `card_transaction_alert`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 188, "end_char": 301, "span_text": "If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 115, "span_text": "A pending authorization of $4,712.00 at Apple Store Manhattan was flagged by automated fraud monitoring."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 116, "end_char": 187, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Important: A pending authorization of $4,712.00 at Apple Store Manhattan was flagged by automated fraud monitoring. Time-sensitive alert: immediate verification is required without delay. If unauthorized, reply with the 6-digit confirmation passcode sent to your phone to void this charge immediately.
```

---

### Subtype Group: `refund_chargeback`

#### Record PILOT2-0021
- **ID:** `PILOT2-0021`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 289, "end_char": 441, "span_text": "Our accounts desk accidentally deposited an excess balance of $1,500 into your account; please return the difference via electronic wire transfer today."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 208, "span_text": "An automated billing error resulted in an overcharge of $1,251.80 for your annual NetDefender Support subscription."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 210, "end_char": 287, "span_text": "Statutory validation reference: CF-46335 filed with merchant claims registry."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-46335 - Verification Required

Attention Account Holder,

An automated billing error resulted in an overcharge of $1,251.80 for your annual NetDefender Support subscription.

Statutory validation reference: CF-46335 filed with merchant claims registry.

Our accounts desk accidentally deposited an excess balance of $1,500 into your account; please return the difference via electronic wire transfer today.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0022
- **ID:** `PILOT2-0022`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 423, "span_text": "Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 197, "span_text": "Your disputed chargeback for $3,700.00 with PrimeStore Online requires technical receipt reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 199, "end_char": 290, "span_text": "You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-17482 - Verification Required

Attention Account Holder,

Your disputed chargeback for $3,700.00 with PrimeStore Online requires technical receipt reconciliation.

You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture.

Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0023
- **ID:** `PILOT2-0023`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["false_legitimacy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 375, "end_char": 506, "span_text": "Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 145, "span_text": "Your disputed chargeback for $1,446.00 with BestBuy Electronics #841 requires technical receipt reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 283, "end_char": 374, "span_text": "You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Your disputed chargeback for $1,446.00 with BestBuy Electronics #841 requires technical receipt reconciliation.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-33299. You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture. Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly.
```

---

#### Record PILOT2-0024
- **ID:** `PILOT2-0024`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["urgency", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 294, "end_char": 425, "span_text": "Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 199, "span_text": "Your disputed chargeback for $497.50 with Apple Store Manhattan requires technical receipt reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 201, "end_char": 292, "span_text": "You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-41154 - Verification Required

Attention Account Holder,

Your disputed chargeback for $497.50 with Apple Store Manhattan requires technical receipt reconciliation.

You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture.

Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT2-0025
- **ID:** `PILOT2-0025`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["false_legitimacy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 423, "span_text": "Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 197, "span_text": "Your disputed chargeback for $3,056.80 with PrimeStore Online requires technical receipt reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 199, "end_char": 290, "span_text": "You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-78768 - Verification Required

Attention Account Holder,

Your disputed chargeback for $3,056.80 with PrimeStore Online requires technical receipt reconciliation.

You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture.

Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT2-0026
- **ID:** `PILOT2-0026`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 366, "end_char": 518, "span_text": "Our accounts desk accidentally deposited an excess balance of $1,500 into your account; please return the difference via electronic wire transfer today."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 150, "span_text": "An automated billing error resulted in an overcharge of $2,749.50 for your annual CloudShield Security subscription."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 288, "end_char": 365, "span_text": "Statutory validation reference: CF-91457 filed with merchant claims registry."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: An automated billing error resulted in an overcharge of $2,749.50 for your annual CloudShield Security subscription.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-91457. Statutory validation reference: CF-91457 filed with merchant claims registry. Our accounts desk accidentally deposited an excess balance of $1,500 into your account; please return the difference via electronic wire transfer today.
```

---

#### Record PILOT2-0027
- **ID:** `PILOT2-0027`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 202, "end_char": 354, "span_text": "Our accounts desk accidentally deposited an excess balance of $1,500 into your account; please return the difference via electronic wire transfer today."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 123, "span_text": "An automated billing error resulted in an overcharge of $2,884.80 for your annual Apex ID Services subscription."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 124, "end_char": 201, "span_text": "Statutory validation reference: CF-53145 filed with merchant claims registry."}]`

**Complete Original Text:**
```text
Important: An automated billing error resulted in an overcharge of $2,884.80 for your annual Apex ID Services subscription. Statutory validation reference: CF-53145 filed with merchant claims registry. Our accounts desk accidentally deposited an excess balance of $1,500 into your account; please return the difference via electronic wire transfer today.
```

---

#### Record PILOT2-0028
- **ID:** `PILOT2-0028`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 279, "end_char": 429, "span_text": "To deposit your full refund of $1,605.80, please provide your checking account number and bank routing digits at https://refunds.apexid.example/claim."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 188, "span_text": "Your travel booking cancellation credit of $1,605.80 has been approved for direct disbursement."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 190, "end_char": 277, "span_text": "Claim your guaranteed refund allocation of $1,605.80 credited directly to your profile."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-86593 - Verification Required

Attention Account Holder,

Your travel booking cancellation credit of $1,605.80 has been approved for direct disbursement.

Claim your guaranteed refund allocation of $1,605.80 credited directly to your profile.

To deposit your full refund of $1,605.80, please provide your checking account number and bank routing digits at https://refunds.apexid.example/claim.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0029
- **ID:** `PILOT2-0029`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 217, "end_char": 348, "span_text": "Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 124, "span_text": "Your disputed chargeback for $1,930.80 with BestBuy Electronics #841 requires technical receipt reconciliation."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 125, "end_char": 216, "span_text": "You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Please note: Your disputed chargeback for $1,930.80 with BestBuy Electronics #841 requires technical receipt reconciliation. You must complete this mandatory requirement within 24 hours to avoid automatic forfeiture. Install TeamViewer QuickSupport so our billing representative can connect to your desktop and process your refund voucher directly.
```

---

#### Record PILOT2-0030
- **ID:** `PILOT2-0030`
- **Subtype (`phishing_type`):** `refund_chargeback`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 351, "end_char": 499, "span_text": "To deposit your full refund of $380.00, please provide your checking account number and bank routing digits at https://refunds.apexid.example/claim."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 127, "span_text": "Your travel booking cancellation credit of $380.00 has been approved for direct disbursement."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 265, "end_char": 350, "span_text": "Claim your guaranteed refund allocation of $380.00 credited directly to your profile."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Your travel booking cancellation credit of $380.00 has been approved for direct disbursement.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-44092. Claim your guaranteed refund allocation of $380.00 credited directly to your profile. To deposit your full refund of $380.00, please provide your checking account number and bank routing digits at https://refunds.apexid.example/claim.
```

---

### Subtype Group: `invoice_payment_request`

#### Record PILOT2-0031
- **ID:** `PILOT2-0031`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 254, "end_char": 352, "span_text": "Please provide your corporate credit card details and billing address to settle invoice #CF-67724."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 194, "span_text": "Annual IT infrastructure maintenance statement #CF-67724 totaling $225.00 is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 196, "end_char": 252, "span_text": "Official dispute tracking registration number: CF-67724."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-67724 - Verification Required

Attention Account Holder,

Annual IT infrastructure maintenance statement #CF-67724 totaling $225.00 is past due for settlement.

Official dispute tracking registration number: CF-67724.

Please provide your corporate credit card details and billing address to settle invoice #CF-67724.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT2-0032
- **ID:** `PILOT2-0032`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["false_legitimacy", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 172, "end_char": 270, "span_text": "Please provide your corporate credit card details and billing address to settle invoice #CF-92301."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 114, "span_text": "Annual IT infrastructure maintenance statement #CF-92301 totaling $2,779.50 is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 115, "end_char": 171, "span_text": "Official dispute tracking registration number: CF-92301."}]`

**Complete Original Text:**
```text
Important: Annual IT infrastructure maintenance statement #CF-92301 totaling $2,779.50 is past due for settlement. Official dispute tracking registration number: CF-92301. Please provide your corporate credit card details and billing address to settle invoice #CF-92301.
```

---

#### Record PILOT2-0033
- **ID:** `PILOT2-0033`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 322, "end_char": 427, "span_text": "Please remit payment of $3,783.00 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 243, "span_text": "Regarding invoice statement INV-8921 for $3,783.00 from SecureVault Tech, our corporate banking coordinates have been updated due to our fiscal audit."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 245, "end_char": 320, "span_text": "Immediate response required before 5:00 PM today to prevent late penalties."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-49450 - Verification Required

Attention Account Holder,

Regarding invoice statement INV-8921 for $3,783.00 from SecureVault Tech, our corporate banking coordinates have been updated due to our fiscal audit.

Immediate response required before 5:00 PM today to prevent late penalties.

Please remit payment of $3,783.00 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT2-0034
- **ID:** `PILOT2-0034`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 322, "end_char": 427, "span_text": "Please remit payment of $2,890.80 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 243, "span_text": "Regarding invoice statement INV-8921 for $2,890.80 from Apex ID Services, our corporate banking coordinates have been updated due to our fiscal audit."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 245, "end_char": 320, "span_text": "Immediate response required before 5:00 PM today to prevent late penalties."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-73069 - Verification Required

Attention Account Holder,

Regarding invoice statement INV-8921 for $2,890.80 from Apex ID Services, our corporate banking coordinates have been updated due to our fiscal audit.

Immediate response required before 5:00 PM today to prevent late penalties.

Please remit payment of $2,890.80 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT2-0035
- **ID:** `PILOT2-0035`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["fear_or_threat", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 172, "end_char": 270, "span_text": "Please provide your corporate credit card details and billing address to settle invoice #CF-83582."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 114, "span_text": "Annual IT infrastructure maintenance statement #CF-83582 totaling $3,612.80 is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 115, "end_char": 171, "span_text": "Official dispute tracking registration number: CF-83582."}]`

**Complete Original Text:**
```text
Important: Annual IT infrastructure maintenance statement #CF-83582 totaling $3,612.80 is past due for settlement. Official dispute tracking registration number: CF-83582. Please provide your corporate credit card details and billing address to settle invoice #CF-83582.
```

---

#### Record PILOT2-0036
- **ID:** `PILOT2-0036`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 322, "end_char": 427, "span_text": "Please remit payment of $1,225.80 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 243, "span_text": "Regarding invoice statement INV-8921 for $1,225.80 from SecureVault Tech, our corporate banking coordinates have been updated due to our fiscal audit."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 245, "end_char": 320, "span_text": "Immediate response required before 5:00 PM today to prevent late penalties."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-82008 - Verification Required

Attention Account Holder,

Regarding invoice statement INV-8921 for $1,225.80 from SecureVault Tech, our corporate banking coordinates have been updated due to our fiscal audit.

Immediate response required before 5:00 PM today to prevent late penalties.

Please remit payment of $1,225.80 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT2-0037
- **ID:** `PILOT2-0037`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 256, "end_char": 354, "span_text": "Please provide your corporate credit card details and billing address to settle invoice #CF-71598."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 196, "span_text": "Annual IT infrastructure maintenance statement #CF-71598 totaling $2,861.00 is past due for settlement."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 198, "end_char": 254, "span_text": "Official dispute tracking registration number: CF-71598."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-71598 - Verification Required

Attention Account Holder,

Annual IT infrastructure maintenance statement #CF-71598 totaling $2,861.00 is past due for settlement.

Official dispute tracking registration number: CF-71598.

Please provide your corporate credit card details and billing address to settle invoice #CF-71598.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT2-0038
- **ID:** `PILOT2-0038`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 182, "end_char": 337, "span_text": "Please log into our updated vendor billing portal at https://billing.cloudshield.example/login with your administrative credentials to approve the invoice."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 108, "span_text": "Your vendor portal service contract #CF-17276 requires immediate administrative authorization."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 109, "end_char": 181, "span_text": "Failure to act immediately will result in permanent service termination."}]`

**Complete Original Text:**
```text
Urgent alert: Your vendor portal service contract #CF-17276 requires immediate administrative authorization. Failure to act immediately will result in permanent service termination. Please log into our updated vendor billing portal at https://billing.cloudshield.example/login with your administrative credentials to approve the invoice.
```

---

#### Record PILOT2-0039
- **ID:** `PILOT2-0039`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 263, "end_char": 418, "span_text": "Please log into our updated vendor billing portal at https://billing.cloudshield.example/login with your administrative credentials to approve the invoice."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 187, "span_text": "Your vendor portal service contract #CF-33992 requires immediate administrative authorization."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 189, "end_char": 261, "span_text": "Failure to act immediately will result in permanent service termination."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-33992 - Verification Required

Attention Account Holder,

Your vendor portal service contract #CF-33992 requires immediate administrative authorization.

Failure to act immediately will result in permanent service termination.

Please log into our updated vendor billing portal at https://billing.cloudshield.example/login with your administrative credentials to approve the invoice.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT2-0040
- **ID:** `PILOT2-0040`
- **Subtype (`phishing_type`):** `invoice_payment_request`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 322, "end_char": 427, "span_text": "Please remit payment of $1,804.00 via wire transfer to our settlement escrow routing account immediately."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 243, "span_text": "Regarding invoice statement INV-8921 for $1,804.00 from SecureVault Tech, our corporate banking coordinates have been updated due to our fiscal audit."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 245, "end_char": 320, "span_text": "Immediate response required before 5:00 PM today to prevent late penalties."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-89607 - Verification Required

Attention Account Holder,

Regarding invoice statement INV-8921 for $1,804.00 from SecureVault Tech, our corporate banking coordinates have been updated due to our fiscal audit.

Immediate response required before 5:00 PM today to prevent late penalties.

Please remit payment of $1,804.00 via wire transfer to our settlement escrow routing account immediately.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

### Subtype Group: `loan_offer`

#### Record PILOT2-0041
- **ID:** `PILOT2-0041`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 200, "end_char": 312, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($4,324.80) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 116, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 117, "end_char": 199, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
For your security: You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate. This reservation window is strictly limited to the first ten verified respondents. Pay the mandatory 2% loan origination and documentation fee ($4,324.80) via wire transfer to release your funds.
```

---

#### Record PILOT2-0042
- **ID:** `PILOT2-0042`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 276, "end_char": 388, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($2,392.80) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 190, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 192, "end_char": 274, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-82539 - Verification Required

Attention Account Holder,

You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate.

This reservation window is strictly limited to the first ten verified respondents.

Pay the mandatory 2% loan origination and documentation fee ($2,392.80) via wire transfer to release your funds.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT2-0043
- **ID:** `PILOT2-0043`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 276, "end_char": 388, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($3,284.50) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 190, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 192, "end_char": 274, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-15761 - Verification Required

Attention Account Holder,

You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate.

This reservation window is strictly limited to the first ten verified respondents.

Pay the mandatory 2% loan origination and documentation fee ($3,284.50) via wire transfer to release your funds.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0044
- **ID:** `PILOT2-0044`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 277, "end_char": 453, "span_text": "To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.summitfcu.example/apply."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 196, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 198, "end_char": 275, "span_text": "Secure an immediate personal advance disbursement of $35,000 upon enrollment."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-65271 - Verification Required

Attention Account Holder,

Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.

Secure an immediate personal advance disbursement of $35,000 upon enrollment.

To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.summitfcu.example/apply.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0045
- **ID:** `PILOT2-0045`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 276, "end_char": 388, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($3,203.50) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 190, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 192, "end_char": 274, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-84544 - Verification Required

Attention Account Holder,

You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate.

This reservation window is strictly limited to the first ten verified respondents.

Pay the mandatory 2% loan origination and documentation fee ($3,203.50) via wire transfer to release your funds.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT2-0046
- **ID:** `PILOT2-0046`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 353, "end_char": 529, "span_text": "To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.summitfcu.example/apply."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 137, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 275, "end_char": 352, "span_text": "Secure an immediate personal advance disbursement of $35,000 upon enrollment."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-82236. Secure an immediate personal advance disbursement of $35,000 upon enrollment. To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.summitfcu.example/apply.
```

---

#### Record PILOT2-0047
- **ID:** `PILOT2-0047`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 201, "end_char": 380, "span_text": "To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.pinnaclebank.example/apply."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 122, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 123, "end_char": 200, "span_text": "Secure an immediate personal advance disbursement of $35,000 upon enrollment."}]`

**Complete Original Text:**
```text
For your security: Your application for an emergency debt consolidation credit line of $35,000 has been formally approved. Secure an immediate personal advance disbursement of $35,000 upon enrollment. To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.pinnaclebank.example/apply.
```

---

#### Record PILOT2-0048
- **ID:** `PILOT2-0048`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 192, "end_char": 304, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($4,101.50) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 108, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 109, "end_char": 191, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Important: You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate. This reservation window is strictly limited to the first ten verified respondents. Pay the mandatory 2% loan origination and documentation fee ($4,101.50) via wire transfer to release your funds.
```

---

#### Record PILOT2-0049
- **ID:** `PILOT2-0049`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 277, "end_char": 453, "span_text": "To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.beaconfin.example/apply."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 196, "span_text": "Your application for an emergency debt consolidation credit line of $35,000 has been formally approved."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 198, "end_char": 275, "span_text": "Secure an immediate personal advance disbursement of $35,000 upon enrollment."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-85147 - Verification Required

Attention Account Holder,

Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.

Secure an immediate personal advance disbursement of $35,000 upon enrollment.

To finalize direct deposit disbursement of your loan, submit your full Social Security number, monthly income, and bank routing digits at https://loans.beaconfin.example/apply.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

#### Record PILOT2-0050
- **ID:** `PILOT2-0050`
- **Subtype (`phishing_type`):** `loan_offer`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 352, "end_char": 462, "span_text": "Pay the mandatory 2% loan origination and documentation fee ($673.80) via wire transfer to release your funds."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 131, "span_text": "You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 269, "end_char": 351, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-25006. This reservation window is strictly limited to the first ten verified respondents. Pay the mandatory 2% loan origination and documentation fee ($673.80) via wire transfer to release your funds.
```

---

### Subtype Group: `investment_crypto`

#### Record PILOT2-0051
- **ID:** `PILOT2-0051`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 283, "end_char": 384, "span_text": "Deposit an initial investment of $201.50 into the NovaChain Markets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 201, "span_text": "Our proprietary AI algorithmic trading engine on NovaChain Markets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 203, "end_char": 281, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-71048 - Verification Required

Attention Account Holder,

Our proprietary AI algorithmic trading engine on NovaChain Markets achieved an audited 24.5% monthly return.

Secure your daily automated profit distribution averaging 18.5% weekly return.

Deposit an initial investment of $201.50 into the NovaChain Markets automated arbitrage trading pool.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT2-0052
- **ID:** `PILOT2-0052`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["reward_or_benefit", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 390, "span_text": "Deposit an initial investment of $1,800.50 into the CryptoSphere Assets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 203, "span_text": "Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 205, "end_char": 283, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-27043 - Verification Required

Attention Account Holder,

Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return.

Secure your daily automated profit distribution averaging 18.5% weekly return.

Deposit an initial investment of $1,800.50 into the CryptoSphere Assets automated arbitrage trading pool.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0053
- **ID:** `PILOT2-0053`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["scarcity", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 134, "end_char": 237, "span_text": "Deposit an initial investment of $2,671.80 into the EtherPeak Trading automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 133, "span_text": "Our proprietary AI algorithmic trading engine on EtherPeak Trading achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🔔 [QuickTransfer Notice] Our proprietary AI algorithmic trading engine on EtherPeak Trading achieved an audited 24.5% monthly return. Deposit an initial investment of $2,671.80 into the EtherPeak Trading automated arbitrage trading pool.
```

---

#### Record PILOT2-0054
- **ID:** `PILOT2-0054`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["secrecy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 390, "span_text": "Deposit an initial investment of $2,055.80 into the CryptoSphere Assets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 203, "span_text": "Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 205, "end_char": 283, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-87392 - Verification Required

Attention Account Holder,

Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return.

Secure your daily automated profit distribution averaging 18.5% weekly return.

Deposit an initial investment of $2,055.80 into the CryptoSphere Assets automated arbitrage trading pool.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT2-0055
- **ID:** `PILOT2-0055`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 361, "end_char": 466, "span_text": "Deposit an initial investment of $4,208.00 into the CryptoSphere Assets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 144, "span_text": "Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 282, "end_char": 360, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-73605. Secure your daily automated profit distribution averaging 18.5% weekly return. Deposit an initial investment of $4,208.00 into the CryptoSphere Assets automated arbitrage trading pool.
```

---

#### Record PILOT2-0056
- **ID:** `PILOT2-0056`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["secrecy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 367, "end_char": 511, "span_text": "Download and install our specialized algorithmic trading client APK from https://trade.cryptosphere.example/app to initiate automated execution."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 141, "span_text": "An institutional arbitrage contract on CryptoSphere Assets is now available for direct terminal connection."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 279, "end_char": 366, "span_text": "Keep this private settlement between us until the documentation is officially archived."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: An institutional arbitrage contract on CryptoSphere Assets is now available for direct terminal connection.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-45082. Keep this private settlement between us until the documentation is officially archived. Download and install our specialized algorithmic trading client APK from https://trade.cryptosphere.example/app to initiate automated execution.
```

---

#### Record PILOT2-0057
- **ID:** `PILOT2-0057`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 201, "end_char": 306, "span_text": "Deposit an initial investment of $4,263.80 into the CryptoSphere Assets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 121, "span_text": "Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 122, "end_char": 200, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
Important: Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return. Secure your daily automated profit distribution averaging 18.5% weekly return. Deposit an initial investment of $4,263.80 into the CryptoSphere Assets automated arbitrage trading pool.
```

---

#### Record PILOT2-0058
- **ID:** `PILOT2-0058`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 358, "end_char": 460, "span_text": "Deposit an initial investment of $4,692.00 into the BitCrest Capital automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 141, "span_text": "Our proprietary AI algorithmic trading engine on BitCrest Capital achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 279, "end_char": 357, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Our proprietary AI algorithmic trading engine on BitCrest Capital achieved an audited 24.5% monthly return.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-84384. Secure your daily automated profit distribution averaging 18.5% weekly return. Deposit an initial investment of $4,692.00 into the BitCrest Capital automated arbitrage trading pool.
```

---

#### Record PILOT2-0059
- **ID:** `PILOT2-0059`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 390, "span_text": "Deposit an initial investment of $4,132.50 into the CryptoSphere Assets automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 203, "span_text": "Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 205, "end_char": 283, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-43946 - Verification Required

Attention Account Holder,

Our proprietary AI algorithmic trading engine on CryptoSphere Assets achieved an audited 24.5% monthly return.

Secure your daily automated profit distribution averaging 18.5% weekly return.

Deposit an initial investment of $4,132.50 into the CryptoSphere Assets automated arbitrage trading pool.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0060
- **ID:** `PILOT2-0060`
- **Subtype (`phishing_type`):** `investment_crypto`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 198, "end_char": 298, "span_text": "Deposit an initial investment of $201.50 into the BitCrest Capital automated arbitrage trading pool."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 118, "span_text": "Our proprietary AI algorithmic trading engine on BitCrest Capital achieved an audited 24.5% monthly return."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 119, "end_char": 197, "span_text": "Secure your daily automated profit distribution averaging 18.5% weekly return."}]`

**Complete Original Text:**
```text
Important: Our proprietary AI algorithmic trading engine on BitCrest Capital achieved an audited 24.5% monthly return. Secure your daily automated profit distribution averaging 18.5% weekly return. Deposit an initial investment of $201.50 into the BitCrest Capital automated arbitrage trading pool.
```

---

### Subtype Group: `prize_reward`

#### Record PILOT2-0061
- **ID:** `PILOT2-0061`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["scarcity", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 189, "end_char": 307, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 105, "span_text": "You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 106, "end_char": 188, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Important: You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing. This reservation window is strictly limited to the first ten verified respondents. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly.
```

---

#### Record PILOT2-0062
- **ID:** `PILOT2-0062`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 189, "end_char": 307, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 105, "span_text": "You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 106, "end_char": 188, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Important: You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing. This reservation window is strictly limited to the first ten verified respondents. Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly.
```

---

#### Record PILOT2-0063
- **ID:** `PILOT2-0063`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 120, "end_char": 214, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via CashFlow to release your prize."}`
- **Narrative Evidence:** `{"start_char": 20, "end_char": 119, "span_text": "Official winner notification: your entry ticket was awarded the $2,774.80 retail promotional grant."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🔔 [CashFlow Notice] Official winner notification: your entry ticket was awarded the $2,774.80 retail promotional grant. Pay the mandatory $125 delivery and insurance handling fee via CashFlow to release your prize.
```

---

#### Record PILOT2-0064
- **ID:** `PILOT2-0064`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 125, "end_char": 224, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via QuickTransfer to release your prize."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 124, "span_text": "Official winner notification: your entry ticket was awarded the $1,542.80 retail promotional grant."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🔔 [QuickTransfer Notice] Official winner notification: your entry ticket was awarded the $1,542.80 retail promotional grant. Pay the mandatory $125 delivery and insurance handling fee via QuickTransfer to release your prize.
```

---

#### Record PILOT2-0065
- **ID:** `PILOT2-0065`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 189, "end_char": 324, "span_text": "Enter your customer rewards portal password and security PIN at https://portal.applestrore-support.example/login to claim your voucher."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 112, "span_text": "You have an unclaimed merchandise voucher and cash bonus totaling $1,655.00 awaiting verification."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 113, "end_char": 188, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}]`

**Complete Original Text:**
```text
Urgent alert: You have an unclaimed merchandise voucher and cash bonus totaling $1,655.00 awaiting verification. Act within the next 60 minutes to prevent irreversible account restriction. Enter your customer rewards portal password and security PIN at https://portal.applestrore-support.example/login to claim your voucher.
```

---

#### Record PILOT2-0066
- **ID:** `PILOT2-0066`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 181, "end_char": 275, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via CashFlow to release your prize."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 110, "span_text": "Official winner notification: your entry ticket was awarded the $2,536.80 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 111, "end_char": 180, "span_text": "Unlock your confirmed prize distribution voucher valued at $2,536.80."}]`

**Complete Original Text:**
```text
Important: Official winner notification: your entry ticket was awarded the $2,536.80 retail promotional grant. Unlock your confirmed prize distribution voucher valued at $2,536.80. Pay the mandatory $125 delivery and insurance handling fee via CashFlow to release your prize.
```

---

#### Record PILOT2-0067
- **ID:** `PILOT2-0067`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 189, "end_char": 287, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via ZelleConnect to release your prize."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 118, "span_text": "Official winner notification: your entry ticket was awarded the $2,123.50 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 119, "end_char": 188, "span_text": "Unlock your confirmed prize distribution voucher valued at $2,123.50."}]`

**Complete Original Text:**
```text
For your security: Official winner notification: your entry ticket was awarded the $2,123.50 retail promotional grant. Unlock your confirmed prize distribution voucher valued at $2,123.50. Pay the mandatory $125 delivery and insurance handling fee via ZelleConnect to release your prize.
```

---

#### Record PILOT2-0068
- **ID:** `PILOT2-0068`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 273, "end_char": 391, "span_text": "Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 187, "span_text": "You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 189, "end_char": 271, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-44850 - Verification Required

Attention Account Holder,

You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing.

This reservation window is strictly limited to the first ten verified respondents.

Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code to credit the reward directly.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0069
- **ID:** `PILOT2-0069`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 189, "end_char": 283, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via SwiftPay to release your prize."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 118, "span_text": "Official winner notification: your entry ticket was awarded the $1,256.00 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 119, "end_char": 188, "span_text": "Unlock your confirmed prize distribution voucher valued at $1,256.00."}]`

**Complete Original Text:**
```text
For your security: Official winner notification: your entry ticket was awarded the $1,256.00 retail promotional grant. Unlock your confirmed prize distribution voucher valued at $1,256.00. Pay the mandatory $125 delivery and insurance handling fee via SwiftPay to release your prize.
```

---

#### Record PILOT2-0070
- **ID:** `PILOT2-0070`
- **Subtype (`phishing_type`):** `prize_reward`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 265, "end_char": 364, "span_text": "Pay the mandatory $125 delivery and insurance handling fee via QuickTransfer to release your prize."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 192, "span_text": "Official winner notification: your entry ticket was awarded the $4,016.00 retail promotional grant."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 194, "end_char": 263, "span_text": "Unlock your confirmed prize distribution voucher valued at $4,016.00."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-30449 - Verification Required

Attention Account Holder,

Official winner notification: your entry ticket was awarded the $4,016.00 retail promotional grant.

Unlock your confirmed prize distribution voucher valued at $4,016.00.

Pay the mandatory $125 delivery and insurance handling fee via QuickTransfer to release your prize.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

### Subtype Group: `tax_payment`

#### Record PILOT2-0071
- **ID:** `PILOT2-0071`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 303, "end_char": 435, "span_text": "Enter your statutory filing credentials and security PIN at https://portal.tax-compliance.example/verify to resolve this deficiency."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 203, "span_text": "A discrepancy in your annual wage withholding report requires immediate statutory reconciliation of $2,327.80."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 205, "end_char": 301, "span_text": "You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-61941 - Verification Required

Attention Account Holder,

A discrepancy in your annual wage withholding report requires immediate statutory reconciliation of $2,327.80.

You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture.

Enter your statutory filing credentials and security PIN at https://portal.tax-compliance.example/verify to resolve this deficiency.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0072
- **ID:** `PILOT2-0072`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 208, "end_char": 329, "span_text": "Remit payment of $2,655.80 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 112, "span_text": "Statutory audit docket #CF-65516 identified an underreported income tax liability totaling $2,655.80."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 113, "end_char": 207, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Important: Statutory audit docket #CF-65516 identified an underreported income tax liability totaling $2,655.80. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. Remit payment of $2,655.80 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

#### Record PILOT2-0073
- **ID:** `PILOT2-0073`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 413, "span_text": "Remit payment of $4,605.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 194, "span_text": "Statutory audit docket #CF-88983 identified an underreported income tax liability totaling $4,605.50."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 196, "end_char": 290, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-88983 - Verification Required

Attention Account Holder,

Statutory audit docket #CF-88983 identified an underreported income tax liability totaling $4,605.50.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.

Remit payment of $4,605.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0074
- **ID:** `PILOT2-0074`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 122, "end_char": 243, "span_text": "Remit payment of $2,114.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 20, "end_char": 121, "span_text": "Statutory audit docket #CF-25022 identified an underreported income tax liability totaling $2,114.50."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🚨 [CashFlow Notice] Statutory audit docket #CF-25022 identified an underreported income tax liability totaling $2,114.50. Remit payment of $2,114.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

#### Record PILOT2-0075
- **ID:** `PILOT2-0075`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 209, "end_char": 328, "span_text": "Remit payment of $354.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 113, "span_text": "Statutory audit docket #CF-55713 identified an underreported income tax liability totaling $354.00."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 114, "end_char": 208, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Urgent alert: Statutory audit docket #CF-55713 identified an underreported income tax liability totaling $354.00. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. Remit payment of $354.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

#### Record PILOT2-0076
- **ID:** `PILOT2-0076`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 210, "end_char": 331, "span_text": "Remit payment of $1,365.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 114, "span_text": "Statutory audit docket #CF-82807 identified an underreported income tax liability totaling $1,365.00."}`
- **Tactics Evidence:** `[{"tactic": "fear_or_threat", "start_char": 115, "end_char": 209, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Please note: Statutory audit docket #CF-82807 identified an underreported income tax liability totaling $1,365.00. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. Remit payment of $1,365.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

#### Record PILOT2-0077
- **ID:** `PILOT2-0077`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 413, "span_text": "Remit payment of $3,628.80 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 194, "span_text": "Statutory audit docket #CF-26896 identified an underreported income tax liability totaling $3,628.80."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 196, "end_char": 290, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-26896 - Verification Required

Attention Account Holder,

Statutory audit docket #CF-26896 identified an underreported income tax liability totaling $3,628.80.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.

Remit payment of $3,628.80 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0078
- **ID:** `PILOT2-0078`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 413, "span_text": "Remit payment of $4,103.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 194, "span_text": "Statutory audit docket #CF-67872 identified an underreported income tax liability totaling $4,103.50."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 196, "end_char": 290, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-67872 - Verification Required

Attention Account Holder,

Statutory audit docket #CF-67872 identified an underreported income tax liability totaling $4,103.50.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.

Remit payment of $4,103.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT2-0079
- **ID:** `PILOT2-0079`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 413, "span_text": "Remit payment of $2,843.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 194, "span_text": "Statutory audit docket #CF-90301 identified an underreported income tax liability totaling $2,843.50."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 196, "end_char": 290, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-90301 - Verification Required

Attention Account Holder,

Statutory audit docket #CF-90301 identified an underreported income tax liability totaling $2,843.50.

Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.

Remit payment of $2,843.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0080
- **ID:** `PILOT2-0080`
- **Subtype (`phishing_type`):** `tax_payment`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 208, "end_char": 329, "span_text": "Remit payment of $3,446.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 112, "span_text": "Statutory audit docket #CF-24463 identified an underreported income tax liability totaling $3,446.50."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 113, "end_char": 207, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

**Complete Original Text:**
```text
Important: Statutory audit docket #CF-24463 identified an underreported income tax liability totaling $3,446.50. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. Remit payment of $3,446.50 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.
```

---

### Subtype Group: `job_task_commission`

#### Record PILOT2-0081
- **ID:** `PILOT2-0081`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `notification`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 131, "end_char": 313, "span_text": "Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.cloudshield.example/payroll."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 130, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[]`

**Complete Original Text:**
```text
🔔 [QuickTransfer Notice] Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily. Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.cloudshield.example/payroll.
```

---

#### Record PILOT2-0082
- **ID:** `PILOT2-0082`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 204, "end_char": 313, "span_text": "Recharge your work platform account with $200 USDT through PayLink Mobile to unlock the next task commission."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 119, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 120, "end_char": 203, "span_text": "Earn daily automated commission distributions averaging $300 daily upon onboarding."}]`

**Complete Original Text:**
```text
For your security: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations. Earn daily automated commission distributions averaging $300 daily upon onboarding. Recharge your work platform account with $200 USDT through PayLink Mobile to unlock the next task commission.
```

---

#### Record PILOT2-0083
- **ID:** `PILOT2-0083`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["reward_or_benefit", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 474, "span_text": "Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.netdefender.example/payroll."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 198, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 200, "end_char": 290, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-91822 - Verification Required

Attention Account Holder,

Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily.

Only 2 participant allocations remain available before registration is permanently closed.

Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.netdefender.example/payroll.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0084
- **ID:** `PILOT2-0084`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 169, "end_char": 301, "span_text": "Install our certified TaskTracker software client from https://work.securevault.example/setup to begin completing daily evaluations."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 118, "span_text": "Work-from-home logistics quality inspector opening offering $45.00 per hour with weekly direct deposits."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 119, "end_char": 168, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
Urgent alert: Work-from-home logistics quality inspector opening offering $45.00 per hour with weekly direct deposits. Immediate response required before 5:00 PM today. Install our certified TaskTracker software client from https://work.securevault.example/setup to begin completing daily evaluations.
```

---

#### Record PILOT2-0085
- **ID:** `PILOT2-0085`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 356, "end_char": 463, "span_text": "Recharge your work platform account with $200 USDT through ZelleConnect to unlock the next task commission."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 134, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 272, "end_char": 355, "span_text": "Earn daily automated commission distributions averaging $300 daily upon onboarding."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-90148. Earn daily automated commission distributions averaging $300 daily upon onboarding. Recharge your work platform account with $200 USDT through ZelleConnect to unlock the next task commission.
```

---

#### Record PILOT2-0086
- **ID:** `PILOT2-0086`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["reward_or_benefit", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 280, "end_char": 388, "span_text": "Recharge your work platform account with $200 USDT through QuickTransfer to unlock the next task commission."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 193, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 195, "end_char": 278, "span_text": "Earn daily automated commission distributions averaging $300 daily upon onboarding."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-40255 - Verification Required

Attention Account Holder,

Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.

Earn daily automated commission distributions averaging $300 daily upon onboarding.

Recharge your work platform account with $200 USDT through QuickTransfer to unlock the next task commission.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0087
- **ID:** `PILOT2-0087`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["scarcity", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 474, "span_text": "Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.cloudshield.example/payroll."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 198, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 200, "end_char": 290, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-51507 - Verification Required

Attention Account Holder,

Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily.

Only 2 participant allocations remain available before registration is permanently closed.

Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.cloudshield.example/payroll.

Sincerely,
Operations & Risk Desk
Pinnacle Bank
```

---

#### Record PILOT2-0088
- **ID:** `PILOT2-0088`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 292, "end_char": 474, "span_text": "Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.netdefender.example/payroll."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 198, "span_text": "Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 200, "end_char": 290, "span_text": "Only 2 participant allocations remain available before registration is permanently closed."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-85233 - Verification Required

Attention Account Holder,

Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily.

Only 2 participant allocations remain available before registration is permanently closed.

Please submit your full Social Security number, date of birth, and checking account details to complete direct deposit payroll onboarding at https://work.netdefender.example/payroll.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0089
- **ID:** `PILOT2-0089`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 198, "end_char": 306, "span_text": "Recharge your work platform account with $200 USDT through QuickTransfer to unlock the next task commission."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 113, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "scarcity", "start_char": 114, "end_char": 197, "span_text": "Earn daily automated commission distributions averaging $300 daily upon onboarding."}]`

**Complete Original Text:**
```text
Please note: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations. Earn daily automated commission distributions averaging $300 daily upon onboarding. Recharge your work platform account with $200 USDT through QuickTransfer to unlock the next task commission.
```

---

#### Record PILOT2-0090
- **ID:** `PILOT2-0090`
- **Subtype (`phishing_type`):** `job_task_commission`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 199, "end_char": 302, "span_text": "Recharge your work platform account with $200 USDT through SwiftPay to unlock the next task commission."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 114, "span_text": "Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 115, "end_char": 198, "span_text": "Earn daily automated commission distributions averaging $300 daily upon onboarding."}]`

**Complete Original Text:**
```text
Urgent alert: Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations. Earn daily automated commission distributions averaging $300 daily upon onboarding. Recharge your work platform account with $200 USDT through SwiftPay to unlock the next task commission.
```

---

### Subtype Group: `romance_financial_manipulation`

#### Record PILOT2-0091
- **ID:** `PILOT2-0091`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 260, "end_char": 359, "span_text": "Please wire $3,056.80 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 84, "end_char": 194, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 196, "end_char": 258, "span_text": "Please do not abandon me when I need your compassion the most."}]`

**Complete Original Text:**
```text
Subject: My love, please read this as soon as you can - urgent update

My dearest,

My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.

Please do not abandon me when I need your compassion the most.

Please wire $3,056.80 to the medical clearing officer today so I can receive the emergency surgery.

With all my love,
Jennifer
```

---

#### Record PILOT2-0092
- **ID:** `PILOT2-0092`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["urgency", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 346, "end_char": 456, "span_text": "Download and launch the AnyDesk remote support client so I can walk you through the wallet setup step-by-step."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 148, "span_text": "My love, I want to set up our shared cryptocurrency investment profile on NovaChain Markets so we can manage our savings together."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 263, "end_char": 345, "span_text": "I am in complete despair and do not know who else can help me through this crisis."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My love, I want to set up our shared cryptocurrency investment profile on NovaChain Markets so we can manage our savings together.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am trying to stay calm. I am in complete despair and do not know who else can help me through this crisis. Download and launch the AnyDesk remote support client so I can walk you through the wallet setup step-by-step.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

#### Record PILOT2-0093
- **ID:** `PILOT2-0093`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 306, "end_char": 403, "span_text": "Please wire $640.50 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 128, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 243, "end_char": 305, "span_text": "Please do not abandon me when I need your compassion the most."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am trying to stay calm. Please do not abandon me when I need your compassion the most. Please wire $640.50 to the medical clearing officer today so I can receive the emergency surgery.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

#### Record PILOT2-0094
- **ID:** `PILOT2-0094`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 214, "end_char": 355, "span_text": "If we deposit $3,970.80 together into the BitCrest Capital liquidity pool, the profits can be our down payment for our dream house next year."}`
- **Narrative Evidence:** `{"start_char": 14, "end_char": 130, "span_text": "Sweetheart, my uncle showed me an exclusive decentralized trading node on BitCrest Capital that made 25% this month."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 131, "end_char": 213, "span_text": "You know our mutual trust and love mean everything to me in this difficult moment."}]`

**Complete Original Text:**
```text
Urgent alert: Sweetheart, my uncle showed me an exclusive decentralized trading node on BitCrest Capital that made 25% this month. You know our mutual trust and love mean everything to me in this difficult moment. If we deposit $3,970.80 together into the BitCrest Capital liquidity pool, the profits can be our down payment for our dream house next year.
```

---

#### Record PILOT2-0095
- **ID:** `PILOT2-0095`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 306, "end_char": 403, "span_text": "Please wire $870.80 to the medical clearing officer today so I can receive the emergency surgery."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 128, "span_text": "My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 243, "end_char": 305, "span_text": "Please do not abandon me when I need your compassion the most."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am trying to stay calm. Please do not abandon me when I need your compassion the most. Please wire $870.80 to the medical clearing officer today so I can receive the emergency surgery.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

#### Record PILOT2-0096
- **ID:** `PILOT2-0096`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["trust_exploitation", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 333, "end_char": 475, "span_text": "If we deposit $2,921.00 together into the EtherPeak Trading liquidity pool, the profits can be our down payment for our dream house next year."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 135, "span_text": "Sweetheart, my uncle showed me an exclusive decentralized trading node on EtherPeak Trading that made 25% this month."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 250, "end_char": 332, "span_text": "You know our mutual trust and love mean everything to me in this difficult moment."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: Sweetheart, my uncle showed me an exclusive decentralized trading node on EtherPeak Trading that made 25% this month.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am trying to stay calm. You know our mutual trust and love mean everything to me in this difficult moment. If we deposit $2,921.00 together into the EtherPeak Trading liquidity pool, the profits can be our down payment for our dream house next year.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

#### Record PILOT2-0097
- **ID:** `PILOT2-0097`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 335, "end_char": 475, "span_text": "If we deposit $874.50 together into the NovaChain Markets liquidity pool, the profits can be our down payment for our dream house next year."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 136, "span_text": "Sweetheart, my uncle showed me an exclusive decentralized trading node on NovaChain Markets that made 25% this month."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 252, "end_char": 334, "span_text": "You know our mutual trust and love mean everything to me in this difficult moment."}]`

**Complete Original Text:**
```text
[10:14 AM] Marcus: Sweetheart, my uncle showed me an exclusive decentralized trading node on NovaChain Markets that made 25% this month.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Marcus: I am trying to stay calm. You know our mutual trust and love mean everything to me in this difficult moment. If we deposit $874.50 together into the NovaChain Markets liquidity pool, the profits can be our down payment for our dream house next year.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

#### Record PILOT2-0098
- **ID:** `PILOT2-0098`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 348, "end_char": 458, "span_text": "Download and launch the AnyDesk remote support client so I can walk you through the wallet setup step-by-step."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 150, "span_text": "My love, I want to set up our shared cryptocurrency investment profile on CryptoSphere Assets so we can manage our savings together."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 265, "end_char": 347, "span_text": "I am in complete despair and do not know who else can help me through this crisis."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My love, I want to set up our shared cryptocurrency investment profile on CryptoSphere Assets so we can manage our savings together.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am trying to stay calm. I am in complete despair and do not know who else can help me through this crisis. Download and launch the AnyDesk remote support client so I can walk you through the wallet setup step-by-step.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

#### Record PILOT2-0099
- **ID:** `PILOT2-0099`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_fraudulent_investment`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 286, "end_char": 427, "span_text": "If we deposit $1,443.00 together into the BitCrest Capital liquidity pool, the profits can be our down payment for our dream house next year."}`
- **Narrative Evidence:** `{"start_char": 84, "end_char": 200, "span_text": "Sweetheart, my uncle showed me an exclusive decentralized trading node on BitCrest Capital that made 25% this month."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 202, "end_char": 284, "span_text": "You know our mutual trust and love mean everything to me in this difficult moment."}]`

**Complete Original Text:**
```text
Subject: My love, please read this as soon as you can - urgent update

My dearest,

Sweetheart, my uncle showed me an exclusive decentralized trading node on BitCrest Capital that made 25% this month.

You know our mutual trust and love mean everything to me in this difficult moment.

If we deposit $1,443.00 together into the BitCrest Capital liquidity pool, the profits can be our down payment for our dream house next year.

With all my love,
Amanda
```

---

#### Record PILOT2-0100
- **ID:** `PILOT2-0100`
- **Subtype (`phishing_type`):** `romance_financial_manipulation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["emotional_manipulation", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 348, "end_char": 458, "span_text": "Download and launch the AnyDesk remote support client so I can walk you through the wallet setup step-by-step."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 150, "span_text": "My love, I want to set up our shared cryptocurrency investment profile on CryptoSphere Assets so we can manage our savings together."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 265, "end_char": 347, "span_text": "I am in complete despair and do not know who else can help me through this crisis."}]`

**Complete Original Text:**
```text
[10:14 AM] Elena: My love, I want to set up our shared cryptocurrency investment profile on CryptoSphere Assets so we can manage our savings together.
[10:16 AM] Honey: Oh my love, what happened?! Are you safe right now?
[10:17 AM] Elena: I am trying to stay calm. I am in complete despair and do not know who else can help me through this crisis. Download and launch the AnyDesk remote support client so I can walk you through the wallet setup step-by-step.
[10:19 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

---

### Subtype Group: `family_emergency_request`

#### Record PILOT2-0101
- **ID:** `PILOT2-0101`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 211, "end_char": 311, "span_text": "Please send $1,507.00 via QuickTransfer to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 13, "end_char": 126, "span_text": "Hey Uncle Dave, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 127, "end_char": 210, "span_text": "Hi Uncle Dave, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
Please note: Hey Uncle Dave, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Uncle Dave, it's really me reaching out directly because I trust you completely. Please send $1,507.00 via QuickTransfer to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT2-0102
- **ID:** `PILOT2-0102`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["emotional_manipulation", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 384, "end_char": 500, "span_text": "Can you text me your 16-digit debit card number and 3-digit CVV so the mechanic can charge the emergency repair fee?"}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 116, "span_text": "Hey Uncle Dave, I am stranded at an auto repair shop after my alternator failed on the interstate."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 334, "end_char": 383, "span_text": "Immediate response required before 5:00 PM today."}]`

**Complete Original Text:**
```text
[10:14 AM] Chris: Hey Uncle Dave, I am stranded at an auto repair shop after my alternator failed on the interstate.
[10:16 AM] Uncle Dave: Wait, is this really you? Why aren't you calling me from your normal phone?
[10:17 AM] Chris: My phone screen shattered when it fell on the pavement. A stranger at the roadside let me text you. Immediate response required before 5:00 PM today. Can you text me your 16-digit debit card number and 3-digit CVV so the mechanic can charge the emergency repair fee?
[10:19 AM] Uncle Dave: Oh god, okay! I'm opening the app right now to send it. Hold on.
```

---

#### Record PILOT2-0103
- **ID:** `PILOT2-0103`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 203, "end_char": 296, "span_text": "Please send $991.80 via CashFlow to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 121, "span_text": "Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 122, "end_char": 202, "span_text": "Hi Grandma, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
Important: Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Grandma, it's really me reaching out directly because I trust you completely. Please send $991.80 via CashFlow to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT2-0104
- **ID:** `PILOT2-0104`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 412, "end_char": 513, "span_text": "Please send $2,276.00 via PayLink Mobile to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 124, "span_text": "Hey Mom, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 335, "end_char": 411, "span_text": "Hi Mom, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
[10:14 AM] Kevin: Hey Mom, I was involved in an unexpected fender bender and need to settle the repair before police arrive.
[10:16 AM] Mom: Wait, is this really you? Why aren't you calling me from your normal phone?
[10:17 AM] Kevin: My phone screen shattered when it fell on the pavement. A stranger at the roadside let me text you. Hi Mom, it's really me reaching out directly because I trust you completely. Please send $2,276.00 via PayLink Mobile to the towing driver right now so they don't impound my car.
[10:19 AM] Mom: Oh god, okay! I'm opening the app right now to send it. Hold on.
```

---

#### Record PILOT2-0105
- **ID:** `PILOT2-0105`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 433, "end_char": 531, "span_text": "Please send $694.00 via QuickTransfer to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 131, "span_text": "Hey Uncle Dave, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 349, "end_char": 432, "span_text": "Hi Uncle Dave, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
[10:14 AM] Kevin: Hey Uncle Dave, I was involved in an unexpected fender bender and need to settle the repair before police arrive.
[10:16 AM] Uncle Dave: Wait, is this really you? Why aren't you calling me from your normal phone?
[10:17 AM] Kevin: My phone screen shattered when it fell on the pavement. A stranger at the roadside let me text you. Hi Uncle Dave, it's really me reaching out directly because I trust you completely. Please send $694.00 via QuickTransfer to the towing driver right now so they don't impound my car.
[10:19 AM] Uncle Dave: Oh god, okay! I'm opening the app right now to send it. Hold on.
```

---

#### Record PILOT2-0106
- **ID:** `PILOT2-0106`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 195, "end_char": 292, "span_text": "Please send $881.80 via ZelleConnect to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 117, "span_text": "Hey Dad, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 118, "end_char": 194, "span_text": "Hi Dad, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
Important: Hey Dad, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Dad, it's really me reaching out directly because I trust you completely. Please send $881.80 via ZelleConnect to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT2-0107
- **ID:** `PILOT2-0107`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 211, "end_char": 306, "span_text": "Please send $2,155.80 via SwiftPay to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 129, "span_text": "Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 130, "end_char": 210, "span_text": "Hi Grandma, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
For your security: Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Grandma, it's really me reaching out directly because I trust you completely. Please send $2,155.80 via SwiftPay to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT2-0108
- **ID:** `PILOT2-0108`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 203, "end_char": 301, "span_text": "Please send $696.80 via QuickTransfer to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 125, "span_text": "Hey Dad, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 126, "end_char": 202, "span_text": "Hi Dad, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
For your security: Hey Dad, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Dad, it's really me reaching out directly because I trust you completely. Please send $696.80 via QuickTransfer to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT2-0109
- **ID:** `PILOT2-0109`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["trust_exploitation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 203, "end_char": 298, "span_text": "Please send $3,104.00 via SwiftPay to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 121, "span_text": "Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 122, "end_char": 202, "span_text": "Hi Grandma, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
Important: Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Grandma, it's really me reaching out directly because I trust you completely. Please send $3,104.00 via SwiftPay to the towing driver right now so they don't impound my car.
```

---

#### Record PILOT2-0110
- **ID:** `PILOT2-0110`
- **Subtype (`phishing_type`):** `family_emergency_request`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 211, "end_char": 309, "span_text": "Please send $856.80 via QuickTransfer to the towing driver right now so they don't impound my car."}`
- **Narrative Evidence:** `{"start_char": 19, "end_char": 129, "span_text": "Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 130, "end_char": 210, "span_text": "Hi Grandma, it's really me reaching out directly because I trust you completely."}]`

**Complete Original Text:**
```text
For your security: Hey Grandma, I was involved in an unexpected fender bender and need to settle the repair before police arrive. Hi Grandma, it's really me reaching out directly because I trust you completely. Please send $856.80 via QuickTransfer to the towing driver right now so they don't impound my car.
```

---

### Subtype Group: `recovery_support`

#### Record PILOT2-0111
- **ID:** `PILOT2-0111`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 278, "end_char": 379, "span_text": "Remit the mandatory legal escrow bond of $3,670.00 via wire transfer to release your recovered funds."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 198, "span_text": "You are named in court restitution docket #CF-70183 to receive recovered fraud compensation of $3,670.00."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 200, "end_char": 276, "span_text": "Certified clearance code: CF-70183-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-70183 - Verification Required

Attention Account Holder,

You are named in court restitution docket #CF-70183 to receive recovered fraud compensation of $3,670.00.

Certified clearance code: CF-70183-AUTH verified through centralized ledger.

Remit the mandatory legal escrow bond of $3,670.00 via wire transfer to release your recovered funds.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0112
- **ID:** `PILOT2-0112`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 278, "end_char": 379, "span_text": "Remit the mandatory legal escrow bond of $1,349.80 via wire transfer to release your recovered funds."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 198, "span_text": "You are named in court restitution docket #CF-69432 to receive recovered fraud compensation of $1,349.80."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 200, "end_char": 276, "span_text": "Certified clearance code: CF-69432-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-69432 - Verification Required

Attention Account Holder,

You are named in court restitution docket #CF-69432 to receive recovered fraud compensation of $1,349.80.

Certified clearance code: CF-69432-AUTH verified through centralized ledger.

Remit the mandatory legal escrow bond of $1,349.80 via wire transfer to release your recovered funds.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0113
- **ID:** `PILOT2-0113`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 257, "end_char": 383, "span_text": "Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 201, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $1,307.80."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 203, "end_char": 255, "span_text": "Authorized by senior financial auditor Robert Vance."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-60096 - Verification Required

Attention Account Holder,

Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $1,307.80.

Authorized by senior financial auditor Robert Vance.

Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node.

Sincerely,
Operations & Risk Desk
Vanguard Bancorp
```

---

#### Record PILOT2-0114
- **ID:** `PILOT2-0114`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 245, "end_char": 386, "span_text": "Provide your 12-word master recovery seed phrase at https://restore.asset-recovery.example/verify so our technician can sign the restitution."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 170, "span_text": "Restitution docket #CF-92199 is finalized to restore your compromised assets."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 172, "end_char": 243, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-92199 - Verification Required

Attention Account Holder,

Restitution docket #CF-92199 is finalized to restore your compromised assets.

Time-sensitive alert: immediate verification is required without delay.

Provide your 12-word master recovery seed phrase at https://restore.asset-recovery.example/verify so our technician can sign the restitution.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

---

#### Record PILOT2-0115
- **ID:** `PILOT2-0115`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 354, "end_char": 455, "span_text": "Remit the mandatory legal escrow bond of $3,026.80 via wire transfer to release your recovered funds."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 139, "span_text": "You are named in court restitution docket #CF-20511 to receive recovered fraud compensation of $3,026.80."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 277, "end_char": 353, "span_text": "Certified clearance code: CF-20511-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: You are named in court restitution docket #CF-20511 to receive recovered fraud compensation of $3,026.80.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-20511. Certified clearance code: CF-20511-AUTH verified through centralized ledger. Remit the mandatory legal escrow bond of $3,026.80 via wire transfer to release your recovered funds.
```

---

#### Record PILOT2-0116
- **ID:** `PILOT2-0116`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 245, "end_char": 386, "span_text": "Provide your 12-word master recovery seed phrase at https://restore.asset-recovery.example/verify so our technician can sign the restitution."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 170, "span_text": "Restitution docket #CF-87009 is finalized to restore your compromised assets."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 172, "end_char": 243, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-87009 - Verification Required

Attention Account Holder,

Restitution docket #CF-87009 is finalized to restore your compromised assets.

Time-sensitive alert: immediate verification is required without delay.

Provide your 12-word master recovery seed phrase at https://restore.asset-recovery.example/verify so our technician can sign the restitution.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

---

#### Record PILOT2-0117
- **ID:** `PILOT2-0117`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["authority_impersonation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 352, "end_char": 451, "span_text": "Remit the mandatory legal escrow bond of $784.00 via wire transfer to release your recovered funds."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 137, "span_text": "You are named in court restitution docket #CF-53553 to receive recovered fraud compensation of $784.00."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 275, "end_char": 351, "span_text": "Certified clearance code: CF-53553-AUTH verified through centralized ledger."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: You are named in court restitution docket #CF-53553 to receive recovered fraud compensation of $784.00.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-53553. Certified clearance code: CF-53553-AUTH verified through centralized ledger. Remit the mandatory legal escrow bond of $784.00 via wire transfer to release your recovered funds.
```

---

#### Record PILOT2-0118
- **ID:** `PILOT2-0118`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_credentials_or_codes`
- **Social-Engineering Tactics:** `["authority_impersonation", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 245, "end_char": 386, "span_text": "Provide your 12-word master recovery seed phrase at https://restore.asset-recovery.example/verify so our technician can sign the restitution."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 170, "span_text": "Restitution docket #CF-41552 is finalized to restore your compromised assets."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 172, "end_char": 243, "span_text": "Time-sensitive alert: immediate verification is required without delay."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-41552 - Verification Required

Attention Account Holder,

Restitution docket #CF-41552 is finalized to restore your compromised assets.

Time-sensitive alert: immediate verification is required without delay.

Provide your 12-word master recovery seed phrase at https://restore.asset-recovery.example/verify so our technician can sign the restitution.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT2-0119
- **ID:** `PILOT2-0119`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["urgency", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 257, "end_char": 383, "span_text": "Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node."}`
- **Narrative Evidence:** `{"start_char": 93, "end_char": 201, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $1,561.80."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 203, "end_char": 255, "span_text": "Authorized by senior financial auditor Robert Vance."}]`

**Complete Original Text:**
```text
Subject: Notice Regarding Case #CF-88106 - Verification Required

Attention Account Holder,

Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $1,561.80.

Authorized by senior financial auditor Robert Vance.

Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

---

#### Record PILOT2-0120
- **ID:** `PILOT2-0120`
- **Subtype (`phishing_type`):** `recovery_support`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `gain_account_or_device_access`
- **Social-Engineering Tactics:** `["false_legitimacy", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 331, "end_char": 457, "span_text": "Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 140, "span_text": "Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $428.50."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 278, "end_char": 330, "span_text": "Authorized by senior financial auditor Robert Vance."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of $428.50.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-94203. Authorized by senior financial auditor Robert Vance. Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node.
```

---

### Subtype Group: `charity_donation`

#### Record PILOT2-0121
- **ID:** `PILOT2-0121`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 377, "span_text": "Donate $3,781.50 today through SwiftPay to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 198, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 200, "end_char": 283, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Every passing minute puts an innocent life in severe jeopardy without your support.

Donate $3,781.50 today through SwiftPay to provide emergency supplies to displaced children.

Sincerely,
Community Outreach Coordinator
Pinnacle Bank
```

---

#### Record PILOT2-0122
- **ID:** `PILOT2-0122`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 381, "span_text": "Donate $1,049.50 today through ZelleConnect to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 198, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 200, "end_char": 283, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Every passing minute puts an innocent life in severe jeopardy without your support.

Donate $1,049.50 today through ZelleConnect to provide emergency supplies to displaced children.

Sincerely,
Community Outreach Coordinator
Pinnacle Bank
```

---

#### Record PILOT2-0123
- **ID:** `PILOT2-0123`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 383, "span_text": "Donate $2,862.80 today through PayLink Mobile to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 198, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 200, "end_char": 283, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Every passing minute puts an innocent life in severe jeopardy without your support.

Donate $2,862.80 today through PayLink Mobile to provide emergency supplies to displaced children.

Sincerely,
Community Outreach Coordinator
Apex National Bank
```

---

#### Record PILOT2-0124
- **ID:** `PILOT2-0124`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["urgency", "emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 383, "span_text": "Donate $3,070.00 today through PayLink Mobile to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 198, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 200, "end_char": 283, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Every passing minute puts an innocent life in severe jeopardy without your support.

Donate $3,070.00 today through PayLink Mobile to provide emergency supplies to displaced children.

Sincerely,
Community Outreach Coordinator
Beacon Financial
```

---

#### Record PILOT2-0125
- **ID:** `PILOT2-0125`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `sms`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 203, "end_char": 295, "span_text": "Donate $3,461.00 today through CashFlow to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 11, "end_char": 118, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 119, "end_char": 202, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
Important: Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water. Every passing minute puts an innocent life in severe jeopardy without your support. Donate $3,461.00 today through CashFlow to provide emergency supplies to displaced children.
```

---

#### Record PILOT2-0126
- **ID:** `PILOT2-0126`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 285, "end_char": 377, "span_text": "Donate $4,749.50 today through SwiftPay to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 198, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 200, "end_char": 283, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.

Every passing minute puts an innocent life in severe jeopardy without your support.

Donate $4,749.50 today through SwiftPay to provide emergency supplies to displaced children.

Sincerely,
Community Outreach Coordinator
Vanguard Bancorp
```

---

#### Record PILOT2-0127
- **ID:** `PILOT2-0127`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy", "urgency"]`
- **Primary Intent Evidence:** `{"start_char": 363, "end_char": 461, "span_text": "Donate $4,403.00 today through PayLink Mobile to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 141, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 279, "end_char": 362, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-54987. Every passing minute puts an innocent life in severe jeopardy without your support. Donate $4,403.00 today through PayLink Mobile to provide emergency supplies to displaced children.
```

---

#### Record PILOT2-0128
- **ID:** `PILOT2-0128`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 278, "end_char": 417, "span_text": "Please provide your debit card number and 3-digit CVV at https://donate.disaster-relief.example/gift to set up your emergency contribution."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 197, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 199, "end_char": 276, "span_text": "Statutory validation reference: CF-88507 filed with merchant claims registry."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support.

Statutory validation reference: CF-88507 filed with merchant claims registry.

Please provide your debit card number and 3-digit CVV at https://donate.disaster-relief.example/gift to set up your emergency contribution.

Sincerely,
Community Outreach Coordinator
Vanguard Bancorp
```

---

#### Record PILOT2-0129
- **ID:** `PILOT2-0129`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `email`
- **Primary Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Social-Engineering Tactics:** `["emotional_manipulation"]`
- **Primary Intent Evidence:** `{"start_char": 278, "end_char": 417, "span_text": "Please provide your debit card number and 3-digit CVV at https://donate.disaster-relief.example/gift to set up your emergency contribution."}`
- **Narrative Evidence:** `{"start_char": 91, "end_char": 197, "span_text": "Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 199, "end_char": 276, "span_text": "Statutory validation reference: CF-43745 filed with merchant claims registry."}]`

**Complete Original Text:**
```text
Subject: Urgent Appeal: Emergency Relief for Displaced Disaster Families

Dear Supporter,

Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support.

Statutory validation reference: CF-43745 filed with merchant claims registry.

Please provide your debit card number and 3-digit CVV at https://donate.disaster-relief.example/gift to set up your emergency contribution.

Sincerely,
Community Outreach Coordinator
Beacon Financial
```

---

#### Record PILOT2-0130
- **ID:** `PILOT2-0130`
- **Subtype (`phishing_type`):** `charity_donation`
- **Channel (`scam_channel`):** `chat`
- **Primary Fraudulent Intent:** `induce_payment_or_transfer`
- **Social-Engineering Tactics:** `["false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 363, "end_char": 459, "span_text": "Donate $4,290.80 today through ZelleConnect to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 141, "span_text": "Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 279, "end_char": 362, "span_text": "Every passing minute puts an innocent life in severe jeopardy without your support."}]`

**Complete Original Text:**
```text
[10:14 AM] Representative_Morgan: Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.
[10:16 AM] You: Can you provide the reference docket number for this matter?
[10:17 AM] Representative_Morgan: Case Docket is #CF-73814. Every passing minute puts an innocent life in severe jeopardy without your support. Donate $4,290.80 today through ZelleConnect to provide emergency supplies to displaced children.
```

---
