from fastapi import Request
from fastapi.responses import JSONResponse
from .types import ApiFail

async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ApiFail(
            error="Internal server error",
            status=500,
        ).model_dump(),
    )