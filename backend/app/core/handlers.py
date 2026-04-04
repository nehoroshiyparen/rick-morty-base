from fastapi import FastAPI, HTTPException

def register_handlers(app: FastAPI):
    from app.infrastructure.lib.handlers import (
        http_exception_handler,
        unhandled_exception_handler
    )

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)