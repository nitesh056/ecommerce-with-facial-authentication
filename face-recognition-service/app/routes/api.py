from fastapi import APIRouter

from routes import video

router = APIRouter()

router.include_router(video.router, tags=["video"], prefix="/video-feed")
