"""
Entidad de dominio: User
Representa un usuario del sistema sin dependencias de frameworks.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class UserEntity:
    """Entidad pura de dominio. Sin SQLAlchemy ni Pydantic."""
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    role: str  # 'trainer' | 'client' | 'independent'
    id: Optional[int] = None
    created_at: Optional[datetime] = field(default_factory=datetime.utcnow)

    VALID_ROLES = frozenset({"trainer", "client", "independent"})

    def __post_init__(self):
        if self.role not in self.VALID_ROLES:
            raise ValueError(f"Rol inválido: '{self.role}'. Debe ser: {self.VALID_ROLES}")
        if len(self.first_name) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        if len(self.last_name) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
