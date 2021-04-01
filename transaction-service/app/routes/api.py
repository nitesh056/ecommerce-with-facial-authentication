from fastapi import APIRouter

from routes import invoice

router = APIRouter()

router.include_router(invoice.router, tags=["invoice"], prefix="/invoice")
