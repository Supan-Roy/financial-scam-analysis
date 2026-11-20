# Processed Datasets Directory

This directory contains the canonical preprocessed dataset files:

1. **`real_fin_scam_processed.csv`**
   - Canonical processed real scam communications (13,861 records, 30 columns).
2. **`real_fin_legit_processed.csv`**
   - Canonical processed legitimate financial communications (62,332 records, 30 columns).
3. **`synthetic_financial_scams_v3_1_processed.csv`** (Active Programmatic Synthetic Corpus V3.1)
   - Canonical processed synthetic scam communications (7,800 records, 36 columns).
   - Includes canonical entity placeholders, MinHash LSH deduplication cluster mappings (`duplicate_cluster_id`), and group-isolated partition assignments (`split_partition`: 6,240 Train / 780 Val / 780 Test).
4. **`llm_authored_financial_scams_processed.csv`** (LLM-Reasoned Diverse Synthetic Corpus)
   - Canonical processed LLM-authored scam communications (2,730 records, 45 columns).
   - Features rich 7-style writing taxonomy, 4 digital channels, canonical placeholder masking, 100% verified evidence substring slices, and scenario-isolated partition assignments (`split_partition`: 2,184 Train / 273 Val / 273 Test; 80% / 10% / 10%).
5. **`synthetic_financial_scams_v3_corrected_processed.csv`** (Archived V3 Corrected Interim Corpus)
   - 7,800 records preceding V3.1 notification channel rebalancing.

*Note:* Prior processed synthetic iterations (V1, V2, and original V3) have been archived in [`data/archive/synthetic_iterations/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/archive/synthetic_iterations/README.md).
