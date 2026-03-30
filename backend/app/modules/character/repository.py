from app.infrastructure.database import BaseRepository
from .models import Character
from sqlalchemy import update, case
from sqlalchemy.dialects.sqlite import insert
from ..associations import CharacterEpisode

class CharacterRepository(BaseRepository):
    def __init__(self):
        super().__init__(Character)

    async def update_locations(self, updates):
        char_ids = [u[0] for u in updates]

        location_case = case(
            {char_id: loc_id for char_id, loc_id, _ in updates},
            value=Character.id
        )

        origin_case = case(
            {char_id: origin_id for char_id, _, origin_id in updates},
            value=Character.id
        )

        stmt = (
            update(Character)
            .where(Character.id.in_(char_ids))
            .values(
                location_id=location_case,
                origin_id=origin_case
            )
        )

        await self.session.execute(stmt)

    async def add_episode_links_batch(self, links):
        stmt = insert(CharacterEpisode).values([
            {"character_id": c, "episode_id": e}
            for c, e in links
        ])

        stmt = stmt.on_conflict_do_nothing(
            index_elements=["character_id", "episode_id"]
        )

        await self.session.execute(stmt)