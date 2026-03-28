from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database.base_model import Base

character_episode = Table(
    "character_episode",
    Base.metadata,
    Column("character_id", Integer, ForeignKey("characters.id"), primary_key=True),
    Column("episode_id", Integer, ForeignKey("episodes.id"), primary_key=True),
)