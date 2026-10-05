from pydantic import BaseModel
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
    created_at: datetime
    user_id: int
    plan_id: int

    class Config:
        orm_mode = True
