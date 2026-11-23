# Research Report: Synthetic Data Augmentation for Binary Financial Scam Detection (Notebook 08)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-23  
**Notebook Reference:** [`notebooks/08_synthetic_data_augmentation_evaluation.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/08_synthetic_data_augmentation_evaluation.ipynb)  
**Evaluated Corpora:** Real Benchmark (76,193 records) + Synthetic Corpora (10,530 records: 7,800 V3.1 + 2,730 LLM-authored)  
**Evaluated Architecture:** DistilBERT (`distilbert/distilbert-base-uncased`) evaluated across three independent training regimes (Experiments A, B, and C)

---

## 1. Executive Summary & Research Motivation

In multi-level financial scam analysis, synthetic narratives provide controlled, balanced supervision across granular scam subtypes, fraudulent intents, and psychological tactics. However, a foundational research question remains:
*Can synthetic scam narratives effectively substitute for, or measurably augment, real scam communications in binary financial scam detection?*

Notebook 08 conducts a rigorous empirical investigation of synthetic data augmentation within a DistilBERT classification framework. By evaluating three distinct training regimes on the **exact same untouched real-world test partition (7,618 records)**, the study evaluates the real-world transferability, augmentation utility, and vulnerability to distribution shifts of both programmatic and LLM-authored synthetic data.

### Key Scientific Takeaways
1. **Synthetic-Only Training Collapses on Real Data:** Training exclusively on synthetic scam narratives alongside real legitimate messages yielded a deceptive **100.0% validation accuracy**, but suffered a catastrophic collapse on the real-world test set, detecting only **11.70% of real scams** (1,223 false negatives across 1,385 scams). This demonstrates the severe risk of source-class confounding when synthetic data is used in isolation.
2. **Combined Training Preserves Near-Baseline Performance:** Incorporating synthetic scam narratives into real-world training (Experiment C) maintained high real-world detection capability (**99.8819% accuracy**, **99.8556% scam recall**, **99.8017% macro F1**), producing only 9 total errors on 7,618 test records.
3. **No Statistically Measurable Augmentation Improvement:** A paired McNemar exact binomial test between real-only training (Experiment A) and combined training (Experiment C) revealed only 5 discordant predictions across 7,618 records ($p = 1.0000$). Synthetic data acts as safe supplementary supervision without performance degradation, but does not independently surpass real-only training on the represented test benchmark.

---

## 2. Dataset Composition & Data Hygiene

### A. Real-World Binary Benchmark Corpus
- **Total Records:** 76,193 real communications (13,861 financial scams [18.19%], 62,332 legitimate communications [81.81%]).
- **Partitioning:** Stratified Group-Aware Greedy Partitioning (SGGP) preserving duplicate cluster integrity:
  - **Train:** 60,957 records (11,091 scam, 49,866 legit)
  - **Validation:** 7,618 records (1,385 scam, 6,233 legit)
  - **Test:** 7,618 records (1,385 scam, 6,233 legit)
- No synthetic records were included in the real-data benchmark splits.

### B. Synthetic Corpora (10,530 Records Total)
Both synthetic datasets previously developed for multi-level research were mapped to binary label `1` (scam):
- **V3.1 Programmatic Synthetic Corpus:** 7,800 records across 104 isolated scenario families (Train: 6,240; Val: 780; Test: 780).
- **LLM-Authored Synthetic Corpus:** 2,730 records across 130 isolated scenario families and 7 writing styles (Train: 2,184; Val: 273; Test: 273).
- **Combined Synthetic Training Pool:** 8,424 records (6,240 V3.1 + 2,184 LLM-authored).
- **Combined Synthetic Validation Pool:** 1,053 records (780 V3.1 + 273 LLM-authored).
- **Combined Synthetic Test Pool:** 1,053 records (780 V3.1 + 273 LLM-authored).

### C. Data Integrity & Leakage Verification
- Confirmed zero missing or empty values in `normalized_text`.
- Verified that synthetic train, validation, and test partitions have zero detected cross-partition exact-text overlap.
- Verified that synthetic training and validation partitions have zero exact-text overlap with the real training, validation, or test partitions.
- Note: A small number of duplicate rows within individual synthetic partitions were preserved intentionally rather than silently discarded, maintaining full provenance.

---

## 3. Synthetic Transfer Evaluation (Cross-Distribution Diagnostic)

Before evaluating augmentation regimes, the baseline DistilBERT model trained exclusively on real communications (Model A from Notebook 06) was evaluated on held-out synthetic test partitions paired with real legitimate test records:

| Evaluation Partition | Accuracy | Scam Precision | Scam Recall | Scam F1-score | Macro F1 | PR-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Real Legitimate + V3.1 Test Scams** (7,013 records) | 99.8859% | 99.1094% | 99.8718% | 99.4891% | 99.7125% | 99.9443% |
| **Real Legitimate + LLM Test Scams** (6,506 records) | 99.8309% | 97.4638% | 98.5348% | 97.9964% | 98.9540% | 99.6755% |

### Analysis of Missed Synthetic Scams
The real-only model detected 779/780 V3.1 scams (99.87% recall) and 269/273 LLM-authored scams (98.53% recall). The 5 false negatives comprised:
- 2 LLM-authored charity donation appeals.
- 2 LLM-authored invoice payment requests.
- 1 V3.1 job task commission notification.

All 5 messages were well within the 512-token sequence limit (no truncation occurred). Their misclassification was driven by subtle lexical framing resembling legitimate philanthropic solicitations and routine corporate billing rather than overt threat markers.

---

## 4. Experimental Training Regimes

All three configurations were trained on a single NVIDIA A100 GPU utilizing identical hyperparameters:
- **Base Architecture:** `distilbert/distilbert-base-uncased` (66M parameters).
- **Max Sequence Length:** 512 tokens.
- **Hyperparameters:** Epochs = 3, Batch Size = 16, Learning Rate = 2e-5 (AdamW, linear decay), Weight Decay = 0.01, FP16 enabled, Random Seed = 42.
- **Model Checkpoint Selection:** Best validation macro F1.

| Configuration | Training Composition | Real Legit | Real Scam | Synthetic Scam | Total Train Size | Checkpoint Metric |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Experiment A (Real-Only)** | Real legitimate + Real scams | 49,866 | 11,091 | 0 | 60,957 | Val Macro F1: 99.8458% (Epoch 2) |
| **Experiment B (Synthetic-Only Scams)** | Real legitimate + Synthetic scams | 49,866 | 0 | 8,424 | 58,290 | Val Macro F1: 100.000% (Epoch 1) |
| **Experiment C (Real + Synthetic)** | Real legitimate + Real scams + Synthetic scams | 49,866 | 11,091 | 8,424 | 69,381 | Val Macro F1: 99.9145% (Epoch 3) |

---

## 5. Comparative Performance on Held-Out Real Test Partition (7,618 Records)

All models were evaluated on the exact same untouched real test set (6,233 legitimate, 1,385 real scams):

| Metric | Experiment A (Real-Only) | Experiment B (Synthetic-Only Scams) | Experiment C (Real + Synthetic) |
| :--- | :---: | :---: | :---: |
| **Accuracy** | **99.8950%** | 83.9459% | 99.8819% |
| **Scam Precision** | 99.4968% | **100.0000%** | 99.4964% |
| **Scam Recall** | **99.9278%** | 11.6968% | 99.8556% |
| **Scam F1-score** | **99.7118%** | 20.9438% | 99.6757% |
| **Macro F1-score** | **99.8238%** | 56.0048% | 99.8017% |
| **PR-AUC** | **99.9894%** | 82.8774% | 99.9704% |

### Confusion Matrices & Error Breakdown

| Regime | True Negatives (TN) | False Positives (FP) | False Negatives (FN) | True Positives (TP) | Total Errors | Error Rate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Experiment A (Real-Only)** | 6,226 | 7 | 1 | 1,384 | **8** | 0.105% |
| **Experiment B (Synthetic-Only)** | 6,233 | 0 | 1,223 | 162 | **1,223** | 16.054% |
| **Experiment C (Real + Synthetic)** | 6,226 | 7 | 2 | 1,383 | **9** | 0.118% |

---

## 6. Forensic Deconstruction of Findings

### A. Finding 1: The Illusion of Synthetic-Only Validation (Experiment B)
Experiment B achieved a deceptive **100.0% validation score across all three training epochs**. Yet on the real-world test partition, it suffered an **88.30% false negative rate**, failing to identify 1,223 out of 1,385 real scams.
- **Underlying Cause:** In Experiment B, the scam class was composed 100% of synthetic narratives (V3.1 and LLM-authored), while the legitimate class was composed 100% of real emails and SMS. The neural network learned to discriminate *data provenance* (synthetic vs. real source features) rather than *financial fraud mechanics*.
- **Validation Fallacy:** Because the validation split mirrored this exact source-class alignment, validation metrics were artificially perfect, hiding severe out-of-distribution failure.

### B. Finding 2: Retention of Real Detection Capability (Experiment C)
When real scams were included alongside synthetic data, DistilBERT successfully avoided source shortcut learning. It correctly detected 1,383 out of 1,385 real scam messages (99.86% recall), closely tracking the real-only baseline (99.93% recall). This confirms that synthetic data does not pollute or degrade the decision boundary when grounded by real examples.

### C. Finding 3: McNemar Paired Statistical Comparison (A vs. C)
To rigorously test whether synthetic augmentation yielded a statistically significant difference over real-only training, a paired McNemar exact binomial test was conducted across the 7,618 test records:

| Contingency Cell | Value | Description |
| :--- | :---: | :--- |
| **Model A Correct, Model C Correct** | 7,607 | Both models predicted correctly |
| **Model A Correct, Model C Incorrect** | 3 | Model A identified scam/legit, Model C erred |
| **Model A Incorrect, Model C Correct** | 2 | Model C identified scam/legit, Model A erred |
| **Model A Incorrect, Model C Incorrect** | 6 | Both models erred (common failure modes) |
| **Total Discordant Pairs ($b + c$)** | **5** | Disagreements across 7,618 records |
| **Two-Sided Exact $p$-Value** | **1.0000** | Binomial test against null hypothesis ($p=0.5$) |

**Scientific Conclusion:** With $p = 1.0000 > 0.05$, there is no statistically significant evidence that synthetic augmentation improves or harms binary detection on this benchmark.

---

## 7. Model Artifacts & Provenance Tracking

All trained models were verified and saved to dedicated disk directories:
- **Model A Checkpoint:** [`models/distilbert_binary/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/models/distilbert_binary/)
- **Model B Checkpoint:** [`models/distilbert_experiment_b/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/models/distilbert_experiment_b/)
- **Model C Checkpoint:** [`models/distilbert_experiment_c/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/models/distilbert_experiment_c/)

Each directory contains complete weights (`model.safetensors`), configuration (`config.json`), and full tokenizer serialization files.

---

## 8. Limitations & Guidelines for Academic Publication

1. **Source Exclusivity in Real Corpora:** In the underlying benchmark, real data sources are class-exclusive (e.g., MeAJOR is entirely legitimate; IMC25 is entirely smishing). Models may partially leverage channel/source-specific distributions.
2. **Ceiling Effects in Binary Evaluation:** Model A already operates at an empirical ceiling (99.8950% accuracy, 8 errors / 7,618 records). Detecting statistically significant improvements in binary performance would require an order of magnitude larger test corpus or challenging out-of-distribution adversarial examples.
3. **Multi-Level Value Distinction:** While synthetic data provides no measurable binary advantage on this test partition, its primary academic value lies in providing granular supervision for multi-level tasks (13 scam subtypes, 5 fraudulent intents, and 9 psychological tactics) where labeled real-world data is severely limited or non-existent.
