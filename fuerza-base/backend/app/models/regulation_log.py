from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.models import Base

class RegulationLog(Base):
    __tablename__ = "regulation_logs"

    id = Column(Integer, primary_key=True, index=True)
    adjustment_factor = Column(Float, nullable=False)
    reason = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    plan_id = Column(Integer, ForeignKey("workout_plans.id"))

    plan = relationship("WorkoutPlan")
