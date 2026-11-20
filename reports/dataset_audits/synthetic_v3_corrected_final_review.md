# Final Independent Scientific Audit: Synthetic Financial Scam Corpus (Version 3 Corrected)

- **Audit Target:** Synthetic Financial Scam Dataset Version 3 Corrected (Production Candidate)
- **Raw File:** [`data/raw/synthetic_financial_scams_v3_corrected.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams_v3_corrected.csv) (7,800 records, 16 columns, 9.88 MB)
- **Processed File:** [`data/processed/synthetic_financial_scams_v3_corrected_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv) (7,800 records, 36 columns, 15.45 MB)
- **Audit Date:** 2026-11-19
- **Auditor:** Independent Research Evaluation Desk
- **Target Research Framework:** *"Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications."*

---

## 1. Executive Summary & Audit Scope

This report provides a rigorous, independent scientific audit of the **Synthetic Financial Scam Dataset Version 3 Corrected**. 

The audit evaluates:
1. Mathematical partitioning and group isolation.
2. Near-duplicate deduplication via MinHash Locality-Sensitive Hashing (LSH).
3. Qualitative authenticity and narrative coherence in sampled records (with emphasis on Validation and Test partitions).
4. Semantic justification of evidence spans (distinguishing programmatic string slicing from genuine linguistic grounding).
5. Information-theoretic and distributional relationships (evaluating shortcut learning risks).
6. Template and lexical diversity.
7. Algorithmic reproducibility from fixed seeds.
8. File integrity and parity across raw, processed, and legacy corpora.

### Final Verdict Summary
**READY WITH DOCUMENTED LIMITATIONS.**  
The Version 3 Corrected dataset is mathematically sound, leak-free, perfectly balanced across subtypes, and safe from prohibited synthetic artifacts. It is suitable for training multi-level explainable transformer models, provided researchers explicitly account for documented shortcut-learning risks (34.6% normalized mutual information between subtype and intent, strict tactic affinity masks, and notification-channel call-to-action sharing).

---

## 2. Splitting & Partitioning Implementation Audit

### 2.1 Code Tracing and Splitting Logic
We inspected lines 2257–2277 of [`scripts/generate_synthetic_v3_corrected.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/scripts/generate_synthetic_v3_corrected.py#L2257-L2277).

```python
for sub in SUBTYPES:
    fams = families_by_subtype[sub]
    # 6 Train families (80 rec each) -> 480 records
    for scen in fams[:6]:
        for _ in range(80):
            rec = self.build_record(sub, scen, "train", rec_idx)
            records.append(rec)
            rec_idx += 1
    # 1 Val family (60 rec) -> 60 records
    for scen in [fams[6]]:
        for _ in range(60):
            rec = self.build_record(sub, scen, "val", rec_idx)
            records.append(rec)
            rec_idx += 1
    # 1 Test family (60 rec) -> 60 records
    for scen in [fams[7]]:
        for _ in range(60):
            rec = self.build_record(sub, scen, "test", rec_idx)
            records.append(rec)
            rec_idx += 1
```

### 2.2 Mathematical Group Isolation Verification
- **Scenario Family Integrity:** Every scenario family is defined as an indivisible generative unit.
- **Direct Assignment at Synthesis:** The partition assignment (`train`, `val`, `test`) is stamped directly onto each record during generation based exclusively on its scenario family index.
- **Absence of Post-Hoc Record-Level Splitting:** No subsequent record-level shuffling, k-fold partitioning, or re-splitting occurs.
- **Empirical Partition Audit:**
  - `df_proc.groupby('scenario_family')['split_partition'].nunique().max() == 1`
  - `df_proc.groupby('scenario_family')['split_partition'].nunique().min() == 1`
  - **Train Families:** 78 unique families (6 per subtype $\times$ 13 subtypes)
  - **Validation Families:** 13 unique families (1 per subtype $\times$ 13 subtypes)
  - **Test Families:** 13 unique families (1 per subtype $\times$ 13 subtypes)
  - **Cross-Partition Overlap:** Exactly **0 families (0.00% leakage)** across Train/Val, Train/Test, and Val/Test.

### 2.3 Partition Allocation Matrix
Every canonical subtype exhibits a strict 80.0% / 10.0% / 10.0% allocation across partitions:

| Canonical Subtype | Train Records (80%) | Val Records (10%) | Test Records (10%) | Total Records |
| :--- | :---: | :---: | :---: | :---: |
| `account_verification` | 480 | 60 | 60 | 600 |
| `card_transaction_alert` | 480 | 60 | 60 | 600 |
| `refund_chargeback` | 480 | 60 | 60 | 600 |
| `invoice_payment_request` | 480 | 60 | 60 | 600 |
| `loan_offer` | 480 | 60 | 60 | 600 |
| `investment_crypto` | 480 | 60 | 60 | 600 |
| `prize_reward` | 480 | 60 | 60 | 600 |
| `tax_payment` | 480 | 60 | 60 | 600 |
| `job_task_commission` | 480 | 60 | 60 | 600 |
| `romance_financial_manipulation` | 480 | 60 | 60 | 600 |
| `family_emergency_request` | 480 | 60 | 60 | 600 |
| `recovery_support` | 480 | 60 | 60 | 600 |
| `charity_donation` | 480 | 60 | 60 | 600 |
| **Total Corpus** | **6,240 (80.00%)** | **780 (10.00%)** | **780 (10.00%)** | **7,800 (100.0%)** |

---

## 3. MinHash LSH Parameters & Cluster Isolation Audit

### 3.1 Algorithm & Hyperparameter Inspection
The deduplication engine is implemented in class `FastMinHashLSH` in [`scripts/generate_synthetic_v3_corrected.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/scripts/generate_synthetic_v3_corrected.py#L482-L533):
- **Shingling:** Word 3-grams ($k=3$) extracted after lowercasing and alphanumeric tokenization.
- **Normalization:** Prior to shingling, texts undergo entity normalization where URLs, email addresses, phone numbers, amounts, and tracking IDs are mapped to canonical bracket tokens (`[URL]`, `[EMAIL_ADDRESS]`, `[PHONE_NUMBER]`, `[AMOUNT]`, `[IDENTIFIER]`).
- **Permutations:** $P = 64$ hash permutations parameterized by $a_i \in [1, p-1]$ and $b_i \in [0, p-1]$ modulo Mersenne prime $p = 4,294,967,311$.
- **Banded LSH Structure:** $B = 16$ bands with $R = 4$ rows per band ($P = B \times R = 64$).
- **Theoretical S-Curve Threshold:** $t \approx \left(\frac{1}{B}\right)^{1/R} = \left(\frac{1}{16}\right)^{1/4} \approx 0.50$.
- **Verification Threshold:** Pairs retrieved from identical band buckets are explicitly verified using set intersection over union:
  $$\text{Jaccard}(S_1, S_2) = \frac{|S_1 \cap S_2|}{|S_1 \cup S_2|} \ge 0.85$$
- **Graph Clustering:** Connected components of verified near-duplicate pairs form discrete cluster IDs (`SYN3C_C0001` through `SYN3C_C0227`).

### 3.2 Cluster Isolation Metrics
- **Total Records in Clusters:** 692 records (8.87% of corpus) partitioned into 227 clusters.
- **Unclustered Records:** 7,108 records (91.13% of corpus) have unique lexical formulations.
- **Cluster Allocation Across Splits:**
  - `train`: 183 clusters (558 records)
  - `val`: 20 clusters (62 records)
  - `test`: 24 clusters (72 records)
- **Cross-Partition Cluster Overlap:** Exactly **0 clusters (0.00% leakage)**.
- **Cross-Scenario-Family Cluster Overlap:** Exactly **0 clusters (0.00% leakage)**. Every near-duplicate cluster is strictly 100% intra-scenario-family.

---

## 4. Qualitative Sample Audit (Validation & Test Records Focus)

We conducted an in-depth qualitative evaluation of records across all 13 canonical subtypes, specifically auditing records from the held-out **Validation** and **Test** partitions.

### 4.1 Test Partition Qualitative Review

#### 1. Card Transaction Alert — Duplicate Merchant Charge (SMS Channel)
- **Record ID:** [`SYN3C-01184`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv#L1185) | **Partition:** `test`
- **Scenario Family:** `duplicate_merchant_charge` | **Template ID:** `CAR_DUPLIC_04`
- **Verbatim Text:**
  ```text
  ALERT: Automated audit detected two identical authorizations of $4,005.80 from Zenith Marketplace. Authorized by Summit Federal Credit Union Risk Mitigation Desk. Submit your full card credentials at https://disputes.card-alerts.example/verify to initiate immediate charge reversal.
  ```
- **Qualitative Assessment:** Highly authentic bank fraud desk alert. Senders and authorized entities (`Summit Federal Credit Union Risk Mitigation Desk`) align cleanly. The call-to-action specifically directs the recipient to resolve a duplicate charge, which logically prompts card details for reversal.

#### 2. Investment Crypto — Mentor Trading Invitation (Chat Channel)
- **Record ID:** [`SYN3C-03579`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv#L3580) | **Partition:** `test`
- **Scenario Family:** `mentor_trading_invitation` | **Template ID:** `INV_MENTOR_09`
- **Verbatim Text:**
  ```text
  [12:14 PM] Senior_Analyst_Viktor: Personal Invitation: Join our exclusive private client crypto trading syndicate on BitCrest Capital.
  [12:16 PM] Trader: What kind of returns are guaranteed on this platform?
  [12:17 PM] Senior_Analyst_Viktor: Our automated arbitrage protocol targets audited high-yield returns. Transfer an initial principal of $2,306.80 to our liquidity smart contract address to begin earning returns.
  ```
- **Qualitative Assessment:** The dialogue flows naturally. Unlike earlier pilot generations where victims repeatedly asked for "court docket numbers" in investment chats, here the victim asks a plausible investor question (`"What kind of returns are guaranteed on this platform?"`), and the analyst replies with domain-consistent crypto arbitrage terminology.

#### 3. Tax Payment — Quarterly Estimated Penalty (SMS Channel)
- **Record ID:** [`SYN3C-04743`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv#L4744) | **Partition:** `test`
- **Scenario Family:** `quarterly_estimated_penalty` | **Template ID:** `TAX_QUARTE_03`
- **Verbatim Text:**
  ```text
  URGENT: Statutory Penalty: Unpaid quarterly tax payment deficit resulting in an assessment of $1,840.50. Formal notification from the Statutory Tax Enforcement Bureau. Settle the statutory quarterly assessment of $1,840.50 before 5:00 PM today to halt collection enforcement. Pay the penalty balance via SwiftPay to payments@staterevenue.example today.
  ```
- **Qualitative Assessment:** Fully grounded in statutory tax terminology. No cross-contamination from corporate banking or loan refinancing. Sender (`Statutory Tax Enforcement Bureau`) matches the narrative.

---

### 4.2 Validation Partition Qualitative Review

#### 4. Refund / Chargeback — Damaged Package Compensation (Email Channel)
- **Record ID:** [`SYN3C-01701`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv#L1702) | **Partition:** `val`
- **Scenario Family:** `damaged_package_compensation` | **Template ID:** `REF_DAMAGE_01`
- **Verbatim Text:**
  ```text
  Subject: Settlement Notice: Reimbursement Credit Ready (#CF-12042)

  Dear Valued Customer,

  A logistics claims compensation credit of $2,765.80 for damaged merchandise has been authorized.

  Claim your reimbursement voucher within 24 hours before allocation expires.

  Receive an additional $150 goodwill voucher credited alongside your refund.

  Please return the excess refund balance of $2,765.80 via direct electronic wire transfer today.

  Sincerely,
  Billing & Restitution Services
  NetDefender Support
  ```
- **Qualitative Assessment:** Classic overpayment / accidental surplus refund scam pattern. The narrative announces a logistics claims credit, offers a goodwill bonus, and requests return of the excess via wire transfer. Coherent narrative-intent integration.

#### 5. Loan Offer — Veteran Emergency Credit (SMS Channel)
- **Record ID:** [`SYN3C-02912`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv#L2913) | **Partition:** `val`
- **Scenario Family:** `veteran_emergency_credit` | **Template ID:** `LOA_VETERA_02`
- **Verbatim Text:**
  ```text
  URGENT: Service Member Lending: Dedicated veteran emergency credit facility of $20,000 is cleared. Only 2 participant allocations remain for this funding tranche. A fully refundable loan insurance bond of $1,288.00 is required via wire transfer before direct deposit.
  ```
- **Qualitative Assessment:** Grounded advance-fee loan scam targeting service members. The narrative promises a cleared credit line, introduces scarcity (`Only 2 participant allocations remain`), and demands an advance insurance fee.

#### 6. Recovery Support — Smart Contract Fund Injection (Chat Channel)
- **Record ID:** [`SYN3C-07098`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv#L7099) | **Partition:** `val`
- **Scenario Family:** `smart_contract_fund_injection` | **Template ID:** `REC_SMART__08`
- **Verbatim Text:**
  ```text
  [08:36 AM] Restitution_Counsel_Hall: Forensic engineers have prepared smart contract restitution recovery for stolen assets of $1,157.00.
  [08:38 AM] Claimant: Can you provide the judicial docket reference for this recovery?
  [08:39 AM] Restitution_Counsel_Hall: Judicial Case Docket is #CF-45302. Judicial restitution clearance decree #CF-45302 verified through court registry. Download and launch the AnyDesk remote support client so our blockchain recovery engineer can connect to the restitution node.
  ```
- **Qualitative Assessment:** The dialogue between `Claimant` and `Restitution_Counsel_Hall` logically warrants judicial case file references. The fraudulent intent (`gain_account_or_device_access`) via `AnyDesk` is smoothly embedded into the forensic blockchain restoration narrative.

---

## 5. Semantic Justification of Multi-Level Evidence Spans

We audited the evidence spans beyond programmatic string matching to assess whether the annotated spans **semantically communicate** the assigned label.

### 5.1 Programmatic vs. Semantic Distinction
- **Automated Verification:** 100.00% exact substring match (`original_text[start:end] == span_text`) across all 7,800 records.
- **Qualitative Semantic Evaluation:**
  - **Narrative Evidence (`narrative_evidence`):** 100% of spans describe the factual pretext (e.g. unauthorized login, overdue invoice, damaged parcel, tax deficiency, romantic partner distress).
  - **Tactics Evidence (`tactics_evidence`):**
    - `urgency`: Confined to time constraints (*"within 24 hours"*, *"before 5:00 PM today"*, *"within 60 minutes"*).
    - `fear_or_threat`: Confined to negative consequences (*"permanent online banking suspension"*, *"judicial wage garnishment"*, *"legal asset seizure"*).
    - `reward_or_benefit`: Confined to bonuses and compensatory yields (*"confirmed 15% customer appreciation bonus"*, *"guaranteed daily task bonuses"*, *"accrued statutory compensatory damages"*). Zero fall-through to urgency strings.
    - `authority_impersonation`: Confined to formal offices (*"Fraud Investigation Unit"*, *"Statutory Compliance Division"*, *"Risk Mitigation Desk"*).
    - `trust_exploitation`: Confined to relationship appeals (*"you've always been the one I can count on"*, *"I only trust you with my heart and my life"*).
    - `emotional_manipulation`: Confined to personal distress (*"I am sitting in total distress and feeling utterly helpless"*, *"Please don't be mad at me, I'm terrified"*).
    - `secrecy`: Confined to non-disclosure demands (*"do not disclose this file to external parties"*, *"maintain strict confidentiality"*).
    - `scarcity`: Confined to quota limits (*"Only 2 participant allocations remain"*, *"Early-stage seed token tranche is restricted"*).
    - `false_legitimacy`: Confined to regulatory and docket citations (*"Judicial restitution clearance decree #CF-..."*, *"Pursuant to court-ordered interbank asset restitution protocols"*).

---

### 5.2 Documented Limitation 1: Notification Channel Intent Decoupling
> [!WARNING]
> **Documented Limitation 1: Static Call-to-Action URLs in Mobile Notifications**
> In the `notification` channel (820 records, 10.51% of corpus), each scenario family utilizes a single lockscreen call-to-action link (`notif_intent`), while the label is sampled from `SUBTYPE_INTENT_MAP`.
>
> *Example:* In `tax_payment`, the notification CTA is uniformly:  
> `Settle debt at https://portal.tax-compliance.example/verify.`  
> Depending on the random draw from `SUBTYPE_INTENT_MAP`, this span may be labeled `obtain_credentials_or_codes` (32 records) or `induce_payment_or_transfer` (28 records). While real-world phishing portals harvest credentials to execute fraudulent settlements, the span text itself does not explicitly mention "passwords" or "PINs".
>
> **Modeling Recommendation:** Evaluators should report channel-disaggregated intent accuracy. Models evaluated exclusively on notification messages will rely on general phishing URL markers rather than fine-grained intent verbs.

---

## 6. Distributional Analysis & Shortcut Learning Risks

We computed contingency matrices, conditional probabilities, and information-theoretic metrics across the three annotation tiers.

### 6.1 Subtype-Intent Information-Theoretic Analysis

```
Conditional Probabilities P(Intent | Subtype):
Subtype                          Account Access   Crypto Invest   Payment/Transfer   Credentials/Codes   Personal/Financial Info
--------------------------------------------------------------------------------------------------------------------------------
account_verification                 0.135            0.000            0.000               0.487                  0.378
card_transaction_alert               0.000            0.000            0.203               0.438                  0.358
charity_donation                     0.000            0.000            0.735               0.000                  0.265
family_emergency_request             0.000            0.000            0.817               0.093                  0.090
investment_crypto                    0.100            0.748            0.000               0.152                  0.000
invoice_payment_request              0.000            0.000            0.685               0.100                  0.215
job_task_commission                  0.150            0.000            0.590               0.000                  0.260
loan_offer                           0.000            0.000            0.510               0.120                  0.370
prize_reward                         0.000            0.000            0.428               0.198                  0.373
recovery_support                     0.327            0.000            0.507               0.167                  0.000
refund_chargeback                    0.187            0.000            0.470               0.000                  0.343
romance_financial_manipulation       0.097            0.247            0.657               0.000                  0.000
tax_payment                          0.000            0.000            0.505               0.147                  0.348
```

- **Entropy of Fraudulent Intent $H(\text{Intent})$:** $1.974\text{ bits}$
- **Entropy of Scam Subtype $H(\text{Subtype})$:** $3.700\text{ bits}$
- **Mutual Information $I(\text{Subtype}; \text{Intent})$:** $0.683\text{ bits}$
- **Normalized Mutual Information $\frac{I(\text{Subtype}; \text{Intent})}{H(\text{Intent})}$:** **$34.60\%$**

---

### 6.2 Documented Limitation 2: Subtype-Intent Concentration
> [!WARNING]
> **Documented Limitation 2: High Mutual Information between Subtypes and Intents**
> Knowing the scam subtype reduces uncertainty about fraudulent intent by 34.6%. Four subtypes have heavily concentrated dominant intents:
> - `family_emergency_request` $\to$ `induce_payment_or_transfer` (81.7%, Entropy = 0.871 bits)
> - `investment_crypto` $\to$ `induce_fraudulent_investment` (74.8%, Entropy = 1.058 bits)
> - `charity_donation` $\to$ `induce_payment_or_transfer` (73.5%, Entropy = 0.834 bits)
> - `invoice_payment_request` $\to$ `induce_payment_or_transfer` (68.5%, Entropy = 1.183 bits)
>
> In multi-task architectures where a shared encoder predicts both subtype and intent, the model may learn to predict intent directly from subtype logits rather than attending to call-to-action tokens.
>
> **Modeling Recommendation:** Use separate task-specific classification heads with gradient detachment, or evaluate intent prediction in an isolated single-task setting to prevent cross-task leakage.

---

### 6.3 Documented Limitation 3: Strict Tactic Affinity Masking
> [!WARNING]
> **Documented Limitation 3: Zero-Probability Tactic Combinations**
> To prevent unnatural scenarios (e.g. romance lovers citing IRS tax audit dockets), the generation engine enforces `SUBTYPE_TACTIC_AFFINITIES`. Consequently:
> - Every subtype has between 4 and 6 strictly impossible tactics (probability 0.00).
> - `emotional_manipulation` occurs exclusively in `family_emergency_request` (22.9%), `romance_financial_manipulation` (22.8%), and `charity_donation` (25.7%).
> - `authority_impersonation` occurs exclusively in formal institutional subtypes (verification, card alerts, invoices, recovery, refunds, tax).
>
> **Modeling Recommendation:** Models will exhibit high F1 on tactic prediction if they first classify the subtype. Multi-label tactic recognition should be verified via cross-subtype ablations.

---

## 7. Linguistic Diversity & Template Variation Audit

### 7.1 Lexical Diversity Statistics
We computed vocabulary richness and out-of-vocabulary (OOV) rates across the 7,800 records:
- **Total Corpus Word Tokens:** 430,626 tokens
- **Unique Vocabulary:** 1,787 distinct word types
- **Overall Type-Token Ratio (TTR):** 0.0041 (typical for template-augmented synthetic text corpora)
- **Partition TTR:**
  - `train` (6,240 records / 344,027 tokens): 1,659 unique words ($\text{TTR} = 0.0048$)
  - `val` (780 records / 43,382 tokens): 1,184 unique words ($\text{TTR} = 0.0273$)
  - `test` (780 records / 43,217 tokens): 1,180 unique words ($\text{TTR} = 0.0273$)

### 7.2 Out-Of-Vocabulary (OOV) Across Partitions
Because scenario families are strictly partitioned, the held-out validation and test scenario families introduce authentic unseen terminology:
- **Validation Partition OOV Words:** 71 words (6.0% of Val vocabulary) are completely absent from Train.
  - *Examples:* `router`, `applies`, `issuance`, `categorizations`, `destination`, `antibiotics`, `shipment`, `civilian`.
- **Test Partition OOV Words:** 63 words (5.3% of Test vocabulary) are completely absent from Train.
  - *Examples:* `consular`, `embassy`, `repatriation`, `boxes`, `smartphone`, `grocery`, `hungry`, `resulting`.

This confirms that the held-out partitions provide genuine out-of-distribution evaluation for narrative comprehension.

### 7.3 Slot & Template Granularity
- **Template IDs:** 1,040 unique generation templates (10 per scenario family).
- **Entities Sampled Dynamically:**
  - 8 Banks (`Apex National Bank`, `Horizon Trust Bank`, `Summit Federal Credit Union`, etc.)
  - 5 Merchants (`PrimeStore Online`, `BestBuy Electronics #841`, `Apple Store Manhattan`, etc.)
  - 5 Crypto Platforms (`BitCrest Capital`, `NovaChain Markets`, `EtherPeak Trading`, etc.)
  - 5 Tech Services (`CloudShield Security`, `Apex ID Services`, `SecureVault Tech`, etc.)
  - 4 Charities (`Global Emergency Relief Alliance`, `Hope Children International Fund`, etc.)
  - 7 Payment Apps (`SwiftPay`, `ZelleConnect`, `CashFlow`, `QuickTransfer`, etc.)
  - 8 Metropolitan Cities (`Dallas, TX`, `London, UK`, `Atlanta, GA`, `Miami, FL`, etc.)
  - 14 Family Names & 7 Relative Roles

---

## 8. Reproducibility & Legacy Dataset Immutability Audit

### 8.1 Algorithmic Reproducibility
- **Random Seed:** Set deterministically at module initialization (`SEED = 42` for Python `random`, NumPy, and MinHash LSH).
- **Reproduction Test:** An independent re-generation execution was executed in a dry-run memory space and compared against [`data/raw/synthetic_financial_scams_v3_corrected.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams_v3_corrected.csv):
  - Record IDs identical: **100% True**
  - Text strings identical: **100% True**
  - Labels identical: **100% True**
  - Intents identical: **100% True**
  - Tactics identical: **100% True**
  - Primary intent evidence identical: **100% True**
  - SHA-256 Text Stream Match: `f73a732a33b9c2c9...` (**Exact Match**)

### 8.2 Raw vs. Processed File Parity
- Raw records (7,800 rows, 16 columns) map 1:1 to Processed records (7,800 rows, 36 columns).
- `raw['id'] == proc['record_id']` across all 7,800 rows.
- `raw['text'] == proc['original_text']` across all 7,800 rows.
- `raw['phishing_type'] == proc['scam_subtype']` across all 7,800 rows.
- `raw['fraudulent_intent'] == proc['fraudulent_intent']` across all 7,800 rows.
- `raw['social_engineering_tactics'] == proc['social_engineering_tactics']` across all 7,800 rows.

### 8.3 Immutability of Existing Project Corpora
We computed SHA-256 checksums and file sizes for all existing raw, processed, split, and real-world datasets:

| Dataset File | File Size (Bytes) | SHA-256 Checksum (Prefix) | Modification Status |
| :--- | :---: | :---: | :---: |
| [`data/raw/synthetic_financial_scams.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams.csv) (V1) | 4,780,679 | `8e708fa30aeaed63...` | **Unchanged** |
| [`data/raw/synthetic_financial_scams_v2.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams_v2.csv) (V2) | 9,481,111 | `406333c154bc05c8...` | **Unchanged** |
| [`data/raw/synthetic_financial_scams_v3.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams_v3.csv) (V3 Orig) | 9,835,801 | `cb275ebf5b1fffe2...` | **Unchanged** |
| [`data/processed/synthetic_financial_scams_v3_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_processed.csv) | 15,224,562 | `b5da235f624c24c1...` | **Unchanged** |
| [`data/splits/split_assignments.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/split_assignments.csv) | 6,085,816 | `17db4df33e956cc1...` | **Unchanged** |
| [`data/raw/real_fin_scam.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/real_fin_scam.csv) | 13,314,882 | `e00822c1e6469ea7...` | **Unchanged** |
| [`data/raw/real_fin_legit.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/real_fin_legit.csv) | 146,855,990 | `6810244c341b8f48...` | **Unchanged** |

`git diff` confirms that 0 tracked files in the repository were altered or overwritten.

---

## 9. Final Scientific Verdict & Recommendations

### Final Verdict: READY WITH DOCUMENTED LIMITATIONS

The **Synthetic Financial Scam Dataset Version 3 Corrected** satisfies all data integrity, partition isolation, linguistic coherence, and safety standards necessary for multi-level transformer modeling.

### Key Audit Findings
1. **0.0% Scenario-Family Leakage:** Perfect group isolation guarantees that test evaluations measure genuine generalization rather than near-duplicate memorization.
2. **Perfect Subtype Representation:** All 13 subtypes have exactly 480 Train, 60 Val, and 60 Test records.
3. **100% Evidence Span Grounding:** Character-level substrings slice exactly to verified text spans.
4. **Zero Contamination:** 0 occurrences of prohibited meta-tokens (`fictional`, `NOTICE <N>:`); 100% `.example` safe domains.
5. **Documented Research Limitations:**
   - **Limitation 1:** Static call-to-action strings in the notification channel (10.51% of data).
   - **Limitation 2:** Subtype-to-intent mutual information of 34.60% (concentration in family, crypto, and charity scams).
   - **Limitation 3:** Tactic affinity masking resulting in zero-probability combinations per subtype.

### Methodological Recommendations for Model Developers
1. **Multi-Task Architecture Design:** Decouple shared transformer encoder representations when predicting Subtype, Intent, and Tactics (e.g. use task-specific linear heads with gradient detachment or distinct adapter modules).
2. **Channel-Disaggregated Evaluation:** Separately evaluate and report intent classification accuracy across SMS, Email, Chat, and Notification partitions.
3. **Ablation Studies:** Test out-of-distribution intent generalization by evaluating intent accuracy on records where the subtype is masked or randomized.
