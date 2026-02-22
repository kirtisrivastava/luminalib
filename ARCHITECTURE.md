# LuminaLib Architecture

LuminaLib is designed as a **production-grade intelligent library system** built with FastAPI, PostgreSQL, Docker, and Generative AI. This document explains the architectural choices, async strategy, and recommendation model.

---

## 🏛️ Clean Architecture Principles
- **Dependency Injection (DI)**: All core services (storage, LLM, recommender) are injected via interfaces. This allows swapping implementations by changing configuration (`STORAGE_BACKEND`, `LLM_PROVIDER`).
- **Interface-Driven Development**: 
  - `StorageService` → Local disk or S3.
  - `LLMService` → Llama 3 (Ollama) or OpenAI.
  - `Recommender` → Content-based or collaborative filtering.
- **Extensibility**: Adding new providers requires only implementing the interface, not rewriting business logic.

---

## 📂 Layered Design
- **Routers (API Layer)**: FastAPI endpoints (`auth`, `books`, `reviews`, `intel`).
- **Schemas (DTO Layer)**: Pydantic models for request/response validation.
- **Models (Persistence Layer)**: SQLAlchemy ORM models for `User`, `Book`, `Review`.
- **Services (Business Logic Layer)**: Storage, LLM, recommender, security.
- **Utils (Infrastructure Layer)**: JWT, password hashing, async tasks.

---

## 🔑 User Preferences Schema
User preferences are modeled in two ways:
1. **Explicit Tags**: Users can select genres, topics, or categories.
2. **Implicit History**: Borrowed books and submitted reviews are tracked.

Schema example:
```sql
CREATE TABLE user_preferences (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    preference_type VARCHAR(50), -- 'tag' or 'history'
    preference_value TEXT
);
