from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .service import EpisodeService
from .repository import EpisodeRepository
from .schemas import EpisodeUpdateSchema, EpisodeFullResponseSchema, EpisodePreviewResponseSchema
from app.infrastructure.database import get_session
from app.infrastructure.lib.handlers import ApiSuccess

router = APIRouter()

def get_service(session: AsyncSession = Depends(get_session)):
    repo = EpisodeRepository().bind(session)
    return EpisodeService(repo)

@router.get(
        '/',
        response_model=ApiSuccess[list[EpisodePreviewResponseSchema]]
    )
async def get_episodes(
    limit: int = 20,
    offset: int = 0,
    service: EpisodeService = Depends(get_service)
):
    episodes = await service.get_list(limit=limit, offset=offset)
    return ApiSuccess(data=episodes)

@router.get(
        "/{episode_id}",
        response_model=ApiSuccess[EpisodeFullResponseSchema],
    )
async def get_episode(
    episode_id: int,
    service: EpisodeService = Depends(get_service)
):
    episode = await service.get_by_id(episode_id)
    return ApiSuccess(data=episode)

@router.patch(
        "/{episode_id}",
        response_model=ApiSuccess[EpisodeFullResponseSchema],
    )
async def update_episode(
    episode_id: int,
    data: EpisodeUpdateSchema,
    service: EpisodeService = Depends(get_service)
):
    updated_data = await service.update(episode_id, data)
    return ApiSuccess(data=updated_data)

@router.delete(
        "/{episode_id}",
        status_code=204
    )
async def delete_episode(
    episode_id: int,
    service: EpisodeService = Depends(get_service)
):
    return await service.delete(episode_id)