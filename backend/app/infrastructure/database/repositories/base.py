from typing import Generic, TypeVar, Type, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy import select

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.session: AsyncSession | None = None
    
    def bind(self, session: AsyncSession):
        self.session = session
        return self
    
    async def upsert_many(self, entities: Sequence[ModelType]) -> None:
        if not entities:
            return
        
        values = [self._to_dict(e) for e in entities]

        stmt = insert(self.model).values(values)

        update_fields = {
            c.name: getattr(stmt.excluded, c.name)
            for c in self.model.__table__.columns
            if not c.primary_key and c.name != "created_at"
        }

        stmt = stmt.on_conflict_do_update(
            index_elements=["external_id"],
            set_=update_fields,
        )

        await self.session.execute(stmt)

    async def get_by_external_ids(self, external_ids: list[str]):
        stmt = select(ModelType).where(ModelType.external_id.in_(external_ids))
        result = await self.session.execute(stmt)
        return result.scalars().all()

    def _to_dict(self, entity):
        data = {}
        for c in self.model.__table__.columns:
            data[c.name] = getattr(entity, c.name, None)
        return data