# UCalgaryConfessionsaurus 🚀

A full-stack web app to automate anonymous student confessions for the University of Calgary. Built with Flask, React, and AWS.

---

## 🛠️ Tech Stack

- **Frontend:** React (Vite), Tailwind/MUI
- **Backend:** Flask (REST API), SQLAlchemy, Flask-Admin
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
    ├── services/api.ts
    └── App.tsx, main.tsx

/backend # Flask app
├── app.py
├── confessions/
│   ├── models.py
│   ├── routes.py
│   ├── moderation.py
├── admin/ # Flask-Admin setup
└── config.py

/.ebextensions # Elastic Beanstalk config
.env # Environment variables (not committed)
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
flask run
```
