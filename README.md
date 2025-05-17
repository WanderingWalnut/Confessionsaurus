# UCalgaryConfessionsaurus 🚀

A full-stack web app to automate anonymous student confessions for the University of Calgary. Built with FastAPI, React, and AWS.

---

## 🛠️ Tech Stack

- **Frontend:** React (Vite), Tailwind/MUI
- **Backend:** FastAPI (REST API), SQLAlchemy
- **Database:** PostgreSQL (RDS)
- **Moderation:** better_profanity → Perspective API (planned)
- **Hosting:**
  - Frontend: S3 + CloudFront
  - Backend: Elastic Beanstalk (later Lambda)
- **DevOps:** AWS, GitHub Actions (future)

---

## 📂 Project Structure

```
/frontend # React app
└── src/
    ├── components/
    ├── pages/
    ├── services/api.js
    └── App.jsx, main.jsx

/backend # FastAPI app
├── app/
│   ├── main.py              # Entry point: creates FastAPI app
│   ├── api/                 # All route definitions
│   │   ├── __init__.py
│   │   ├── confess.py       # Routes like POST /confess, GET /confessions
│   │   └── admin.py         # Admin moderation routes (approve/reject)
│   ├── models/              # SQLAlchemy models (DB schema)
│   │   ├── __init__.py
│   │   └── confession.py
│   ├── schemas/             # Pydantic models (request/response shapes)
│   │   ├── __init__.py
│   │   └── confession.py
│   ├── services/            # Business logic (moderation, etc.)
│   │   ├── __init__.py
│   │   └── moderation.py
│   ├── db/                  # DB connection + session setup
│   │   ├── __init__.py
│   │   └── session.py
│   ├── config.py            # App settings, env vars
│   └── utils/               # Helper functions
│       └── profanity_filter.py
├── requirements.txt         # Python deps
├── .env                     # Environment variables (not committed)
└── alembic/                 # DB migrations (if using Alembic)
```

---

## ✅ Features

- Anonymous confession submission
- Auto-flagging based on profanity
- Admin dashboard for moderation
- Mobile responsive
- Deployed via AWS (S3 + Elastic Beanstalk)

---

## 🧪 Local Dev Setup

```bash
# Frontend
cd frontend
npm install
npm run dev

# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
