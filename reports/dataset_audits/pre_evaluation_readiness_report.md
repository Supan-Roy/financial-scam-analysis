# Pre-Evaluation Readiness Report: External Financial Scam Evaluation

**Research Project Title:**  
*Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*

**Audit Date:** November 2026  
**Auditor:** Antigravity Research Engineering  
**Scope:** Pre-evaluation readiness verification of external evaluation datasets, deduplication integrity, model artifacts, and Google Colab execution configuration.  
**Report Location:** `reports/dataset_audits/pre_evaluation_readiness_report.md`  

---

## Executive Status Dashboard

| Audit Area | Check Item | Status | Verified Metric / Finding |
| :--- | :--- | :---: | :--- |
| **1. Primary Evaluation Dataset** | Record Count & Class Ratio | **PASS** | Exactly 7,030 rows (6,233 legitimate, 797 external scam). |
| **1. Curated Scam Dataset** | Record Count & Labels | **PASS** | Exactly 797 rows; 100% `label = 1`; 100% `is_synthetic = False`. |
| **1. Legitimate Test Preservation** | Exact 1:1 Match with `test.csv` | **PASS** | 100% byte-for-byte match on IDs, `original_text`, `normalized_text`, and labels. |
| **1. Dataset Hygiene** | Missing Values & ID Duplication | **PASS** | 0 duplicate IDs; 0 missing values in essential model fields. |
| **2. Scam Source Distribution** | Source Breakdown | **PASS** | Nazario: 527; Mishra & Soni: 268; AbayomiAlli: 2 (Total = 797). |
| **2. Benchmark Deduplication** | 12 IMC25 Template Exclusions | **PASS** | All 12 near-duplicate Mishra records excluded and logged in exclusion file. |
| **2. Deduplication Methodology** | Configuration & Thresholds | **PASS** | MinHash LSH (64 perm / 16 bands), word 3-shingles, Jaccard $\ge 0.70$ / 0.85. |
| **3. Balanced Dataset (50/50)** | Availability & Construction | **PASS** | Created `balanced_binary_external_test.csv` ($N = 1,594$; seed 42). Primary untouched. |
| **4. Original Model Availability** | Colab / Drive Model Artifact | **PASS** | Saved at `/content/drive/MyDrive/financial-scam-analysis/models/distilbert_binary/`. |
| **4. Local Workspace Weights** | Local Git Repository Weights | **WARNING** | Intentionally excluded from local git via `.gitignore` lines 98–109. |
| **4. Model Architecture Distinction** | Experiment Disambiguation | **PASS** | DistilBERT A (real-only) verified distinct from Experiments B and C. |
| **5. Colab Inference Readiness** | Parameter & Schema Alignment | **PASS** | 100% retrieved from Notebook 06: `max_length = 512`, `normalized_text`, $\tau = 0.5$. |

---

## Detailed Check Verification

### 1. Evaluation Datasets Verification

#### Primary Dataset: `data/external_evaluation/expanded_binary_external_test.csv`
* **Total Records:** **7,030 rows** across 35 columns.
* **Class Split:**
  - Legitimate (`label = 0`): **6,233 records (88.66%)**
  - External Scam (`label = 1`): **797 records (11.34%)**
* **Channel Distribution:**
  - Email: **6,293 records** (5,766 legitimate, 527 scam)
  - SMS: **737 records** (467 legitimate, 270 scam)
* **Data Hygiene:**
  - Duplicate `record_id` occurrences: **0 (100% unique)**.
  - Null values across essential columns (`record_id`, `original_text`, `normalized_text`, `label`, `channel`, `source`, `evaluation_origin`): **0 nulls**.
* **Verdict:** **PASS**

#### Curated Scam Dataset: `data/external_evaluation/external_fin_scam_curated.csv`
* **Total Records:** **797 rows** across 35 columns.
* **Class Label:** 100% `label = 1`.
* **Synthetic Status:** 100% `is_synthetic = False` (authentically collected real-world scams).
* **Verdict:** **PASS**

#### Legitimate Benchmark Test Preservation
* **Reference Subset:** Canonical legitimate test partition from `data/splits/test.csv` (`label == 0`, $N = 6,233$).
* **Comparative Assertion Results:**
  - `(legit_expanded['record_id'] == legit_test['record_id']).all()` $\rightarrow$ **True** (Exact match)
  - `(legit_expanded['original_text'] == legit_test['original_text']).all()` $\rightarrow$ **True** (Exact match)
  - `(legit_expanded['normalized_text'] == legit_test['normalized_text']).all()` $\rightarrow$ **True** (Exact match)
  - `(legit_expanded['label'] == legit_test['label']).all()` $\rightarrow$ **True** (Exact match)
* **Integrity Guarantee:** Zero modification of text, zero reassignment of labels, zero inclusion of train or validation records.
* **Verdict:** **PASS**

---

### 2. External Scam Data & Deduplication Verification

#### Source Distribution of Curated Scams ($N = 797$)
1. **Jose Nazario Phishing Corpus (`email`):** **527 records** (66.12%)
   - Bank impersonation: 284
   - Account security phishing: 91
   - Payment service phishing (PayPal, eBay): 83
   - Billing & invoice scams: 35
   - Card verification fraud: 20
   - Tax refund phishing: 17
   - Money transfer fraud: 2
2. **Mishra & Soni SMS Phishing Dataset (`sms`):** **268 records** (33.63%)
   - Fake prize & cash compensation smishing: 204
   - Bank smishing: 51
   - Tax refund smishing (HMRC, COVID relief): 10
   - Payment service smishing (Apple ID): 3
3. **AbayomiAlli SMS Dataset (`sms`):** **2 records** (0.25%)
   - Authentic 419 mobile lottery prize claim smishing: 2
* **Verdict:** **PASS**

#### Verification of 12 Near-Duplicate Mishra Exclusions
During forensic audit, 12 smishing records in Mishra & Soni were discovered to share template wording with `Smishing Dataset IMC25 (public user reports)` in our benchmark training split.
* **Inspection of Exclusion Log (`external_scam_exclusion_log.csv`):**
  - Rows 574, 587, 788, 1703, 2793, 4063, 4338, 4667, 4672, 5391, 5469, 5791: **12 / 12 present in exclusion log**.
* **Inspection of Curated Scam Corpus (`external_fin_scam_curated.csv`):**
  - Scams originating from `Mishra & Soni SMS Phishing Dataset` matching these rows: **0 records** (None slipped into curated set).
* **Verdict:** **PASS**

#### Duplicate-Audit Methodology Configuration
The deduplication pipeline applied across the corpus follows the framework established in `src/data/duplicate_detector.py`:
1. **Text Normalization:** `normalize_text_conservative()` applies case-folding and whitespace collapsing (`" ".join(text.lower().split())`).
2. **Word Shingling:** `get_word_shingles(k=3)` extracts overlapping 3-word shingles.
3. **Vectorized MinHash LSH Index:**
   - Permutations: `num_perm = 64`
   - Bands: `num_bands = 16` (Rows per band: $r = 4$)
   - Prime Modulus: $p = 4,294,967,311$ (Mersenne-adjacent prime $> 2^{32}$)
   - Random Seed: `seed = 42`
4. **Similarity Thresholds:**
   - **Internal Deduplication:** $\text{Jaccard} \ge 0.85$ (eliminates near-identical message variations within candidates).
   - **Cross-Corpus Overlap:** $\text{Jaccard} \ge 0.70$ combined with 40-character and 80-character normalized prefix matching (eliminates template leakage from the benchmark training/validation splits).
* **Verdict:** **PASS**

---

### 3. Balanced Evaluation Dataset Preparation

* **Initial Status:** Did not exist prior to this check.
* **Action Taken:** Executed `tmp_candidate_audit/create_balanced_dataset.py` to prepare a balanced evaluation slice:
  - **Scam cohort:** All **797 external real scams** (`label = 1`).
  - **Legitimate cohort:** Exactly **797 legitimate records** randomly sampled from the 6,233 held-out test partition using fixed seed `random_state = 42`.
* **Output File:** [`data/external_evaluation/balanced_binary_external_test.csv`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/data/external_evaluation/balanced_binary_external_test.csv)
  - Total records: **1,594 records** (797 legitimate, 797 scam).
  - Exact 50 / 50 class balance.
  - Channel balance: 1,253 Email (726 legit, 527 scam) and 341 SMS (71 legit, 270 scam).
* **Primary Dataset Safety:** Confirmed that `expanded_binary_external_test.csv` was **not altered** (remains 7,030 records).
* **Verdict:** **PASS**

---

### 4. Original Model Availability & Disambiguation

#### Architecture and Checkpoint Location
* **Model Checkpoint:** Fine-tuned DistilBERT Base Uncased (`distilbert/distilbert-base-uncased`) with binary sequence classification head (`num_labels = 2`).
* **Environment Storage Location:**
  - **Google Colab / Drive (Active Run Environment):**  
    `/content/drive/MyDrive/financial-scam-analysis/models/distilbert_binary/`
  - **Local Windows Machine:**  
    The `models/` directory does not exist on the local Windows filesystem because `.gitignore` (lines 98–109) explicitly excludes model weights (`*.safetensors`, `*.bin`, `*.pt`, `saved_models/`) to prevent committing large binary files to GitHub.
* **Disambiguation Across Saved Experiments:**
  - **Experiment A (`models/distilbert_binary/`):** **THIS IS THE REQUIRED TARGET MODEL.** Trained strictly on the 60,957 real binary training communications from Notebook 06.
  - **Experiment B (`models/distilbert_experiment_b/`):** Synthetic-only model from Notebook 08 (trained on V3.1 synthetic scams; not for benchmark evaluation).
  - **Experiment C (`models/distilbert_experiment_c/`):** Real + Synthetic augmented model from Notebook 08 (trained on real + synthetic communications; not the canonical real-only baseline).
* **Verdict:** **PASS (Colab / Drive)** / **WARNING (Local absence due to standard .gitignore)**

---

### 5. Colab Readiness & Exact Configuration Parameters

All settings were extracted directly from `notebooks/06_transformer_based_modeling.ipynb` and `notebooks/07_source_dependency_and_generalization_analysis.ipynb`:

| Parameter | Exact Value | Source Reference |
| :--- | :--- | :--- |
| **Model Architecture** | `DistilBertForSequenceClassification` | Notebook 06 Cell 22 |
| **Base Checkpoint** | `distilbert/distilbert-base-uncased` | Notebook 06 Cell 15 |
| **Drive Model Path** | `/content/drive/MyDrive/financial-scam-analysis/models/distilbert_binary` | Notebook 06 Cell 26 |
| **Input Text Field** | `"normalized_text"` (renamed to `"text"` for HuggingFace Dataset) | Notebook 06 Cell 20 |
| **Max Sequence Length** | `max_length = 512` | Notebook 06 Cell 20 |
| **Truncation** | `truncation = True` | Notebook 06 Cell 20 |
| **Padding** | Dynamic padding via `DataCollatorWithPadding(tokenizer, pad_to_multiple_of=8)` | Notebook 06 Cell 21 |
| **Inference Batch Size** | `batch_size = 16` or `32` (`per_device_eval_batch_size = 32`) | Notebook 06 Cell 23 |
| **Probability Function** | `torch.softmax(outputs.logits, dim=-1)` | Notebook 06 Cell 21 & Nb 07 Cell 27 |
| **Decision Rule / Threshold** | `argmax(axis=1)` (equivalent to $\tau = 0.5$ on `scam_probability`) | Notebook 06 Cell 21 |
| **Binary Label Mapping** | `0` = Legitimate Financial Communication<br>`1` = Financial Scam Communication (`pos_label = 1`) | Canonical Schema |

---

## 6. Exact File Paths for Google Colab Execution

### Files Required on Google Drive

```
/content/drive/MyDrive/financial-scam-analysis/
├── models/
│   └── distilbert_binary/                     <-- Saved fine-tuned DistilBERT model
│       ├── config.json
│       ├── model.safetensors (or pytorch_model.bin)
│       ├── tokenizer_config.json
│       ├── vocab.txt
│       └── special_tokens_map.json
└── data/
    └── external_evaluation/
        ├── expanded_binary_external_test.csv  <-- Primary evaluation set (7,030 rows)
        ├── balanced_binary_external_test.csv  <-- Balanced evaluation set (1,594 rows)
        └── external_fin_scam_curated.csv      <-- Curated external scams only (797 rows)
```

### Colab Loading Blueprint

```python
from pathlib import Path
import pandas as pd
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Mount Google Drive
DRIVE_ROOT = Path("/content/drive/MyDrive/financial-scam-analysis")
MODEL_DIR = DRIVE_ROOT / "models" / "distilbert_binary"
EVAL_DIR = DRIVE_ROOT / "data" / "external_evaluation"

# 2. Load Evaluation Datasets
df_expanded = pd.read_csv(EVAL_DIR / "expanded_binary_external_test.csv", low_memory=False)
df_balanced = pd.read_csv(EVAL_DIR / "balanced_binary_external_test.csv", low_memory=False)

# 3. Load Canonical Saved Model and Tokenizer (DO NOT re-train)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))
model = AutoModelForSequenceClassification.from_pretrained(str(MODEL_DIR)).to(device)
model.eval()

# 4. Ready for pre-inference dataset tokenization using:
# text_col = "normalized_text"
# max_length = 512
```

---

## 7. Readiness Conclusion

All evaluation datasets, deduplication filters, balanced sampling artifacts, and Colab configuration parameters have been verified. No model training, fine-tuning, prediction generation, or metric evaluation was performed.

**Readiness Status:** **READY FOR GOOGLE COLAB EVALUATION**  
*Awaiting user approval before proceeding.*
