from fastapi import FastAPI
import uvicorn

from routes.api import router as api_router
from tortoise.contrib.fastapi import register_tortoise

def get_application() -> FastAPI:
    application = FastAPI()
    
    application.include_router(api_router, prefix='/api')

    return application

app = get_application()

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models.domain.user']},
    generate_schemas=True,
    add_exception_handlers=True
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")