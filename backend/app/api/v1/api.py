from fastapi import APIRouter
from app.api.v1.endpoints import examples, users, auth as auth_router

api_router = APIRouter()
api_router.include_router(examples.router, prefix="/examples", tags=["Examples"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])

api_router.include_router(auth_router.router, prefix="/auth", tags=["auth"])