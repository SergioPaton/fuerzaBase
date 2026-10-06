from pydantic import BaseModel, ConfigDict
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
    created_at: Optional[datetime] = None
    trainer_id: int
    client_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
