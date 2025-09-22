# UCalgaryConfessionsaurus 🚀

A production-ready, full-stack web app that automates anonymous student confessions and Instagram posting for the University of Calgary.

---

## 🛠️ Tech Stack (Final)

- **Frontend**: React 19 (Vite), MUI (Material UI), custom CSS
- **Backend**: FastAPI, Mangum (AWS Lambda adapter)
- **Database**: PostgreSQL (Neon Serverless)
- **AI**: Google Gemini 2.0 Flash (caption generation)
- **Instagram**: `instagrapi` (session-based posting)
- **Infra/Hosting**:
  - Frontend: Amazon S3 + CloudFront
  - Backend: AWS Lambda + API Gateway
  - Secrets/Config: AWS Console env vars
- **Migrations**: Alembic

---

## 📂 Project Structure (Final)

```
/frontend
└── src/
    ├── components/
    ├── pages/
    ├── services/api.ts
    ├── App.tsx, main.tsx
    └── index.css (custom responsive styles)

/backend
├── app/
│   ├── main.py                  # FastAPI app + CORS + Mangum handler
│   ├── api/
│   │   ├── __init__.py          # Consolidated router
│   │   ├── confess.py           # POST /api/confess/submit
│   │   ├── instagram.py         # POST /api/instagram/post
│   │   └── admin.py             # Placeholder admin endpoints
│   ├── services/
│   │   ├── instagram_poster.py  # Session mgmt + post (single/carousel)
│   │   ├── gemini_client.py     # Gemini client (2.0 Flash)
│   │   └── moderation.py        # Profanity/moderation helpers
│   ├── db/
│   │   ├── session.py           # SQLAlchemy engine/session (Neon)
│   │   ├── crud_confession.py
│   │   └── reset_db.py
│   ├── models/
│   ├── schemas/
│   ├── tasks/                   # Backgroundable tasks
│   ├── jobs/run_jobs.py         # Posting job used by Lambda handler
│   └── utils/profanity_filter.py
├── lambda/
│   ├── handler_post.py          # Triggers posting job
│   ├── handler_moderate.py
│   └── handler_delete.py
└── alembic/                     # DB migrations
```

---

## ✅ Key Features

- **Anonymous confession submission** via REST API
- **Profanity/moderation pipeline** before publishing
- **Automated Instagram posting** (single + carousel)
- **AI-generated captions** via Gemini 2.0 Flash
- **Serverless backend** on AWS Lambda with API Gateway
- **Production frontend** on S3 + CloudFront

---

## 🔌 API Overview

- **Health**: `GET /health` → `{ "status": "ok" }`
- **Root**: `GET /` → Hello world
- **Confessions**: `POST /api/confess/submit`
  - Body: `{ "content": string }`
  - Returns created record with `id`, `published`, `created_at`
- **Instagram Post**: `POST /api/instagram/post`
  - Body: `{ "image_path": string, "caption": string }`
  - Requires valid Instagram session (managed server-side)
- **Admin**: `POST /api/admin/approve`, `POST /api/admin/reject` (placeholders)

---

## 🔐 Environment Variables

Backend expects environment variables (locally via `.env`, in prod via AWS):

- `NEON_TECH_DB_URL` – Postgres connection string (Neon)
- `GEMINI_API_KEY` – Google Generative AI API key
- `INSTAGRAM_USERNAME` – Instagram username (posting account)
- `INSTAGRAM_PASSWORD` – Instagram password (posting account)

Frontend can run without special env vars (points to backend URL configured via CORS).

---

## 🧪 Local Development

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

Notes:

- CORS is configured for `http://localhost:5173` and the production domains.
- Alembic migrations live under `backend/alembic`. Run them as needed.

---

## 🚀 Deployment (Final)

- **Frontend**: Build and upload `frontend/dist` to S3. Distribute via CloudFront.
- **Backend**: Pack backend (with dependencies) for AWS Lambda. Exposed through API Gateway. Uses `Mangum` to adapt FastAPI.
- **Jobs**: `backend/lambda/handler_post.py` invokes `job_post()` to run the posting workflow on a schedule (via EventBridge/Cron).
- **Secrets**: Configure all runtime secrets as Lambda environment variables.

---

## 📝 License

MIT
