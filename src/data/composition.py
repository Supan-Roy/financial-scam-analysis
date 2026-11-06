"""Dataset composition and demographic auditing module."""

import json
import logging
from collections import Counter
from typing import Any, Dict

import pandas as pd

from src.data.schemas import CompositionAuditResult

logger = logging.getLogger(__name__)


def audit_dataset_composition(df: pd.DataFrame, dataset_name: str) -> CompositionAuditResult:
    """
    Audit categorical distributions and metadata composition across dataset fields.
    Gracefully skips unavailable fields.
    """
    logger.info(f"Auditing composition for {dataset_name} (N={len(df)})")
    total_records = len(df)

    # 1. Label distribution
    if "label" in df.columns:
        label_dist = {str(k): int(v) for k, v in df["label"].value_counts().items()}
    else:
        label_dist = {}

    # 2. Channel distribution
    if "scam_channel" in df.columns:
        channel_dist = {str(k): int(v) for k, v in df["scam_channel"].value_counts().items()}
    elif "channel" in df.columns:
        channel_dist = {str(k): int(v) for k, v in df["channel"].value_counts().items()}
    else:
        channel_dist = {}

    # 3. Source distribution
    if "source" in df.columns:
        source_dist = {str(k): int(v) for k, v in df["source"].value_counts().items()}
    else:
        source_dist = {}

    # 4. Synthetic distribution
    if "synthetic" in df.columns:
        syn_dist = {str(k): int(v) for k, v in df["synthetic"].value_counts().items()}
    else:
        syn_dist = {}

    # 5. Subtypes / Phishing types / Legitimate categories
    subtypes_dist: Dict[str, int] = {}
    if "phishing_type" in df.columns:
        subtypes_dist = {str(k): int(v) for k, v in df["phishing_type"].value_counts().items()}
    elif "legitimate_category" in df.columns:
        subtypes_dist = {str(k): int(v) for k, v in df["legitimate_category"].value_counts().items()}

    # 6. Communication types
    comm_types_dist: Dict[str, int] = {}
    if "communication_type" in df.columns:
        comm_types_dist = {str(k): int(v) for k, v in df["communication_type"].value_counts().items()}

    # 7. Fraudulent intent
    intent_dist: Dict[str, int] = {}
    if "fraudulent_intent" in df.columns:
        intent_dist = {str(k): int(v) for k, v in df["fraudulent_intent"].value_counts().items()}

    # 8. Social engineering tactics (parse JSON list if string)
    tactics_dist: Dict[str, int] = {}
    if "social_engineering_tactics" in df.columns:
        counter: Counter = Counter()
        for item in df["social_engineering_tactics"].dropna():
            if isinstance(item, str):
                try:
                    tactics = json.loads(item)
                    if isinstance(tactics, list):
                        counter.update(tactics)
                    else:
                        counter[str(tactics)] += 1
                except json.JSONDecodeError:
                    # Comma separated fallback
                    parts = [p.strip() for p in item.split(",") if p.strip()]
                    counter.update(parts)
            elif isinstance(item, list):
                counter.update(item)
        tactics_dist = dict(counter.most_common())

    return CompositionAuditResult(
        dataset_name=dataset_name,
        total_records=total_records,
        label_distribution=label_dist,
        channel_distribution=channel_dist,
        source_distribution=source_dist,
        synthetic_distribution=syn_dist,
        subtypes_distribution=subtypes_dist,
        fraudulent_intent_distribution=intent_dist,
        social_engineering_tactics_distribution=tactics_dist,
        communication_types_distribution=comm_types_dist,
    )

