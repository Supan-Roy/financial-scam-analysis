# An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Framework: PyTorch & HuggingFace](https://img.shields.io/badge/framework-PyTorch%20%7C%20Transformers-orange.svg)](https://pytorch.org/)
[![Tests: 29 Passed](https://img.shields.io/badge/tests-29%20passed-brightgreen.svg)](tests/)

---

## 1. Project Overview & Research Objectives

Digital financial fraud increasingly exploits sophisticated linguistic narratives, psychological manipulation, and contextual deception across various digital communication channels (e.g., email, SMS/smishing, instant messaging). Traditional detection paradigms often reduce this challenge to shallow binary spam/ham classification, failing to unpack the underlying deceptive mechanisms or provide interpretable rationale for security analysts and end users.

This research project develops an intelligent, explainable, natural language processing (NLP) framework designed for in-depth financial scam analysis. The framework adopts a multi-level Transformer-based architecture coupled with Explainable AI (XAI) techniques to achieve four primary analytical objectives:

1. **Financial Scam Narrative Detection:** Identify, parse, and analyze financial scam-related communicative patterns, tropes, and thematic structures.
2. **Fraudulent Intent Analysis:** Model and classify the underlying objective behind suspicious messages (e.g., inducing credential harvesting, unauthorized fund transfers, advance-fee payments, fake invoices, or fraudulent investment schemes).
3. **Social Engineering Pattern Recognition:** Detect and decompose psychological manipulation tactics, including *urgency, authority impersonation, fear or threat, reward or benefit, scarcity, trust exploitation, emotional manipulation, false legitimacy,* and *secrecy*.
4. **Explainable AI (XAI):** Deliver transparent, human-interpretable rationales for model inferences by highlighting textual evidence, token-level attributions, and attention distributions (utilizing SHAP, LIME, and attention visualization).

---

## 2. Research Milestones & Implementation Progress

| Phase / Milestone | Status | Key Deliverables & Documentation |
| :--- | :---: | :--- |
| **Task 01: Initial Dataset Audit Pipeline** | **Completed** | Full structural inspection, text profiling, and data quality audits across 83,836 records. [`reports/dataset_audits/dataset_audit_report.md`](reports/dataset_audits/dataset_audit_report.md) |
| **Task 02: Audit Validation & Leakage Investigation** | **Completed** | MinHash LSH deduplication, placeholder inventory, carrier gateway headers (`FRM:`), and class overlap audits. [`reports/dataset_audits/validation_report.md`](reports/dataset_audits/validation_report.md) |
| **Task 03: Canonical Dataset Engineering** | **Completed** | 30-column canonical schema, non-destructive normalization, and source provenance tracking. [`docs/canonical_preprocessing_and_schema.md`](docs/canonical_preprocessing_and_schema.md) |
| **Task 03.1: Preprocessing Forensic Verification** | **Completed** | Empirical gateway header verification (46 verified gateway transports), semantic placeholder alignment, and text reduction mathematical proof. [`reports/preprocessing/task_03_1_verification_report.md`](reports/preprocessing/task_03_1_verification_report.md) |
| **Task 04.0: Group-Aware Splitting Feasibility Analysis** | **Completed** | Disproved source-level grouping; established 71,533 indivisible group units; designed Stratified Group-Aware Greedy Partitioning (SGGP). [`reports/splitting/split_feasibility_report.md`](reports/splitting/split_feasibility_report.md) |
| **Task 04.1: Leakage-Resistant Dataset Splitting** | **Completed** | Partitioned 76,193 real records into Train (80%), Val (10%), Test (10%) with **0% duplicate cluster leakage** and < 0.004% deviation. [`docs/splitting_methodology.md`](docs/splitting_methodology.md) |
| **Exploratory Research & Text Profiling** | **Completed** | Distribution analysis, channel-class interaction, Simpson's Paradox word counts, 115k vocabulary forensic profiling, and sparsity pruning. [`docs/exploratory_data_analysis_and_text_representation.md`](docs/exploratory_data_analysis_and_text_representation.md) |
| **Task 05+: Baseline Models & Transformers** | *Next Phase* | Classical ML benchmarks (TF-IDF + SVM/XGBoost), fine-tuning modern Transformers (DeBERTa-v3, RoBERTa), and multi-task learning. |

---

## 3. Research Datasets & Data Governance

The research framework incorporates three complementary datasets located in `data/raw/` (total **83,836 records**). Raw datasets serve as immutable research assets:

| Dataset Asset | Filename | Record Count | Class Label | Synthetic Flag | Description & Documentation |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Real-world Financial Scams** | `real_fin_scam.csv` | 13,861 | `label=1` | `false` | Real-world email and SMS/smishing messages spanning banking, card alerts, loan offers, crypto investments, tax, refunds, and invoice fraud. Sources include IMC25 smishing, Nigerian Fraud, Kaggle phishing, and smishtank. [`docs/real_scam_dataset_card.md`](docs/real_scam_dataset_card.md) |
| **Synthetic Financial Scams** | `synthetic_financial_scams.csv` | 7,643 | `label=1` | `true` | Controlled synthetic corpus covering 13 scam subtypes, 4 channels (email, SMS, chat, notification), and fine-grained annotations for fraudulent intent and social engineering tactics. Fictional entities and redacted placeholders only. Held out for OOD/transfer evaluation. [`docs/synthetic_dataset_card.md`](docs/synthetic_dataset_card.md) |
| **Legitimate Communications** | `real_fin_legit.csv` | 62,332 | `label=0` | `false` | Baseline legitimate communications (4,670 SMS, 57,662 emails) covering `financial_legitimate` (19,201) and `general_legitimate` (43,131) categories. Sources include UCI SMS, Mendeley, and MeAJOR benign emails (trec5/6/7). [`docs/legitimate_dataset_card.md`](docs/legitimate_dataset_card.md) |

> **Data Governance Policy:** Raw CSV files in `data/raw/` are strictly read-only. All transformations produce derived data in `data/processed/` or `data/splits/`.

---

## 4. Real-World Benchmark Splits (Leakage-Resistant)

The initial empirical benchmark includes all **76,193 real-world records**, partitioned using **Stratified Group-Aware Greedy Partitioning (SGGP)**. Every duplicate cluster is kept intact in a single split to eliminate data leakage:

| Split Name | Target % | Actual Records | Actual % | Scam Records (%) | Legit Records (%) | Email Records (%) | SMS Records (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Train** | 80.00% | 60,957 | **80.00%** | 11,091 (18.19%) | 49,866 (81.81%) | 49,143 (80.62%) | 11,814 (19.38%) |
| **Validation** | 10.00% | 7,618 | **10.00%** | 1,385 (18.18%) | 6,233 (81.82%) | 6,142 (80.62%) | 1,476 (19.38%) |
| **Test** | 10.00% | 7,618 | **10.00%** | 1,385 (18.18%) | 6,233 (81.82%) | 6,142 (80.62%) | 1,476 (19.38%) |
| **Total Benchmark** | **100.00%** | **76,193** | **100.00%** | **13,861 (18.19%)** | **62,332 (81.81%)** | **61,427 (80.62%)** | **14,766 (19.38%)** |

*Complete split assignments are tracked for instant 1-click reproducibility in [`data/splits/split_assignments.csv`](data/splits/split_assignments.csv).*

---

## 5. Exploratory Notebooks & Text Representation Research

The repository includes two foundational exploratory research notebooks in `notebooks/` detailing linguistic distributions, representation mechanics, and forensic vocabulary profiling on the training split (60,957 records):

- **[`notebooks/01_dataset_understanding.ipynb`](notebooks/01_dataset_understanding.ipynb):** Comprehensive dataset understanding, class balance (81.81% legit vs 18.19% scam), cross-channel interaction (Scams are 72.83% SMS while Legit is 92.51% Email), word count distribution by channel and class (uncovering Simpson's Paradox in message lengths), and placeholder frequency asymmetry across sources.
- **[`notebooks/02_text_representation.ipynb`](notebooks/02_text_representation.ipynb):** Classical Bag-of-Words and TF-IDF representations, word-order invariance demonstrations, matrix sparsity analysis (99.28% sparse at full vocabulary), forensic tracing of numeric zero-strings (C source code and R statistical mailing list artifacts in legitimate emails), vocabulary document-frequency distribution (48.83% hapax legomena), and empirical pruning rationale (`min_df=5` cutting 75.13% noise).

*For a full technical report of the methodology, statistical distributions, and engineering takeaways, see [`docs/exploratory_data_analysis_and_text_representation.md`](docs/exploratory_data_analysis_and_text_representation.md).*

---

## 6. Pipeline Execution & CLI Reference

The project provides an integrated CLI interface through `main.py`:

```powershell
# 1. Run complete dataset audit pipeline (Task 01)
python main.py --audit

# 2. Run audit validation & near-duplicate leakage investigation (Task 02)
python main.py --validate

# 3. Run canonical preprocessing & text harmonization (Task 03 / 03.1)
python main.py --preprocess

# 4. Run leakage-resistant group-aware dataset splitting (Task 04.1)
python main.py --split

# 5. Execute automated test suite (29 tests)
python -m pytest tests/ -v
```

---

## 7. Repository Structure

```text
financial-scam-analysis/
│
├── configs/                     # Experiment, training, and splitting configurations
│   └── splitting_config.yaml    # Declarative SGGP splitting parameters and random seed
│
├── data/                        # Governed data storage (raw is strictly immutable)
│   ├── raw/                     # Original CSVs (real_fin_scam, synthetic, real_fin_legit)
│   ├── interim/                 # Intermediate artifacts
│   ├── processed/               # Canonical 30-column preprocessed CSV datasets
│   └── splits/                  # Benchmark partitions and split_assignments.csv
│
├── docs/                        # Research documentation, methodology, and dataset cards
│   ├── real_scam_dataset_card.md
│   ├── synthetic_dataset_card.md
│   ├── legitimate_dataset_card.md
│   ├── canonical_preprocessing_and_schema.md
│   ├── splitting_methodology.md
│   ├── exploratory_data_analysis_and_text_representation.md
│   └── meajor_legit_audit.md
│
├── notebooks/                   # Interactive Jupyter research and exploration notebooks
│   ├── 01_dataset_understanding.ipynb   # Exploratory distributions, text profiling, and split verification
│   └── 02_text_representation.ipynb      # Bag-of-Words, n-grams, and TF-IDF representations
│
├── reports/                     # Generated academic reports and audit deliverables
│   ├── dataset_audits/          # Data quality, near-duplicate clusters, and validation reports
│   ├── preprocessing/           # Normalization stats, gateway verification, and text reduction audits
│   └── splitting/               # Group integrity, strata distributions, and split summaries
│
├── src/                         # Modular research framework package
│   ├── analysis/                # Data profiling, bias analysis, and duplicate detection
│   ├── data/                    # Splitter, split validators, reporters, and schema definitions
│   ├── preprocessing/           # Channel mapping, placeholder harmonization, and pipeline driver
│   ├── models/                  # (Upcoming) Baselines, Transformer architectures, multi-level heads
│   └── explainability/          # (Upcoming) XAI attribution methods (SHAP, LIME, attention maps)
│
├── scripts/                     # Standalone CLI orchestration drivers
│   ├── run_dataset_audit.py
│   ├── run_audit_validation.py
│   ├── run_preprocessing.py
│   └── run_split.py
│
├── tests/                       # Automated regression and unit test suite (29 tests)
│   ├── test_audit.py
│   ├── test_validation.py
│   ├── test_preprocessing.py
│   └── test_splitter.py
│
├── requirements.txt             # Project dependency specification
├── LICENSE                      # Apache License 2.0
├── README.md                    # Research overview and framework documentation
└── main.py                      # Unified CLI driver
```

---

## 8. Technology Stack

- **Core & Numerics:** Python (>=3.10), [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [PyYAML](https://pyyaml.org/)
- **Machine Learning Baselines:** [scikit-learn](https://scikit-learn.org/), [SciPy](https://scipy.org/)
- **Deep Learning & Transformers:** [PyTorch](https://pytorch.org/), [Hugging Face Transformers](https://huggingface.co/docs/transformers), Datasets, Accelerate
- **Linguistic Processing:** [NLTK](https://www.nltk.org/), [spaCy](https://spacy.io/)
- **Explainability (XAI):** [SHAP](https://shap.readthedocs.io/), [LIME](https://github.com/marcotcr/lime)
- **Visualization:** [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Testing & Verification:** [pytest](https://pytest.org/)

---

## 9. License & Attribution

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

Third-party datasets utilized or referenced retain their original licenses and attribution requirements (MeAJOR CC BY 4.0, UCI SMS Spam Collection, Mendeley Data, and public domain threat feeds).
