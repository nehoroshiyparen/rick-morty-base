from sqlalchemy import Table, Column, Integer, ForeignKey
from app.infrastructure.database.base_model import Base

CharacterEpisode = Table(
    "character_episode",
    Base.metadata,
    Column(
        "character_id",
        Integer,
        ForeignKey("characters.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "episode_id",
        Integer,
        ForeignKey("episodes.id", ondelete="CASCADE"),
        primary_key=True
    ),
)