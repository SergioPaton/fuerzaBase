"""
Router API v1 — adaptador HTTP.
Responsabilidad: parsear requests, delegar al caso de uso y serializar respuestas.
"""
from fastapi import APIRouter, Depends, HTTPException, status

from app.core.database import get_db
from app.infrastructure.db.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.schemas.user import UserCreate, UserResponse
from app.use_cases.user.create_user import CreateUserUseCase

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": "v1"}


@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user_data: UserCreate, db=Depends(get_db)):
    """
    Registra un nuevo usuario en el sistema.
    Roles válidos: trainer, client, independent.
    """
    try:
        repository = SQLAlchemyUserRepository(db)
        entity = CreateUserUseCase(repository).execute(user_data)
        return UserResponse(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email,
            role=entity.role,
            created_at=entity.created_at,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

