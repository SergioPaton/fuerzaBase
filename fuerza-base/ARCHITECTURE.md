# Arquitectura Propuesta — Fuerza Base

## 1. Estructura de directorios

fuerza-base/
├── backend/app/
│   ├── models/              # SQLAlchemy: User, WorkoutPlan, Feedback, RegulationLog
│   ├── schemas/             # Pydantic v2 (validación estricta)
│   ├── services/            # Lógica de negocio
│   │   ├── trainer_service.py
│   │   ├── workout_prescription.py
│   │   ├── auto_generation_engine.py
│   │   └── adaptive_regulation_service.py
│   ├── api/                 # FastAPI routers
│   │   ├── v1/
│   │   └── v2/              # Versionado de API
│   ├── core/                # Configuración, dependencias, seguridad
│   └── alembic/             # Migraciones de base de datos
├── frontend/src/            # React 19 + Vite + Tailwind CSS
│   ├── components/
│   ├── hooks/               # TanStack Query
│   └── pages/
├── docs/
└── docker-compose.yml

## 2. Stack tecnológico

- Backend: Python, FastAPI, Uvicorn, Pydantic v2
- ORM / DB: SQLAlchemy (modo async con asyncpg), PostgreSQL, Alembic
- Frontend: React 19, TanStack Query (React Query), Tailwind CSS
- Observabilidad: Prometheus, Loki, Grafana
- Eventos / Mensajería: RabbitMQ o Redis (feedback adaptativo)

## 3. Módulos centrales

- TrainerService: gestión de cartera de atletas, asignación de planes, notificaciones.
- WorkoutPrescription: creación, edición y calendarización de entrenamientos.
- AutoGenerationEngine: generación automática de rutinas iniciales desde cuestionario.
- AdaptiveRegulationService: regulación dinámica de cargas según feedback; incorpora motor de reglas (Drools o pydantic avanzado).

## 4. Mejoras propuestas (ya incorporadas en el diseño)

1. Feedback event-driven mediante RabbitMQ / Redis.
2. Versionado de planes con modelo WorkoutPlanVersion.
3. Motor de reglas dentro de AdaptiveRegulationService.
4. Observabilidad completa (métricas, logs, trazas).
5. API versionada bajo api/v2/ para evolución sin romper clientes.
