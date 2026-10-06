from pydantic import BaseModel, ConfigDict
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
    created_at: Optional[datetime] = None
    plan_id: int

    model_config = ConfigDict(from_attributes=True)
