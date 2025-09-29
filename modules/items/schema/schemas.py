from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Literal, Optional
from datetime import datetime
import re


class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=6,
        max_length=15,
        pattern="^[a-z0-9]+$",
        description="Username huruf kecil & angka, panjang 6-15 karakter."
    )
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=20,
        description="Password 8-20 karakter, mengandung huruf besar, kecil, angka, dan !/@."
    )
    role: Literal["admin", "staff"]

    @field_validator("password")
    def validate_password_strength(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password harus mengandung huruf besar.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password harus mengandung huruf kecil.")
        if not re.search(r"\d", value):
            raise ValueError("Password harus mengandung angka.")
        if not re.search(r"[!@]", value):
            raise ValueError("Password harus mengandung karakter spesial (! atau @).")
        return value


class UserUpdate(BaseModel):
    username: Optional[str] = Field(
        None,
        min_length=6,
        max_length=15,
        pattern="^[a-z0-9]+$",
        description="Username huruf kecil & angka, panjang 6-15 karakter."
    )
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(
        None,
        min_length=8,
        max_length=20,
        description="Password 8-20 karakter, mengandung huruf besar, kecil, angka, dan !/@."
    )
    role: Optional[Literal["admin", "staff"]] = None

    @field_validator("password")
    def validate_password_strength(cls, value):
        if value is None:
            return value
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password harus mengandung huruf besar.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password harus mengandung huruf kecil.")
        if not re.search(r"\d", value):
            raise ValueError("Password harus mengandung angka.")
        if not re.search(r"[!@]", value):
            raise ValueError("Password harus mengandung karakter spesial (! atau @).")
        return value


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True