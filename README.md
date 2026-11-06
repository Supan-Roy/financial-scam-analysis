# An Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: Academic Research](https://img.shields.io/badge/license-Research%20Only-lightgrey.svg)](LICENSE)
[![Framework: PyTorch & HuggingFace](https://img.shields.io/badge/framework-PyTorch%20%7C%20Transformers-orange.svg)](https://pytorch.org/)

## 1. Project Overview & Research Objectives

Digital financial fraud increasingly exploits sophisticated linguistic narratives, psychological manipulation, and contextual deception across various digital communication channels (e.g., email, SMS/smishing, instant messaging). Traditional detection paradigms often reduce this challenge to shallow binary spam/ham classification, failing to unpack the underlying deceptive mechanisms or provide interpretable rationale for security analysts and end users.

This research project develops an intelligent, explainable, natural language processing (NLP) framework designed for in-depth financial scam analysis. The framework adopts a multi-level Transformer-based architecture coupled with Explainable AI (XAI) techniques to achieve four primary analytical objectives:

1. **Financial Scam Narrative Detection:** Identify, parse, and analyze financial scam-related communicative patterns, tropes, and thematic structures.
2. **Fraudulent Intent Analysis:** Model and classify the underlying objective behind suspicious messages (e.g., inducing credential harvesting, unauthorized fund transfers, advance-fee payments, fake invoices, or fraudulent investment schemes).
3. **Social Engineering Pattern Recognition:** Detect and decompose psychological manipulation tactics, including *urgency, authority impersonation, fear or threat, reward or benefit, scarcity, trust exploitation, emotional manipulation, false legitimacy,* and *secrecy*.
4. **Explainable AI (XAI):** Deliver transparent, human-interpretable rationales for model inferences by highlighting textual evidence, token-level attributions, and attention distributions (utilizing SHAP, LIME, and attention visualization).

---

## 2. Research Datasets & Data Governance

The research repository integrates three complementary corpora located in `data/raw/`. These datasets serve as immutable research assets: original records and provenance metadata are preserved without alteration.

| Dataset Asset | Filename | Record Count | Class Label | Synthetic Flag | Description & Provenance |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Real-world Financial Scams** | `real_fin_scam.csv` | 13,861 | `label=1` | `false` | Real-world email and SMS/smishing messages spanning banking, card alerts, loan offers, crypto investments, tax, refunds, and invoice fraud. Includes source attribution and provenance metadata. |
| **Synthetic Financial Scams** | `synthetic_financial_scams.csv` | 7,643 | `label=1` | `true` | Controlled, fully synthetic corpus covering 13 scam subtypes, four channels (email, SMS, chat, notification), and fine-grained annotations for fraudulent intent and social engineering tactics. Fictional entities and redacted placeholders only. |
| **Legitimate Communications** | `real_fin_legit.csv` | 62,332 | `label=0` | `false` | Baseline legitimate communications (4,670 SMS, 57,662 emails) covering `financial_legitimate` and `general_legitimate` categories. Sources include UCI SMS Spam Collection, Mendeley financial communications, and MeAJOR benign emails. |

> **Data Governance Policy:** Raw CSV files in `data/raw/` are strictly read-only. All transformations, tokenizations, and derived feature sets are saved to `data/interim/`, `data/processed/`, or `data/splits/`.

Detailed dataset cards and auditing reports are maintained under [`docs/`](docs/).

---

## 3. Technology Stack

The project prioritizes open-source, reproducible, and locally executable workflows:

- **Core & Numerics:** Python (>=3.10), [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Machine Learning Baselines:** [scikit-learn](https://scikit-learn.org/), SciPy
- **Deep Learning & Modeling:** [PyTorch](https://pytorch.org/), [Hugging Face Transformers](https://huggingface.co/docs/transformers), Datasets, Accelerate
- **Linguistic & Text Processing:** [NLTK](https://www.nltk.org/), [spaCy](https://spacy.io/)
- **Explainability (XAI):** [SHAP](https://shap.readthedocs.io/), [LIME](https://github.com/marcotcr/lime)
- **Data Visualization & Auditing:** [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Exploration & Prototyping:** [JupyterLab / Notebooks](https://jupyter.org/)
- **Testing & Verification:** [pytest](https://pytest.org/)

---

## 4. Repository Structure

```text
financial-scam-analysis/
│
├── data/                       # Data storage (governed, raw is immutable)
│   ├── raw/                    # Original raw CSV datasets (real_fin_scam, synthetic, legit)
│   ├── interim/                # Intermediate, normalized, or partially cleaned data
│   ├── processed/              # Fully preprocessed, tokenized, and model-ready artifacts
│   └── splits/                 # Stratified train/val/test splits (leakage-controlled)
│
├── notebooks/                  # Exploratory research and interactive prototyping
│
├── src/                        # Modular application and research source code
│   ├── __init__.py
│   ├── data/                   # Data loaders, dataset wrappers, and provenance tracking
│   ├── preprocessing/          # Cleaning, tokenization, text normalization
│   ├── analysis/               # Exploratory data analysis, vocabulary and narrative audits
│   ├── features/               # Handcrafted features, embeddings, and representations
│   ├── models/                 # Classical baselines, Transformer architectures, multi-level heads
│   ├── explainability/         # XAI implementations (SHAP, LIME, attention heatmaps)
│   └── evaluation/             # Evaluation metrics, confusion matrices, audit reporters
│
├── experiments/                # Experiment tracking and specialized run scripts
│   ├── baseline/               # Classical ML benchmarks (TF-IDF + SVM, Logistic Regression, etc.)
│   ├── transformers/           # Standard Transformer fine-tuning (BERT, RoBERTa, DeBERTa)
│   ├── multi_level/            # Joint multi-task narrative & intent architectures
│   └── explainability/         # Interpretability and rationale evaluation experiments
│
├── reports/                    # Generated research deliverables
│   ├── figures/                # Publication-quality charts, confusion matrices, and XAI plots
│   ├── tables/                 # Quantitative benchmark tables and performance comparisons
│   └── dataset_audits/         # Distribution, leakage, and data quality audit reports
│
├── configs/                    # Model, training, and experiment configuration files
│
├── tests/                      # Unit and integration test suite
│   └── __init__.py
│
├── docs/                       # Research documentation, dataset cards, and methodology notes
│   ├── generation_audit.md
│   ├── legitimate_dataset_audit.md
│   ├── legitimate_dataset_card.md
│   ├── meajor_legit_audit.md
│   └── synthetic_dataset_card.md
│
├── scripts/                    # Standalone utility scripts (e.g., preprocessing, batch runs)
│
├── requirements.txt            # Project dependencies and stack definition
├── README.md                   # Research project overview and documentation
├── .gitignore                  # Git ignore rules for ML workflows and datasets
└── main.py                     # Entry point driver for pipeline execution
```

---

## 5. Development Guidelines & Next Steps

1. **Environment Setup:** Dependency specifications are recorded in `requirements.txt`.
2. **Reproducibility:** Experiments are controlled via structured configurations in `configs/`.
3. **Data Integrity:** Any script accessing `data/raw/` must treat raw files as strictly read-only.

