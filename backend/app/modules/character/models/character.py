from app.core.database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum
import enum

from app.modules.associations import character_episode


class Status(str, enum.Enum):
    ALIVE = "alive"
    DEAD = "dead"
    UNKNOWN = "unknown"


class Gender(str, enum.Enum):
    FEMALE = "female"
    MALE = "male"
    GENDERLESS = "genderless"
    UNKNOWN = "unknown"


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, nullable=False)

    status = Column(
        SAEnum(Status, name="status_enum", native_enum=False),
        nullable=False,
        default=Status.UNKNOWN
    )

    species = Column(String, nullable=False)
    type = Column(String, nullable=True)

    gender = Column(
        SAEnum(Gender, name="gender_enum", native_enum=False),
        nullable=False,
        default=Gender.UNKNOWN
    )

    origin_id = Column(
        Integer,
        ForeignKey("locations.id", ondelete="SET NULL"),
        nullable=True
    )

    location_id = Column(
        Integer,
        ForeignKey("locations.id", ondelete="SET NULL"),
        nullable=True
    )

    image = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
    )

    origin = relationship(
        "Location",
        back_populates="characters_origin",
        foreign_keys=[origin_id]
    )

    location = relationship(
        "Location",
        back_populates="characters_location",
        foreign_keys=[location_id]
    )

    episodes = relationship(
        "Episode",
        secondary=character_episode,
        back_populates="characters"
    )