# Legitimate Financial Communication Dataset

`real_fin_legit.csv` is the original SMS-focused legitimate corpus. `real_fin_legit_expanded.csv` adds **53543** benign, anonymized MeAJOR email records while preserving the original SMS records.

## Categories

- `financial_legitimate`: financial, account, payment, banking, billing, trading, or business-finance communication.
- `general_legitimate`: ordinary legitimate personal or workplace communication that is not specifically financial.

## Expanded corpus

- Total records: **58213**
- Financial legitimate: **17401**
- General legitimate: **40812**
- Channels: existing SMS plus MeAJOR email.
- All records retain `label=0` and `synthetic=false`.

## MeAJOR provenance

MeAJOR is the official Zenodo release at https://zenodo.org/records/18471483. It defines `label=0` as benign, anonymizes entities with bracketed tokens, and is released under CC BY 4.0. Candidate email subjects and bodies are preserved separately where available, with original source identifiers.

## Limitations

Neither the SMS ham labels nor MeAJOR benign labels prove sender authenticity. The expanded corpus is not exclusively financial, and its category assignment is rule-based. Evaluate by source, channel, and category; avoid random splits that leak near-duplicate email threads.
