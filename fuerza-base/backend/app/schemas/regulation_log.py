from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RegulationLogCreate(BaseModel):
    adjustment_factor: float
    reason: Optional[str] = None
    plan_id: int

class RegulationLogResponse(BaseModel):
    id: int
    adjustment_factor: float
    reason: Optional[str] = None
    created_at: datetime
    plan_id: int

    class Config:
        orm_mode = True
