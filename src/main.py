from fastapi import FastAPI
from .api.routes import router
from .utils.logger import setup_logging

app = FastAPI()

# Setup logging
setup_logging()

# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Advisor Bot API"}