from fastapi import APIRouter, status, HTTPException
from datetime import datetime
from modules.items.schema.schemas import UserCreate, UserResponse
from utils import hash_password

router = APIRouter(tags=["Users"])

# Database sementara dalam memori
users_db = []
id_counter = 1

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    global id_counter

    # Enkripsi password sebelum disimpan
    hashed_pw = hash_password(user.password)

    new_user = {
        "id": id_counter,
        "username": user.username,
        "email": user.email,
        "password": hashed_pw,  # ✅ simpan hasil hash
        "role": user.role,
        "created_at": datetime.now()
    }

    # Simpan user ke "database" sementara
    users_db.append(new_user)
    id_counter += 1

    return new_user