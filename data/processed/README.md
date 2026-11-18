# Processed Datasets Directory

This directory contains the canonical preprocessed dataset files:

1. **`real_fin_scam_processed.csv`**
   - Canonical processed real scam communications (13,861 records, 30 columns).
2. **`real_fin_legit_processed.csv`**
   - Canonical processed legitimate financial communications (62,332 records, 30 columns).
3. **`synthetic_financial_scams_v3_corrected_processed.csv`** (Active Production Synthetic Corpus)
   - Canonical processed synthetic scam communications (7,800 records, 36 columns).
   - Includes canonical entity placeholders, MinHash LSH deduplication cluster mappings (`duplicate_cluster_id`), and group-isolated partition assignments (`split_partition`: 6,240 Train / 780 Val / 780 Test).

*Note:* Prior processed synthetic iterations (V1, V2, and original V3) have been archived in [`data/archive/synthetic_iterations/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/archive/synthetic_iterations/README.md).
