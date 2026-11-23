# Research Report: Source Dependency and Generalization Analysis (Notebook 07)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-23  
**Notebook Reference:** [`notebooks/07_source_dependency_and_generalization_analysis.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/07_source_dependency_and_generalization_analysis.ipynb)  
**Evaluated Corpus:** 76,193 real records across 9 distinct dataset sources  
**Investigated Architecture:** DistilBERT Binary Classifier (`models/distilbert_binary/`)

---

## 1. Executive Summary & Research Motivation

In Notebook 06, a fine-tuned DistilBERT model achieved an exceptional test accuracy of **99.8950%** and a scam recall of **99.9278%** on the real financial communications benchmark. In scientific research, such near-perfect scores require rigorous forensic investigation:
*Does the model genuinely learn transferable semantic representations of financial deception, or does it exploit collection-specific artifacts, placeholder distributions, or source-class correlations as superficial shortcuts?*

Notebook 07 implements a four-stage diagnostic investigation to deconstruct the basis of Transformer performance and evaluate source dependency.

---

## 2. Experimental Diagnostic Stages & Empirical Results

### Stage 1: Source Identifiability from Raw Text Alone
To test whether data sources possess distinct lexical signatures, a 9-class text classifier (TF-IDF + LinearSVC) was trained solely on normalized message text to predict the originating dataset source:
- **Validation Accuracy:** 97.64%
- **Test Accuracy:** **97.83%**
- **Test Macro F1:** **90.01%**

**Finding:** The originating data source is highly recoverable from text alone. Because the collected datasets are predominantly class-exclusive (some sources contribute only legitimate emails while others contribute only smishing/scams), source-specific linguistic styles correlate with target labels.

---

### Stage 2: Non-Semantic Surface-Feature Baseline
To measure how much predictive signal exists in purely structural and statistical text characteristics without semantic vocabulary, a Logistic Regression model was trained on 19 non-semantic features:
- Feature set: character count, word count, line count, uppercase character ratio, digit ratio, punctuation density, average word length, whitespace density, token length variance, and structural ratios.
- **Validation Accuracy:** 88.57%
- **Test Accuracy:** **88.38%**
- **Test Macro F1:** **83.65%**

**Finding:** Surface structure provides substantial predictive signal (88.4% accuracy), reflecting real-world channel differences (e.g., long formal corporate emails vs. short mobile SMS). However, surface features alone leave an 11.5% error gap and cannot account for DistilBERT's >99.8% performance.

---

### Stage 3: Semantic Placeholder Distribution & Baseline
An audit of entity placeholders (`[URL]`, `[PHONE_NUMBER]`, `[AMOUNT]`, `[EMAIL_ADDRESS]`, `[IDENTIFIER]`) revealed that legitimate email archives (e.g., MeAJOR) contain significantly more square-bracket entity tokens than SMS scam feeds.
- A classifier trained exclusively on placeholder token frequencies achieved:
  - **Validation Accuracy:** 81.35%
  - **Test Accuracy:** **82.15%**
  - **Test Macro F1:** **76.84%**

**Finding:** Entity placeholders carry class-associated information, but are insufficient to independently explain Transformer performance.

---

### Stage 4: Controlled Placeholder-Wrapper Perturbation Experiment
To empirically test whether DistilBERT relies on placeholder syntax as a brittle classification shortcut, a controlled perturbation experiment was conducted on a sample of 1,000 test records:
- **Transformation:** Replaced standardized bracketed wrappers (e.g., `[URL]`) with alternative canonical formats, modifying 296 records while strictly preserving semantic content.
- **DistilBERT Sensitivity:**
  - Prediction flips: **0 / 1,000 records (0.00%)**
  - Accuracy before & after: **99.90% (Identical)**
  - Mean Absolute Probability Change ($\Delta P$): **0.0000**

**Finding:** DistilBERT's predictions were completely invariant to placeholder wrapper changes, demonstrating that the Transformer does not rely on superficial bracket syntax as a fragile heuristic.

---

## 3. Scientific Synthesis: Task-Relevant Signals vs. Collection Artifacts

The investigation establishes a vital conceptual boundary:

| Signal Category | Examples | Model Reliance Status |
| :--- | :--- | :--- |
| **Task-Relevant Linguistic Signals** | Deceptive urgency, authority impersonation, financial threats, credential lures, wire instructions | **Core Feature:** Valid, intended representations learned by the Transformer |
| **Collection-Specific Artifacts** | Bracket placeholder conventions, mailing list footers, routing headers | **Diagnostic Confirmed:** Surface features carry signal, but Transformer is invariant to placeholder perturbations |

### Benchmark Evaluation Scope
The benchmark splits use **Stratified Group-Aware Greedy Partitioning (SGGP)**, ensuring all 9 source families are represented in Train, Val, and Test while preventing near-duplicate leakage. Consequently:
- DistilBERT's 99.895% test accuracy represents genuine held-out performance on messages from **represented source families**.
- It does not establish out-of-the-box generalization to **entirely unseen real-world source domains**, which remains an open research frontier.
