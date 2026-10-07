"""
UserService — LEGADO.
La lógica de negocio ha sido migrada al caso de uso:
    app.use_cases.user.create_user.CreateUserUseCase

Este servicio se mantiene temporalmente para referencia pero
el router v1 ya NO lo usa.
"""
from fastapi import HTTPException, status

from app.schemas.user import UserCreate, UserResponse
from app.infrastructure.db.models.user import UserORM
from app.core.database import SessionLocal
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


class UserService:
    """Clase legado — usar CreateUserUseCase en su lugar."""

    @staticmethod
    def create_user(user_data: UserCreate) -> UserResponse:
        db = SessionLocal()
        try:
            existing = db.query(UserORM).filter(UserORM.email == user_data.email).first()
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El usuario ya existe",
                )

            hashed_password = hash_password(user_data.password)

            user = UserORM(
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                email=user_data.email,
                hashed_password=hashed_password,
                role=user_data.role,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

            return UserResponse(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                role=user.role,
                created_at=user.created_at,
            )
        except HTTPException:
            db.rollback()
            raise
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exc),
            ) from exc
        finally:
            db.close()

