"""
Caso de uso: Crear usuario.
Orquesta la creación de un usuario aplicando reglas de negocio.
No depende de SQLAlchemy, FastAPI ni ningún framework externo.
"""
import hashlib

from app.domain.entities.user import UserEntity
from app.use_cases.user.interfaces import AbstractUserRepository
from app.schemas.user import UserCreate


def _hash_password(password: str) -> str:
    """Función privada de hashing. Centralizada aquí para no duplicar lógica."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


class CreateUserUseCase:
    """
    Caso de uso: registrar un nuevo usuario.
    Recibe un puerto (repositorio abstracto) por inyección de dependencias.
    """

    def __init__(self, repository: AbstractUserRepository) -> None:
        self._repo = repository

    def execute(self, data: UserCreate) -> UserEntity:
        """
        Ejecuta el caso de uso.
        
        Args:
            data: DTO de entrada validado por Pydantic (UserCreate).

        Returns:
            UserEntity con el id asignado por la BD.

        Raises:
            ValueError: si el email ya está registrado.
        """
        if self._repo.find_by_email(data.email):
            raise ValueError(f"El email '{data.email}' ya está registrado.")

        user = UserEntity(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            hashed_password=_hash_password(data.password),
            role=data.role,
        )

        return self._repo.save(user)
