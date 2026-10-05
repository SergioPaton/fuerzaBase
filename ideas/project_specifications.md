# Fuerza Base - Technical Specifications & Project Architecture

## 1. Project Overview & Core Idea
**Fuerza Base** is an all-in-one platform for the prescription, tracking, and auto-generation of strength training workouts. It bridges two main domains:
1. **B2B2C (Trainer & Clients)**: A centralized portal for trainers to manage their entire client roster, prescribe routines, calculate advanced strength metrics (RPE, RIR, 1RM, weekly volume, frequency), and maintain direct feedback channels.
2. **B2C (Independent Users / Beginners)**: A self-guided platform for individuals wanting to start strength training, featuring manual workout logging, progress tracking, and an intelligent auto-generation engine based on initial questionnaires.

---

## 2. Technology Stack
* **Frontend**: React 19, Vite, Tailwind CSS, TanStack Query (React Query). Responsive design (Mobile-First approach for athletes/clients, desktop-optimized views for trainers).
* **Backend**: Python (FastAPI), Uvicorn, Pydantic v2 (for strict runtime validation).
* **Database & ORM**: PostgreSQL, SQLAlchemy (Async mode using `asyncpg`), Alembic (for database migrations).
* **Version Control / Assistant**: Git + Aider workflow.