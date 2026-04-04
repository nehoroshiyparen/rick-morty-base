from typing import Generic, TypeVar, Type, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy import select, delete, update

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

    async def get_by_external_ids(self, external_ids: list[int]):
        stmt = select(self.model).where(self.model.external_id.in_(external_ids))
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_by_id(self, id: int, options: list = None):
        stmt = select(self.model).where(self.model.id == id)

        if options:
            stmt = stmt.options(*options)

        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_list(self, limit: int = 20, offset: int = 0):
        stmt = select(self.model).limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete(self, id: int):
        stmt = (
            delete(self.model)
            .where(self.model.id == id)
        )

        result = await self.session.execute(stmt)

        if result.rowcount == 0:
            return False

        return True

    async def update(self, id: int, data: dict):
        filtered = {k: v for k, v in data.items() if v is not None}
        stmt = update(self.model).where(self.model.id == id).values(**filtered).returning(self.model)
        result = await self.session.execute(stmt)
        updated = result.scalar_one_or_none()
        return updated

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    def _to_dict(self, entity):
        data = {}
        for c in self.model.__table__.columns:
            data[c.name] = getattr(entity, c.name, None)
        return data