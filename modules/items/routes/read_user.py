from fastapi import APIRouter, HTTPException
from typing import List
from modules.items.schema.schemas import UserResponse
from modules.items.routes.create_user import users_db  # ambil data dari create_user.py

router = APIRouter(tags=["Users"])

# ✅ Ambil semua user
@router.get("/users", response_model=List[UserResponse])
def get_all_users():
    return users_db

# ✅ Ambil user berdasarkan ID
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User tidak ditemukan.")
