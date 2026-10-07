"""
Entidad de dominio: WorkoutPlan
Representa un plan de entrenamiento sin dependencias de frameworks.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class WorkoutPlanEntity:
    """Entidad pura de dominio. Sin SQLAlchemy ni Pydantic."""
    name: str
    trainer_id: int
    id: Optional[int] = None
    description: Optional[str] = None
    client_id: Optional[int] = None
    created_at: Optional[datetime] = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("El nombre del plan no puede estar vacío.")
