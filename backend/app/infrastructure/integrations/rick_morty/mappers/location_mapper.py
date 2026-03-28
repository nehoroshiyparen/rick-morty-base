from ..schemas import LocationSchema
from app.modules.location.models import Location
from ..utils import extract_ids

class LocationMapper():
    def transform_to_dto(dto: LocationSchema) -> Location:
        return {
            "location": Location(
                id=dto.id,
                name=dto.name,
                type=dto.type,
                dimension=dto.dimension,

                url=str(dto.url),
                created=dto.created,
            ),

            "resident_ids": extract_ids(dto.residents),
        }