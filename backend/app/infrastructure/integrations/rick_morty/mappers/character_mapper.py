from app.modules.character import Character
from ..schemas import CharacterSchema
from ..utils import extract_id, extract_ids, normalize_character

class CharacterMapper():
    @staticmethod
    def transform_to_model(data: dict) -> dict:
        dto = CharacterSchema.model_validate(normalize_character(data))
        return {
            "entity": Character(
                external_id=dto.id,
                name=dto.name,
                status=dto.status,
                species=dto.species,
                type=dto.type,
                gender=dto.gender,
                origin_id=None,
                location_id=None,
                image=str(dto.image),
                url=str(dto.url),
                created_at=dto.created,
            ),
            "relations": {
                "origin": extract_id(dto.origin.url) if dto.origin.url else None,
                "location": extract_id(dto.location.url) if dto.location.url else None,
                "episodes": extract_ids(dto.episode),
            },
        }