"""
Modelo ORM SQLAlchemy: FeedbackORM.
Adaptador de infraestructura — mapea FeedbackEntity a la tabla 'feedback'.
"""
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.infrastructure.db.models import Base


class FeedbackORM(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_id = Column(Integer, ForeignKey("workout_plans.id"))

    user = relationship("UserORM")
    plan = relationship("WorkoutPlanORM")
