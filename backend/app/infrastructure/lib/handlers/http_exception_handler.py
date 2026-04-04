from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from .types import ApiFail

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiFail(
            error=exc.detail if isinstance(exc.detail, str) else str(exc.detail),
            status=exc.status_code,
        ).model_dump(),
    )