"""
Punto de entrada de la aplicación FastAPI — Fuerza Base.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_v1_router
from app.api.v2.router import router as api_v2_router
from app.core.database import engine
from app.infrastructure.db.models import Base  # importa todos los modelos ORM

# Crear tablas en BD (modo desarrollo; en producción usar Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fuerza Base",
    version="1.0.0",
    description="Plataforma de Prescripción y Regulación Adaptativa de Cargas",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Fuerza Base iniciado con éxito", "status": "online"}


app.include_router(api_v1_router, prefix="/api/v1")
app.include_router(api_v2_router, prefix="/api/v2")

