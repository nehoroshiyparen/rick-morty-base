from fastapi import FastAPI

def register_routers(app: FastAPI, prefix: str = "/api"):
    from app.modules.character.router import router as character_router
    from app.modules.episode.router import router as episode_router
    from app.modules.location.router import router as location_router

    app.include_router(character_router, prefix=f"{prefix}/characters", tags=["characters"])
    app.include_router(episode_router, prefix=f"{prefix}/episodes", tags=["episodes"])
    app.include_router(location_router, prefix=f"{prefix}/locations", tags=["locations"])