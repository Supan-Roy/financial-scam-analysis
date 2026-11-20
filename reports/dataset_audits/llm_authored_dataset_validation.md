# Forensic Validation & Audit Report: LLM-Authored Financial Scam Dataset

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*
**Date:** 2026-11-20 21:09:30 UTC  
**Generator Engine:** `scripts/generate_llm_authored_scams.py`  
**Underlying LLM:** `gemini-3.8-flash-low` via Antigravity Engine (Temperature: Contextual Reasoning Mode)  
**Raw Dataset File:** `data\raw\llm_authored_financial_scams.csv`  
**Processed Dataset File:** `data\processed\llm_authored_financial_scams_processed.csv`  

---

## 1. Executive Summary & Architecture Rationale

This dataset was engineered to address a primary research question in financial fraud detection:
*Do multi-level transformer models trained on programmatically synthesized financial scam narratives (such as Version 3.1) generalize to scam communications authored through contextual LLM reasoning?*

### Exact Record Count Justification (2,730 Records)
Rather than targeting an arbitrary number, the dataset size was derived directly from balanced multi-dimensional coverage requirements:
- **13 Canonical Scam Subtypes** (fully aligned with the research framework).
- **10 Grounded Scenario Families per Subtype** = **130 distinct scenario families**.
- **21 Records per Scenario Family** = **2,730 total records**.
- **7 Canonical Writing Styles** evenly represented (3 records per style per scenario family).
- **Strict 80 / 10 / 10 Group Partitioning** across scenario families:
  - **Train:** 8 families per subtype $\times$ 21 records = **168 records/subtype** $\rightarrow$ **2,184 records (80.0%)** across 104 families.
  - **Validation:** 1 family per subtype $\times$ 21 records = **21 records/subtype** $\rightarrow$ **273 records (10.0%)** across 13 families.
  - **Test:** 1 family per subtype $\times$ 21 records = **21 records/subtype** $\rightarrow$ **273 records (10.0%)** across 13 families.
- **Partition Leakage:** **0.0% scenario family overlap** across Train, Val, and Test.

---

## 2. Dataset Partition & Group Isolation Verification

| Partition Split | Scenario Families | Record Count | Percentage of Dataset | Subtypes Represented | Partition Leakage |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Train** | 104 | 2,184 | 80.00% | 13 / 13 (100%) | **0.0% (Zero)** |
| **Validation** | 13 | 273 | 10.00% | 13 / 13 (100%) | **0.0% (Zero)** |
| **Test** | 13 | 273 | 10.00% | 13 / 13 (100%) | **0.0% (Zero)** |
| **Total** | **130** | **2,730** | **100.00%** | **13 / 13 (100%)** | **Strictly Disjoint** |

### Scenario Family Disjointness Verification

- `Train_Families ∩ Val_Families`: **0 families (Passed - Zero Leakage)**
- `Train_Families ∩ Test_Families`: **0 families (Passed - Zero Leakage)**
- `Val_Families ∩ Test_Families`: **0 families (Passed - Zero Leakage)**

---

## 3. Writing Style Diversity & Linguistic Features

The dataset explicitly incorporates 7 writing styles spanning the full spectrum of digital deception:

| Writing Style | Count | Pct | Mean Words | Median Words | Min Words | Max Words | Mean Chars |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `casual_informal` | 390 | 14.29% | 54.1 | 52 | 26 | 107 | 340.2 |
| `direct_terse` | 390 | 14.29% | 26.1 | 26 | 14 | 45 | 218.2 |
| `conversational_personal` | 390 | 14.29% | 104.6 | 103 | 45 | 185 | 693.3 |
| `professional_neutral` | 390 | 14.29% | 88.9 | 88 | 34 | 141 | 689.2 |
| `corporate_institutional` | 390 | 14.29% | 85.3 | 93 | 24 | 156 | 676.0 |
| `sophisticated_formal` | 390 | 14.29% | 67.7 | 47 | 22 | 169 | 549.8 |
| `dialogue_interactive` | 390 | 14.29% | 82.3 | 86 | 26 | 163 | 535.9 |

---

## 4. Communication Channel Distributions & Delivery Modality

| Channel | Message Count | Percentage | Mean Words | Median Words | Min Words | Max Words |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `email` | 1,145 | 41.94% | 101.4 | 99 | 57 | 185 |
| `sms` | 383 | 14.03% | 42.7 | 40 | 16 | 96 |
| `chat` | 543 | 19.89% | 82.1 | 81 | 35 | 163 |
| `notification` | 659 | 24.14% | 32.5 | 31 | 14 | 76 |

### Notification Modality Balance (Eliminating URL Monopoly)
- **Total Notifications:** 659
- **Notifications with URL Link:** 308 (46.74%)
- **Notifications without URL (In-App / Status / Direct Action):** 351 (53.26%)

---

## 5. Multi-Level Semantic Annotations

### Fraudulent Intent Representation

| Fraudulent Intent | Record Count | Percentage | Intent Grounding Verification |
| :--- | :---: | :---: | :--- |
| `induce_payment_or_transfer` | 1,247 | 45.68% | **100.0% Exact Substring Match** |
| `obtain_credentials_or_codes` | 582 | 21.32% | **100.0% Exact Substring Match** |
| `obtain_personal_or_financial_information` | 506 | 18.53% | **100.0% Exact Substring Match** |
| `gain_account_or_device_access` | 228 | 8.35% | **100.0% Exact Substring Match** |
| `induce_fraudulent_investment` | 167 | 6.12% | **100.0% Exact Substring Match** |

### Social Engineering Tactics Frequency

| Social Engineering Tactic | Total Occurrences | Frequency Relative to Dataset |
| :--- | :---: | :---: |
| `urgency` | 1,743 | 63.85% |
| `false_legitimacy` | 1,857 | 68.02% |
| `reward_or_benefit` | 1,046 | 38.32% |
| `authority_impersonation` | 971 | 35.57% |
| `trust_exploitation` | 802 | 29.38% |
| `secrecy` | 40 | 1.47% |
| `scarcity` | 300 | 10.99% |
| `emotional_manipulation` | 554 | 20.29% |
| `fear_or_threat` | 883 | 32.34% |

---

## 6. Real-World Missingness Analysis

To prevent models from relying on artificial tabular completeness, intentional missingness was introduced in non-essential metadata fields, while primary supervisory labels maintain strictly 0.0% missingness:

| Column Name | Column Type | Missing Count | Missing Percentage | Research Purpose |
| :--- | :---: | :---: | :---: | :--- |
| `id` | Primary Key | 0 | **0.00% (Complete)** | Supervisory Core |
| `original_text` | Core Feature | 0 | **0.00% (Complete)** | Supervisory Core |
| `normalized_text` | Core Feature | 0 | **0.00% (Complete)** | Supervisory Core |
| `scam_subtype` | Level 1 Target | 0 | **0.00% (Complete)** | Supervisory Core |
| `fraudulent_intent` | Level 2 Target | 0 | **0.00% (Complete)** | Supervisory Core |
| `social_engineering_tactics` | Level 3 Target | 0 | **0.00% (Complete)** | Supervisory Core |
| `writing_style` | Linguistic Attribute | 0 | **0.00% (Complete)** | Supervisory Core |
| `channel` | Modality Attribute | 0 | **0.00% (Complete)** | Supervisory Core |
| `split_partition` | Group Partition | 0 | **0.00% (Complete)** | Experimental Setup |
| `optional_scenario_description` | Context Description | 403 | 14.76% (Controlled) | Optional Pretext Feature |
| `urgency_rating` | Metadata Rating | 382 | 13.99% (Controlled) | Auxiliary Rating |
| `secondary_channel_source` | Routing Telemetry | 423 | 15.49% (Controlled) | Network Metadata |
| `email_subject` | Gateway Header | 1,585 | 58.06% (Controlled) | Channel-Conditioned Header |

---

## 7. MinHash LSH Deduplication & Cluster Isolation

- **MinHash Configuration:** 64 permutation hashes, 16 bands (4 rows/band), Jaccard threshold $\ge 0.85$ over word 3-shingles.
- **Clustered Near-Duplicate Records:** 0 records (0.00%).
- **Distinct Duplicate Clusters Formed:** 0 clusters.
- **Cross-Partition Cluster Collisions:** **0 (Zero)** — no near-duplicate clusters cross partitions.

---

## 8. Comparative Analysis: LLM-Authored vs. Programmatic V3.1

To quantitatively establish that this LLM-authored dataset provides genuine linguistic diversity distinct from the programmatic V3.1 dataset, key comparative dimensions are summarized below:

| Metric / Dimension | Programmatic Dataset (V3.1) | LLM-Authored Dataset (This Dataset) | Linguistic Implication |
| :--- | :--- | :--- | :--- |
| **Generation Paradigm** | Slot-filling modular templates | Contextual persona reasoning | Eliminates rigid grammar templates |
| **Total Record Count** | 7,800 records | 2,730 records | High-density diverse sample |
| **Scenario Families** | 104 families (8 per subtype) | 130 families (10 per subtype) | 25% broader scenario space |
| **Writing Style Explicit Taxonomy** | Implicit (3 broad channels) | Explicit 7-style taxonomy | Rigorously controlled registers |
| **Mean Original Word Count** | 35.8 words | 72.7 words | Authentic narrative complexity |
| **Word Count Range** | 12 – 144 words | 14 – 185 words | Spans short SMS to multi-paragraph emails |
| **Syntactic Variability** | Fixed template clauses | Unconstrained generation | Varied sentence starters and clauses |
| **Domain Nomenclature** | Fixed synthetic token pool | Dynamic fictional naming | Zero token repetition artifacts |
| **Zero-Leakage Partitioning** | 100% scenario-isolated | 100% scenario-isolated | Valid cross-evaluation test bed |

---

## 9. Comprehensive Integrity & Quality Verification

| Verification Dimension | Target Specification | Observed Result | Status |
| :--- | :--- | :--- | :---: |
| Total Records | Exactly 2,730 records | 2,730 records | **PASS** |
| Subtype Coverage | 13/13 subtypes (210 recs each) | 210 records per subtype (13/13) | **PASS** |
| Intent Coverage | 5/5 canonical intents | All 5 intents represented | **PASS** |
| Tactic Coverage | 9/9 canonical tactics | All 9 tactics represented | **PASS** |
| Writing Style Coverage | 7/7 canonical writing styles | All 7 writing styles represented | **PASS** |
| Channel Coverage | 4/4 digital channels | All 4 channels represented | **PASS** |
| Primary Intent Evidence Match | 100.0% verbatim substring slice | 100.0% (2730/2730) | **PASS** |
| Scenario Family Isolation | 0 overlapping families | 0 overlapping families | **PASS** |
| Real Entity Prohibition | 0 real financial institutions | 100% fictional entities | **PASS** |
| Reserved Domain RFC 2606 | 100% .example / safe domains | 100.0% safe domains | **PASS** |
| Raw-Processed Parity | 1-to-1 exact record alignment | 100.0% parity | **PASS** |

---

## 10. Qualitative Sample Gallery (1 Record per Subtype)

### Subtype: `account_verification`
- **Record ID:** `LLM-SCAM-00019`
- **Writing Style:** `corporate_institutional` | **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `suspicious_device_login_lock`
- **Primary Intent:** `obtain_personal_or_financial_information`
- **Intent Evidence Text:** `submitting your full tax identification number and digital authorization token`
- **Social Engineering Tactics:** `["authority_impersonation", "fear_or_threat", "urgency", "false_legitimacy"]`
- **Email Subject:** `MANDATORY COMPLIANCE: Account Quarantine Ref #BF-8820`

```text
ATTENTION ACCOUNT HOLDER:

Pursuant to Section 14-B of the Horizon Mutual Electronic Fund Transfers Oversight Charter, notice is hereby served that unvalidated hardware initiated connection with Profile Ref #BF-8820 from an anomalous geographical origin. Under statutory regulatory compliance guidelines, administrative quarantine has been imposed upon all ledger facilities associated with this profile.

Failure to clear this administrative lock within twenty-four (24) hours of this dispatch shall result in total revocation of electronic transacting privileges. Execute mandatory clearance immediately via our compliance hub: https://compliance.horizon-mutual.example/remedy by submitting your full tax identification number and digital authorization token.

By Order Of:
Division of Fraud Containment & Statutory Integrity
Horizon Mutual Depository
```

---

### Subtype: `card_transaction_alert`
- **Record ID:** `LLM-SCAM-00373`
- **Writing Style:** `direct_terse` | **Channel:** `notification` | **Partition:** `train`
- **Scenario Family:** `crypto_exchange_card_purchase`
- **Primary Intent:** `obtain_personal_or_financial_information`
- **Intent Evidence Text:** `verify card identity immediately: https://verify.beacon-financial.example/card-protect`
- **Social Engineering Tactics:** `["urgency", "false_legitimacy", "authority_impersonation"]`

```text
Beacon Financial Card Alert: $2,140.00 crypto asset order placed at NovaCoin Exchange. Card ending 8819. If unauthorized, verify card identity immediately: https://verify.beacon-financial.example/card-protect
```

---

### Subtype: `refund_chargeback`
- **Record ID:** `LLM-SCAM-00558`
- **Writing Style:** `corporate_institutional` | **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `duplicate_toll_road_charge_reimbursement`
- **Primary Intent:** `obtain_personal_or_financial_information`
- **Intent Evidence Text:** `Complete official certification and claim authorization: https://statutory.avalon-tollways.example/remedy-claim`
- **Social Engineering Tactics:** `["authority_impersonation", "fear_or_threat", "urgency", "false_legitimacy"]`
- **Email Subject:** `OFFICIAL NOTICE: Statutory Overcharge Remediation under Directive TR-409`

```text
ATTENTION: REGISTERED VEHICLE OPERATOR

Pursuant to Section 12-A of the Regional Transportation Code, the Avalon Highway Authority hereby notifies you of an erroneous secondary fee assessment incurred at Plaza Gantry 04. Statutory compliance mandates the immediate restitution of $19.80.

Under regulatory protocol, unclaimed reimbursements are forfeited to the central transport coffer if settlement credentials are not certified within seventy-two (72) business hours. Complete official certification and claim authorization: https://statutory.avalon-tollways.example/remedy-claim

Issued by:
Bureau of Tolling Oversight & Fiscal Rectification
Avalon Highway Infrastructure Commission
```

---

### Subtype: `invoice_payment_request`
- **Record ID:** `LLM-SCAM-00723`
- **Writing Style:** `direct_terse` | **Channel:** `notification` | **Partition:** `train`
- **Scenario Family:** `freight_logistics_port_clearance`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `Settle invoice immediately at https://portal.crestline-maritime.example/clearance`
- **Social Engineering Tactics:** `["urgency", "fear_or_threat", "false_legitimacy"]`

```text
PORT CLEARANCE HOLD: Bill of Lading BL-4401-Z. Outstanding harbor demurrage fee: $840.00. Payment deadline: 60 minutes. Settle invoice immediately at https://portal.crestline-maritime.example/clearance to avoid container seizure.
```

---

### Subtype: `loan_offer`
- **Record ID:** `LLM-SCAM-00931`
- **Writing Style:** `dialogue_interactive` | **Channel:** `chat` | **Partition:** `train`
- **Scenario Family:** `student_loan_forgiveness_enrollment`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `please wire the $95 state filing retainer to account ref #9928-VX`
- **Social Engineering Tactics:** `["trust_exploitation", "reward_or_benefit", "urgency"]`

```text
Advisor: Hello! I'm reviewing your student debt profile and have great news—you've cleared the preliminary screen for full balance forgiveness.
User: Are you sure? I thought the program was delayed.
Advisor: Not for your bracket! We just need to finalize your enrollment right now. I just generated an electronic enrollment voucher, so please wire the $95 state filing retainer to account ref #9928-VX via https://pay.solaria-clearing.example/checkout so I can lock in your zero balance.
```

---

### Subtype: `investment_crypto`
- **Record ID:** `LLM-SCAM-01231`
- **Writing Style:** `sophisticated_formal` | **Channel:** `email` | **Partition:** `val`
- **Scenario Family:** `institutional_staking_rewards_tier`
- **Primary Intent:** `obtain_credentials_or_codes`
- **Intent Evidence Text:** `authenticate your hardware security credentials at https://syndicate.horizon-mutual.example/access-tier.`
- **Social Engineering Tactics:** `["false_legitimacy", "scarcity", "reward_or_benefit", "urgency"]`
- **Email Subject:** `Private Invitation: Horizon Mutual Sovereign Staking Syndicate`

```text
Esteemed Client,

We trust this missive finds your enterprise in prosperous standing. The Investment Syndicate of Horizon Mutual cordially conveys this bespoke accession into our ultra-high-echelon Diamond Node Consortium.

Historically restricted to sovereign wealth institutions and multilateral endowments, this proprietary protocol synthesizes algorithmic liquidity aggregation to confer an annualized yield premium of 24.6% across distributed ledger tranches. Participation confers priority epoch finality and complete exemption from conventional slashing penalties.

To consummate your induction and authenticate your institutional ledger allocation, you are invited to authenticate your hardware security credentials at https://syndicate.horizon-mutual.example/access-tier.

Given the finite capacity of our current consensus cluster, invitations remain unencumbered for seventy-two hours subsequent to dispatch, after which unclaimed allocations shall irrevocably sunset.

With our highest consideration,

Julian Montgomery, Senior Partner
Horizon Mutual Institutional Liquidity Group
```

---

### Subtype: `prize_reward`
- **Record ID:** `LLM-SCAM-01279`
- **Writing Style:** `corporate_institutional` | **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `national_sweepstakes_unclaimed_cash`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `SUBMITTING AN ADMINISTRATIVE CLEARANCE LEVY OF $350.00`
- **Social Engineering Tactics:** `["authority_impersonation", "fear_or_threat", "urgency", "false_legitimacy"]`
- **Email Subject:** `OFFICIAL SUMMONS: Statutory Claim for Escheated National Sweepstakes Assets`

```text
ATTENTION CITIZEN,

PURSUANT TO ACT 44-B OF THE AVALON REVENUE DEPT COMPREHENSIVE SETTLEMENT DIRECTIVE, PUBLIC RECORD DOCKET #SW-902 IDENTIFIES AN UNCLAIMED SWEEPSTAKES CASH ASSET IN THE AMOUNT OF $215,000.00 ASSOCIATED WITH YOUR CITIZEN RECORD.

UNDER STATUTORY SECTION 12.4, YOU ARE HEREBY ORDERED TO COMPLETE STATUTORY VERIFICATION BY SUBMITTING AN ADMINISTRATIVE CLEARANCE LEVY OF $350.00 VIA SECURE CLEARINGHOUSE AT HTTPS://AUDIT.AVALON-TAX.EXAMPLE/STATUTORY-RELEASE. FAILURE TO COMPLY WITHIN SEVENTY-TWO (72) HOURS SHALL RESULT IN PERMANENT ESCHEATMENT AND REALLOCATION OF ASSETS TO THE GENERAL TREASURY.

BY ORDER OF:
INSPECTOR GENERAL J. VANCE
BUREAU OF UNCLAIMED PROPERTY
AVALON REVENUE DEPT
```

---

### Subtype: `tax_payment`
- **Record ID:** `LLM-SCAM-01617`
- **Writing Style:** `dialogue_interactive` | **Channel:** `chat` | **Partition:** `train`
- **Scenario Family:** `foreign_asset_fbar_penalty_waiver`
- **Primary Intent:** `obtain_credentials_or_codes`
- **Intent Evidence Text:** `confirm your foreign banking PIN and routing coordinates directly in this chat session`
- **Social Engineering Tactics:** `["authority_impersonation", "fear_or_threat", "reward_or_benefit"]`

```text
[14:02:11] Support Agent Clara: Welcome to Beacon Financial Offshore Services. I see you have an unfiled 2025 foreign asset declaration on record.
[14:02:40] User: What does that mean? Am I going to get fined?
[14:03:05] Support Agent Clara: Standard non-willful fines start at $10,000 per missing account, but we have an active penalty waiver voucher available for your profile.
[14:03:32] User: How do I get that waiver applied?
[14:04:01] Support Agent Clara: I can apply the zero-liability waiver right now. I just need you to confirm your foreign banking PIN and routing coordinates directly in this chat session to bind the waiver certificate.
```

---

### Subtype: `job_task_commission`
- **Record ID:** `LLM-SCAM-01723`
- **Writing Style:** `casual_informal` | **Channel:** `chat` | **Partition:** `train`
- **Scenario Family:** `product_rebate_affiliate_clicker`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `you gotta deposit a quick $85 security top-up into the affiliate escrow to unlock the order batch.`
- **Social Engineering Tactics:** `["reward_or_benefit", "false_legitimacy"]`

```text
hey! quick heads up if ur looking to make extra cash online rn 🙌 nexus merchant partners is paying users to optimize merchant product ratings. basically u just click 'boost rebate' on 30 items per set to simulate shopper traffic. you get a 12% commission instantly back to your dashboard! only thing is for Tier 2 packages you gotta deposit a quick $85 security top-up into the affiliate escrow to unlock the order batch. ping me once you transfer it at https://portal.nexus-affiliate.example/rebate-booster and ill send the manager code!
```

---

### Subtype: `romance_financial_manipulation`
- **Record ID:** `LLM-SCAM-01910`
- **Writing Style:** `sophisticated_formal` | **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `military_doctor_deployment_leave_fee`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `We entreat you to wire the designated liquidation levy directly to the depository vault managed by Beacon Financial, noting statutory clearance code #BF-MED-994.`
- **Social Engineering Tactics:** `["authority_impersonation", "false_legitimacy", "trust_exploitation"]`
- **Email Subject:** `Requisite Fiduciary Intervention: Humanitarian Surgeon Repatriation Protocol`

```text
Distinguished Benefactor,

It is with profound solemnity that I address this correspondence to your esteemed attention regarding the provisional release of Dr. Ethan Harrington from forward operational hospital command.

While command hierarchy has affirmed the doctor's eligibility for extended personal respite, bilateral treaty stipulations strictly preclude active field surgeons from directly discharging logistical indemnity charges. Hence, an external guarantor of unimpeachable standing must assume statutory custodianship of the $4,200 civilian replacement assessment.

We entreat you to wire the designated liquidation levy directly to the depository vault managed by Beacon Financial, noting statutory clearance code #BF-MED-994. Prompt fulfillment shall expedite immediate diplomatic charter conveyance.

Respectfully and faithfully yours,
Lt. Col. Alistair Sterling
Chief Liaison of Overseas Medical Deployments
```

---

### Subtype: `family_emergency_request`
- **Record ID:** `LLM-SCAM-02211`
- **Writing Style:** `sophisticated_formal` | **Channel:** `notification` | **Partition:** `train`
- **Scenario Family:** `broken_phone_temp_whatsapp_borrow`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `a remittance of 950 credits is urgently sought via Quantum Vault`
- **Social Engineering Tactics:** `["trust_exploitation", "urgency", "false_legitimacy"]`

```text
Message Alert: Your son has encountered hardware decimation on his cellular terminal and established an ad-hoc session. Due to mandatory clearance deadlines for his tenancy covenant, a remittance of 950 credits is urgently sought via Quantum Vault at https://transfers.quantum-vault.example/emergency-clearing.
```

---

### Subtype: `recovery_support`
- **Record ID:** `LLM-SCAM-02515`
- **Writing Style:** `direct_terse` | **Channel:** `notification` | **Partition:** `test`
- **Scenario Family:** `unclaimed_property_vault_retrieval`
- **Primary Intent:** `obtain_credentials_or_codes`
- **Intent Evidence Text:** `Confirm ownership code and security PIN immediately to halt forfeiture: https://vault-retrieval.beacon-fin.example/verify`
- **Social Engineering Tactics:** `["urgency", "fear_or_threat", "scarcity"]`

```text
Beacon Financial Alert: Dormant safety vault unit #882-B marked for state liquidation. Unclaimed valuation: $24,850. Confirm ownership code and security PIN immediately to halt forfeiture: https://vault-retrieval.beacon-fin.example/verify.
```

---

### Subtype: `charity_donation`
- **Record ID:** `LLM-SCAM-02675`
- **Writing Style:** `casual_informal` | **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `homeless_veterans_holiday_meals`
- **Primary Intent:** `induce_payment_or_transfer`
- **Intent Evidence Text:** `chip in here real quick if u can: https://holidaymeals.vetcare-aid.example/donate`
- **Social Engineering Tactics:** `["urgency", "emotional_manipulation", "trust_exploitation"]`

```text
hey friend!! we're setting up hot thanksgiving plates for homeless vets downtown tomorrow. even $10 feeds two guys who served our country. chip in here real quick if u can: https://holidaymeals.vetcare-aid.example/donate
```

---
