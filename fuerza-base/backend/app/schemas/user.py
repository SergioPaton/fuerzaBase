from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str  # trainer, client, independent

    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        if not re.search(r"[A-Z]", v):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula')
        if not re.search(r"[a-z]", v):
            raise ValueError('La contraseña debe contener al menos una letra minúscula')
        if not re.search(r"\d", v):
            raise ValueError('La contraseña debe contener al menos un número')
        return v

    @validator('role')
    def validate_role(cls, v):
        if v not in ['trainer', 'client', 'independent']:
            raise ValueError('El rol debe ser: trainer, client o independent')
        return v

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    role: str
    created_at: datetime

    class Config:
        orm_mode = True
