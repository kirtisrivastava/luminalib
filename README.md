# luminalib

# LuminaLib 📚🤖
A next-generation intelligent library system built with **FastAPI**, **PostgreSQL**, **Docker**, and **Generative AI (Llama 3)**.

LuminaLib is not just a metadata CRUD app — it ingests actual book files, generates summaries using LLMs, analyzes user reviews, and provides personalized recommendations.

---

## 🚀 Features
- **Authentication & User Management**
  - JWT-based stateless authentication
  - Signup, Login, Profile, Logout
- **Book Ingestion & Management**
  - Upload actual book files (PDF/Text)
  - CRUD operations for metadata + content
  - Borrow/Return mechanics
- **Intelligence Layer**
  - Async book summarization via LLM
  - Review sentiment aggregation
  - ML-based recommendation engine
- **Clean Architecture**
  - Dependency Injection
  - Interface-driven design (swap storage/LLM easily)
- **Dockerized Deployment**
  - One-command startup with `docker compose up --build`

---

## 📂 Project Structure


luminalib/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── utils/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── ARCHITECTURE.md

