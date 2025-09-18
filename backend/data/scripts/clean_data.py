import argparse
import logging
from typing import List

import numpy as np
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def load_csv(path: str) -> pd.DataFrame:
    """Load CSV file from given path."""
    logger.info(f"Loading data from: {path}")
    return pd.read_csv(path)


def inspect_df(df: pd.DataFrame):
    """Log basic information about the DataFrame."""
    logger.info("First 5 rows:\n%s", df.head().to_string())
    logger.info("Shape: %s", df.shape)
    logger.info("Columns and dtypes:\n%s", df.dtypes)
    logger.info("Missing values per column:\n%s", df.isna().sum().sort_values(ascending=False))


def drop_duplicates(df: pd.DataFrame, subset: List[str] | None = None) -> pd.DataFrame:
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates(subset=subset).reset_index(drop=True)
    logger.info("Dropped duplicates: %d -> %d", before, len(df))
    return df


def strip_string_columns(df: pd.DataFrame, cols: List[str] | None = None) -> pd.DataFrame:
    """Remove extra spaces from string columns."""
    if cols is None:
        cols = df.select_dtypes(include="object").columns.tolist()
    for c in cols:
        df[c] = df[c].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return df


def convert_types(df: pd.DataFrame, numeric_cols: List[str] | None = None, date_cols: List[str] | None = None):
    """Convert columns to numeric or datetime where possible."""
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=["int64", "float64", "object"]).columns.tolist()
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if date_cols:
        for c in date_cols:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    return df


def handle_missing(df: pd.DataFrame, numeric_strategy: str = "median", cat_fill: str = "unknown") -> pd.DataFrame:
    """Fill missing values in numeric and categorical columns."""
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        if numeric_strategy == "median":
            df[num_cols] = df[num_cols].fillna(df[num_cols].median())
        elif numeric_strategy == "mean":
            df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
        elif numeric_strategy == "zero":
            df[num_cols] = df[num_cols].fillna(0)
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    for c in cat_cols:
        df[c] = df[c].fillna(cat_fill)
    return df


def cap_outliers_iqr(df: pd.DataFrame, cols: List[str] | None = None, multiplier: float = 1.5) -> pd.DataFrame:
    """Cap numeric outliers using IQR method."""
    if cols is None:
        cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for c in cols:
        if df[c].dropna().empty:
            continue
        Q1 = df[c].quantile(0.25)
        Q3 = df[c].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - multiplier * IQR
        upper = Q3 + multiplier * IQR
        df[c] = df[c].clip(lower=lower, upper=upper)
    return df


def make_json_safe(df: pd.DataFrame) -> pd.DataFrame:
    """Replace NaN with None to make it JSON serializable."""
    return df.where(pd.notnull(df), None)


def full_clean(
    df: pd.DataFrame,
    *,
    drop_dup_subset=None,
    numeric_strategy="median",
    cat_fill="unknown",
    date_cols=None,
):
    """Run full cleaning pipeline on DataFrame."""
    inspect_df(df)
    df = drop_duplicates(df, subset=drop_dup_subset)
    df = strip_string_columns(df)
    df = convert_types(df, date_cols=date_cols)
    df = handle_missing(df, numeric_strategy=numeric_strategy, cat_fill=cat_fill)
    df = cap_outliers_iqr(df)
