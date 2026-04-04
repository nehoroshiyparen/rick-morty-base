from .repository import EpisodeRepository
from .schemas import EpisodeUpdateSchema
from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from .models import Episode

class EpisodeService:
    def __init__(self, repo: EpisodeRepository):
        self.repo = repo

    async def get_list(self, limit, offset):
        return await self.repo.get_list(limit, offset)

    async def get_by_id(self, episode_id):
        episode = await self.repo.get_by_id(
            episode_id,
            options=[
                selectinload(Episode.characters)
            ]
        )
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")
        return episode

    async def update(self, episode_id: int, data: EpisodeUpdateSchema):
        episode = await self.repo.get_by_id(episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields provided for update")
        await self.repo.update(episode_id, update_data)
        await self.repo.commit()
        return await self.repo.get_by_id(
            episode_id,
            options=[
                selectinload(Episode.characters)
            ]
        )

    async def delete(self, episode_id):
        episode = await self.repo.delete(episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")
        await self.repo.commit()
        return {"status": "ok"}