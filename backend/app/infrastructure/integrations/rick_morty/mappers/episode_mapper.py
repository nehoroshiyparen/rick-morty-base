from ..schemas import EpisodeSchema
from app.modules.episode.models import Episode
from ..utils import extract_ids

class EpisodeMapper():
    def transform_to_model(dto: EpisodeSchema) -> Episode:
        return {
            "episode": Episode(
                id=dto.id,
                name=dto.name,
                air_date=dto.air_date,
                episode=dto.episode,

                url=str(dto.url),
                created=dto.created,
            ),

            "character_ids": extract_ids(dto.characters),
        }