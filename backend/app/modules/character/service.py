from .repository import CharacterRepository
from .schemas import CharacterUpdateSchema
from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from .models import Character

class CharacterService:
    def __init__(self, repo: CharacterRepository):
        self.repo = repo

    async def get_list(self, limit, offset):
        return await self.repo.get_list(limit, offset)

    async def get_by_id(self, character_id):
        character = await self.repo.get_by_id(
            character_id,
            options=[
                selectinload(Character.origin),
                selectinload(Character.location),
                selectinload(Character.episodes),
            ]
        )
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        return character

    async def update(self, character_id: int, data: CharacterUpdateSchema):
        character = await self.repo.get_by_id(character_id)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields provided for update")
        await self.repo.update(character_id, update_data)
        await self.repo.commit()
        return await self.repo.get_by_id(
            character_id,
            options=[
                selectinload(Character.origin),
                selectinload(Character.location),
                selectinload(Character.episodes),
            ]
        )

    async def delete(self, character_id):
        character = await self.repo.delete(character_id)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        await self.repo.commit()
        return {"status": "ok"}