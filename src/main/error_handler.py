from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

def register_error_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc: HTTPException):
        return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

    @app.exception_handler(Exception)
    async def generic_exception_handler(request, exc: Exception):
        return JSONResponse(status_code=500, content={"error": "Internal server error"})