"""
Generates the Qualitative Inspection Report for Synthetic Financial Scams V2.

Samples 5 records per subtype (65 total) and writes:
reports/dataset_audits/synthetic_v2_qualitative_sample.md
"""

import json
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "synthetic_financial_scams_v2.csv"
OUTPUT_REPORT_PATH = PROJECT_ROOT / "reports" / "dataset_audits" / "synthetic_v2_qualitative_sample.md"

def build_report():
    df = pd.read_csv(CSV_PATH)
    subtypes = df["phishing_type"].unique()

    sample_rows = []
    for sub in subtypes:
        sub_df = df[df["phishing_type"] == sub]
        sampled = sub_df.sample(n=5, random_state=42)
        sample_rows.append(sampled)

    sample_df = pd.concat(sample_rows)

    lines = []
    lines.append("# Qualitative Inspection of Synthetic Financial Scam Dataset (Version 2)")
    lines.append("")
    lines.append("**Dataset Source:** `data/raw/synthetic_financial_scams_v2.csv`  ")
    lines.append("**Evaluation Scope:** Read-only qualitative inspection of 65 randomly sampled records (5 records per each of the 13 canonical `phishing_type` categories).  ")
    lines.append("**Sampling Strategy:** Stratified random sample with fixed seed (`random_state=42`).  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Sample Distribution Summary")
    lines.append("")
    lines.append(f"- **Total Sampled Records:** {len(sample_df)}")
    lines.append(f"- **Subtypes Represented (13):** {sample_df['phishing_type'].nunique()} (5 records each)")
    lines.append("- **Primary Fraudulent Intents (5):**")
    for intent, count in sample_df["fraudulent_intent"].value_counts().items():
        lines.append(f"  - `{intent}`: {count} records")
    lines.append("- **Channels Represented (4):**")
    for ch, count in sample_df["scam_channel"].value_counts().items():
        lines.append(f"  - `{ch}`: {count} records")
    t_cards = sample_df["social_engineering_tactics"].apply(lambda x: len(json.loads(x))).value_counts().sort_index()
    lines.append("- **Tactics Cardinalities:**")
    for card, count in t_cards.items():
        lines.append(f"  - {card} tactics: {count} records")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Qualitative Inspection Records (65 Total)")
    lines.append("")

    curr_sub = ""
    rec_num = 1
    for idx, r in sample_df.iterrows():
        if r["phishing_type"] != curr_sub:
            curr_sub = r["phishing_type"]
            lines.append(f"### Subtype Group: `{curr_sub}`")
            lines.append("")

        lines.append(f"#### Record {rec_num}: `{r['id']}`")
        lines.append(f"- **ID:** `{r['id']}`")
        lines.append(f"- **Subtype (`phishing_type`):** `{r['phishing_type']}`")
        lines.append(f"- **Channel (`scam_channel`):** `{r['scam_channel']}`")
        lines.append(f"- **Primary Fraudulent Intent:** `{r['fraudulent_intent']}`")
        lines.append(f"- **Social-Engineering Tactics:** `{r['social_engineering_tactics']}`")
        lines.append(f"- **Primary Intent Evidence:** `{r['primary_intent_evidence']}`")
        lines.append(f"- **Narrative Evidence:** `{r['narrative_evidence']}`")
        lines.append(f"- **Tactics Evidence:** `{r['tactics_evidence']}`")
        lines.append("")
        lines.append("**Complete Original Text:**")
        lines.append("```text")
        lines.append(r["text"])
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        rec_num += 1

    # Detailed qualitative assessment section
    lines.append("## 3. Qualitative Assessment of Generated Language and Patterns")
    lines.append("")
    lines.append("### 3.1 Observed Linguistic and Structural Artifacts")
    lines.append("")
    lines.append("While Version 2 successfully eliminated the overt vocabulary contaminants of Version 1 (0 occurrences of 'fictional', 'synthetic', 'NOTICE N:', or prompt meta-commentary) and introduced non-deterministic intent mapping (H = 1.2939 bits), qualitative inspection reveals several unmistakable hallmarks of modular synthetic generation:")
    lines.append("")
    lines.append("1. **Tone & Register Clashes (Emotional vs. Bureaucratic Incongruity):**")
    lines.append("   - *Observed Examples:*")
    lines.append("     - `SYN2-05511` (`romance_financial_manipulation`, SMS): Starts with an intimate romantic appeal (*\"❤️ My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery... Please do not abandon me when I need your compassion the most.\"*) and abruptly ends with cold, bureaucratic administrative phrasing: *\"Remit the mandatory documentation fee of $2,628.80 to our accounting escrow department.\"*")
    lines.append("     - `SYN2-06182` (`family_emergency_request`, SMS): A child texting their parent (*\"Hi Dad, my phone was severely damaged in an accident so I am messaging you from this temporary line. I am sitting in total distress and feeling utterly helpless right now.\"*) suddenly speaks like a commercial collections officer: *\"You must complete this mandatory requirement before 5:00 PM today to avoid automatic forfeiture. Settle the required statutory handling fee of $2,799.00 using PayLink Mobile before the deadline.\"*")
    lines.append("     - `SYN2-06111` (`family_emergency_request`, SMS): A person reporting an urgent roadside crash to a cousin (*\"Hey Cousin Mark, I was involved in an unexpected fender bender and need to settle the repair before police arrive.\"*) ends with an automated online banking login prompt: *\"Input your electronic banking credentials and secondary password to confirm ownership.\"*")
    lines.append("   - *General Conclusion:* In informal relationship-based scenarios (romance, family emergencies), modularly concatenating institutional call-to-action strings produces severe pragmatic dissonance. In the real world, victims in romance or family emergency scams are directed to send peer-to-peer transfers to individuals or travel/hospital liaisons, not to an 'accounting escrow department' or asked to 'confirm ownership' with secondary passwords.")
    lines.append("")
    lines.append("2. **Formulaic Multi-Turn Chat Architecture:**")
    lines.append("   - *Observed Examples:* Across all 13 sampled chat records (`SYN2-02220`, `SYN2-02820`, `SYN2-03420`, `SYN2-03566`, `SYN2-05366`, `SYN2-05820`, `SYN2-05966`, `SYN2-05478`, `SYN2-05582`, `SYN2-06420`, `SYN2-06566`, `SYN2-06078`, `SYN2-06711`), Turn 2 is verbatim identical:")
    lines.append("     `[HH:MM AM] <User>: What happened? What do I need to do right now?`")
    lines.append("   - *General Conclusion:* Every chat conversation follows an invariable 3-turn choreography: Turn 1 (Scammer alert) -> Turn 2 (Victim asks the exact same prompt question) -> Turn 3 (Scammer pressure + call to action). This rigid back-and-forth structure is a glaring mechanical artifact that a transformer model could trivially exploit to identify chat records.")
    lines.append("")
    lines.append("3. **Unnatural Length and Density in Mobile Notifications:**")
    lines.append("   - *Observed Examples:*")
    lines.append("     - `SYN2-00566` (Notification, 46 words): *\"[Wallet Alert] An unrecognized login attempt was detected from a new device located in Chicago, IL. Audit Case Docket: CF-70398 registered under statutory financial compliance protocol. Keep this private settlement between us until the documentation is officially archived. Enter your online banking password and security PIN at https://apex-portal-verify.net/login to authenticate.\"*")
    lines.append("     - `SYN2-04766` (Notification, 49 words): *\"[Wallet Alert] An uncollected tax rebate of $378.50 from the previous statutory filing year has been processed. Failure to act immediately will result in permanent account termination and referral to collection authorities. Settle the required statutory handling fee of $378.50 using SwiftPay before the deadline.\"*")
    lines.append("   - *General Conclusion:* Authentic mobile push notifications and app alerts are strictly constrained by screen real estate (typically 15 to 25 words). Packing 3 to 4 full declarative sentences (problem statement, legal docket, secrecy admonition, and payment URL) into a single notification creates an unnaturally dense communication block.")
    lines.append("")
    lines.append("4. **Cross-Domain Tactic Contamination (Hybrid Templates):**")
    lines.append("   - *Observed Examples:*")
    lines.append("     - `SYN2-04020` (`prize_reward`, SMS): *\"Official winner notification: your entry ticket was awarded the $1,644.00 retail promotional grant. You have been pre-approved for an unrestricted credit line of $25,000 at zero introductory interest. Transfer the required security deposit of $1,644.00 via direct electronic bank wire today.\"*")
    lines.append("   - *General Conclusion:* The reward_or_benefit snippet for a $25,000 credit line was sampled into a retail sweepstakes prize scenario, creating a bizarre hybrid message where the recipient is simultaneously told they won a grant and pre-approved for a credit line.")
    lines.append("")
    lines.append("5. **Syntactic Modular Stacking (Sentence Concatenation Artifacts):**")
    lines.append("   - *Observed Examples:* In nearly every SMS and notification (e.g. `SYN2-00111`, `SYN2-00711`, `SYN2-00678`, `SYN2-02478`), the text consists of 3–4 disconnected declarative sentences placed back-to-back without transitional discourse markers (e.g., *\"Problem occurred. Threat/docket citation. Action required.\"*).")
    lines.append("   - *General Conclusion:* Real scam communications use subordinating conjunctions ('because', 'in order to', 'so that') and conversational connective tissue ('Please note that...', 'To prevent this,...'). Pure modular concatenation creates a staccato cadence that distinguishes synthetic messages from genuine social engineering communications.")
    lines.append("")
    lines.append("### 3.2 Label-Text Consistency Assessment")
    lines.append("")
    lines.append("- **Intent Realism:** In 100% of the 65 records, the assigned `fraudulent_intent` accurately describes the action demanded in the call-to-action sentence (e.g. `obtain_credentials_or_codes` when demanding passwords/PINs, `obtain_personal_or_financial_information` when demanding SSNs/debit card numbers, `induce_payment_or_transfer` when demanding wire/SwiftPay transfers).")
    lines.append("- **Contextual Plausibility:** However, in several cases (notably `SYN2-06111` where a car crash cousin asks for banking credentials to 'confirm ownership'), the intent is semantically matched to the sentence, but pragmatically ungrounded in the narrative.")
    lines.append("")
    lines.append("### 3.3 Summary Recommendation")
    lines.append("")
    lines.append("The Version 2 dataset represents a substantial leap forward over Version 1 by eliminating hard keyword leaks and non-deterministic label mappings. However, researchers must be aware of its structural regularities (rigid chat turn 2, modular sentence stacking, and occasional register clashes). These observations indicate that while Version 2 provides a solid synthetic testbed, model evaluation must ultimately be cross-validated on real-world financial communications to avoid overfitting to modular concatenation grammars.")

    OUTPUT_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Report generated successfully: {OUTPUT_REPORT_PATH} ({len(lines)} lines)")

if __name__ == "__main__":
    build_report()
