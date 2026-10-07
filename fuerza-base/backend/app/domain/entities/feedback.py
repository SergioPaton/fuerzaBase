"""
Entidad de dominio: Feedback
Representa el feedback de un atleta sobre un plan de entrenamiento.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class FeedbackEntity:
    """Entidad pura de dominio. Sin SQLAlchemy ni Pydantic."""
    rating: int
    user_id: int
    plan_id: int
    id: Optional[int] = None
    comments: Optional[str] = None
    created_at: Optional[datetime] = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if not (1 <= self.rating <= 10):
            raise ValueError("El rating debe estar entre 1 y 10.")
