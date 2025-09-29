from fastapi import APIRouter, HTTPException, status
from modules.items.schema.schemas import UserUpdate, UserResponse
from modules.items.routes.create_user import users_db
from datetime import datetime

router = APIRouter(tags=["Users"])

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_data: UserUpdate):
    for user in users_db:
        if user["id"] == user_id:
            if updated_data.username:
                user["username"] = updated_data.username
            if updated_data.email:
                user["email"] = updated_data.email
            if updated_data.password:
                user["password"] = updated_data.password
            user["updated_at"] = datetime.now()
            return user
    raise HTTPException(status_code=404, detail="User tidak ditemukan.")