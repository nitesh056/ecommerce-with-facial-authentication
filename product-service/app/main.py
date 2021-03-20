from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise

from routes.api import router as api_router

def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(api_router, prefix='/api')

    return application

app = get_application()

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={
        'models': [
            'models.domain.brand',
            'models.domain.product',
            'models.domain.cart',
            'models.domain.cartItem',
            'models.domain.checkout'
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True, log_level="info")