from fastapi import APIRouter, HTTPException, status
from modules.items.routes.create_user import users_db

router = APIRouter(tags=["Users"])

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return
    raise HTTPException(status_code=404, detail="User tidak ditemukan.")