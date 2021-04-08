from fastapi import APIRouter

from routes import notification

router = APIRouter()

router.include_router(notification.router, tags=["notification"], prefix="/notification")
