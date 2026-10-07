from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from typing import Optional
import re
from datetime import datetime


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str  # trainer | client | independent

    @field_validator("first_name")
    @classmethod
    def min_first_name_length(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        return v

    @field_validator("last_name")
    @classmethod
    def min_last_name_length(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")
        return v

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", v):
            raise ValueError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"\d", v):
            raise ValueError("La contraseña debe contener al menos un número.")
        return v

    @field_validator("role")
    @classmethod
    def validate_role(cls, v: str) -> str:
        if v not in ("trainer", "client", "independent"):
            raise ValueError("El rol debe ser: trainer, client o independent.")
        return v


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    role: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

