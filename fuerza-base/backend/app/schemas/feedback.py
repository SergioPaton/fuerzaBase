from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class FeedbackCreate(BaseModel):
    rating: int
    comments: Optional[str] = None
    user_id: int
    plan_id: int

class FeedbackResponse(BaseModel):
    id: int
    rating: int
    comments: Optional[str] = None
    created_at: Optional[datetime] = None
    user_id: int
    plan_id: int

    model_config = ConfigDict(from_attributes=True)
