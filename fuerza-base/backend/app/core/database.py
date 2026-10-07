"""
Sesión de base de datos — capa de infraestructura.
Proporciona el engine y la sesión SQLAlchemy al resto de la aplicación.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Compatibilidad SQLite (check_same_thread necesario para desarrollo local)
_connect_args = (
    {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
)

engine = create_engine(
    settings.DATABASE_URL,
    connect_args=_connect_args,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Generador de sesión — usar como dependencia FastAPI con Depends(get_db)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

