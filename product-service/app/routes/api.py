from fastapi import APIRouter

from routes import product
from routes import brand
from routes import cart

router = APIRouter()

router.include_router(product.router, tags=["product"], prefix="/product")
router.include_router(brand.router, tags=["brand"], prefix="/brand")
router.include_router(cart.router, tags=["cart"], prefix="/cart")
