"""
Repositorio SQLAlchemy: implementa AbstractUserRepository.
Adaptador de infraestructura — traduce entre ORM y entidades de dominio.
"""
from typing import Optional

from sqlalchemy.orm import Session

from app.domain.entities.user import UserEntity
from app.infrastructure.db.models.user import UserORM
from app.use_cases.user.interfaces import AbstractUserRepository


class SQLAlchemyUserRepository(AbstractUserRepository):
    """Implementación concreta del puerto AbstractUserRepository usando SQLAlchemy."""

    def __init__(self, db: Session) -> None:
        self._db = db

    # ------------------------------------------------------------------ #
    #  Métodos del puerto                                                  #
    # ------------------------------------------------------------------ #

    def find_by_email(self, email: str) -> Optional[UserEntity]:
        row = self._db.query(UserORM).filter(UserORM.email == email).first()
        return self._to_entity(row) if row else None

    def save(self, user: UserEntity) -> UserEntity:
        row = UserORM(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            hashed_password=user.hashed_password,
            role=user.role,
        )
        self._db.add(row)
        self._db.commit()
        self._db.refresh(row)
        return self._to_entity(row)

    # ------------------------------------------------------------------ #
    #  Helpers privados                                                    #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _to_entity(row: UserORM) -> UserEntity:
        """Convierte un registro ORM a entidad de dominio."""
        return UserEntity(
            id=row.id,
            first_name=row.first_name,
            last_name=row.last_name,
            email=row.email,
            hashed_password=row.hashed_password,
            role=row.role,
            created_at=row.created_at,
        )
