from ..schemas import LocationSchema
from app.modules.location import Location
from ..utils import extract_ids

class LocationMapper():
    def transform_to_dto(dto: LocationSchema) -> Location:
        return {
            "entity": Location(
                external_id=dto.id,
                name=dto.name,
                type=dto.type,
                dimension=dto.dimension,

                url=str(dto.url),
                created=dto.created,
            ),
            "relations": {
                "residents": extract_ids(dto.residents),
            },
        }