from app.modules.character.models import Character
from ..schemas import CharacterSchema
from ..utils import extract_id, extract_ids

class CharacterMapper():
    def transform_to_model(dto: CharacterSchema) -> Character:
        return {
            "character": Character(
                id=dto.id,
                name=dto.name,
                status=dto.status.value if hasattr(dto.status, "value") else dto.status,
                species=dto.species,
                type=dto.type,
                gender=dto.gender.value if hasattr(dto.gender, "value") else dto.gender,

                origin_id=extract_id(dto.origin.url) if dto.origin.url else None,
                location_id=extract_id(dto.location.url) if dto.location.url else None,

                image=str(dto.image),
                url=str(dto.url),
                created_at=dto.created,
            ),

            "origin_id": extract_id(dto.origin.url) if dto.origin.url else None,
            "location_id": extract_id(dto.location.url) if dto.location.url else None,

            "episode_ids": extract_ids(dto.episode),
        }