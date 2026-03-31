from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .service import EpisodeService
from .repository import EpisodeRepository
from .schemas import EpisodeUpdateSchema, EpisodeResponseSchema
from app.infrastructure.database import get_session

router = APIRouter()

def get_service(session: AsyncSession = Depends(get_session)):
    repo = EpisodeRepository().bind(session)
    return EpisodeService(repo)

@router.get(
        '/',
        response_model=list[EpisodeResponseSchema]
    )
async def get_episodes(
    limit: int = 20,
    offset: int = 0,
    service: EpisodeService = Depends(get_service)
):
    return await service.get_list(limit=limit, offset=offset)

@router.get(
        "/{episode_id}",
        response_model=EpisodeResponseSchema,
    )
async def get_episode(
    episode_id: int,
    service: EpisodeService = Depends(get_service)
):
    return await service.get_by_id(episode_id)

@router.patch(
        "/{episode_id}",
        response_model=EpisodeResponseSchema,
    )
async def update_episode(
    episode_id: int,
    data: EpisodeUpdateSchema,
    service: EpisodeService = Depends(get_service)
):
    return await service.update(episode_id, data)

@router.delete(
        "/{episode_id}",
        status_code=204
    )
async def delete_episode(
    episode_id: int,
    service: EpisodeService = Depends(get_service)
):
    return await service.delete(episode_id)