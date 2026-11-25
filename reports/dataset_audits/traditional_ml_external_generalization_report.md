# Research Report: Traditional ML External Generalization & Statistical Model Comparison (Notebook 10)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-26  
**Notebook Reference:** [`notebooks/10_external_generalization_traditional_ml.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/10_external_generalization_traditional_ml.ipynb)  
**Evaluated Models:**
- Contextual Deep Learning: DistilBERT Binary Classifier (`models/distilbert_binary/` from Notebook 06)
- Traditional Linear Baselines: Linear SVM (`LinearSVC`), Logistic Regression, Multinomial Naive Bayes (`models/traditional_binary/`)
**Evaluated External Datasets:**
- Primary Expanded Test Set: [`data/external_evaluation/expanded_binary_external_test.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/expanded_binary_external_test.csv) ($N = 7,025$)
- Balanced Test Companion: [`data/external_evaluation/balanced_binary_external_test.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/balanced_binary_external_test.csv) ($N = 1,584$)
- Curated External Scams: [`data/external_evaluation/external_fin_scam_curated.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/external_fin_scam_curated.csv) ($N = 792$)
**Statistical Testing Framework:** Paired McNemar Exact Tests with Holm-Bonferroni Family-Wise Error Rate (FWER) Correction  
**Results & Visualizations Directory:** [`outputs/external_evaluation_traditional_ml/results/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/outputs/external_evaluation_traditional_ml/results/)

---

## 1. Executive Summary & Research Motivation

In Notebook 09, our fine-tuned DistilBERT binary classifier demonstrated strong generalization on independently sourced external scam datasets, achieving an **external scam recall of 96.72%** and a **balanced accuracy of 98.30%**. However, in rigorous academic research, evaluating a complex deep contextual model in isolation leaves an essential comparative question unanswered:
> *Are deep contextual Transformer representations strictly necessary to generalize across independently sourced financial scam narratives, or can lightweight, computationally efficient Bag-of-Words / TF-IDF traditional machine learning baselines achieve comparable out-of-distribution detection?*

In early benchmark modeling (Notebook 03), Linear Support Vector Machines (LinearSVC) and Logistic Regression proved surprisingly competitive with deep models on identically distributed validation data (~99.17% Scam F1). To evaluate whether this competitiveness persists under genuine distribution shift, **Notebook 10 reconstructs the canonical TF-IDF vectorizer and three traditional ML classifiers, evaluates them on the exact same external evaluation datasets used in Notebook 09, and executes paired statistical significance testing (McNemar exact tests with Holm-Bonferroni correction) against DistilBERT.**

```
                               MODEL EVALUATION & COMPARISON ARCHITECTURE
                                    (Expanded Test Set: N = 7,025)
                                                  │
                 ┌────────────────────────────────┴────────────────────────────────┐
                 ▼                                                                 ▼
      [CONTEXTUAL TRANSFORMER]                                        [TRADITIONAL N-GRAM BASELINES]
             DistilBERT                                            Fitted TF-IDF Vectorizer (115,436 vocab)
       (Notebook 06 Checkpoint)                                                    │
                 │                                        ┌────────────────────────┼────────────────────────┐
                 │                                        ▼                        ▼                        ▼
                 │                                   Linear SVM           Logistic Regression      Multinomial Naive Bayes
                 │                                  (LinearSVC)              (liblinear)                 (alpha=1.0)
                 │                                        │                        │                        │
                 └────────────────────────────────────────┼────────────────────────┴────────────────────────┘
                                                          ▼
                                      [PAIRED STATISTICAL EVALUATION]
                               • McNemar Exact Binomial Tests (Overall & Class-Specific)
                               • Holm-Bonferroni Family-Wise Error Rate (FWER) Multiplicity Control
                               • Source-Wise & Channel-Wise Recall Stratification
```

### Key Scientific Takeaways

1. **DistilBERT Demonstrates Statistically Significant Out-of-Distribution Superiority:**  
   DistilBERT achieved an external scam recall of **96.72%** (26 false negatives), significantly outperforming both Linear SVM (**92.68% recall**, 58 false negatives) and Logistic Regression (**92.68% recall**, 58 false negatives). Paired McNemar exact tests confirm that DistilBERT's advantage over Linear SVM ($p = 1.214 \times 10^{-6}$, Holm-adjusted $p = 2.429 \times 10^{-6}$) and Logistic Regression ($p = 1.808 \times 10^{-9}$, Holm-adjusted $p = 5.423 \times 10^{-9}$) is statistically significant.
2. **The "Smishing Generalization Gap" (Root Cause Discovery):**  
   Dissecting detection rates by communication channel and originating source reveals an extraordinary empirical insight:
   - **On External Email Phishing (Jose Nazario Corpus; $N = 522$):**  
     Linear SVM (94.64% recall; 494/522) and Logistic Regression (95.02% recall; 496/522) performed **virtually identical to DistilBERT (95.02% recall; 496/522)**. Only 2 errors separated DistilBERT and Linear SVM across 522 external phishing emails!
   - **On External Mobile Smishing (Mishra & Soni Dataset; $N = 268$):**  
     DistilBERT achieved **flawless 100.00% recall (268 / 268 detected; 0 missed)**. In stark contrast, Linear SVM collapsed to **88.81% recall (30 missed)** and Logistic Regression collapsed to **88.06% recall (32 missed)**.
   - *Scientific Interpretation:* The entire statistical superiority of DistilBERT over traditional ML is concentrated in **mobile SMS smishing**. Traditional n-gram models suffer from lexical mismatch, vocabulary sparsity, and out-of-vocabulary perturbations in informal mobile text. Deep contextual subword embeddings generalize seamlessly across concise, non-standard smishing narratives.
3. **Multinomial Naive Bayes Suffers Catastrophic Out-of-Distribution Collapse:**  
   While Naive Bayes achieved 96.93% accuracy on in-distribution validation data, it experienced a catastrophic failure on external scams, detecting only **33.33% of external scams (528 false negatives out of 792)**. Its independence assumption and frequency-based posteriors completely fail when evaluating unseen scam vocabularies under class imbalance.
4. **Legitimate Specificity Remains Near-Perfect Across All Models:**  
   All four models preserved exceptional specificity on the 6,233 held-out legitimate benchmark controls: DistilBERT produced 7 false positives (99.89% specificity), Linear SVM produced 13 false positives (99.79% specificity), Logistic Regression produced 27 false positives (99.57% specificity), and Naive Bayes produced 5 false positives (99.92% specificity). Paired McNemar testing shows no statistically significant difference between DistilBERT and Linear SVM on legitimate controls ($p = 0.1460$, Holm $p = 0.2920$).

---

## 2. Reconstructed Model Architectures & Training Protocol

To guarantee strict scientific equivalence, the traditional ML models were trained on the exact same canonical training split (60,957 records) and validated on the exact same validation split (7,618 records) established in Task 04.

### 1. Vectorization Architecture
- **Feature Extractor:** `TfidfVectorizer` (scikit-learn)
- **Analyzer:** Word-level unigrams (`ngram_range=(1, 1)`)
- **Document Frequency Bounds:** `min_df=1`, `max_df=1.0`
- **Fitted Vocabulary Size:** **115,436 unique tokens**
- **Precision:** `float32` (memory-optimized sparse matrix computation)

### 2. Traditional Classifier Hyperparameters
- **Logistic Regression:**
  - Solver: `liblinear` (coordinate descent)
  - Class Weight: `'balanced'` (inverse frequency weighting: $w_j = \frac{N}{2 \cdot N_j}$)
  - Maximum Iterations: 1,000
  - Random State: 42
- **Linear Support Vector Machine (`LinearSVC`):**
  - Penalty / Loss: L2 penalty, squared hinge loss
  - Dual: `dual=True`
  - Regularization Parameter: $C = 1.0$
  - Class Weight: `'balanced'`
  - Maximum Iterations: 2,000
  - Random State: 42
- **Multinomial Naive Bayes (`MultinomialNB`):**
  - Additive Smoothing: $\alpha = 1.0$ (Laplace smoothing)
  - Prior: Learned from empirical class frequencies

### 3. Verification of In-Distribution Validation Performance

Evaluating the reconstructed models on the canonical validation partition (7,618 records: 6,233 legitimate, 1,385 scam) confirmed exact alignment with the historical baselines from Notebook 03:

| Model Architecture | Validation Accuracy | Validation Precision | Validation Recall | Validation Scam F1 | Validation Macro F1 | Validation PR-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM (`LinearSVC`)** | **99.6981%** | 98.9928% | 99.3502% | **99.1712%** | **99.4933%** | **99.9673%** |
| **Logistic Regression** | **99.4093%** | 97.2496% | **99.5668%** | **98.3946%** | **99.0163%** | **99.9126%** |
| **Multinomial Naive Bayes** | **96.9283%** | **99.9133%** | 83.1769% | **90.7801%** | **94.4687%** | **99.3580%** |
| *DistilBERT (Notebook 06)* | *99.8950%* | *99.4975%* | *99.9278%* | *99.7118%* | *99.8238%* | *99.9894%* |

The trained vectorizer and model weights were serialized to `models/traditional_binary/` with comprehensive experiment metadata (`experiment_metadata.json`).

---

## 3. Comprehensive External Evaluation Results

Both traditional classifiers and DistilBERT were evaluated across the two independent external evaluation datasets constructed in Notebook 09.

### 1. Primary Expanded Test Set Performance ($N = 7,025$)
*(6,233 held-out legitimate controls + 792 curated external real scams; 11.27% scam ratio)*

| Model Architecture | Accuracy | Scam Precision | Scam Recall | Scam F1-Score | Macro F1 | Balanced Accuracy | Average Precision (PR-AUC) | ROC-AUC | False Positives | False Negatives |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DistilBERT** | **0.995302** | **0.990900** | **0.967200** | **0.978900** | **0.988100** | **0.983000** | **0.996820** | **0.999400** | **7** | **26** |
| **Linear SVM** | 0.989893 | 0.982597 | 0.926768 | 0.953866 | 0.974096 | 0.962341 | 0.990086 | 0.998621 | 13 | 58 |
| **Logistic Regression** | 0.987900 | 0.964520 | 0.926768 | 0.945267 | 0.969233 | 0.961218 | 0.985473 | 0.998213 | 27 | 58 |
| **Multinomial Naive Bayes** | 0.924128 | 0.981413 | 0.333333 | 0.497644 | 0.728305 | 0.666266 | 0.924043 | 0.985440 | 5 | 528 |

### 2. Balanced External Test Set Performance ($N = 1,584$)
*(792 held-out legitimate controls sampled with seed 42 + 792 curated external real scams; exact 50.0% scam ratio)*

| Model Architecture | Accuracy | Scam Precision | Scam Recall | Scam F1-Score | Macro F1 | Balanced Accuracy | Average Precision (PR-AUC) | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DistilBERT** | **0.982955** | 0.998696 | **0.967172** | **0.982681** | **0.982955** | **0.982955** | **0.999300** | **0.999200** |
| **Linear SVM** | 0.962753 | **0.998639** | 0.926768 | 0.961362 | 0.962704 | 0.962753 | 0.997878 | 0.998342 |
| **Logistic Regression** | 0.962121 | 0.997283 | 0.926768 | 0.960733 | 0.962074 | 0.962121 | 0.996813 | 0.997985 |
| **Multinomial Naive Bayes** | 0.666035 | 0.996226 | 0.333333 | 0.499527 | 0.624467 | 0.666035 | 0.983979 | 0.984021 |

---

## 4. Rigorous Statistical Significance Testing

To rigorously determine whether DistilBERT's performance gain is statistically meaningful or attributable to chance, paired McNemar exact tests were conducted across all 7,025 predictions. Family-wise error rate was strictly controlled using the step-down Holm-Bonferroni method.

### 1. Overall Paired McNemar Tests (All 7,025 Expanded Test Records)

For models A and B, $n_{01}$ represents cases where A is correct and B is incorrect; $n_{10}$ represents cases where A is incorrect and B is correct:

| Model Comparison ($A \text{ vs } B$) | $n_{01}$ ($A$ correct, $B$ wrong) | $n_{10}$ ($A$ wrong, $B$ correct) | Discordant Pairs ($n_{01} + n_{10}$) | Exact $p$-Value (Two-Sided) | Holm-Adjusted $p$-Value | Statistically Significant ($\alpha = 0.05$) | Direction of Superiority |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DistilBERT vs Linear SVM** | **50** | **12** | 62 | $1.2144 \times 10^{-6}$ | **$2.4288 \times 10^{-6}$** | **TRUE** | **DistilBERT > Linear SVM** |
| **DistilBERT vs Logistic Regression** | **65** | **13** | 78 | $1.8077 \times 10^{-9}$ | **$5.4231 \times 10^{-9}$** | **TRUE** | **DistilBERT > Logistic Regression** |
| **DistilBERT vs Naive Bayes** | **505** | **5** | 510 | $1.6989 \times 10^{-142}$ | **$6.7956 \times 10^{-142}$** | **TRUE** | **DistilBERT > Naive Bayes** |
| **Linear SVM vs Logistic Regression** | **29** | **15** | 44 | $0.0488$ | **$0.0488$** | **TRUE** | **Linear SVM > Logistic Regression** |

### 2. Class-Specific Paired McNemar Tests

Breaking down discordance by ground-truth class isolates where model decisions diverge:

| Target Class | Model Comparison ($A \text{ vs } B$) | $n_{01}$ ($A$ right, $B$ wrong) | $n_{10}$ ($A$ wrong, $B$ right) | Discordant Pairs | Exact $p$-Value | Holm-Adjusted $p$-Value | Statistically Significant |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scam ($N = 792$)** | **DistilBERT vs Linear SVM** | **41** | **9** | 50 | $5.6141 \times 10^{-6}$ | **$2.8071 \times 10^{-5}$** | **TRUE (DistilBERT detects +32 net scams)** |
| **Scam ($N = 792$)** | **DistilBERT vs Logistic Regression** | **41** | **9** | 50 | $5.6141 \times 10^{-6}$ | **$2.8071 \times 10^{-5}$** | **TRUE (DistilBERT detects +32 net scams)** |
| **Scam ($N = 792$)** | **DistilBERT vs Naive Bayes** | **502** | **0** | 502 | $1.5275 \times 10^{-151}$ | **$9.1648 \times 10^{-151}$** | **TRUE (DistilBERT detects +502 net scams)** |
| **Legitimate ($N = 6,233$)** | **DistilBERT vs Linear SVM** | **9** | **3** | 12 | $0.1460$ | **$0.2920$** | **FALSE (Statistically Equivalent)** |
| **Legitimate ($N = 6,233$)** | **DistilBERT vs Logistic Regression** | **24** | **4** | 28 | $1.7999 \times 10^{-4}$ | **$5.3997 \times 10^{-4}$** | **TRUE (DistilBERT has -20 fewer FPs)** |
| **Legitimate ($N = 6,233$)** | **DistilBERT vs Naive Bayes** | **3** | **5** | 8 | $0.7266$ | **$0.7266$** | **FALSE (Statistically Equivalent)** |

#### Key Takeaway from Statistical Testing:
DistilBERT and Linear SVM are **statistically indistinguishable on legitimate communications** ($p = 0.2920$). Their statistical divergence is driven exclusively by the **Scam class ($p = 2.807 \times 10^{-5}$)**, where DistilBERT correctly identifies 41 external scams that Linear SVM misses.

---

## 5. The Smishing Generalization Gap: Source & Channel Dissection

Analyzing per-source and per-channel detection rates provides the empirical explanation for DistilBERT's statistical superiority:

### Source-Level Detection Performance ($N = 792$ External Scams)

| External Source Dataset | Channel | Total Scams | DistilBERT Detected | Linear SVM Detected | Logistic Reg Detected | Naive Bayes Detected | DistilBERT Recall | Linear SVM Recall | Logistic Reg Recall | Naive Bayes Recall |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AbayomiAlli SMS** | SMS | 2 | 2 | 2 | 2 | 2 | **100.00%** | **100.00%** | **100.00%** | **100.00%** |
| **Jose Nazario Phishing** | Email | 522 | 496 | 494 | 496 | 163 | **95.02%** | **94.64%** | **95.02%** | **31.23%** |
| **Mishra & Soni SMS** | SMS | 268 | **268** | **238** | **236** | **99** | **100.00%** | **88.81%** | **88.06%** | **36.94%** |
| **Combined Total** | -- | **792** | **766** | **734** | **734** | **264** | **96.72%** | **92.68%** | **92.68%** | **33.33%** |

```
                       EXTERNAL SCAM RECALL BY SOURCE & MODALITY
100% ┌────────────────────────────────────────────────────────────────────────┐
     │  ████████████████████  ████████████████████                            │
 90% │  ████  ████  ████      ████                                            │
     │  ████  ████  ████      ████  ████  ████                                │
 80% │  ████  ████  ████      ████  ████  ████                                │
     │  ████  ████  ████      ████  ████  ████                                │
 50% │  ████  ████  ████      ████  ████  ████                                │
     │  ████  ████  ████      ████  ████  ████                                │
 30% │  ████  ████  ████ ░░░  ████  ████  ████ ░░░                            │
  0% └────┬─────┬─────┬───┬─────┬─────┬─────┬───┬─────┬─────┬─────┬───────────┘
        Dist   SVM   LR  NB   Dist   SVM   LR  NB   Dist   SVM   LR  NB
        [Jose Nazario Email]  [Mishra & Soni SMS]   [AbayomiAlli SMS]
        (N = 522; ~95% Tied)  (N = 268; SMISHING GAP) (N = 2; 100% Tied)
```

### Forensic Analysis of the Smishing Gap

1. **Email Phishing Parity (Nazario Corpus):**  
   On long-form email phishing (mean length: 1,489 characters), traditional TF-IDF models perform on par with DistilBERT. Because phishing emails contain dense collections of typical financial keywords (`"account"`, `"verify"`, `"security"`, `"bank"`, `"statement"`, `"login"`), simple term-frequency vectors reliably trigger linear decision boundaries. Both DistilBERT and Logistic Regression detected 496/522 emails (95.02%), while Linear SVM detected 494/522 (94.64%).
2. **Mobile Smishing Failure (Mishra & Soni Corpus):**  
   On short mobile smishing texts (mean length: 147 characters), traditional n-gram models experienced severe performance degradation, missing 30 to 32 smishing attacks (11.2% false negative rate). In contrast, DistilBERT detected **100.00% of all 268 smishing messages**.
3. **Linguistic Mechanisms Driving the Gap:**  
   - **Lexical Condensation:** SMS messages lack standard email headers, greeting formalisms, and explanatory paragraphs. Attackers compress the fraudulent narrative into 15–30 words (`"URGENT: Your Barclays debit card has been suspended due to unusual activity. Tap [URL] to restore access"`). If key tokens differ from training n-grams (e.g. unfamiliar URL shorteners, colloquial abbreviations, alternate institution names), TF-IDF vectors become sparse or zero-weighted.
   - **Contextual Semantic Generalization:** DistilBERT's multi-head self-attention models syntactic relationships and semantic roles (e.g., urgency cue + negative financial consequence + imperative action link) rather than literal token matches. Subword tokenization (WordPiece) further protects DistilBERT from out-of-vocabulary misspellings and token variations that completely break unigram dictionaries.

---

## 6. Generated Visualizations & Analytical Artifacts

Notebook 10 generated seven publication-ready figures in both high-resolution PNG and vector PDF formats, stored in [`outputs/external_evaluation_traditional_ml/results/figures/`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/outputs/external_evaluation_traditional_ml/results/figures/):

| Figure ID & Filename | Visual Representation | Key Empirical Finding Illustrated |
| :--- | :--- | :--- |
| **`01_overall_performance_comparison`** | Grouped bar chart comparing Accuracy, Scam Recall, Scam F1, and Balanced Accuracy across all 4 models. | Visually establishes DistilBERT's across-the-board dominance, Linear SVM's strong second-place performance, and Naive Bayes's collapse. |
| **`02_confusion_matrix_comparison`** | $2 \times 2$ grid of normalized confusion matrices for DistilBERT, Linear SVM, Logistic Regression, and Naive Bayes. | Highlights the extreme false negative asymmetry (Naive Bayes: 528 FN; SVM/LR: 58 FN; DistilBERT: 26 FN) alongside uniform low false positives (5–27 FP). |
| **`03_precision_recall_curves`** | Superimposed Precision-Recall curves on the primary expanded test set with Average Precision (PR-AUC) scores. | Illustrates DistilBERT's near-perfect area under the curve (PR-AUC = 0.9968) compared to Linear SVM (0.9901), Logistic Regression (0.9855), and Naive Bayes (0.9240). |
| **`04_mcnemar_discordance_comparison`** | Bi-directional bar chart plotting $n_{01}$ (A correct, B wrong) versus $n_{10}$ (A wrong, B correct) for all 4 paired model comparisons. | Demonstrates the extreme statistical skew favoring DistilBERT: 50 vs 12 against SVM ($p < 10^{-5}$), 65 vs 13 against LR ($p < 10^{-8}$), and 505 vs 5 against Naive Bayes ($p < 10^{-141}$). |
| **`05_false_positive_negative_comparison`** | Side-by-side grouped bar chart illustrating total False Positives and False Negatives on the expanded test set. | Visualizes the critical tradeoff: DistilBERT achieves both the lowest false negatives (26) and the lowest false positives among competitive models (7), dominating the Pareto frontier. |
| **`06_validation_external_macro_f1`** | Paired bar chart contrasting in-distribution validation Macro F1 against out-of-distribution external Macro F1. | Exposes the out-of-distribution generalization drop: DistilBERT drops only 1.04% (0.9985 $\rightarrow$ 0.9881), Linear SVM drops 2.08% (0.9949 $\rightarrow$ 0.9741), Logistic Regression drops 2.10% (0.9902 $\rightarrow$ 0.9692), while Naive Bayes collapses by 21.64% (0.9447 $\rightarrow$ 0.7283). |
| **`07_per_source_scam_recall`** | Stratified bar chart showing external scam recall across Jose Nazario Phishing, Mishra & Soni SMS, and AbayomiAlli SMS. | Clearly visualizes the "Smishing Gap": all competitive models achieve ~95% recall on email phishing, but DistilBERT achieves 100% on SMS smishing where Linear SVM drops to 88.8% and LR to 88.1%. |

---

## 7. Direct Answers to Core Research Questions

### Question 1: Are traditional ML baselines competitive with Transformers on external financial scams?
**Answer: Partially competitive on email, but uncompetitive on mobile smishing.**  
Linear SVM and Logistic Regression achieve respectable external detection (**92.68% scam recall**, ~0.974 Macro F1). On long-form email phishing, their performance matches DistilBERT (~95.0% recall). However, they cannot reliably substitute for Transformers across multi-channel environments due to an 11.2% drop in smishing detection.

### Question 2: Is DistilBERT's superior performance statistically significant?
**Answer: YES, conclusively.**  
Paired McNemar exact tests with Holm-Bonferroni correction confirm that DistilBERT statistically outperforms Linear SVM ($p = 2.43 \times 10^{-6}$), Logistic Regression ($p = 5.42 \times 10^{-9}$), and Naive Bayes ($p = 6.80 \times 10^{-142}$).

### Question 3: Where does the contextual deep learning advantage originate?
**Answer: In syntactic compositionality and robust subword representations under length constraints.**  
The empirical advantage does not stem from recognizing longer emails, but from correctly detecting concise mobile SMS smishing narratives where keyword frequency signals are scarce and semantic structure carries the deceptive intent.

---

## 8. Directory Artifact & Reproducibility Inventory

All models, metadata, prediction outputs, and statistical evaluation tables are versioned and preserved in the repository:

1. **Model Checkpoints & Vectorizer Artifacts (`models/traditional_binary/`):**
   - `experiment_metadata.json`: Full training configuration, vocabulary parameters, and validation metrics.
   - `tfidf_vectorizer.joblib`: Fitted 115,436-feature TF-IDF vectorizer.
   - `linear_svm.joblib`, `logistic_regression.joblib`, `multinomial_nb.joblib`: Serialized trained classifier objects.
2. **Tabular Results & Statistical Outputs (`outputs/external_evaluation_traditional_ml/results/`):**
   - `final_model_comparison_summary.csv`: Master evaluation table across all 4 models and 11 performance metrics.
   - `mcnemar_overall.csv`: Overall paired McNemar test statistics, exact $p$-values, and Holm-adjusted decisions.
   - `mcnemar_class_specific.csv`: Class-stratified (Scam vs Legitimate) paired McNemar tests.
   - `source_level_recall.csv` & `source_level_counts.csv`: Detailed per-source detection counts and recall percentages.
   - `external_metrics.csv`: Performance metrics broken down across Expanded ($N = 7,025$) and Balanced ($N = 1,584$) datasets.
   - `validation_metrics.csv`: In-distribution validation baseline benchmarks.
   - `expanded_paired_predictions.csv`: Row-level aligned predictions across all 7,025 records for all four models.
3. **Visualizations (`outputs/external_evaluation_traditional_ml/results/figures/`):**
   - Figures 01 through 07 available in both `.png` and `.pdf` formats.
