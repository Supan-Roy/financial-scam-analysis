"""Publication-quality figure generation module for dataset audits."""

import logging
from pathlib import Path
from typing import Any, Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

logger = logging.getLogger(__name__)


def setup_plotting_style() -> None:
    """Configure matplotlib and seaborn aesthetics for academic publication."""
    sns.set_theme(style="whitegrid", font_scale=1.1)
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["figure.dpi"] = 300
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["axes.titlesize"] = 13
    plt.rcParams["axes.labelsize"] = 11
    plt.rcParams["xtick.labelsize"] = 10
    plt.rcParams["ytick.labelsize"] = 10


def generate_all_audit_figures(
    dfs: Dict[str, pd.DataFrame],
    structural_infos: Dict[str, Any],
    compositions: Dict[str, Any],
    text_stats: Dict[str, Any],
    duplicates: Any,
    biases: Dict[str, Any],
    output_dir: Path,
) -> List[Path]:
    """Generate and save all required audit figures."""
    setup_plotting_style()
    output_dir.mkdir(parents=True, exist_ok=True)
    generated_figures: List[Path] = []

    palette = sns.color_palette("muted")

    # 1. Record counts by dataset
    fig, ax = plt.subplots(figsize=(8, 5))
    names = list(dfs.keys())
    counts = [len(dfs[name]) for name in names]
    pretty_names = [n.replace("_", " ").title() for n in names]
    bars = ax.bar(pretty_names, counts, color=palette[:len(names)], width=0.55, edgecolor="black", linewidth=0.8)
    ax.set_ylabel("Number of Records")
    ax.set_title("Total Record Counts Across Research Datasets", pad=15, fontweight="bold")
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:,}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontweight="bold",
            fontsize=10,
        )
    ax.set_ylim(0, max(counts) * 1.15)
    plt.tight_layout()
    p1 = output_dir / "record_counts_by_dataset.png"
    plt.savefig(p1)
    plt.close()
    generated_figures.append(p1)

    # 2. Label distribution
    fig, ax = plt.subplots(figsize=(8, 5))
    label_data = []
    for name, df in dfs.items():
        pretty_name = name.replace("_", " ").title()
        if "label" in df.columns:
            for lbl, count in df["label"].value_counts().items():
                lbl_str = "Scam (1)" if lbl == 1 else "Legitimate (0)"
                label_data.append({"Dataset": pretty_name, "Class Label": lbl_str, "Count": count})
    label_df = pd.DataFrame(label_data)
    sns.barplot(
        data=label_df,
        x="Dataset",
        y="Count",
        hue="Class Label",
        palette={"Scam (1)": "#d95f02", "Legitimate (0)": "#1b9e77"},
        edgecolor="black",
        linewidth=0.8,
        ax=ax,
    )
    ax.set_ylabel("Number of Records")
    ax.set_title("Class Label Distribution (Binary Scam vs Legitimate)", pad=15, fontweight="bold")
    for p in ax.patches:
        h = p.get_height()
        if h > 0:
            ax.annotate(f"{int(h):,}", (p.get_x() + p.get_width() / 2, h), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
    ax.set_ylim(0, max(label_df["Count"]) * 1.15)
    plt.tight_layout()
    p2 = output_dir / "label_distribution.png"
    plt.savefig(p2)
    plt.close()
    generated_figures.append(p2)

    # 3. Channel distribution
    fig, ax = plt.subplots(figsize=(10, 5))
    channel_data = []
    for name, df in dfs.items():
        pretty_name = name.replace("_", " ").title()
        col = "scam_channel" if "scam_channel" in df.columns else ("channel" if "channel" in df.columns else None)
        if col:
            for ch, count in df[col].value_counts().items():
                channel_data.append({"Dataset": pretty_name, "Channel": str(ch), "Count": count})
    ch_df = pd.DataFrame(channel_data)
    sns.barplot(data=ch_df, x="Channel", y="Count", hue="Dataset", palette="deep", edgecolor="black", linewidth=0.8, ax=ax)
    ax.set_ylabel("Number of Records")
    ax.set_title("Communication Channel Representation Across Datasets", pad=15, fontweight="bold")
    ax.set_yscale("log")
    ax.set_ylabel("Number of Records (Log Scale)")
    plt.tight_layout()
    p3 = output_dir / "channel_distribution.png"
    plt.savefig(p3)
    plt.close()
    generated_figures.append(p3)

    # 4. Message-length distributions (Word count KDE)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    for name, df in dfs.items():
        pretty_name = name.replace("_", " ").title()
        words = df["text"].astype(str).str.split().apply(len)
        sns.kdeplot(words, ax=ax1, label=pretty_name, log_scale=True, common_norm=False, linewidth=2)
        # Zoomed in linear plot up to 300 words
        sns.kdeplot(words[words <= 300], ax=ax2, label=pretty_name, common_norm=False, linewidth=2)

    ax1.set_title("Word Count Distribution (Log Scale)", fontweight="bold")
    ax1.set_xlabel("Words per Message (Log Scale)")
    ax1.set_ylabel("Density")
    ax1.legend()

    ax2.set_title("Word Count Distribution (<= 300 words)", fontweight="bold")
    ax2.set_xlabel("Words per Message")
    ax2.set_ylabel("Density")
    ax2.legend()

    plt.tight_layout()
    p4 = output_dir / "text_length_distributions.png"
    plt.savefig(p4)
    plt.close()
    generated_figures.append(p4)

    # 5. Word-count boxplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    plot_data = []
    for name, df in dfs.items():
        pretty_name = name.replace("_", " ").title()
        # Sample for plotting to keep file render crisp
        sample_df = df.sample(min(10000, len(df)), random_state=42)
        for _, row in sample_df.iterrows():
            w = len(str(row["text"]).split())
            ch = row.get("scam_channel", "unknown")
            plot_data.append({"Dataset": pretty_name, "Channel": str(ch), "Word Count": w})
    box_df = pd.DataFrame(plot_data)

    sns.boxplot(data=box_df, x="Dataset", y="Word Count", palette="Set2", showfliers=False, ax=ax1)
    ax1.set_title("Word Count by Dataset (Outliers Trimmed)", fontweight="bold")

    sns.boxplot(data=box_df, x="Channel", y="Word Count", hue="Dataset", palette="Set2", showfliers=False, ax=ax2)
    ax2.set_title("Word Count by Communication Channel", fontweight="bold")
    plt.tight_layout()
    p5 = output_dir / "word_count_boxplots.png"
    plt.savefig(p5)
    plt.close()
    generated_figures.append(p5)

    # 6. Scam subtype & category distributions
    syn_df = dfs.get("synthetic_financial_scams")
    legit_df = dfs.get("real_fin_legit")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    if syn_df is not None and "phishing_type" in syn_df.columns:
        sub_counts = syn_df["phishing_type"].value_counts().sort_values(ascending=True)
        sub_names = [s.replace("_", " ").title() for s in sub_counts.index]
        ax1.barh(sub_names, sub_counts.values, color="#4c72b0", edgecolor="black", linewidth=0.7)
        ax1.set_title("Synthetic Scam Subtype Frequencies (N=7,643)", fontweight="bold")
        ax1.set_xlabel("Records")
        for i, v in enumerate(sub_counts.values):
            ax1.text(v + 5, i, str(v), va="center", fontsize=9)

    if legit_df is not None and "legitimate_category" in legit_df.columns:
        legit_counts = legit_df["legitimate_category"].value_counts().sort_values(ascending=True)
        legit_names = [s.replace("_", " ").title() for s in legit_counts.index]
        ax2.barh(legit_names, legit_counts.values, color="#55a868", edgecolor="black", linewidth=0.7)
        ax2.set_title("Legitimate Category Frequencies (N=62,332)", fontweight="bold")
        ax2.set_xlabel("Records")
        for i, v in enumerate(legit_counts.values):
            ax2.text(v + 500, i, f"{v:,}", va="center", fontsize=9)

    plt.tight_layout()
    p6 = output_dir / "subtype_and_category_distributions.png"
    plt.savefig(p6)
    plt.close()
    generated_figures.append(p6)

    # 7. Synthetic tactics & intent
    if syn_df is not None and "fraudulent_intent" in syn_df.columns:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        intent_counts = syn_df["fraudulent_intent"].value_counts().sort_values(ascending=True)
        ax1.barh(intent_counts.index, intent_counts.values, color="#c44e52", edgecolor="black", linewidth=0.7)
        ax1.set_title("Synthetic Fraudulent Intent Distribution", fontweight="bold")
        ax1.set_xlabel("Records")
        for i, v in enumerate(intent_counts.values):
            ax1.text(v + 30, i, f"{v:,}", va="center", fontsize=9)

        tactics_dist = compositions.get("synthetic_financial_scams", {}).social_engineering_tactics_distribution
        if tactics_dist:
            tac_s = pd.Series(tactics_dist).sort_values(ascending=True)
            tac_names = [t.replace("_", " ").title() for t in tac_s.index]
            ax2.barh(tac_names, tac_s.values, color="#8172b3", edgecolor="black", linewidth=0.7)
            ax2.set_title("Social Engineering Tactic Annotations", fontweight="bold")
            ax2.set_xlabel("Frequency Count")
            for i, v in enumerate(tac_s.values):
                ax2.text(v + 15, i, f"{v:,}", va="center", fontsize=9)

        plt.tight_layout()
        p7 = output_dir / "synthetic_tactics_and_intent.png"
        plt.savefig(p7)
        plt.close()
        generated_figures.append(p7)

    # 8. Duplicate and overlap summary
    fig, ax = plt.subplots(figsize=(9, 5))
    dup_categories = ["Exact Duplicate Texts", "Normalized Duplicate Texts", "Near-Duplicate Pairs (LSH >= 0.85)", "Cross-Dataset Overlaps"]
    
    scam_near = duplicates.near_duplicates_within.get("real_fin_scam", 0)
    syn_near = duplicates.near_duplicates_within.get("synthetic_financial_scams", 0)
    legit_near = duplicates.near_duplicates_within.get("real_fin_legit", 0)
    
    dup_summary = pd.DataFrame({
        "Category": ["Exact (Within)", "Normalized (Within)", "Near-Duplicate Pairs (Within)", "Cross-Dataset Overlaps"],
        "Real Scam": [duplicates.exact_duplicates_within.get("real_fin_scam", 0), duplicates.normalized_duplicates_within.get("real_fin_scam", 0), scam_near, 0],
        "Synthetic Scam": [duplicates.exact_duplicates_within.get("synthetic_financial_scams", 0), duplicates.normalized_duplicates_within.get("synthetic_financial_scams", 0), syn_near, 0],
        "Real Legit": [duplicates.exact_duplicates_within.get("real_fin_legit", 0), duplicates.normalized_duplicates_within.get("real_fin_legit", 0), legit_near, 0],
    })
    
    dup_melt = dup_summary.melt(id_vars="Category", var_name="Dataset", value_name="Count")
    sns.barplot(data=dup_melt, x="Category", y="Count", hue="Dataset", palette="muted", edgecolor="black", linewidth=0.8, ax=ax)
    ax.set_title("Duplicate & Near-Duplicate Summary Across Corpora", pad=15, fontweight="bold")
    ax.set_ylabel("Count (Log Scale)")
    ax.set_yscale("symlog")
    plt.tight_layout()
    p8 = output_dir / "duplicate_and_overlap_summary.png"
    plt.savefig(p8)
    plt.close()
    generated_figures.append(p8)

    # 9. Research bias & shortcut risk comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    # Placeholder shortcut risk
    shortcut_risks = biases.get("spurious_shortcut_risks", {})
    if shortcut_risks:
        short_df = pd.DataFrame([
            {"Dataset": k.replace("_", " ").title(), "Angle Brackets (<...>) %": v["angle_bracket_rate_pct"], "Square Brackets ([...]) %": v["square_bracket_rate_pct"]}
            for k, v in shortcut_risks.items()
        ])
        short_melt = short_df.melt(id_vars="Dataset", var_name="Token Artifact", value_name="Occurrence Rate (%)")
        sns.barplot(data=short_melt, x="Dataset", y="Occurrence Rate (%)", hue="Token Artifact", palette={"Angle Brackets (<...>) %": "#e74c3c", "Square Brackets ([...]) %": "#3498db"}, edgecolor="black", linewidth=0.8, ax=ax1)
        ax1.set_title("Spurious Shortcut Risk: Placeholder Artifact Rates", fontweight="bold")
        ax1.set_ylim(0, 105)
        for p in ax1.patches:
            h = p.get_height()
            if h > 0:
                ax1.annotate(f"{h:.1f}%", (p.get_x() + p.get_width() / 2, h), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)

    # Channel length contrast
    ch_disp = biases.get("channel_length_disparity", [])
    if ch_disp:
        ch_disp_df = pd.DataFrame(ch_disp)
        ch_disp_df["Dataset"] = ch_disp_df["dataset"].str.replace("_", " ").str.title()
        sns.barplot(data=ch_disp_df, x="channel", y="median_words", hue="Dataset", palette="deep", edgecolor="black", linewidth=0.8, ax=ax2)
        ax2.set_title("Median Word Count by Communication Channel", fontweight="bold")
        ax2.set_xlabel("Channel")
        ax2.set_ylabel("Median Words")

    plt.tight_layout()
    p9 = output_dir / "research_bias_comparisons.png"
    plt.savefig(p9)
    plt.close()
    generated_figures.append(p9)

    logger.info(f"Generated {len(generated_figures)} audit figures in {output_dir}")
    return generated_figures

