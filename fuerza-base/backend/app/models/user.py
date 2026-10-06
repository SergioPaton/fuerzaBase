from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.app.models import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # trainer, client, independent
    created_at = Column(DateTime, default=datetime.utcnow)
