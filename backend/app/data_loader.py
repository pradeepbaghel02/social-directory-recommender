import pandas as pd
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_talent():
    """Load talent profiles from CSV"""
    df = pd.read_csv(DATA_DIR / "talent_samples.csv")
    return df

def load_jobs():
    """Load job postings from JSON"""
    with open(DATA_DIR / "job_postings.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)
    return jobs
