from fastapi import FastAPI
from app.data_loader import load_talent, load_jobs
from app.recommender import recommend

# Create FastAPI app
app = FastAPI(title="Social Directory Recommender API")

# Load data
talent_df = load_talent()
jobs = load_jobs()

@app.get("/")
def root():
    return {"message": "Welcome to the Social Directory Recommender API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/jobs")
def get_jobs():
    return jobs

@app.get("/recommend/{job_id}")
def recommend_candidates(job_id: int):
    # find job by ID
    job = next((j for j in jobs if j["id"] == job_id), None)
    if job is None:
        return {"error": "Job not found"}
    
    results = recommend(job, talent_df, top_k=10)
    return {"job": job, "recommendations": results}
