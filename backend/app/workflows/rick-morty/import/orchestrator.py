from ...base import ImportOrchestrator
from .characters_import import CharacterImportWorkflow
from .episodes_import import EpisodeImportWorkflow
from .locations_import import LocationImportWorkflow
from app.infrastructure.integrations.rick_morty.client import RickMortyClient
from app.infrastructure.integrations.rick_morty.mappers import CharacterMapper, EpisodeMapper, LocationMapper

orchestrator = ImportOrchestrator(
    workflows={
        "character": CharacterImportWorkflow(
            RickMortyClient(), CharacterMapper(), CharacterRepository()
        ),
        "episode": EpisodeImportWorkflow(
            RickMortyClient(), EpisodeMapper(), EpisodeRepository()
        ),
        "location": LocationImportWorkflow(
            RickMortyClient(), LocationMapper(), LocationRepository()
        ),
    }
)