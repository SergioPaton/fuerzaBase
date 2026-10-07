# Arquitectura — Fuerza Base

## 1. Principio: Clean Architecture

El proyecto sigue **Clean Architecture** (Robert C. Martin).
Las capas internas no conocen las externas. Las dependencias apuntan hacia adentro.

```
[HTTP / FastAPI]  →  [Casos de Uso]  →  [Dominio]
                           ↑
                    [Infraestructura]
```

---

## 2. Estructura de directorios

```
fuerza-base/
├── backend/
│   ├── app/
│   │   ├── domain/                  # Capa 1 — Entidades puras (sin frameworks)
│   │   │   └── entities/
│   │   │       ├── user.py          # UserEntity (dataclass)
│   │   │       ├── workout_plan.py  # WorkoutPlanEntity
│   │   │       ├── feedback.py      # FeedbackEntity
│   │   │       └── regulation_log.py
│   │   │
│   │   ├── use_cases/               # Capa 2 — Casos de uso + Puertos
│   │   │   └── user/
│   │   │       ├── interfaces.py    # AbstractUserRepository (puerto)
│   │   │       └── create_user.py   # CreateUserUseCase
│   │   │
│   │   ├── infrastructure/          # Capa 3 — Adaptadores de BD
│   │   │   └── db/
│   │   │       ├── models/          # ORM SQLAlchemy (UserORM, etc.)
│   │   │       └── repositories/   # SQLAlchemyUserRepository
│   │   │
│   │   ├── api/                     # Capa 4 — Adaptadores HTTP (FastAPI)
│   │   │   ├── v1/router.py         # Delega a use_cases
│   │   │   └── v2/router.py
│   │   │
│   │   ├── schemas/                 # DTOs Pydantic v2 (entrada/salida HTTP)
│   │   │   ├── user.py
│   │   │   ├── workout_plan.py
│   │   │   ├── feedback.py
│   │   │   └── regulation_log.py
│   │   │
│   │   ├── services/                # Servicios de dominio (legado / en migración)
│   │   │   ├── trainer_service.py
│   │   │   ├── workout_prescription.py
│   │   │   ├── auto_generation_engine.py
│   │   │   └── adaptive_regulation_service.py
│   │   │
│   │   ├── core/                    # Config, sesión BD, seguridad
│   │   │   ├── config.py            # pydantic-settings (singleton settings)
│   │   │   ├── database.py          # engine + get_db()
│   │   │   └── security.py          # JWT
│   │   │
│   │   └── main.py                  # FastAPI app entry point
│   │
│   ├── tests/
│   │   └── test_users.py            # Tests con DB SQLite en memoria
│   └── requirements.txt
│
├── frontend/                        # React 18 + Vite + Tailwind CSS
│   └── src/
│       ├── components/              # UserForm, Dashboard, FeedbackForm, WorkoutList
│       ├── hooks/                   # TanStack Query: useUserMutation, useWorkoutQuery
│       └── pages/                   # TrainerDashboard, ClientDashboard, IndependentUserDashboard
│
├── docs/
├── ARCHITECTURE.md
├── CONVENTIONS.md
└── docker-compose.yml
```

---

## 3. Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend API | Python 3.11+, FastAPI, Uvicorn |
| Validación | Pydantic v2, pydantic-settings |
| ORM / BD | SQLAlchemy (sync), SQLite (dev), PostgreSQL (prod) |
| Migraciones | Alembic |
| Frontend | React 18, TanStack Query v5, Tailwind CSS 3, Vite |
| Seguridad | python-jose (JWT) |
| Tests | pytest, FastAPI TestClient |
| Observabilidad | Prometheus, Loki, Grafana (pendiente) |
| Mensajería | RabbitMQ / Redis (pendiente) |

---

## 4. Reglas de dependencia

| Capa | Puede importar de | NO puede importar de |
|------|-------------------|----------------------|
| `domain/` | — nadie | `use_cases`, `infrastructure`, `api`, `core` |
| `use_cases/` | `domain/`, `schemas/` | `infrastructure`, `api`, FastAPI, SQLAlchemy |
| `infrastructure/` | `domain/`, `use_cases/`, `core/` | `api/` |
| `api/` | todo lo anterior | `services/` directamente |
| `schemas/` | Pydantic únicamente | todo lo demás |

---

## 5. Módulos de negocio

- **CreateUserUseCase**: registro de usuarios con validación de unicidad de email.
- **TrainerService**: gestión de cartera de atletas (en migración a use_cases).
- **WorkoutPrescription**: creación y calendarización de planes (en migración).
- **AutoGenerationEngine**: generación automática desde cuestionario (pendiente).
- **AdaptiveRegulationService**: regulación dinámica de cargas con motor de reglas (pendiente).

---

## 6. Mejoras planificadas

1. Migrar `TrainerService`, `WorkoutPrescription` y `AutoGenerationEngine` a use_cases.
2. Feedback event-driven mediante RabbitMQ / Redis.
3. Versionado de planes con `WorkoutPlanVersion`.
4. Motor de reglas dentro de `AdaptiveRegulationService` (Pydantic avanzado).
5. Observabilidad completa (métricas, logs estructurados, trazas OpenTelemetry).
6. API versionada bajo `api/v2/` para evolución sin romper clientes.

