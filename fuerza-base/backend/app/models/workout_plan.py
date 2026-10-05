from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app.models.__init__ import Base

class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    trainer_id = Column(Integer, ForeignKey("users.id"))
    client_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    trainer = relationship("User", foreign_keys=[trainer_id])
    client = relationship("User", foreign_keys=[client_id])
    sessions = relationship("WorkoutSession", back_populates="plan")
