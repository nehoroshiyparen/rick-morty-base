from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .service import CharacterService
from .repository import CharacterRepository
from .schemas import CharacterUpdateSchema, CharacterResponseSchema
from app.infrastructure.database import get_session

router = APIRouter()

def get_service(session: AsyncSession = Depends(get_session)):
    repo = CharacterRepository().bind(session)
    return CharacterService(repo)

@router.get(
        '/',
        response_model=list[CharacterResponseSchema]
    )
async def get_characters(
    limit: int = 20,
    offset: int = 0,
    service: CharacterService = Depends(get_service)
):
    return await service.get_list(limit=limit, offset=offset)

@router.get(
        "/{character_id}",
        response_model=CharacterResponseSchema
    )
async def get_character(
    character_id: int,
    service: CharacterService = Depends(get_service)
):
    return await service.get_by_id(character_id)

@router.patch(
        "/{character_id}",
        response_model=CharacterResponseSchema
    )
async def update_character(
    character_id: int,
    data: CharacterUpdateSchema,
    service: CharacterService = Depends(get_service)
):
    return await service.update(character_id, data)

@router.delete(
        "/{character_id}",
        status_code=204
    )
async def delete_character(
    character_id: int,
    service: CharacterService = Depends(get_service)
):
    return await service.delete(character_id)