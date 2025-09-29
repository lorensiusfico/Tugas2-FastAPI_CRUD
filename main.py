from fastapi import FastAPI
from modules.items.routes.create_user import router as create_router
from modules.items.routes.read_user import router as read_router
from modules.items.routes.update_user import router as update_router
from modules.items.routes.delete_user import router as delete_router

app = FastAPI()

# Daftarkan semua router
app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)
app.include_router(delete_router)