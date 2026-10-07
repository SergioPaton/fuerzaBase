"""
Entidad de dominio: RegulationLog
Representa un ajuste de carga registrado por el AdaptiveRegulationService.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RegulationLogEntity:
    """Entidad pura de dominio. Sin SQLAlchemy ni Pydantic."""
    adjustment_factor: float
    plan_id: int
    id: Optional[int] = None
    reason: Optional[str] = None
    created_at: Optional[datetime] = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if self.adjustment_factor <= 0:
            raise ValueError("El factor de ajuste debe ser mayor que 0.")
