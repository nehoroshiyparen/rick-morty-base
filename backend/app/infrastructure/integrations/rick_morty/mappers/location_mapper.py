from ..schemas import LocationSchema
from app.modules.location import Location
from ..utils import extract_ids

class LocationMapper():
    @staticmethod
    def transform_to_model(data: dict) -> dict:
        dto = LocationSchema.model_validate(data)
        return {
            "entity": Location(
                external_id=dto.id,
                name=dto.name,
                type=dto.type,
                dimension=dto.dimension,

                url=str(dto.url),
                created_at=dto.created,
            ),
            "relations": {
                "residents": extract_ids(dto.residents),
            },
        }