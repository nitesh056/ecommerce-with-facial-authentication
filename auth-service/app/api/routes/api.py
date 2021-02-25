from fastapi import APIRouter

from api.routes import auth

router = APIRouter()

router.include_router(auth.router, tags=["auth"], prefix="/u")