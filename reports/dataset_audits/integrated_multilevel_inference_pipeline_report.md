# Research Report: Integrated Multi-Level Financial Scam Inference Pipeline (Notebook 12)

**Research Project:** *Explainable Multi-Level Transformer-Based Framework for Financial Scam Narrative Detection and Fraud Analysis in Digital Communications*  
**Date:** 2026-11-27  
**Notebook Reference:** [`notebooks/12_integrated_multilevel_inference.ipynb`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/notebooks/12_integrated_multilevel_inference.ipynb)  
**Evaluated Artifacts:**
- **Level 1 Binary Classifier:** DistilBERT Fine-Tuned on Real Benchmark Splits (`models/distilbert_binary/`, Notebook 06)
- **Level 2 Subtype Classifier:** DistilBERT Fine-Tuned on Full Combined Synthetic Corpus (13 classes, `models/distilbert_multilevel/checkpoints/subtype_full_combined/`, Notebook 11)
- **Level 2 Fraudulent Intent Classifier:** DistilBERT Fine-Tuned on Full Combined Synthetic Corpus (5 classes, `models/distilbert_multilevel/checkpoints/intent_full_combined/`, Notebook 11)
- **Level 2 Social-Engineering Tactics Recognizer:** DistilBERT Fine-Tuned on Full Combined Synthetic Corpus (9 multilabel targets, `models/distilbert_multilevel/checkpoints/tactics_full_combined/`, Notebook 11)
**Execution Environment:** NVIDIA Tesla T4 GPU (14.56 GB VRAM), CUDA-accelerated PyTorch, Hugging Face Transformers

---

## 1. Executive Summary & Research Motivation

Prior phases of this research established specialized Transformer models across distinct analytical tiers:
1. **Perimeter Binary Detection (Notebooks 06, 09, 10):** Achieved 99.895% test accuracy on canonical benchmark data and 96.72% recall on independently sourced real-world external scams (100% on SMS smishing).
2. **Multi-Level Semantic Modeling (Notebook 11):** Achieved 0.9027 Subtype Macro F1, 0.9280 Intent Macro F1, and 0.9113 Tactics Macro F1 across pooled synthetic benchmarks ($N = 1,053 / 912$).

However, deploying these independently trained checkpoints into a practical fraud defense system requires an **integrated, conditional inference pipeline**. In real-world operational environments (e.g., enterprise email security gateways, mobile SMS firewalls, digital banking message filters), executing computationally intensive narrative decomposition on every benign message would impose unnecessary latency and GPU overhead.

**Notebook 12** bridges the gap between disconnected model checkpoints and an operational multi-tier system by developing a unified, conditional inference engine. The pipeline enforces a two-stage routing protocol:
- **Level 1 (Binary Gatekeeper):** Evaluates incoming raw communications. If classified as `legitimate`, the pipeline immediately short-circuits and returns a structured verdict, saving computational resources.
- **Level 2 (Deep Fraud Narrative Decomposition):** If classified as `financial_scam`, the message is automatically routed in parallel to the second-level models to decompose the scam subtype, the criminal intent, and all concurrent psychological manipulation tactics.

---

## 2. Integrated System Architecture & Routing Mechanics

```
Incoming Digital Communication (Raw Text)
                    │
                    ▼
┌──────────────────────────────────────────────────────────┐
│ Step 0: Canonical Preprocessing Harmonizer               │
│ - Collapses nested/malformed brackets                    │
│ - Standardizes entity placeholders into 15 tokens        │
└──────────────────────────────────────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────────────────┐
│ Level 1: Binary Scam Gatekeeper (DistilBERT Real-Only)   │
│ - Binary Softmax: P(scam) vs. P(legitimate), tau = 0.50  │
└──────────────────────────────────────────────────────────┘
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
 [P(scam) < 0.50]          [P(scam) >= 0.50]
   LEGITIMATE                FINANCIAL SCAM
       │                         │
       ▼                         ▼
┌──────────────┐   ┌────────────────────────────────────────────────────────┐
│ Terminate    │   │ Level 2: Multi-Level Semantic Decomposition            │
│ Return Result│   ├───────────────────┬──────────────────┬─────────────────┤
│ (Mean: ~19ms)│   │ Task 1: Subtype   │ Task 2: Intent   │ Task 3: Tactics │
└──────────────┘   │ (13 Classes)      │ (5 Classes)      │ (9 Multilabel)  │
                   │ Argmax Softmax    │ Argmax Softmax   │ Sigmoid >= 0.50 │
                   └───────────────────┴──────────────────┴─────────────────┘
                                         │
                                         ▼
                   ┌────────────────────────────────────────────────────────┐
                   │ Unified Structured JSON & Forensic Analysis Verdict    │
                   │ (Total Mean: ~63ms)                                    │
                   └────────────────────────────────────────────────────────┘
```

### Component Model Specifications

| Component Tier | Model Name & Path | Base Architecture | Pretrained Weights / Training Source | Task Type | Output Classes / Dimension |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Level 1** | `distilbert_binary` | `distilbert-base-uncased` | 60,957 Real Benchmark records (`splits/train.csv`) | Binary Single-Label | 2 (`legitimate`, `financial_scam`) |
| **Level 2 (A)**| `subtype_full_combined` | `distilbert-base-uncased` | 8,424 Combined Synthetic records (V3.1 + LLM) | Multiclass Single-Label | 13 scam narrative categories |
| **Level 2 (B)**| `intent_full_combined` | `distilbert-base-uncased` | 8,424 Combined Synthetic records (V3.1 + LLM) | Multiclass Single-Label | 5 criminal intent categories |
| **Level 2 (C)**| `tactics_full_combined`| `distilbert-base-uncased` | 8,424 Combined Synthetic records (V3.1 + LLM) | Multilabel Binary Relevance | 9 psychological manipulation tactics |

---

## 3. Preprocessing Harmonization & Fidelity Verification

To ensure that inference inputs strictly match the representations on which the models were fine-tuned, Notebook 12 integrates the standalone `PreprocessingHarmonizer` class directly from [`src/preprocessing/harmonizer.py`](file:///d:/Programs%20and%20Codes/financial-scam-analysis/src/preprocessing/harmonizer.py):

1. **Bracket Sanitization:** Collapses malformed and nested artifacts (`<<[FILE_NAME]>>` $\to$ `[FILE_NAME]`, `[[[[[PRODUCT]]]]]` $\to$ `[PRODUCT]`, `<<<URL>>>` $\to$ `<URL>`).
2. **Canonical Token Mapping:** Maps 40+ raw entity annotations (`<URL>`, `<PHONE>`, `<EMAIL>`, `<US_SSN>`, etc.) into the canonical 15-token bracket ontology (`[URL]`, `[PHONE_NUMBER]`, `[EMAIL_ADDRESS]`, `[IDENTIFIER]`, etc.).
3. **Idempotence & Verbatim Preservation:** Does not alter natural casing, whitespace, or cleartext punctuation; does not perform destructive regex masking on natural words.

### Empirical Replication Verification
In Cell 7, the newly embedded harmonizer was tested against 1,000 randomly sampled records from the official benchmark training set (`data/splits/train.csv`):
* **Sampled Records Checked:** 1,000
* **Normalization Mismatches:** **0 (0.00%)**
* **Verification Status:** **PASS (100.0% Exact Match)**

---

## 4. Pipeline Routing Validation & Smoke Testing

In Cell 9, the end-to-end inference engine (`analyze_message`) was validated against controlled synthetic cases:

### Case A: Benign Academic Notification (Legitimate Control)
* **Message:** `"Subject: Notice Regarding Semester Registration... registration for the upcoming semester will begin on December 1, 2026..."`
* **Level 1 Binary Prediction:** `legitimate` ($P(\text{legitimate}) = 0.9945$, $P(\text{scam}) = 0.0055$)
* **Routing Behavior:** Short-circuited immediately (`level_2_executed = False`).
* **Execution Latency:** **24.30 ms**.

### Case B: Urgent Phishing Attack (Scam Input)
* **Message:** `"URGENT: Your bank account will be suspended today. Verify your account immediately using the link below to avoid permanent account restriction. Do not share this message with anyone."`
* **Level 1 Binary Prediction:** `financial_scam` ($P(\text{scam}) = 1.0000$)
* **Routing Behavior:** Triggered complete Level 2 execution (`level_2_executed = True`).
* **Level 2 Multi-Level Predictions:**
  - **Subtype:** `account_verification` (Confidence: 0.9914)
  - **Intent:** `obtain_credentials_or_codes` (Confidence: 0.9919)
  - **Detected Tactics:** `secrecy` ($P = 0.9332$), `urgency` ($P = 0.6745$)
* **Execution Latency:** **91.00 ms**.

---

## 5. Multi-Source Demonstration Cohort Analysis ($N = 8$)

To demonstrate operational behavior across heterogeneous digital communications, an 8-message evaluation cohort was assembled spanning 4 diverse sources:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ Multi-Source Evaluation Cohort (8 Selected Demonstrations)                  │
├──────────┬──────────────────┬──────────────────────┬──────────┬─────────────┤
│ Demo ID  │ Source Cohort    │ Upstream Record ID   │ Channel  │ Ground Truth│
├──────────┼──────────────────┼──────────────────────┼──────────┼─────────────┤
│ DEMO-001 │ Real Legitimate  │ MEAJOR-LEG-039121    │ Email    │ Legitimate  │
│ DEMO-002 │ Real Legitimate  │ UCI-LEG-001007       │ SMS      │ Legitimate  │
│ DEMO-003 │ Real Scam (Ext)  │ EXT-SCAM-00569       │ SMS      │ Scam        │
│ DEMO-004 │ Real Scam (Ext)  │ EXT-SCAM-00627       │ SMS      │ Scam        │
│ DEMO-005 │ Synthetic V3.1   │ SYNTH-006509         │ Email    │ Scam        │
│ DEMO-006 │ Synthetic V3.1   │ SYNTH-006841         │ Email    │ Scam        │
│ DEMO-007 │ Synthetic LLM    │ LLM-SCAM-002237      │ Email    │ Scam        │
│ DEMO-008 │ Synthetic LLM    │ LLM-SCAM-000966      │ Chat     │ Scam        │
└──────────┴──────────────────┴──────────────────────┴──────────┴─────────────┘
```

### Integrated Inference Demonstration Results

| Demo ID | Source Corpus | Binary Ground Truth | Predicted Binary | Level 2 Routed | Predicted Subtype (Conf.) | Predicted Intent (Conf.) | Detected Tactics ($\ge 0.50$) |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **DEMO-001** | Real Legitimate (Email) | Legitimate | **Legitimate** | No | — | — | — |
| **DEMO-002** | Real Legitimate (SMS) | Legitimate | **Legitimate** | No | — | — | — |
| **DEMO-003** | Real External Scam (Mishra SMS) | Scam | **Scam** | **Yes** | `bank_transaction_alert` (0.842) | `obtain_credentials_or_codes` (0.781) | `urgency`, `authority_impersonation` |
| **DEMO-004** | Real External Scam (Mishra SMS) | Scam | **Scam** | **Yes** | `prize_reward` (0.912) | `induce_payment_or_transfer` (0.854) | `reward_or_benefit`, `urgency` |
| **DEMO-005** | Synthetic V3.1 (Email) | Scam | **Scam** | **Yes** | `romance_financial_manipulation` (0.995) | `induce_fraudulent_investment` (0.992) | `emotional_manipulation` |
| **DEMO-006** | Synthetic V3.1 (Email) | Scam | **Scam** | **Yes** | `romance_financial_manipulation` (0.995) | `induce_payment_or_transfer` (0.999) | `emotional_manipulation`, `urgency` |
| **DEMO-007** | Synthetic LLM (Email) | Scam | **Scam** | **Yes** | `card_transaction_alert` (0.969) | `obtain_personal_or_financial_info` (0.995) | `false_legitimacy`, `fear_or_threat`, `trust_exploitation`, `urgency` |
| **DEMO-008** | Synthetic LLM (Chat) | Scam | **Scam** | **Yes** | `loan_offer` (0.903) | `induce_fraudulent_investment` (0.971) | `false_legitimacy`, `reward_or_benefit`, `scarcity` |

---

## 6. Qualitative Comparison: Second-Level Predictions vs. Reference Annotations

For the 4 synthetic demonstration messages (where fine-grained ground-truth annotations exist), predictions were compared against reference labels:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ Synthetic Second-Level Ground Truth vs. Prediction Audit                    │
├──────────┬──────────────────┬──────────────────────┬─────────────┬──────────┤
│ Demo ID  │ Task Tier        │ Reference Annotation │ Prediction  │ Match?   │
├──────────┼──────────────────┼──────────────────────┼─────────────┼──────────┤
│ DEMO-005 │ Subtype          │ romance_financial    │ romance_fin │ Exact    │
│ (V3.1)   │ Intent           │ induce_fraud_invest  │ induce_inv  │ Exact    │
│          │ Tactics          │ [emotional_manip]    │ [emotional] │ Exact    │
├──────────┼──────────────────┼──────────────────────┼─────────────┼──────────┤
│ DEMO-006 │ Subtype          │ romance_financial    │ romance_fin │ Exact    │
│ (V3.1)   │ Intent           │ induce_payment       │ induce_pay  │ Exact    │
│          │ Tactics          │ [emotional, urgency] │ [emotional, │ Exact    │
│          │                  │                      │  urgency]   │          │
├──────────┼──────────────────┼──────────────────────┼─────────────┼──────────┤
│ DEMO-007 │ Subtype          │ card_trans_alert     │ card_alert  │ Exact    │
│ (LLM)    │ Intent           │ obtain_personal_info │ obtain_info │ Exact    │
│          │ Tactics          │ [emotional, fear,    │ [false_leg, │ Partial  │
│          │                  │  trust_exploit]      │  fear, trust│ (Missing │
│          │                  │                      │  urgency]   │ emotion) │
├──────────┼──────────────────┼──────────────────────┼─────────────┼──────────┤
│ DEMO-008 │ Subtype          │ investment_crypto    │ loan_offer  │ Mismatch │
│ (LLM)    │ Intent           │ induce_payment       │ induce_inv  │ Semantic │
│          │ Tactics          │ [authority, reward,  │ [false_leg, │ Partial  │
│          │                  │  scarcity, secrecy]  │ reward, scrc│ (Missed  │
│          │                  │                      │             │ secrecy) │
└──────────┴──────────────────┴──────────────────────┴─────────────┴──────────┘
```

### Key Analytical Takeaways
1. **Flawless Agreement on Programmatic Narratives:** On V3.1 messages (DEMO-005 and DEMO-006), the integrated models achieved 100% exact match across subtype, intent, and tactics with >0.99 confidence.
2. **Subtle Style Mismatches on Free-Form LLM Chat:** On DEMO-008, the model predicted `loan_offer` instead of `investment_crypto` (0.9027 confidence). Qualitative review of the chat text revealed conversational framing promising `"exclusive private allocation funds"`, which closely mirrors pre-approved loan disbursement syntax.
3. **Exploratory Real Scam Inferences:** On real external SMS smishing (DEMO-003 and DEMO-004), the pipeline produced highly plausible operational outputs (e.g., classifying a banking alert smish into `bank_transaction_alert` with intent `obtain_credentials_or_codes` and tactics `urgency`).

---

## 7. Computational Latency & GPU Resource Footprint

Inference latency and hardware resource consumption were benchmarked on an NVIDIA Tesla T4 GPU (5 repetitions per message after 2 warm-up cycles):

| Measurement Dimension | Parameter / Result | Operational Interpretation |
| :--- | :--- | :--- |
| **Hardware Platform** | NVIDIA Tesla T4 (14.56 GB GDDR6) | Standard cloud inference environment |
| **Total Model Footprint** | **267,836,189 parameters** (4 DistilBERT models) | ~1.02 GB VRAM memory footprint |
| **Legitimate Path Latency** | **18.88 ms** (Min: 9.37 ms, Max: 35.79 ms) | Only executes Level 1 binary classifier |
| **Scam Path Latency** | **62.58 ms** (Min: 24.21 ms, Max: 146.29 ms) | Executes all 4 models sequentially |
| **Overall Mean Latency** | **51.66 ms** | Combined weighted average across 8 demos |
| **Throughput (Sequential)**| **~19.35 messages/second** (Scam path) | Single-stream unbatched inference |
| **Throughput (Legitimate)**| **~52.96 messages/second** (Benign path) | High-speed perimeter filtering |

```
Inference Latency Profile (Tesla T4 GPU):
Legitimate Path: [█████████] 18.88 ms
Scam Path:       [███████████████████████████████] 62.58 ms
                                            ▲
                                            └── Short-circuit saves ~43.70 ms (69.8%) per benign email!
```

---

## 8. Saved Inference Artifacts

The execution exported structured forensic artifacts to Google Drive under:  
`outputs/distilbert_multilevel/inference/`

1. **`integrated_demo_results.json` (34.9 KB):** Complete serialized JSON objects containing input text, canonical normalized representation, routing flags, Level 1 probabilities, Level 2 predictions with full softmax/sigmoid distributions, and execution timestamps.
2. **`integrated_demo_summary.csv` (1.8 KB):** Compact tabular summary of demonstration inputs, ground-truth labels, predicted classes, and routing outcomes.
3. **`synthetic_level2_comparison.csv` (1.7 KB):** Granular comparison table evaluating synthetic second-level agreement.
4. **`inference_latency_benchmark.csv` (1.2 KB):** Raw timing records across all 5 benchmark runs per demonstration message.
5. **`inference_performance_summary.json` (0.5 KB):** High-level summary metrics (mean, min, max latencies, parameter counts).
6. **`integrated_inference_latency.png` / `.pdf`:** High-resolution latency comparison and resource distribution charts.

---

## 9. Methodological Limitations & Threats to Validity

1. **Sequential Architecture Overhead:** Running 4 separate DistilBERT models results in 4 forward passes through 66M parameters each (267.8M total), with duplicate self-attention computations over the same input sequence.
2. **Cascading Error Propagation:** Because second-level analysis is conditional on Level 1, a binary false negative (missed scam) irrevocably prevents subtype, intent, and tactic analysis from occurring.
3. **Small Demonstration Cohort:** The 8 demonstration messages provide qualitative operational validation; quantitative generalizability remains anchored in Notebooks 06, 09, 10, and 11.
4. **Absence of Real Level 2 Ground Truth:** Real-world scam outputs remain exploratory due to the lack of human-annotated real-world second-level labels.

---

## 10. Strategic Next Steps: Toward Multi-Task Architectures & XAI (Task 16+)

The operational validation in Notebook 12 establishes the blueprint for the next phase of research:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ Next Phase Roadmap (Task 16+)                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Unified Multi-Task Architecture (Multi-Task DistilBERT):                 │
│    Unify the 4 independent models into a single shared Transformer encoder   │
│    with 4 task-specific classification heads. This will collapse memory     │
│    footprint from 267.8M to ~67M parameters and cut scam latency from       │
│    62.58 ms to under 20 ms.                                                 │
│                                                                             │
│ 2. Explainable AI (XAI) Attribution Pipeline:                               │
│    Integrate token-level attribution (SHAP, Integrated Gradients, attention │
│    rollout) to highlight the exact deceptive clauses that triggered each    │
│    detected intent and tactic.                                              │
│                                                                             │
│ 3. Interactive Web Security Dashboard:                                      │
│    Package the unified pipeline and XAI explanations into an interactive    │
│    Streamlit / FastAPI analyst interface.                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 11. Verification & Reproducibility Checklist

- [x] All 4 model checkpoints (`distilbert_binary`, `subtype`, `intent`, `tactics`) successfully loaded and verified on CUDA.
- [x] `PreprocessingHarmonizer` verified against 1,000 canonical training records with 0 mismatches.
- [x] Conditional routing logic smoke tested on benign and phishing controls; 100% routing consistency confirmed.
- [x] Multi-source demonstration collection ($N = 8$) executed; structured JSON and CSV results exported.
- [x] Latency benchmarks measured with 2 warm-up and 5 repeated runs on NVIDIA Tesla T4 GPU.
- [x] Qualitative analysis of synthetic second-level agreement and exploratory real scam inferences documented.
