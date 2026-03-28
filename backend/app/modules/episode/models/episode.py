from app.core.database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.modules.associations import character_episode


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, nullable=False)
    air_date = Column(DateTime(timezone=True))

    episode = Column(String, unique=True, nullable=False)
    url = Column(String, unique=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
    )

    characters = relationship(
        "Character",
        secondary=character_episode,
        back_populates="episodes"
    )