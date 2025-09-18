import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")



def safe_get(row, col):
    return str(row[col]) if col in row and pd.notna(row[col]) else ""

def build_profile_text(row):
    return f"""
    Name: {safe_get(row, 'First Name')} {safe_get(row, 'Last Name')}
    Bio: {safe_get(row, 'Profile Description')}
    Gender: {safe_get(row, 'Gender')}
    Location: {safe_get(row, 'City')}, {safe_get(row, 'Country')}
    Job Types: {safe_get(row, 'Job Types')}
    Skills: {safe_get(row, 'Skills')}
    Software: {safe_get(row, 'Software')}
    Verticals: {safe_get(row, 'Content Verticals')}
    Creative Styles: {safe_get(row, 'Creative Styles')}
    Platforms: {safe_get(row, 'Platforms')}
    Past Creators: {safe_get(row, 'Past Creators')}
    Rates: {safe_get(row, 'Monthly Rate')} per month, {safe_get(row, 'Hourly Rate')} per hour
    Popularity: {safe_get(row, '# of Views by Creators')}
    """


def build_job_text(job):
    return f"""
    Role: {job['role']}
    Required Skills: {", ".join(job['required_skills'])}
    Location Preference: {job['location']}
    Verticals: {", ".join(job['verticals'])}
    Budget: {job['budget']}
    Description: {job['description']}
    """

def embed_texts(texts):
    return model.encode(texts, convert_to_numpy=True, show_progress_bar=False)

def recommend(job, talent_df, top_k=10):
    # Build embeddings
    job_text = build_job_text(job)
    job_emb = embed_texts([job_text])[0]

    cand_texts = [build_profile_text(row) for _, row in talent_df.iterrows()]
    cand_embs = embed_texts(cand_texts)

    sims = cosine_similarity(np.array([job_emb]), cand_embs)[0]
    top_idx = sims.argsort()[::-1][:top_k]

    results = []
    for idx in top_idx:
        results.append({
            "candidate": talent_df.iloc[idx].to_dict(),
            "score": float(sims[idx])
        })
    return results
