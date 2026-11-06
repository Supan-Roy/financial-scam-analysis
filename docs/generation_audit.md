# Synthetic Dataset Generation Audit

## Final result

- Final record count: **7643**
- Exact duplicate texts: **0**
- Duplicate IDs: **0**
- Rows missing required fields: **0**
- Non-English rows: **0**
- Invalid labels or synthetic flags: **0**
- URL, email, or phone-pattern matches: **0**
- Emoji-bearing rows: **2605**
- Exclusions during quality control: **none**

## Counts by subtype

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

## Counts by channel

- `chat`: 1911
- `email`: 1911
- `notification`: 1910
- `sms`: 1911

## Counts by presentation/style family

- `chat_dialogue`: 1270
- `email_or_formatted`: 1267
- `emoji_or_edge`: 2569
- `short_or_notification`: 2537

## Counts by fraudulent intent

- `induce a payment`: 5291
- `obtain sensitive information`: 1763
- `promote a fraudulent investment`: 589

## Counts by social-engineering tactic

- `authority_impersonation`: 748
- `emotional_manipulation`: 762
- `false_legitimacy`: 1397
- `fear_or_threat`: 798
- `reward_or_benefit`: 828
- `scarcity`: 834
- `secrecy`: 707
- `trust_exploitation`: 1618
- `urgency`: 1588

## Saturation decision

The generator covered all planned subtype/channel/style combinations and added a bounded edge-case set. Further expansion would mostly permute the same fictional requests and placeholders, so generation stopped. This is a diversity-oriented synthetic benchmark, not evidence of real-world detector performance.

## Researcher review items

1. Evaluate synthetic and real-world corpora separately.
2. Add a matched legitimate class before supervised training.
3. Report performance by subtype, channel, style family, and tactic combination.
4. Review emoji and chat rows separately because formatting can become a shortcut feature.

## Message-format revision

- Added multi-emoji formatting to **48** chat messages; **296** rows now contain at least three non-ASCII emoji characters.
- Added longer narrative context to **96** existing records; **78** rows are now at least 900 characters.
- Exact duplicate texts after revision: **0**.
- No new records were added, and all IDs and annotations were preserved.
