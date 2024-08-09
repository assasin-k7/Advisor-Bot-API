from fastapi import FastAPI
from .routes import router
from .error_handler import register_error_handlers

def create_app():
    app = FastAPI()

    app.include_router(router)

    register_error_handlers(app)

    return app