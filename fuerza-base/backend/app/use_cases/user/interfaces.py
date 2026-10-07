"""
Puerto (interfaz) del repositorio de usuarios.
Define el contrato que deben implementar los adaptadores de infraestructura.
Sigue el principio de Inversión de Dependencias (DIP) de Clean Architecture.
"""
from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.user import UserEntity


class AbstractUserRepository(ABC):
    """Puerto de salida: contrato para persistencia de usuarios."""

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[UserEntity]:
        """Busca un usuario por email. Retorna None si no existe."""
        ...

    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        """Persiste un usuario y retorna la entidad con id asignado."""
        ...
