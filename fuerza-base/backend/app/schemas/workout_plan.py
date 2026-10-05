from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WorkoutPlanCreate(BaseModel):
    name: str
    description: Optional[str] = None
    trainer_id: int
    client_id: Optional[int] = None

class WorkoutPlanResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    trainer_id: int
    client_id: Optional[int] = None

    class Config:
        orm_mode = True
