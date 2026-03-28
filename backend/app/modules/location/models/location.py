from app.infrastructure.database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=True)
    dimension = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
    )

    characters_location = relationship(
        "Character",
        back_populates="location",
        foreign_keys="Character.location_id"
    )

    characters_origin = relationship(
        "Character",
        back_populates="origin",
        foreign_keys="Character.origin_id"
    )

    @property
    def residents(self):
        return self.characters_location