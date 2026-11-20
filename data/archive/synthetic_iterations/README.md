# Synthetic Financial Scam Dataset Archive

This directory stores archived, intermediate, and legacy iterations of the synthetic financial scam dataset generated during the development of the multi-level research framework:

> *"Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications."*

**Active Production Datasets:**
- Raw Active: [`data/raw/synthetic_financial_scams_v3_corrected.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams_v3_corrected.csv)
- Processed Active: [`data/processed/synthetic_financial_scams_v3_corrected_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_corrected_processed.csv)

These archived files are **preserved for scientific provenance, auditability, and historical reproducibility**. Do not delete or overwrite them.

---

## Inventory of Archived Iterations

| File Name | Stage / Version | Records | Columns | Size (Bytes) | SHA-256 Checksum | Generator Script / Origin | Primary Audit Reference |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| `synthetic_financial_scams.csv` | **Version 1 (Raw)** | 7,643 | 11 | 4,780,679 | `8e708fa30aeaed63067db56c9b5c10e1cbb90b6fb8574c53882e32b3654240d7` | Initial generator (`src/data/`) | [`reports/dataset_audits/multilevel_annotation_readiness.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/multilevel_annotation_readiness.md) |
| `synthetic_financial_scams_processed.csv` | **Version 1 (Processed)** | 7,643 | 30 | 8,184,312 | `e3220f14e83e6b00e79a23c58d7a7e41cf6a06c2d3e9aa369917b2de68101131` | `src/preprocessing/pipeline.py` | [`reports/preprocessing/preprocessing_report.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/preprocessing/preprocessing_report.md) |
| `synthetic_financial_scams_v2.csv` | **Version 2 (Raw)** | 7,800 | 14 | 9,481,111 | `406333c154bc05c852109d5d7ed0773f857d0c3c3b499661ca0a4e8a27c1278b` | `scripts/generate_synthetic_v2.py` | [`reports/dataset_audits/synthetic_v2_qualitative_sample.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/synthetic_v2_qualitative_sample.md) |
| `synthetic_financial_scams_v2_processed.csv` | **Version 2 (Processed)** | 7,800 | 33 | 14,676,422 | `77e8639e7f83ce2b6b99b3763f88c66292a656b670dd7ffbc91d969e63bb2dff` | `scripts/generate_synthetic_v2.py` | [`reports/dataset_audits/synthetic_v2_qualitative_sample.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/synthetic_v2_qualitative_sample.md) |
| `synthetic_v2_pilot_130.csv` | **Pilot 1 (Refinement)** | 130 | 16 | 176,070 | `01e0fec2552240bb6ebb3700d8a31c60558f1bf0f644edd98f5b69dacfa60758` | `scripts/generate_synthetic_v2_pilot.py` | [`reports/dataset_audits/synthetic_v2_pilot_refinement.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/synthetic_v2_pilot_refinement.md) |
| `synthetic_v2_pilot2_130.csv` | **Pilot 2 (Approved)** | 130 | 16 | 174,884 | `a5b2bce96155c65ca053a1c58081ae902e735d4a2be35e921cbfa603f84bd802` | `scripts/generate_synthetic_v2_pilot2.py` | [`reports/dataset_audits/synthetic_v2_pilot2_refinement.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/synthetic_v2_pilot2_refinement.md) |
| `synthetic_financial_scams_v3.csv` | **Version 3 Original (Raw)** | 7,800 | 16 | 9,835,801 | `cb275ebf5b1fffe2860683aaeea07007385f2643f3ea531f9a38902eed89d215` | `scripts/generate_synthetic_v3.py` | [`reports/dataset_audits/synthetic_v3_final_readiness.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/synthetic_v3_final_readiness.md) |
| `synthetic_financial_scams_v3_processed.csv` | **Version 3 Original (Proc)** | 7,800 | 36 | 15,224,562 | `b5da235f624c24c15dfacbbee234fcd0e68813e73eee09018ae3cc8d67266d2c` | `scripts/generate_synthetic_v3.py` | [`reports/dataset_audits/synthetic_v3_final_readiness.md`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/reports/dataset_audits/synthetic_v3_final_readiness.md) |

---

## Lineage & Iteration Summary

1. **Version 1 (`synthetic_financial_scams.csv`):**
   - 7,643 records across early taxonomy. Contained repetitive templates, artificial metadata prefixes (`NOTICE <N>:`), and lacked fine-grained evidence spans.
2. **Version 2 (`synthetic_financial_scams_v2.csv`):**
   - 7,800 records (600 per subtype across 13 subtypes). Added 5 intents and 9 tactics. Audit revealed narrative-intent mismatches, fixed 3-turn chats, and mobile notification bloat.
3. **Pilot 1 & 2 (`synthetic_v2_pilot_130.csv`, `synthetic_v2_pilot2_130.csv`):**
   - 130-record controlled trials introducing 104 scenario families, dynamic conversational progression, and character-level evidence spans. Pilot 2 was approved as the architectural foundation.
4. **Version 3 Original (`synthetic_financial_scams_v3.csv`):**
   - Full 7,800-record generation. Readiness audit discovered cross-partition scenario leakage (60 overlapping families) and subtype partition deficits (3 subtypes missing in Val/Test).
5. **Version 3 Corrected (Active Production Candidate):**
   - Replaced Version 3 Original. Achieved 0.0% scenario family leakage, 0.0% near-duplicate cluster leakage, 100% subtype representation across all splits (480 Train / 60 Val / 60 Test), and explicit tactic mapping. Located at [`data/raw/synthetic_financial_scams_v3_corrected.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/raw/synthetic_financial_scams_v3_corrected.csv).
