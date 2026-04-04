from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .service import CharacterService
from .repository import CharacterRepository
from .schemas import CharacterUpdateSchema, CharacterFullResponseSchema, CharacterPreviewResponseSchema
from app.infrastructure.database import get_session
from app.infrastructure.lib.handlers import ApiSuccess

router = APIRouter()

def get_service(session: AsyncSession = Depends(get_session)):
    repo = CharacterRepository().bind(session)
    return CharacterService(repo)

@router.get(
        '/',
        response_model=ApiSuccess[list[CharacterPreviewResponseSchema]]
    )
async def get_characters(
    limit: int = 20,
    offset: int = 0,
    service: CharacterService = Depends(get_service)
):
    characters = await service.get_list(limit=limit, offset=offset)
    return ApiSuccess(data=characters)

@router.get(
        "/{character_id}",
        response_model=ApiSuccess[CharacterFullResponseSchema]
    )
async def get_character(
    character_id: int,
    service: CharacterService = Depends(get_service)
):
    character = await service.get_by_id(character_id)
    return ApiSuccess(data=character)

@router.patch(
        "/{character_id}",
        response_model=ApiSuccess[CharacterFullResponseSchema]
    )
async def update_character(
    character_id: int,
    data: CharacterUpdateSchema,
    service: CharacterService = Depends(get_service)
):
    updated_data = await service.update(character_id, data)
    return ApiSuccess(data=updated_data)

@router.delete(
        "/{character_id}",
        status_code=204
    )
async def delete_character(
    character_id: int,
    service: CharacterService = Depends(get_service)
):
    return await service.delete(character_id)