# Research Report: Transformer-Based Binary Scam Classification (Notebook 06)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-22  
**Notebook Reference:** [`notebooks/06_transformer_based_modeling.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/06_transformer_based_modeling.ipynb)  
**Evaluated Corpus:** Real Financial Communications Benchmark ([`data/splits/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/splits/): 76,193 records)  
**Model Architecture:** DistilBERT (`distilbert/distilbert-base-uncased`)

---

## 1. Executive Summary & Research Motivation

Binary classification of financial communications into scam versus legitimate messages serves as the foundational gatekeeper in digital fraud prevention. While traditional TF-IDF and Linear Support Vector Classifiers (LinearSVC) achieved strong performance in earlier baseline experiments (~99.17% F1 on validation splits), shallow n-gram representations lack contextual awareness, subword sensitivity, and syntactic clause modeling.

Notebook 06 investigates whether fine-tuning a modern contextual Transformer architecture—specifically DistilBERT—provides superior classification accuracy, probability calibration, and robust generalization on the untouched real-world test partition.

---

## 2. Experimental Methodology & Hyperparameters

### Dataset & Partitioning
- **Corpus:** 76,193 real-world financial communications (13,861 scam records, 62,332 legitimate records).
- **Partitioning:** Stratified Group-Aware Greedy Partitioning (SGGP):
  - **Training Set:** 60,957 records (80.00%)
  - **Validation Set:** 7,618 records (10.00%)
  - **Test Set:** 7,618 records (10.00%)
- **Data Hygiene:** 0.0% duplicate cluster leakage across partitions. Synthetic records were strictly excluded from this benchmark.
- **Input Feature:** `normalized_text` (canonical placeholder-masked message narratives).

### Model Configuration & Training Details
- **Base Architecture:** `distilbert/distilbert-base-uncased` (6 layers, 768 hidden dimensions, 12 attention heads, 66M parameters).
- **Maximum Sequence Length:** 512 tokens.
- **Training Epochs:** 3.
- **Batch Size:** 16 (training and evaluation).
- **Learning Rate:** 2e-5 with AdamW optimizer and linear decay schedule.
- **Weight Decay:** 0.01.
- **Mixed Precision:** FP16 enabled.
- **Loss Function:** Standard unweighted cross-entropy.
- **Model Selection Metric:** Best validation macro F1.

---

## 3. Empirical Test Performance & Evaluation Metrics

The optimal checkpoint (selected based on peak validation macro F1 of 99.8458%) was evaluated on the untouched 7,618-record real test partition:

| Metric | Score | Performance Context |
| :--- | ---: | :--- |
| **Accuracy** | **99.8950%** | 7,610 correct out of 7,618 test records |
| **Scam Precision** | **99.4968%** | Only 7 false alarms across 6,233 legitimate messages |
| **Scam Recall** | **99.9278%** | Only 1 missed scam out of 1,385 fraudulent messages |
| **Scam F1-score** | **99.7118%** | High balance between precision and detection rate |
| **Macro F1-score** | **99.8238%** | Unweighted mean across scam and legitimate classes |
| **Weighted F1-score** | **99.8950%** | Frequency-weighted composite performance |
| **PR-AUC** | **99.9894%** | Near-perfect area under precision-recall curve |

### Confusion Matrix on Held-Out Test Set (7,618 Records)

| Actual \ Predicted | Predicted Legitimate | Predicted Scam | Total Actual |
| :--- | ---: | ---: | ---: |
| **Actual Legitimate** | **6,226** (TN) | **7** (FP) | 6,233 |
| **Actual Scam** | **1** (FN) | **1,384** (TP) | 1,385 |
| **Total Predicted** | 6,227 | 1,391 | 7,618 |

- **Total Test Errors:** Exactly **8 records** (0.105% error rate).
- **False Negative Audit:** The single false negative was a highly abbreviated SMS notification lacking overt urgency tokens or explicit external links.
- **False Positive Audit:** The 7 false positives involved automated institutional bank security notifications that used phrases syntactically similar to fraud warnings (e.g., unrecognized device login alerts from legitimate financial services).

---

## 4. Comparison with Traditional Machine Learning Baselines

| Model Architecture | Feature Representation | Validation Accuracy | Validation F1 (Scam) | Test Accuracy | Test Macro F1 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Multinomial Naive Bayes** | Word TF-IDF (1-gram) | 97.43% | 90.78% | — | — |
| **Logistic Regression** | Word TF-IDF (1-gram, balanced) | 98.39% | 95.83% | — | — |
| **Linear SVM (LinearSVC)** | Word TF-IDF (1-gram, C=1.0) | 99.70% | 99.17% | 99.68% | 99.21% |
| **DistilBERT (Fine-Tuned)** | Pretrained Contextual Embeddings | **99.91%** | **99.76%** | **99.8950%** | **99.8238%** |

### Key Takeaway
While DistilBERT establishes a new empirical ceiling on this benchmark (reducing test errors from ~24 under LinearSVC to 8 under DistilBERT), the margin of improvement over linear models on this specific binary task is incremental (+0.21% accuracy). This finding motivated the detailed diagnostic investigations in Notebook 07 (Source Dependency Analysis) and Notebook 08 (Synthetic Augmentation Evaluation).
