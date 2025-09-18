Great! Here’s a **professional `README.md` template** you can copy-paste into your project root folder (`C:\Users\prade\social-directory-recommender\README.md`).

````markdown
# 📌 Social Directory Recommender

An **AI-powered talent recommendation system** that helps social media creators find the best talent based on skills, experience, and creative fit.  
Built with **FastAPI (Backend)** and **React (Frontend)**, this project processes talent data, ranks candidates, and displays the **Top 10 recommendations per job posting**.

---

## 🚀 Overview

**Problem:**  
Creators receive thousands of applications, making it hard to manually shortlist candidates based on skills, personality, and budget.  

**Solution:**  
This system uses **data cleaning, embeddings, and scoring logic** to rank candidates and recommend the most suitable ones.  
Supports multiple job roles like **Video Editors, Producers, and COOs**, factoring in:

- Required skills (e.g., Editing, Storyboarding)
- Location preferences
- Budget fit (Monthly/Hourly rates)
- Past experience & platform relevance
- Personality & soft-skill keywords (via LLM inference)

---

## 🛠️ Tech Stack

| Layer       | Technology |
|------------|-----------|
| **Backend** | FastAPI, Pandas, Scikit-learn, NumPy |
| **Frontend** | React + Vite |
| **AI/ML** | OpenAI/Gemini Embeddings (optional), Cosine Similarity |
| **Database** | CSV-based data source (500 profiles) |
| **Deployment** | Uvicorn (local), GitHub for version control |

---

## 📂 Project Structure

```bash
social-directory-recommender/
│
├── backend/
│   ├── app/
│   │   ├── main.py             # FastAPI entry point
│   │   ├── recommender.py      # Core recommendation logic
│   │   └── utils/              # Helper scripts
│   ├── data/
│   │   ├── talent_samples.csv
│   │   └── talent_samples_cleaned.csv
│   └── scripts/
│       └── clean_data.py       # Data cleaning pipeline
│
├── frontend/
│   └── social-directory-frontend/
│       ├── src/
│       └── index.html
│
└── README.md
````

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pradeepbaghel02/social-directory-recommender.git
cd social-directory-recommender
```

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### 3️⃣ Setup Frontend

```bash
cd frontend/social-directory-frontend
npm install
npm run dev
```

Frontend available at: **[http://localhost:5173](http://localhost:5173)**

---

## 🎯 Features

✅ Data cleaning pipeline to standardize CSV
✅ Matching engine to rank candidates per job posting
✅ API endpoint `/recommend/{job_id}` returning Top 10 candidates
✅ Web UI to view results in a clean table format
✅ Extensible design (add new features like language, hobbies, platform expertise)

---

## 📊 Sample Output

| Rank | Candidate   | Match Score |
| ---- | ----------- | ----------- |
| 1    | John Doe    | 0.92        |
| 2    | Jane Smith  | 0.88        |
| 3    | Rahul Mehta | 0.85        |

---

## 🧠 Future Improvements

* Add embeddings from OpenAI or Hugging Face for semantic skill matching
* Include personality analysis from bio text
* Build chat-based UI to interact with candidates
* Deploy live on Render/Heroku for public demo

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and share.

---

## 🙌 Acknowledgements

* **DataSlush** – for providing the problem statement
* **OpenAI & Google Gemini** – for embeddings and LLM inference
* **FastAPI + React** – for enabling quick development of this POC

---

👨‍💻 **Author:** [Pradeep Baghel](https://github.com/pradeepbaghel02)
🔗 https://www.linkedin.com/in/pradeepbaghell/
💡 *Feedback and contributions are welcome!*



