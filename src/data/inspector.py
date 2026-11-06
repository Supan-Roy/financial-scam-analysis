"""Dataset structural inspection and schema auditing module."""

import hashlib
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from src.data.schemas import FileStructuralInfo

logger = logging.getLogger(__name__)


def compute_file_sha256(file_path: Path) -> str:
    """Compute cryptographic SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def detect_text_column(columns: List[str]) -> str:
    """Identify the primary message text column."""
    candidates = ["text", "message", "body", "email_body", "content"]
    for candidate in candidates:
        if candidate in columns:
            return candidate
    # Fallback to first object/string-like column
    return columns[0]


def detect_id_column(columns: List[str]) -> Optional[str]:
    """Identify record ID column if present."""
    candidates = ["id", "record_id", "msg_id", "sample_id"]
    for candidate in candidates:
        if candidate in columns:
            return candidate
    return None


def detect_label_column(columns: List[str]) -> Optional[str]:
    """Identify label/target column if present."""
    candidates = ["label", "target", "class", "is_scam", "is_phishing"]
    for candidate in candidates:
        if candidate in columns:
            return candidate
    return None


def inspect_file_structure(file_path: Path, dataset_name: str) -> Tuple[FileStructuralInfo, pd.DataFrame]:
    """
    Perform deep structural inspection of a raw CSV dataset without modifying it.
    
    Returns:
        Tuple of (FileStructuralInfo, loaded DataFrame)
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    logger.info(f"Inspecting file structure for {dataset_name} at {file_path}")
    
    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    sha256_hash = compute_file_sha256(file_path)

    # Read CSV
    # Using low_memory=False to ensure reliable dtype inference on large corpora
    df = pd.read_csv(file_path, low_memory=False)

    num_rows, num_cols = df.shape
    columns = df.columns.tolist()

    # Check for duplicate column names
    seen_cols = set()
    duplicate_columns = []
    for c in columns:
        if c in seen_cols:
            duplicate_columns.append(c)
        seen_cols.add(c)

    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}

    id_col = detect_id_column(columns)
    id_unique = False
    id_unique_count = 0
    if id_col and id_col in df.columns:
        id_unique_count = int(df[id_col].nunique())
        id_unique = bool(id_unique_count == num_rows)

    text_col = detect_text_column(columns)
    label_col = detect_label_column(columns)

    info = FileStructuralInfo(
        dataset_name=dataset_name,
        file_path=str(file_path),
        file_size_bytes=file_size_bytes,
        file_size_mb=round(file_size_mb, 2),
        sha256_hash=sha256_hash,
        num_rows=num_rows,
        num_cols=num_cols,
        columns=columns,
        dtypes=dtypes,
        duplicate_columns=duplicate_columns,
        id_column=id_col,
        id_unique=id_unique,
        id_unique_count=id_unique_count,
        text_column=text_col,
        label_column=label_col,
    )

    return info, df

