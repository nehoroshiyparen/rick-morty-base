from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .service import LocationService
from .repository import LocationRepository
from .schemas import LocationUpdateSchema, LocationResponseSchema
from app.infrastructure.database import get_session

router = APIRouter()

def get_service(session: AsyncSession = Depends(get_session)):
    repo = LocationRepository().bind(session)
    return LocationService(repo)

@router.get(
        '/',
        response_model=list[LocationResponseSchema],
    )
async def get_locations(
    limit: int = 20,
    offset: int = 0,
    service: LocationService = Depends(get_service)
):
    return await service.get_list(limit=limit, offset=offset)

@router.get(
        "/{location_id}",
        response_model=LocationResponseSchema,
    )
async def get_location(
    location_id: int,
    service: LocationService = Depends(get_service)
):
    return await service.get_by_id(location_id)

@router.patch(
        "/{location_id}",
        response_model=LocationResponseSchema,
    )
async def update_location(
    location_id: int,
    data: LocationUpdateSchema,
    service: LocationService = Depends(get_service)
):
    return await service.update(location_id, data)

@router.delete(
        "/{location_id}",
        status_code=204
    )
async def delete_location(
    location_id: int,
    service: LocationService = Depends(get_service)
):
    return await service.delete(location_id)