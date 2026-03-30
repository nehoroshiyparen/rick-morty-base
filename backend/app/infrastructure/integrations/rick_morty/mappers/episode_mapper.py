from ..schemas import EpisodeSchema
from app.modules.episode import Episode
from ..utils import extract_ids, parse_air_date

class EpisodeMapper():
    @staticmethod
    def transform_to_model(data: dict) -> dict:
        dto = EpisodeSchema.model_validate(data)
        return {
            "entity": Episode(
                external_id=dto.id,
                name=dto.name,
                air_date=parse_air_date(dto.air_date),
                episode=dto.episode,

                url=str(dto.url),
                created_at=dto.created,
            ),
            "relations": {
                "characters": extract_ids(dto.characters),
            },
        }