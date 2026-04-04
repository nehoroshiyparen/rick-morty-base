from fastapi import FastAPI
from .config import settings
from .routes import register_routers
from .handlers import register_handlers
from fastapi.middleware.cors import CORSMiddleware

class App:
    def __init__(self):
        self.fastapi_app = FastAPI(title=settings.APP_NAME)

    def get_session(self):
        async def _get_session():
            async with self.sessionmaker() as session:
                yield session
        return _get_session
    
    def setup(self):
        """Натсройка приложения: routes, middlewares etc."""
        register_routers(self.fastapi_app)
        register_handlers(self.fastapi_app)

        # CORS
        self.fastapi_app.add_middleware(
            CORSMiddleware,
            allow_origins=[settings.CLIENT_URL],
            allow_methods=["*"],
            allow_headers=["*"],
        )

    
    def start(self):
        import uvicorn
        uvicorn.run(self.fastapi_app, host=settings.APP_HOST, port=settings.APP_PORT)