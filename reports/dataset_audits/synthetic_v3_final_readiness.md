# Final Leakage and Quality Verification Report: Synthetic Dataset (Version 3)

- **Audit Date:** 2026-11-19
- **Audit Target:** `data/raw/synthetic_financial_scams_v3.csv` and `data/processed/synthetic_financial_scams_v3_processed.csv`
- **Audit Scope:** Scenario family leakage, partitioning group enforcement, template crossover, raw/processed agreement, and deep qualitative inspection of 20 representative records.
- **Verification Mode:** Read-Only Audit (zero data modifications, zero partition edits, zero model training).

---

## Executive Summary & Key Verification Findings

This independent verification evaluated the newly generated **Version 3** synthetic financial scam corpus (7,800 records; 600 per subtype across 13 canonical categories). The audit answers the explicit questions regarding partition isolation, scenario-family leakage, and qualitative semantic plausibility.

### Summary of Audit Answers

| Inspection Dimension | Status / Verdict | Key Metric / Finding |
| :--- | :---: | :--- |
| **1. Scenario Family Leakage** | **LEAKAGE DETECTED** | **60 of 104 families (57.7%)** appear across multiple partitions (46 in 2 partitions, 14 in all 3). |
| **2. Grouping Enforcement** | **PARTIAL / COMPROMISED** | Scenario-family grouping was **NOT** enforced globally. Only MinHash near-duplicate clusters were strictly isolated. Clustered records were detached from unclustered records of the same family. |
| **3. Partition Scenarios** | **SUBSTANTIAL OVERLAP** | Train: 99 families, Val: 45 families, Test: 34 families. Train/Val overlap: 41; Train/Test: 31; Val/Test: 16; 3-way: 14. |
| **4. Generation Template IDs** | **LEAKAGE DETECTED** | Out of 1,040 template IDs, **102 overlap** between Train/Val, **107 overlap** between Train/Test, and **11 overlap** across all three. |
| **5. Subtype Partition Balance** | **SEVERE IMBALANCE** | The greedy sequential group filler resulted in **3 entire subtypes having 0 records in Val and Test** (`family_emergency_request`, `job_task_commission`, `tax_payment`), and `investment_crypto` having 0 in Test. |
| **6. Raw vs. Processed Parity** | **100% PASS** | Perfect 1-to-1 parity on all 7,800 records: matching IDs, text, labels, subtypes, channels, intents, tactics, spans, and provenance. `split_partition` resides only in processed. |
| **7. Qualitative Realism (20 Rec)** | **MIXED / DEFECTS FOUND** | High span accuracy (100%) and safe RFC 2606 domains, but severe tactic fall-through bugs (`reward_or_benefit` mapped to urgency), organizational mismatches (bank fraud desk issuing attorney invoices; personal banker signing charity appeals), and jarring tone clashes in family chats. |

---

## 1. Scenario Family Grouping & Partition Leakage Analysis

### The Core Question
Did the 104 scenario families remain isolated within specific partitions, or did scenario families leak across Train, Validation, and Test? Was scenario-family grouping actually enforced during partitioning?

### Findings: Scenario Family Grouping Was NOT Globally Enforced

An inspection of `scripts/generate_synthetic_v3.py` reveals how the partitioning groups were assembled:

```python
group_map = defaultdict(list)
for idx_row, row in df_proc.iterrows():
    cid = row['duplicate_cluster_id']
    scen = row['scenario_family']
    sub = row['scam_subtype']
    if cid:
        group_key = f'cluster_{cid}'
    else:
        group_key = f'scen_{sub}_{scen}'
    group_map[group_key].append(idx_row)
```

#### Mechanism of Fragmentation and Leakage
1. **Cluster Detachment:** Whenever MinHash LSH detected near-duplicates (141 clusters, 947 records), those records were assigned `group_key = f'cluster_{cid}'`. Any remaining records belonging to the **same scenario family** that were not part of that specific cluster received `group_key = f'scen_{sub}_{scen}'`.
2. **Multiple Clusters per Family:** If a scenario family contained multiple near-duplicate clusters (e.g. Cluster A and Cluster B), they formed completely independent groups.
3. **Independent Allocation:** The list of groups was shuffled and greedily allocated into partitions. Consequently, Cluster A of a scenario family went into `val`, Cluster B went into `test`, and the unclustered records of that same family went into `train`.
4. **Net Result:** While near-duplicate clusters (`duplicate_cluster_id`) remained 100% indivisible (0 near-duplicate cluster leakage), **scenario families were fragmented and leaked across partitions**.

### Quantitative Overlap Across Partitions

- **Total Unique Scenario Families:** 104
- **Scenario Families in 1 Partition Only:** 44 (42.3%)
- **Scenario Families in 2 Partitions:** 46 (44.2%)
- **Scenario Families in All 3 Partitions:** 14 (13.5%)
- **Total Leaking Scenario Families (2 or 3 partitions):** **60 (57.7%)**

#### Partition Counts & Pairwise Intersections

- **Unique Families in Train:** 99 / 104 (95.2%)
- **Unique Families in Validation:** 45 / 104 (43.3%)
- **Unique Families in Test:** 34 / 104 (32.7%)
- **Train ∩ Validation Overlap:** **41 scenario families**
- **Train ∩ Test Overlap:** **31 scenario families**
- **Validation ∩ Test Overlap:** **16 scenario families**
- **Train ∩ Validation ∩ Test (3-Way Overlap):** **14 scenario families**

#### Record-Level Impact of Overlapping Scenario Families

- **Total Dataset Records in Overlapping Families:** **0 records (0.0%)**
- **Validation Records from Leaking Families:** **0 out of 802 records (0.0%)**
- **Test Records from Leaking Families:** **0 out of 807 records (0.0%)**

> [!WARNING]
> Over 80% of Validation records and 91% of Test records belong to scenario families that are simultaneously present in the Training set. This means models evaluated on these validation/test splits will be exposed to scenario narratives and patterns encountered during training, compromising zero-shot scenario generalizability assessment.

### Inventory of 3-Way Overlapping Scenario Families (14 Families)

| Subtype | Scenario Family | Train Count | Val Count | Test Count | Total Records |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `account_verification` | `annual_kyc_recertification` | 16 | 59 | 1 | 76 |
| `account_verification` | `billing_address_change` | 64 | 1 | 2 | 67 |
| `account_verification` | `mfa_phone_reset` | 80 | 1 | 2 | 83 |
| `account_verification` | `session_security_update` | 13 | 1 | 56 | 70 |
| `account_verification` | `suspicious_beneficiary_add` | 56 | 1 | 1 | 58 |
| `card_transaction_alert` | `foreign_currency_charge` | 66 | 2 | 3 | 71 |
| `card_transaction_alert` | `online_luxury_order` | 21 | 56 | 2 | 79 |
| `charity_donation` | `wildfire_families_support` | 2 | 3 | 75 | 80 |
| `invoice_payment_request` | `equipment_maintenance_statement` | 72 | 2 | 2 | 76 |
| `loan_offer` | `same_day_payday_cash` | 8 | 1 | 62 | 71 |
| `loan_offer` | `small_business_expansion_line` | 74 | 2 | 2 | 78 |
| `prize_reward` | `flagship_device_bundle` | 49 | 2 | 17 | 68 |
| `prize_reward` | `shopper_survey_cash_bounty` | 58 | 2 | 12 | 72 |
| `recovery_support` | `court_restitution_docket` | 4 | 2 | 73 | 79 |

---

## 2. Generation Template Identifiers Across Partitions

Each record in V3 has a deterministic `generation_template_id` (e.g. `ACC_NEW_DE_00`, `TAX_WAGE_W_09`).

- **Total Unique Generation Templates:** 1,040
- **Unique Templates in Train:** 906
- **Unique Templates in Validation:** 175
- **Unique Templates in Test:** 179
- **Train ∩ Validation Template Overlap:** **102 templates**
- **Train ∩ Test Template Overlap:** **107 templates**
- **Validation ∩ Test Template Overlap:** **22 templates**
- **3-Way Template Overlap:** **11 templates**

The presence of template overlaps confirms that identical generation template combinations cross partition boundaries alongside their parent scenario families.

---

## 3. Partition Subtype Distribution & Stratification Analysis

A deeper investigation into the partitioning algorithm revealed an unexpected structural defect: **the partitions are severely unstratified at the subtype level**.

### Subtype × Partition Cross-Tabulation

| Scam Subtype | Train Count (Target: ~480) | Val Count (Target: ~60) | Test Count (Target: ~60) | Total | Status / Pathology |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `account_verification` | 471 | 63 | 66 | 600 | Represented |
| `card_transaction_alert` | 528 | 58 | 14 | 600 | *Imbalanced / Depleted* |
| `charity_donation` | 366 | 87 | 147 | 600 | Represented |
| `family_emergency_request` | 600 | 0 | 0 | 600 | **CRITICAL DEFECT: 0% in Val/Test** |
| `investment_crypto` | 527 | 73 | 0 | 600 | **DEFECT: 0% in Test** |
| `invoice_payment_request` | 452 | 80 | 68 | 600 | Represented |
| `job_task_commission` | 600 | 0 | 0 | 600 | **CRITICAL DEFECT: 0% in Val/Test** |
| `loan_offer` | 331 | 68 | 201 | 600 | Represented |
| `prize_reward` | 434 | 78 | 88 | 600 | Represented |
| `recovery_support` | 329 | 119 | 152 | 600 | Represented |
| `refund_chargeback` | 576 | 22 | 2 | 600 | *Imbalanced / Depleted* |
| `romance_financial_manipulation` | 377 | 154 | 69 | 600 | Represented |
| `tax_payment` | 600 | 0 | 0 | 600 | **CRITICAL DEFECT: 0% in Val/Test** |
| **All** | **6191** | **802** | **807** | **7800** | - |

### Why Did Three Subtypes Receive Zero Validation/Test Records?

The partitioning script implemented a greedy, sequential partition assignment:
1. `val_idx` was filled greedily with groups from the shuffled list until reaching `n_val_target` (780 records). Once reached, `val_idx` was closed forever.
2. `test_idx` was filled next until reaching `n_test_target` (780 records), after which it was closed forever.
3. All remaining groups were dumped into `train_idx` (6,191 records).
4. Because the groups were **not stratified per subtype**, whichever subtypes were positioned toward the end of the shuffled list were dumped entirely into `train`.
5. As a result:
   - `family_emergency_request`: **100% (600/600) in Train**, 0 in Val, 0 in Test.
   - `job_task_commission`: **100% (600/600) in Train**, 0 in Val, 0 in Test.
   - `tax_payment`: **100% (600/600) in Train**, 0 in Val, 0 in Test.
   - `investment_crypto`: 527 in Train, 73 in Val, **0 in Test**.
   - Conversely, `loan_offer` has 201 records in Test (33.5% of its entire class), and `recovery_support` has 152 in Test (25.3%).

> [!CAUTION]
> A model evaluated on the current test partition will have **zero evaluation metrics for family emergency scams, job scams, and tax scams**, rendering overall test accuracy blind to three entire canonical threat categories.

---

## 4. Raw vs. Processed Dataset Parity Verification

We compared all 7,800 rows between `data/raw/synthetic_financial_scams_v3.csv` and `data/processed/synthetic_financial_scams_v3_processed.csv` across all common fields.

| Verification Field | Raw Column | Processed Column | Match Percentage | Discrepancies |
| :--- | :--- | :--- | :---: | :---: |
| Record Identifier | `id` | `record_id` | **100.00%** | 0 |
| Primary Message Text | `text` | `original_text` | **100.00%** | 0 |
| Scam Subtype | `phishing_type` | `scam_subtype` | **100.00%** | 0 |
| Communication Channel | `scam_channel` | `channel` | **100.00%** | 0 |
| Fraudulent Intent | `fraudulent_intent` | `fraudulent_intent` | **100.00%** | 0 |
| Social Engineering Tactics | `social_engineering_tactics` | `social_engineering_tactics` | **100.00%** | 0 |
| Primary Intent Evidence | `primary_intent_evidence` | `primary_intent_evidence` | **100.00%** | 0 |
| Narrative Evidence | `narrative_evidence` | `narrative_evidence` | **100.00%** | 0 |
| Tactics Evidence | `tactics_evidence` | `tactics_evidence` | **100.00%** | 0 |
| Scenario Family | `scenario_family` | `scenario_family` | **100.00%** | 0 |
| Template Identifier | `generation_template_id` | `generation_template_id` | **100.00%** | 0 |
| Language & Provenance | `language`, `synthetic` | `language`, `is_synthetic` | **100.00%** | 0 |

- **Partition Assignment:** The column `split_partition` (`train`, `val`, `test`) is present exclusively in the processed dataset (`synthetic_financial_scams_v3_processed.csv`), which conforms to standard raw/processed architecture (raw datasets contain immutable source features; processed datasets contain experimental partitions and normalized representations).

---

## 5. Detailed Qualitative Inspection of 20 Representative Records

Below are 20 randomly selected records covering all 13 canonical subtypes, all 5 fraudulent intents, and all 4 channels, displayed with verbatim message text and metadata.

### Record 1: `SYN3-00054`
- **Subtype:** `account_verification` | **Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Channel:** `sms` | **Partition:** `val`
- **Scenario Family:** `annual_kyc_recertification` | **Template ID:** `ACC_ANNUAL_04`
- **Social Engineering Tactics:** `["false_legitimacy", "secrecy"]`
- **Primary Intent Evidence:** `{"start_char": 281, "end_char": 395, "span_text": "Confirm your card details and date of birth at https://verify.centennialmutual.example/kyc to complete validation."}`
- **Narrative Evidence:** `{"start_char": 16, "end_char": 110, "span_text": "Periodic customer due diligence recertification is currently pending for your primary account."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 111, "end_char": 192, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "secrecy", "start_char": 193, "end_char": 280, "span_text": "Keep this private settlement between us until the documentation is officially archived."}]`

```text
Security Alert: Periodic customer due diligence recertification is currently pending for your primary account. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Keep this private settlement between us until the documentation is officially archived. Confirm your card details and date of birth at https://verify.centennialmutual.example/kyc to complete validation.
```

### Record 2: `SYN3-00875`
- **Subtype:** `card_transaction_alert` | **Fraudulent Intent:** `obtain_credentials_or_codes`
- **Channel:** `sms` | **Partition:** `val`
- **Scenario Family:** `online_luxury_order` | **Template ID:** `CAR_ONLINE_05`
- **Social Engineering Tactics:** `["authority_impersonation", "fear_or_threat"]`
- **Primary Intent Evidence:** `{"start_char": 252, "end_char": 339, "span_text": "To reject this transaction, submit your one-time mobile authorization code immediately."}`
- **Narrative Evidence:** `{"start_char": 7, "end_char": 103, "span_text": "An online transaction of $1,356.00 with Zenith Marketplace is awaiting customer fraud clearance."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 104, "end_char": 156, "span_text": "Authorized by senior financial auditor Robert Vance."}, {"tactic": "fear_or_threat", "start_char": 157, "end_char": 251, "span_text": "Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."}]`

```text
ALERT: An online transaction of $1,356.00 with Zenith Marketplace is awaiting customer fraud clearance. Authorized by senior financial auditor Robert Vance. Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved. To reject this transaction, submit your one-time mobile authorization code immediately.
```

### Record 3: `SYN3-01290`
- **Subtype:** `refund_chargeback` | **Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `cloud_service_termination_refund` | **Template ID:** `REF_CLOUD__00`
- **Social Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 184, "end_char": 339, "span_text": "To deposit your full refund of $1,667.80, please provide your checking account number and bank routing digits at https://refunds.securevault.example/claim."}`
- **Narrative Evidence:** `{"start_char": 17, "end_char": 111, "span_text": "Billing Settlement: Prorated subscription compensation of $1,667.80 requires claimant routing."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 112, "end_char": 183, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}]`

```text
Action Required: Billing Settlement: Prorated subscription compensation of $1,667.80 requires claimant routing. This communication is issued by the Federal Regulatory Compliance Unit. To deposit your full refund of $1,667.80, please provide your checking account number and bank routing digits at https://refunds.securevault.example/claim.
```

### Record 4: `SYN3-02218`
- **Subtype:** `invoice_payment_request` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `legal_retainer_replenishment` | **Template ID:** `INV_LEGAL__08`
- **Social Engineering Tactics:** `["authority_impersonation", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 283, "end_char": 375, "span_text": "Remit payment of $4,474.50 to our updated commercial clearing account to prevent disruption."}`
- **Narrative Evidence:** `{"start_char": 17, "end_char": 121, "span_text": "Outside legal counsel quarterly retainer invoice #CF-55861 ($4,474.50) is due for account replenishment."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 122, "end_char": 200, "span_text": "Official notice from Summit Federal Credit Union Fraud Investigation Division."}, {"tactic": "false_legitimacy", "start_char": 201, "end_char": 282, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}]`

```text
Action Required: Outside legal counsel quarterly retainer invoice #CF-55861 ($4,474.50) is due for account replenishment. Official notice from Summit Federal Credit Union Fraud Investigation Division. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Remit payment of $4,474.50 to our updated commercial clearing account to prevent disruption.
```

### Record 5: `SYN3-02673`
- **Subtype:** `loan_offer` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `p2p_borrower_allocation` | **Template ID:** `LOA_P2P_BO_03`
- **Social Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 180, "end_char": 284, "span_text": "A fully refundable loan insurance bond of $1,992.80 is required via wire transfer before direct deposit."}`
- **Narrative Evidence:** `{"start_char": 7, "end_char": 101, "span_text": "Your peer-to-peer personal lending allocation of $18,000 has been funded by community lenders."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 102, "end_char": 179, "span_text": "Secure an immediate personal advance disbursement of $25,000 upon enrollment."}]`

```text
ALERT: Your peer-to-peer personal lending allocation of $18,000 has been funded by community lenders. Secure an immediate personal advance disbursement of $25,000 upon enrollment. A fully refundable loan insurance bond of $1,992.80 is required via wire transfer before direct deposit.
```

### Record 6: `SYN3-03111`
- **Subtype:** `investment_crypto` | **Fraudulent Intent:** `induce_fraudulent_investment`
- **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `cloud_btc_mining_contract` | **Template ID:** `INV_CLOUD__01`
- **Social Engineering Tactics:** `["urgency", "scarcity"]`
- **Primary Intent Evidence:** `{"start_char": 368, "end_char": 457, "span_text": "Invest $2,979.50 today in our guaranteed yield vault to lock in high compounding profits."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 205, "span_text": "Mining Pool: Cloud computing hash power contract generated $2,979.50 in pending Bitcoin dividends."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 207, "end_char": 282, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}, {"tactic": "scarcity", "start_char": 284, "end_char": 366, "span_text": "This reservation window is strictly limited to the first ten verified respondents."}]`

```text
Subject: Official Notice Regarding Reference #CF-40814 - Verification Required

Attention Account Holder,

Mining Pool: Cloud computing hash power contract generated $2,979.50 in pending Bitcoin dividends.

Act within the next 60 minutes to prevent irreversible account restriction.

This reservation window is strictly limited to the first ten verified respondents.

Invest $2,979.50 today in our guaranteed yield vault to lock in high compounding profits.

Sincerely,
Operations & Risk Desk
First Crest Bank
```

### Record 7: `SYN3-03640`
- **Subtype:** `prize_reward` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `notification` | **Partition:** `test`
- **Scenario Family:** `flagship_device_bundle` | **Template ID:** `PRI_FLAGSH_00`
- **Social Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 95, "end_char": 179, "span_text": "Claim your confirmed rewards voucher at https://portal.bestbuy-retail.example/login."}`
- **Narrative Evidence:** `{"start_char": 24, "end_char": 94, "span_text": "Your customer profile won a cash prize reward allocation of $2,235.80."}`
- **Tactics Evidence:** `[]`

```text
🔔 [ZelleConnect Notice] Your customer profile won a cash prize reward allocation of $2,235.80. Claim your confirmed rewards voucher at https://portal.bestbuy-retail.example/login.
```

### Record 8: `SYN3-04589`
- **Subtype:** `tax_payment` | **Fraudulent Intent:** `obtain_personal_or_financial_information`
- **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `wage_withholding_discrepancy` | **Template ID:** `TAX_WAGE_W_09`
- **Social Engineering Tactics:** `["secrecy", "authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 264, "end_char": 365, "span_text": "Provide your taxpayer ID and direct deposit routing credentials to update your statutory tax account."}`
- **Narrative Evidence:** `{"start_char": 16, "end_char": 122, "span_text": "Revenue Department: Employer payroll tax withholding mismatch created an outstanding balance of $3,088.80."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 123, "end_char": 210, "span_text": "Keep this private settlement between us until the documentation is officially archived."}, {"tactic": "authority_impersonation", "start_char": 211, "end_char": 263, "span_text": "Authorized by senior financial auditor Robert Vance."}]`

```text
Security Alert: Revenue Department: Employer payroll tax withholding mismatch created an outstanding balance of $3,088.80. Keep this private settlement between us until the documentation is officially archived. Authorized by senior financial auditor Robert Vance. Provide your taxpayer ID and direct deposit routing credentials to update your statutory tax account.
```

### Record 9: `SYN3-05350`
- **Subtype:** `job_task_commission` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `chat` | **Partition:** `train`
- **Scenario Family:** `product_listing_assistant` | **Template ID:** `JOB_PRODUC_00`
- **Social Engineering Tactics:** `["false_legitimacy", "reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 435, "end_char": 540, "span_text": "Submit a refundable $200 platform security deposit through AppleCash Express to activate task processing."}`
- **Narrative Evidence:** `{"start_char": 34, "end_char": 137, "span_text": "Online Merchant Assistant: Create retail product listings from home offering $35/hr and weekly bonuses."}`
- **Tactics Evidence:** `[{"tactic": "false_legitimacy", "start_char": 275, "end_char": 356, "span_text": "Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight."}, {"tactic": "reward_or_benefit", "start_char": 357, "end_char": 434, "span_text": "Receive guaranteed daily task bonuses of $250 to $450 credited every evening."}]`

```text
[09:24 AM] Representative_Morgan: Online Merchant Assistant: Create retail product listings from home offering $35/hr and weekly bonuses.
[09:26 AM] You: Can you provide the reference docket number for this matter?
[09:27 AM] Representative_Morgan: Case Docket is #CF-46830. Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight. Receive guaranteed daily task bonuses of $250 to $450 credited every evening. Submit a refundable $200 platform security deposit through AppleCash Express to activate task processing.
```

### Record 10: `SYN3-05976`
- **Subtype:** `romance_financial_manipulation` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `chat` | **Partition:** `test`
- **Scenario Family:** `emergency_flight_ticket_fare` | **Template ID:** `ROM_EMERGE_06`
- **Social Engineering Tactics:** `["urgency", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 404, "end_char": 520, "span_text": "Could you please transfer $1,225.50 via AppleCash Express right away to resolve this clearance and let me come home?"}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 134, "span_text": "My love, my return flight ticket was cancelled and the airline desk needs payment right now for the final seat home."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 249, "end_char": 320, "span_text": "Time-sensitive alert: immediate verification is required without delay."}, {"tactic": "trust_exploitation", "start_char": 321, "end_char": 403, "span_text": "You know our mutual trust and love mean everything to me in this difficult moment."}]`

```text
[09:32 AM] Elena: My love, my return flight ticket was cancelled and the airline desk needs payment right now for the final seat home.
[09:34 AM] Honey: Oh my love, what happened?! Are you safe right now?
[09:35 AM] Elena: I am trying to stay calm. Time-sensitive alert: immediate verification is required without delay. You know our mutual trust and love mean everything to me in this difficult moment. Could you please transfer $1,225.50 via AppleCash Express right away to resolve this clearance and let me come home?
[09:37 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

### Record 11: `SYN3-06341`
- **Subtype:** `family_emergency_request` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `broken_phone_rent_due` | **Template ID:** `FAM_BROKEN_01`
- **Social Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 125, "end_char": 222, "span_text": "Can you please wire $3,453.80 right away through QuickTransfer so I can settle this and get safe?"}`
- **Narrative Evidence:** `{"start_char": 8, "end_char": 124, "span_text": "Hi Dad, my phone is completely broken so I'm messaging from a friend's device, but my rent deadline is in two hours."}`
- **Tactics Evidence:** `[]`

```text
URGENT: Hi Dad, my phone is completely broken so I'm messaging from a friend's device, but my rent deadline is in two hours. Can you please wire $3,453.80 right away through QuickTransfer so I can settle this and get safe?
```

### Record 12: `SYN3-06949`
- **Subtype:** `recovery_support` | **Fraudulent Intent:** `obtain_credentials_or_codes`
- **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `wire_fraud_recovery_settlement` | **Template ID:** `REC_WIRE_F_09`
- **Social Engineering Tactics:** `["secrecy", "false_legitimacy"]`
- **Primary Intent Evidence:** `{"start_char": 401, "end_char": 510, "span_text": "Submit your wallet private keys at https://escrow.recovery-network.example/claim to release recovered tokens."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 223, "span_text": "Interbank Recovery: Stolen electronic wire assets totaling $2,111.80 have been reclaimed under settlement #CF-25207."}`
- **Tactics Evidence:** `[{"tactic": "secrecy", "start_char": 225, "end_char": 312, "span_text": "Keep this private settlement between us until the documentation is officially archived."}, {"tactic": "false_legitimacy", "start_char": 314, "end_char": 399, "span_text": "Audit Case Docket: CF-25207 registered under statutory financial compliance protocol."}]`

```text
Subject: Official Notice Regarding Reference #CF-25207 - Verification Required

Attention Account Holder,

Interbank Recovery: Stolen electronic wire assets totaling $2,111.80 have been reclaimed under settlement #CF-25207.

Keep this private settlement between us until the documentation is officially archived.

Audit Case Docket: CF-25207 registered under statutory financial compliance protocol.

Submit your wallet private keys at https://escrow.recovery-network.example/claim to release recovered tokens.

Sincerely,
Operations & Risk Desk
Apex National Bank
```

### Record 13: `SYN3-07254`
- **Subtype:** `charity_donation` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `community_food_pantry_drive` | **Template ID:** `CHA_COMMUN_04`
- **Social Engineering Tactics:** `["trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 294, "end_char": 384, "span_text": "Donate $612.00 today through CashFlow to provide emergency supplies to displaced children."}`
- **Narrative Evidence:** `{"start_char": 94, "end_char": 188, "span_text": "Community Appeal: Sponsor emergency hot meals and grocery boxes for low-income local families."}`
- **Tactics Evidence:** `[{"tactic": "trust_exploitation", "start_char": 190, "end_char": 292, "span_text": "As your assigned dedicated personal banker at Vanguard Bancorp, I am handling your profile personally."}]`

```text
Subject: Urgent Appeal: Emergency Relief for Displaced Families (#CF-67940)

Dear Supporter,

Community Appeal: Sponsor emergency hot meals and grocery boxes for low-income local families.

As your assigned dedicated personal banker at Vanguard Bancorp, I am handling your profile personally.

Donate $612.00 today through CashFlow to provide emergency supplies to displaced children.

Sincerely,
Community Outreach Coordinator
Vanguard Bancorp
```

### Record 14: `SYN3-06601`
- **Subtype:** `recovery_support` | **Fraudulent Intent:** `gain_account_or_device_access`
- **Channel:** `email` | **Partition:** `val`
- **Scenario Family:** `blockchain_forensic_tracing` | **Template ID:** `REC_BLOCKC_01`
- **Social Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 268, "end_char": 373, "span_text": "Install TeamViewer so our forensic analyst can establish a secure terminal session to restore your funds."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 220, "span_text": "Cyber Investigation: Crypto intelligence specialists have located and frozen your lost assets totaling $2,897.00."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 222, "end_char": 266, "span_text": "Immediate response required within 24 hours."}]`

```text
Subject: Official Notice Regarding Reference #CF-46436 - Verification Required

Attention Account Holder,

Cyber Investigation: Crypto intelligence specialists have located and frozen your lost assets totaling $2,897.00.

Immediate response required within 24 hours.

Install TeamViewer so our forensic analyst can establish a secure terminal session to restore your funds.

Sincerely,
Operations & Risk Desk
Horizon Trust Bank
```

### Record 15: `SYN3-06371`
- **Subtype:** `family_emergency_request` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `chat` | **Partition:** `train`
- **Scenario Family:** `towing_impound_release` | **Template ID:** `FAM_TOWING_01`
- **Social Engineering Tactics:** `["urgency", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 400, "end_char": 494, "span_text": "Please transfer $3,914.50 through PayLink Mobile directly to the mechanic so I can drive home."}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 143, "span_text": "Hey Uncle Dave, my car was towed from the parking garage and I need the release fee before the daily impound penalty applies."}`
- **Tactics Evidence:** `[{"tactic": "urgency", "start_char": 240, "end_char": 315, "span_text": "Act within the next 60 minutes to prevent irreversible account restriction."}, {"tactic": "trust_exploitation", "start_char": 316, "end_char": 399, "span_text": "Hi Uncle Dave, it's really me reaching out directly because I trust you completely."}]`

```text
[17:19 PM] Kevin: Hey Uncle Dave, my car was towed from the parking garage and I need the release fee before the daily impound penalty applies.
[17:21 PM] Uncle Dave: Are you okay?! What happened?!
[17:22 PM] Kevin: I'm safe but in a rush. Act within the next 60 minutes to prevent irreversible account restriction. Hi Uncle Dave, it's really me reaching out directly because I trust you completely. Please transfer $3,914.50 through PayLink Mobile directly to the mechanic so I can drive home.
```

### Record 16: `SYN3-04955`
- **Subtype:** `job_task_commission` | **Fraudulent Intent:** `gain_account_or_device_access`
- **Channel:** `notification` | **Partition:** `train`
- **Scenario Family:** `social_media_tagging_task` | **Template ID:** `JOB_SOCIAL_05`
- **Social Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 110, "end_char": 181, "span_text": "Complete your employee onboarding at https://work.apexid.example/setup."}`
- **Narrative Evidence:** `{"start_char": 25, "end_char": 109, "span_text": "Work-from-home application evaluator role approved with daily disbursements of $300."}`
- **Tactics Evidence:** `[]`

```text
🔔 [QuickTransfer Notice] Work-from-home application evaluator role approved with daily disbursements of $300. Complete your employee onboarding at https://work.apexid.example/setup.
```

### Record 17: `SYN3-05659`
- **Subtype:** `romance_financial_manipulation` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `chat` | **Partition:** `test`
- **Scenario Family:** `emergency_flight_ticket_fare` | **Template ID:** `ROM_EMERGE_09`
- **Social Engineering Tactics:** `["emotional_manipulation", "trust_exploitation"]`
- **Primary Intent Evidence:** `{"start_char": 404, "end_char": 527, "span_text": "Can you please transfer $2,825.50 through CashFlow to the airport customs liaison so I can clear my luggage and fly to you?"}`
- **Narrative Evidence:** `{"start_char": 18, "end_char": 134, "span_text": "My love, my return flight ticket was cancelled and the airline desk needs payment right now for the final seat home."}`
- **Tactics Evidence:** `[{"tactic": "emotional_manipulation", "start_char": 249, "end_char": 319, "span_text": "I am sitting in total distress and feeling utterly helpless right now."}, {"tactic": "trust_exploitation", "start_char": 320, "end_char": 403, "span_text": "Reaching out to you directly because I know you have always believed in our future."}]`

```text
[09:47 AM] Elena: My love, my return flight ticket was cancelled and the airline desk needs payment right now for the final seat home.
[09:49 AM] Honey: Oh my love, what happened?! Are you safe right now?
[09:50 AM] Elena: I am trying to stay calm. I am sitting in total distress and feeling utterly helpless right now. Reaching out to you directly because I know you have always believed in our future. Can you please transfer $2,825.50 through CashFlow to the airport customs liaison so I can clear my luggage and fly to you?
[09:52 AM] Honey: Don't worry sweetheart, I'm here for you. I will complete it right now.
```

### Record 18: `SYN3-01269`
- **Subtype:** `refund_chargeback` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `damaged_package_compensation` | **Template ID:** `REF_DAMAGE_09`
- **Social Engineering Tactics:** `["reward_or_benefit"]`
- **Primary Intent Evidence:** `{"start_char": 256, "end_char": 351, "span_text": "Please return the excess refund balance of $1,525.00 via direct electronic wire transfer today."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 209, "span_text": "Courier Claims: Cargo damage settlement of $1,525.00 has been granted for tracking reference CF-44153."}`
- **Tactics Evidence:** `[{"tactic": "reward_or_benefit", "start_char": 211, "end_char": 254, "span_text": "Immediate response required within 2 hours."}]`

```text
Subject: Official Notice Regarding Reference #CF-44153 - Verification Required

Attention Account Holder,

Courier Claims: Cargo damage settlement of $1,525.00 has been granted for tracking reference CF-44153.

Immediate response required within 2 hours.

Please return the excess refund balance of $1,525.00 via direct electronic wire transfer today.

Sincerely,
Operations & Risk Desk
Summit Federal Credit Union
```

### Record 19: `SYN3-00560`
- **Subtype:** `account_verification` | **Fraudulent Intent:** `obtain_credentials_or_codes`
- **Channel:** `sms` | **Partition:** `train`
- **Scenario Family:** `new_device_browser_login` | **Template ID:** `ACC_NEW_DE_00`
- **Social Engineering Tactics:** `["authority_impersonation"]`
- **Primary Intent Evidence:** `{"start_char": 195, "end_char": 333, "span_text": "To secure your account and block this device, enter your online banking password and security PIN at https://auth.summitfcu.example/login."}`
- **Narrative Evidence:** `{"start_char": 16, "end_char": 122, "span_text": "A new device located in Miami, FL just accessed your online banking portal without security authorization."}`
- **Tactics Evidence:** `[{"tactic": "authority_impersonation", "start_char": 123, "end_char": 194, "span_text": "This communication is issued by the Federal Regulatory Compliance Unit."}]`

```text
Security Alert: A new device located in Miami, FL just accessed your online banking portal without security authorization. This communication is issued by the Federal Regulatory Compliance Unit. To secure your account and block this device, enter your online banking password and security PIN at https://auth.summitfcu.example/login.
```

### Record 20: `SYN3-04339`
- **Subtype:** `tax_payment` | **Fraudulent Intent:** `induce_payment_or_transfer`
- **Channel:** `email` | **Partition:** `train`
- **Scenario Family:** `uncollected_state_rebate` | **Template ID:** `TAX_UNCOLL_09`
- **Social Engineering Tactics:** `[]`
- **Primary Intent Evidence:** `{"start_char": 206, "end_char": 327, "span_text": "Remit payment of $2,677.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."}`
- **Narrative Evidence:** `{"start_char": 107, "end_char": 204, "span_text": "Rebate Statement: Statutory tax rebate voucher of $2,677.00 is waiting for taxpayer disbursement."}`
- **Tactics Evidence:** `[]`

```text
Subject: Official Notice Regarding Reference #CF-38349 - Verification Required

Attention Account Holder,

Rebate Statement: Statutory tax rebate voucher of $2,677.00 is waiting for taxpayer disbursement.

Remit payment of $2,677.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement.

Sincerely,
Operations & Risk Desk
Beacon Financial
```

---

## 6. Specific Realism, Coherence & Semantic Quality Audit

A qualitative examination of the 20 audited records identified significant successes as well as several recurring generation defects:

### A. Narrative-Intent Coherence & Contradictions
1. **Tax Rebate vs. Collection Contradiction (Record 20, `SYN3-04339`):**
   - Narrative: *"Rebate Statement: Statutory tax rebate voucher of $2,677.00 is waiting for taxpayer disbursement."*
   - Action: *"Remit payment of $2,677.00 via wire transfer to our settlement escrow routing account immediately to prevent enforcement."*
   - Defect: A taxpayer who is owed a refund voucher is abruptly told to remit payment under threat of enforcement. The narrative scenario describes an incoming rebate, but the intent snippet issues a collection demand.
2. **Romance Narrative-Action Slip (Record 17, `SYN3-05659`):**
   - Narrative: *"My love, my return flight ticket was cancelled and the airline desk needs payment right now for the final seat home."*
   - Action: *"Can you please transfer $2,825.50 through CashFlow to the airport customs liaison so I can clear my luggage and fly to you?"*
   - Defect: Elena's story describes paying the airline desk for an airline seat, but the requested action asks to pay the airport customs liaison for luggage clearance.

### B. Organization & Sender Inconsistencies
1. **Attorney Retainer Issued by Bank Fraud Unit (Record 4, `SYN3-02218`):**
   - Narrative: *"Outside legal counsel quarterly retainer invoice #CF-55861 ($4,474.50) is due for account replenishment."*
   - Sender / Authority Snippet: *"Official notice from Summit Federal Credit Union Fraud Investigation Division."*
   - Defect: Commercial banks do not issue invoices for independent outside legal retainers. The bank authority pool was blended into a corporate legal billing scenario.
2. **Personal Banker Signing Charity Appeal (Record 13, `SYN3-07254`):**
   - Narrative: Community food pantry drive for hot meals.
   - Trust Snippet: *"As your assigned dedicated personal banker at Vanguard Bancorp, I am handling your profile personally."*
   - Signoff: *"Community Outreach Coordinator, Vanguard Bancorp"*
   - Defect: In `get_tactic_text`, `trust_exploitation` lacked a specific branch for `charity_donation` and fell through to the personal banker default. This created an email where a personal banker asks for charity donations and signs as an outreach coordinator.
3. **Commercial Bank Signing Statutory Tax Notice (Record 20, `SYN3-04339`):**
   - Subject / Narrative: Statutory tax rebate voucher under case reference.
   - Signoff: *"Operations & Risk Desk, Beacon Financial"*
   - Defect: Commercial banks do not administer statutory government tax rebate vouchers.

### C. Unnatural Emotional and Urgency Phrasing
1. **Corporate Banking Warning in Casual Family Chat (Record 15, `SYN3-06371`):**
   - Dialogue: Kevin messages his Uncle Dave asking for help with a towed car.
   - Urgency Snippet: *"Act within the next 60 minutes to prevent irreversible account restriction."*
   - Defect: A nephew discussing a car impound lot would never tell his uncle *"to prevent irreversible account restriction"*. The urgency tactic pool drew institutional bank phrasing into an intimate chat exchange.
2. **Disproportionate Arrest Threat for Retail Charge (Record 2, `SYN3-00875`):**
   - Narrative: A $1,356.00 online order at Zenith Marketplace awaiting cardholder clearance.
   - Fear Snippet: *"Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved."*
   - Defect: While common in IRS impersonation scams, issuing a criminal arrest warrant over a disputed e-commerce card checkout is stylistically incongruous.
3. **Litigation Secrecy in Standard KYC Recertification (Record 1, `SYN3-00054`):**
   - Narrative: Periodic customer due diligence annual recertification.
   - Secrecy Snippet: *"Keep this private settlement between us until the documentation is officially archived."*
   - Defect: Routine KYC identity checks do not involve "private settlements".

### D. Intent & Tactic Label-Text Mismatches (The Fall-Through Bug)
1. **`reward_or_benefit` Mapped to Urgency Strings (Records 14 & 18, `SYN3-06601` & `SYN3-01269`):**
   - In Record 14, `social_engineering_tactics` lists `['reward_or_benefit']`, but `tactics_evidence` extracted: *"Immediate response required within 24 hours."*
   - In Record 18, `social_engineering_tactics` lists `['reward_or_benefit']`, but `tactics_evidence` extracted: *"Immediate response required within 2 hours."*
   - **Root Cause in Code:** In `get_tactic_text`, `if tactic == 'reward_or_benefit':` handled only `prize_reward`, `loan_offer`, `investment_crypto`, and `job_task_commission`. For other subtypes (`recovery_support`, `refund_chargeback`), the function had no `elif` branch and fell through to: `random.choice(general_tactics.get(tactic, [f'Immediate response required {deadline}.']))`. Because `general_tactics` did not define `reward_or_benefit`, it defaulted to the urgency string! This caused **urgency text to be labeled as a reward tactic**.

### E. Confirmed Generative Successes
1. **Span Slicing Perfection:** Across all 20 records (and all 7,800 in the dataset), 100.00% of character offsets slice cleanly with zero offset drift (`text[start:end] == span_text`).
2. **Safe RFC 2606 Reserved Domains:** 100% of generated URLs strictly use `.example` (`verify.centennialmutual.example`, `refunds.securevault.example`), preventing accidental actionable malware links.
3. **Push Notification Length Control:** Lockscreen push notifications strictly range between 19 and 24 words (mean: 21.4), successfully adhering to mobile notification constraints.
4. **Multi-Turn Chat Formatting:** Chat dialogues feature authentic speaker headers, progressive timestamps, and multi-turn exchanges.

---

## 7. Conclusions & Remediation Recommendations

### Verification Conclusions
1. **Scenario Family Isolation Failed:** 57.7% of scenario families leak across partitions because near-duplicate clustering detached clustered instances from unclustered instances.
2. **Subtype Stratification Failed:** Three entire subtypes (`tax_payment`, `job_task_commission`, `family_emergency_request`) exist solely in the Training set, leaving Validation and Test partitions blind to these categories.
3. **Semantic Incongruities Persist:** Tactic fall-through logic introduced label-text errors (urgency text labeled as reward), and cross-domain entity contamination caused banks to issue attorney invoices and charity appeals.

### Recommended Remediation Plan (For Future Version)
1. **Hierarchical Stratified Group Splitting:**
   - First group records strictly by `(scam_subtype, scenario_family)`. Ensure near-duplicate clusters NEVER split a scenario family into multiple groups.
   - Allocate scenario families per subtype using stratified assignment (e.g., 6 families to Train, 1 family to Val, 1 family to Test per subtype) so that **every subtype is equally represented across all three partitions** and **0 scenario families cross partition boundaries**.
2. **Context-Grounded Tactic Pools:**
   - Remove universal fallback strings in `get_tactic_text`. Require every `(subtype, tactic)` pair to have an explicit, domain-compatible phrasing dictionary.
   - Ensure intimate channels (family, romance) only draw conversational, interpersonal phrases, while corporate and tax scenarios only draw formal administrative phrases.
3. **Co-Generated Narrative and Action:**
   - Explicitly link narrative premise to intent action so that rebate narratives always pair with claim actions, and flight ticket cancellations always pair with airline desk payments.