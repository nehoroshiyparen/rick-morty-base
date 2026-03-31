from .repository import LocationRepository
from .schemas import LocationUpdateSchema
from fastapi import HTTPException

class LocationService:
    def __init__(self, repo: LocationRepository):
        self.repo = repo

    async def get_list(self, limit, offset):
        return await self.repo.get_list(limit, offset)

    async def get_by_id(self, location_id):
        location = await self.repo.get_by_id(location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        return location

    async def update(self, location_id: int, data: LocationUpdateSchema):
        location = await self.repo.get_by_id(location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields provided for update")
        result = await self.repo.update(location_id, update_data)
        await self.repo.commit()
        return result

    async def delete(self, location_id):
        location = await self.repo.delete(location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        await self.repo.commit()
        return {"status": "ok"}