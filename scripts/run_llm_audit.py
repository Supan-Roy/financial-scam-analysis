import pandas as pd
import json
import re
from collections import Counter

proc = pd.read_csv("data/processed/llm_authored_financial_scams_processed.csv")
raw = pd.read_csv("data/raw/llm_authored_financial_scams.csv")

print("--- DATASET DIMENSIONS ---")
print(f"Raw shape:       {raw.shape}")
print(f"Processed shape: {proc.shape}")

print("\n--- MISSINGNESS REPORT ---")
audit_cols = [
    "record_id", "original_text", "normalized_text", "scam_subtype", "fraudulent_intent", 
    "social_engineering_tactics", "writing_style", "channel", "split_partition",
    "primary_intent_evidence", "tactics_evidence",
    "optional_scenario_description", "urgency_rating", "secondary_channel_source", "email_subject"
]
for col in audit_cols:
    m = proc[col].isna().sum()
    pct = (m / len(proc)) * 100
    print(f"{col:32s}: {m:4d} missing ({pct:5.2f}%)")

print("\n--- TACTICS FREQUENCY ---")
all_tactics = []
tactic_cardinality = Counter()
for t_str in proc["social_engineering_tactics"]:
    t_list = json.loads(t_str)
    tactic_cardinality[len(t_list)] += 1
    all_tactics.extend(t_list)
t_counts = Counter(all_tactics)
for tac, cnt in t_counts.most_common():
    pct = (cnt / len(proc)) * 100
    print(f"{tac:30s}: {cnt:4d} occurrences ({pct:5.2f}% of messages)")

print("\n--- TACTICS CARDINALITY PER RECORD ---")
for num_t, cnt in sorted(tactic_cardinality.items()):
    pct = (cnt / len(proc)) * 100
    print(f"{num_t} tactics: {cnt:4d} records ({pct:5.2f}%)")

print("\n--- DUPLICATE CLUSTERS ---")
clustered = proc[proc["duplicate_cluster_id"].notna() & (proc["duplicate_cluster_id"] != "")]
clustered_cnt = len(clustered)
n_clusters = clustered["duplicate_cluster_id"].nunique()
print(f"Clustered records: {clustered_cnt} ({clustered_cnt/len(proc)*100:.2f}%), Distinct clusters: {n_clusters}")

print("\n--- TEXT LENGTH PROFILE ---")
print(f"Mean original words:   {proc['word_count_original'].mean():.1f}, Median: {proc['word_count_original'].median():.0f}, Min: {proc['word_count_original'].min()}, Max: {proc['word_count_original'].max()}")
print(f"Mean normalized words: {proc['word_count_normalized'].mean():.1f}, Median: {proc['word_count_normalized'].median():.0f}, Min: {proc['word_count_normalized'].min()}, Max: {proc['word_count_normalized'].max()}")
print(f"Mean original chars:   {proc['char_count_original'].mean():.1f}, Median: {proc['char_count_original'].median():.0f}")

print("\n--- WRITING STYLE PROFILES ---")
for ws in proc["writing_style"].unique():
    sub = proc[proc["writing_style"] == ws]
    print(f"{ws:25s}: count={len(sub)}, mean_words={sub['word_count_original'].mean():.1f}, min_words={sub['word_count_original'].min()}, max_words={sub['word_count_original'].max()}")

print("\n--- CHANNEL PROFILES ---")
for ch in ["email", "sms", "chat", "notification"]:
    sub = proc[proc["channel"] == ch]
    print(f"{ch:15s}: count={len(sub)} ({len(sub)/len(proc)*100:.1f}%), mean_words={sub['word_count_original'].mean():.1f}, min_words={sub['word_count_original'].min()}, max_words={sub['word_count_original'].max()}")

print("\n--- SUBTYPE x INTENT MATRIX ---")
ct = pd.crosstab(proc["scam_subtype"], proc["fraudulent_intent"])
print(ct)

# Check for real entities or unsafe domains
forbidden_domains = [".com", ".org", ".net", ".io", ".co"]
unsafe_urls = []
for idx, txt in enumerate(proc["original_text"]):
    urls = re.findall(r"https?://[^\s/]+", txt)
    for u in urls:
        if not (u.endswith(".example") or ".example" in u or "[URL]" in u):
            unsafe_urls.append((idx, u))
print(f"\nUnsafe non-.example URLs found: {len(unsafe_urls)}")
if unsafe_urls:
    print("Samples:", unsafe_urls[:5])
