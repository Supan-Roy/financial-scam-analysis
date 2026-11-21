# Research Report: Cross-Generation Generalization Evaluation (Notebook 05)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-21  
**Notebook Reference:** [`notebooks/05_llm_authored_generalization_evaluation.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/05_llm_authored_generalization_evaluation.ipynb)  
**Evaluated Corpora:**
- **Programmatic Synthetic Corpus (V3.1):** 7,800 records ([`data/processed/synthetic_financial_scams_v3_1_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/synthetic_financial_scams_v3_1_processed.csv))
- **LLM-Authored Synthetic Corpus:** 2,730 records ([`data/processed/llm_authored_financial_scams_processed.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/processed/llm_authored_financial_scams_processed.csv))

---

## 1. Executive Summary & Research Motivation

A critical open question in natural language processing for financial fraud analysis is whether models trained on programmatically synthesized scam narratives generalize to scam communications authored through fundamentally different generative mechanisms.

Programmatically generated corpora (such as Version 3.1) utilize controlled slot-filling, deterministic grammatical templates, and modular scenario construction. While effective for establishing systematic coverage, programmatic templates risk introducing syntactic and lexical regularities that models can exploit as superficial heuristics.

To evaluate cross-generation robustness, we authored a separate, diverse corpus of 2,730 financial scam messages via contextual LLM reasoning (`gemini-3.8-flash-low`), incorporating 7 distinct writing styles and 4 digital channels. Notebook 05 conducts a systematic cross-generation generalization evaluation across all three multi-level analytical tasks:
1. **Scam Subtype Classification** (13 canonical classes)
2. **Fraudulent Intent Classification** (5 canonical classes)
3. **Social-Engineering Tactic Recognition** (9 binary multi-label targets)

---

## 2. Experimental Methodology & Modeling Setup

### Feature Representation & Estimators
- **Text Representation:** Word-level TF-IDF vectorization (`ngram_range=(1, 2)`, sublinear term frequency scaling).
- **Subtype & Intent Classifiers:** Multi-class Logistic Regression (`C=1.0`, `solver="lbfgs"`, `max_iter=1000`).
- **Social-Engineering Tactic Recognizer:** One-vs-Rest (Binary Relevance) Logistic Regression across 9 binary tactic indicators.
- **Evaluation Splits:**
  - `V3.1 Test Set`: 780 held-out records (11 scenario families, zero leakage).
  - `LLM-Authored Test Set`: 273 held-out records (13 scenario families, zero leakage).

### Training Regimes
1. **`V3.1-only`:** Trained exclusively on V3.1 training partition (6,240 records).
2. **`LLM-only`:** Trained exclusively on LLM-authored training partition (2,184 records).
3. **`Combined`:** Trained on combined training data (8,424 records: 6,240 V3.1 + 2,184 LLM).
4. **`Size-controlled Combined`:** Trained on a balanced 50/50 mixture subsampled to match the exact size of the V3.1-only baseline (6,240 records: 3,120 V3.1 + 3,120 LLM augmented/upsampled) to decouple sample volume from generation diversity.

---

## 3. Master Comparison Results

The table below consolidates the empirical results across all classification tasks, training conditions, and independent test distributions:

| Classification Task | Training Condition | Test Dataset | Samples | Accuracy | Macro F1 | Weighted F1 | Micro F1 | Hamming Loss |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scam Subtype** | V3.1-only | LLM-authored test | 273 | 0.4579 | 0.4819 | 0.4819 | — | — |
| **Scam Subtype** | V3.1-only | Programmatic V3.1 test | 780 | 0.9962 | 0.9962 | 0.9962 | — | — |
| **Scam Subtype** | LLM-only | LLM-authored test | 273 | 0.7326 | 0.7292 | 0.7292 | — | — |
| **Scam Subtype** | LLM-only | Programmatic V3.1 test | 780 | 0.9654 | 0.9652 | 0.9652 | — | — |
| **Scam Subtype** | Combined | LLM-authored test | 273 | 0.7179 | 0.7099 | 0.7099 | — | — |
| **Scam Subtype** | Combined | Programmatic V3.1 test | 780 | 0.9962 | 0.9962 | 0.9962 | — | — |
| **Scam Subtype** | Size-controlled combined | LLM-authored test | 273 | 0.7106 | 0.7060 | 0.7060 | — | — |
| **Scam Subtype** | Size-controlled combined | Programmatic V3.1 test | 780 | 0.9962 | 0.9962 | 0.9962 | — | — |
| **Fraudulent Intent** | V3.1-only | LLM-authored test | 273 | 0.6337 | 0.5354 | 0.6251 | — | — |
| **Fraudulent Intent** | V3.1-only | Programmatic V3.1 test | 780 | 0.9974 | 0.9960 | 0.9974 | — | — |
| **Fraudulent Intent** | LLM-only | LLM-authored test | 273 | 0.7033 | 0.6509 | 0.7123 | — | — |
| **Fraudulent Intent** | LLM-only | Programmatic V3.1 test | 780 | 0.8372 | 0.7310 | 0.8205 | — | — |
| **Fraudulent Intent** | Combined | LLM-authored test | 273 | 0.7106 | 0.6716 | 0.7176 | — | — |
| **Fraudulent Intent** | Combined | Programmatic V3.1 test | 780 | 0.9949 | 0.9891 | 0.9949 | — | — |
| **Fraudulent Intent** | Size-controlled combined | LLM-authored test | 273 | 0.7033 | 0.6559 | 0.7105 | — | — |
| **Fraudulent Intent** | Size-controlled combined | Programmatic V3.1 test | 780 | 0.9949 | 0.9900 | 0.9949 | — | — |
| **Social-Engineering Tactics** | V3.1-only | LLM-authored test | 273 | — | 0.2046 | — | 0.2627 | 0.2902 |
| **Social-Engineering Tactics** | V3.1-only | Programmatic V3.1 test | 639 | — | 0.9941 | — | 0.9950 | 0.0017 |
| **Social-Engineering Tactics** | LLM-only | LLM-authored test | 273 | — | 0.6722 | — | 0.7785 | 0.1461 |
| **Social-Engineering Tactics** | LLM-only | Programmatic V3.1 test | 639 | — | 0.4834 | — | 0.5329 | 0.2408 |
| **Social-Engineering Tactics** | Combined | LLM-authored test | 273 | — | 0.6667 | — | 0.7886 | 0.1538 |
| **Social-Engineering Tactics** | Combined | Programmatic V3.1 test | 639 | — | 0.9746 | — | 0.9799 | 0.0071 |
| **Social-Engineering Tactics** | Size-controlled combined | LLM-authored test | 273 | — | 0.6576 | — | 0.7837 | 0.1575 |
| **Social-Engineering Tactics** | Size-controlled combined | Programmatic V3.1 test | 639 | — | 0.9568 | — | 0.9647 | 0.0127 |

---

## 4. Key Empirical Findings & Discussion

### A. Generalization Gap of Programmatic V3.1-only Models
Models trained exclusively on programmatic data achieve near-perfect in-distribution test performance (>99% Macro F1), but suffer dramatic degradation when evaluated on LLM-authored narratives:
- **Scam Subtypes:** Macro F1 collapses from **0.9962** on V3.1 to **0.4819** on LLM-authored (-51.43 percentage points; Accuracy: 45.79%).
- **Fraudulent Intent:** Macro F1 collapses from **0.9960** on V3.1 to **0.5354** on LLM-authored (-46.06 percentage points; Accuracy: 63.37%).
- **Social-Engineering Tactics:** Macro F1 collapses from **0.9941** on V3.1 to **0.2046** on LLM-authored (-78.95 percentage points; Micro F1: 0.2627; Hamming Loss: 0.2902).

*Root Cause:* Programmatic generation creates strong lexical correlations between specific template phrases and labels. In natural LLM-authored communications, deceptive intent and tactics are expressed through diverse linguistic registers (e.g., casual slang, corporate legal notices, terse status toasts), rendering static n-gram associations ineffective.

### B. Asymmetric Generalization of LLM-only Models
Models trained exclusively on the LLM-authored dataset demonstrated asymmetric transfer:
- On **Scam Subtypes**, the LLM-only model achieved **0.7292 Macro F1** on LLM data and transferred surprisingly well to V3.1 (**0.9652 Macro F1**).
- On **Fraudulent Intent**, the model achieved **0.6509 Macro F1** on LLM data, but dropped to **0.7310 Macro F1** on V3.1.
- On **Social-Engineering Tactics**, the model achieved **0.6722 Macro F1** on LLM data, but degraded to **0.4834 Macro F1** on V3.1.

### C. Restorative Effect of Combined Training
Combining training data from both generation paradigms dramatically bridges the generalization gap:
- **Scam Subtype:** Combined Macro F1 reaches **0.7099** on LLM-authored test while maintaining **0.9962** on V3.1.
- **Fraudulent Intent:** Combined Macro F1 reaches **0.6716** on LLM-authored test while maintaining **0.9891** on V3.1.
- **Social-Engineering Tactics:** Combined Macro F1 reaches **0.6667** on LLM-authored test while retaining **0.9746** on V3.1.

### D. Size-Controlled Ablation Verification
A vital question is whether the combined model improved simply because it had more total data (8,424 records vs. 6,240 records). The size-controlled experiment (fixed at exactly 6,240 records) proved that **data diversity, rather than sample count, drives the improvement**:
- On LLM-authored test data:
  - Subtype Macro F1: **0.7060** (vs. 0.4819 V3.1-only; +22.41 points).
  - Intent Macro F1: **0.6559** (vs. 0.5354 V3.1-only; +12.05 points).
  - Tactic Macro F1: **0.6576** (vs. 0.2046 V3.1-only; +45.30 points).
- On V3.1 test data:
  - Subtype Macro F1: **0.9962** (identical to V3.1-only).
  - Intent Macro F1: **0.9900** (within 0.6 points of V3.1-only).
  - Tactic Macro F1: **0.9568** (strong retention).

---

## 5. Architectural Implications for Transformer Modeling

1. **Motivation for Contextual Representations:** Bag-of-words and n-gram TF-IDF representations are fundamentally constrained by lexical overlap. The sharp drop on LLM-authored data underscores the need for pretrained contextual Transformer backbones (e.g., DeBERTa-v3, RoBERTa) capable of encoding semantic abstractions beyond surface n-grams.
2. **Multi-Source Training Strategy:** Future Transformer fine-tuning should utilize a hybrid training curriculum incorporating both programmatic (V3.1) and contextual (LLM-authored) samples to ensure cross-distribution generalization.
3. **Explainability Ground Truth:** Both datasets provide 100% verified substring evidence spans, creating a dual-corpus ground truth for evaluating token-level attribution (SHAP, LIME) and attention-based explanations in subsequent research phases.
