from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .service import LocationService
from .repository import LocationRepository
from .schemas import LocationUpdateSchema, LocationFullResponseSchema, LocationPreviewResponseSchema
from app.infrastructure.database import get_session
from app.infrastructure.lib.handlers import ApiSuccess

router = APIRouter()

def get_service(session: AsyncSession = Depends(get_session)):
    repo = LocationRepository().bind(session)
    return LocationService(repo)

@router.get(
        '/',
        response_model=ApiSuccess[list[LocationPreviewResponseSchema]],
    )
async def get_locations(
    limit: int = 20,
    offset: int = 0,
    service: LocationService = Depends(get_service)
):
    locations = await service.get_list(limit=limit, offset=offset)
    return ApiSuccess(data=locations)

@router.get(
        "/{location_id}",
        response_model=ApiSuccess[LocationFullResponseSchema],
    )
async def get_location(
    location_id: int,
    service: LocationService = Depends(get_service)
):
    location = await service.get_by_id(location_id)
    return ApiSuccess(data=location)

@router.patch(
        "/{location_id}",
        response_model=ApiSuccess[LocationFullResponseSchema],
    )
async def update_location(
    location_id: int,
    data: LocationUpdateSchema,
    service: LocationService = Depends(get_service)
):
    updated_data = await service.update(location_id, data)
    return ApiSuccess(data=updated_data)

@router.delete(
        "/{location_id}",
        status_code=204
    )
async def delete_location(
    location_id: int,
    service: LocationService = Depends(get_service)
):
    return await service.delete(location_id)