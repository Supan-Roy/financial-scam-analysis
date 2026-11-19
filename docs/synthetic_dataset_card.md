# Synthetic Financial-Scam Research Dataset

## Active Dataset: Version 3 Corrected

The active production candidate is **`synthetic_financial_scams_v3_corrected.csv`** (and processed [`data/processed/synthetic_financial_scams_v3_corrected_processed.csv`](../data/processed/synthetic_financial_scams_v3_corrected_processed.csv)).

- **Total Records:** 7,800 (exactly 600 records per subtype across 13 canonical subtypes).
- **Group Isolation:** 104 scenario families partitioned into Train (78 families / 6,240 records), Validation (13 families / 780 records), and Test (13 families / 780 records) with **0.0% scenario-family leakage** and **0.0% cluster leakage**.
- **Character-Level Evidence Spans:** 100% exact substring match verification across all 7,800 records for `primary_intent_evidence`, `narrative_evidence`, and `tactics_evidence`.
- **Channels:** SMS, Email, Chat (dynamic multi-turn dialogues), and Notification (lockscreen alerts).
- **Safety & RFC 2606:** 100% of URLs strictly use reserved `.example` domains. 0 prohibited meta-tokens (`fictional`, `NOTICE <N>:`).
- **Audit Reports:** [`reports/dataset_audits/synthetic_v3_corrected_validation.md`](../reports/dataset_audits/synthetic_v3_corrected_validation.md) and [`reports/dataset_audits/synthetic_v3_corrected_final_review.md`](../reports/dataset_audits/synthetic_v3_corrected_final_review.md).

*Historical Note:* Prior iterations (Version 1: 7,643 records, Version 2, and original Version 3) have been archived to `data/archive/synthetic_iterations/` for scientific provenance.

---

## Purpose

The synthetic corpus provides controlled, leak-free supervision for multi-level financial scam narrative detection, fraudulent intent analysis, and social-engineering pattern recognition. It is evaluated separately from the real-world binary benchmark.

## Generation and stopping rule

The corpus uses 13 fictional scam subtypes, four channels, six writing styles, twelve subtype-aware openings, sixteen varied requests, and twelve closings. This factorial coverage produced **7643** records. A small edge-case supplement adds terse, long-form, indirect, conversational, and emoji-bearing messages that do not all follow the dominant three-part structure. A limited subset of chat messages contains multiple emoji inserted at varied positions, and 96 existing records contain extended narrative context; these are intentional hard-case formatting variations, not platform-specific templates.

Generation stopped after the coverage audit showed every planned subtype/channel/style family was represented and additional combinations were becoming structural paraphrases. The final count is therefore determined by the coverage design and the saturation check, not by a round-number target.

## Annotation definitions

- `label`: always `1`, meaning synthetic financial scam.
- `phishing_type`: the fictional scam subtype.
- `scam_channel`: `sms`, `email`, `chat`, or `notification`.
- `fraudulent_intent`: the deceptive goal represented in the message.
- `social_engineering_tactics`: JSON list containing only tactics evidenced by the message.
- `language`: always `English`.
- `synthetic`: always `true`.
- `generation_scenario`: concise scenario description.
- `risk_or_safety_note`: confirms fictional entities and redacted details.

Tactic taxonomy: `urgency, authority_impersonation, fear_or_threat, reward_or_benefit, scarcity, trust_exploitation, emotional_manipulation, false_legitimacy, secrecy`.

## Coverage summary

### Subtypes

- `account_verification`: 587
- `card_transaction_alert`: 588
- `charity_donation`: 587
- `family_emergency_request`: 588
- `investment_crypto`: 589
- `invoice_payment_request`: 587
- `job_task_commission`: 589
- `loan_offer`: 588
- `prize_reward`: 587
- `recovery_support`: 589
- `refund_chargeback`: 589
- `romance_financial_manipulation`: 587
- `tax_payment`: 588

### Channels

- `chat`: 1911
- `email`: 1911
- `notification`: 1910
- `sms`: 1911

### Message presentation/style families

- `chat_dialogue`: 1270
- `email_or_formatted`: 1267
- `emoji_or_edge`: 2569
- `short_or_notification`: 2537

### Fraudulent intent

- `induce a payment`: 5291
- `obtain sensitive information`: 1763
- `promote a fraudulent investment`: 589

### Tactics

- `authority_impersonation`: 748
- `emotional_manipulation`: 762
- `false_legitimacy`: 1397
- `fear_or_threat`: 798
- `reward_or_benefit`: 828
- `scarcity`: 834
- `secrecy`: 707
- `trust_exploitation`: 1618
- `urgency`: 1588

## Safety constraints

All organizations, names, case identifiers, amounts, links, phone numbers, emails, and payment destinations are fictional, redacted, or represented by explicit placeholders. No real-world message was copied. Emoji are included only as non-actionable research features; no live Telegram, WhatsApp, or other platform destination is supplied.

## Limitations

Synthetic language does not establish real-world robustness. The corpus contains only scam-labeled records, may reflect generator assumptions, and does not model real sender infrastructure or regional language variation. Researchers should report results separately on real and synthetic data and include legitimate controls before making deployment claims.
