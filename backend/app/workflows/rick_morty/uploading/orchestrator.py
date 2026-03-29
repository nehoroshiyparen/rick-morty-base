from ...base import BaseWorkflowOrchestrator, BaseImportWorkflow
from .characters_import import CharacterImportWorkflow
from app.modules.character import CharacterRepository
from .episodes_import import EpisodeImportWorkflow
from app.modules.episode import EpisodeRepository
from .locations_import import LocationImportWorkflow
from app.modules.location import LocationRepository
from app.infrastructure.integrations.rick_morty.client import RickMortyClient
from app.infrastructure.integrations.rick_morty import CharacterMapper, EpisodeMapper, LocationMapper
from app.infrastructure.database.session import SessionLocal

orchestrator = BaseWorkflowOrchestrator(SessionLocal, {
    "characters": CharacterImportWorkflow(
        RickMortyClient(), CharacterMapper(), CharacterRepository()
    ),
    "episode": EpisodeImportWorkflow(
        RickMortyClient(), EpisodeMapper(), EpisodeRepository()
    ),
    "location": LocationImportWorkflow(
        RickMortyClient(), LocationMapper(), LocationRepository()
    ),
})