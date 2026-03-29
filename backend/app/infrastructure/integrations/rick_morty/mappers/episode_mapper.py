from ..schemas import EpisodeSchema
from app.modules.episode import Episode
from ..utils import extract_ids

class EpisodeMapper():
    def transform_to_model(dto: EpisodeSchema) -> Episode:
        return {
            "entity": Episode(
                external_id=dto.id,
                name=dto.name,
                air_date=dto.air_date,
                episode=dto.episode,

                url=str(dto.url),
                created=dto.created,
            ),
            "relations": {
                "characters": extract_ids(dto.characters),
            },
        }