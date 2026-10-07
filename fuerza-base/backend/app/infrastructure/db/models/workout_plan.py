"""
Modelo ORM SQLAlchemy: WorkoutPlanORM.
Adaptador de infraestructura — mapea WorkoutPlanEntity a la tabla 'workout_plans'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.infrastructure.db.models import Base


class WorkoutPlanORM(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    trainer_id = Column(Integer, ForeignKey("users.id"))
    client_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    trainer = relationship("UserORM", foreign_keys=[trainer_id])
    client = relationship("UserORM", foreign_keys=[client_id])
