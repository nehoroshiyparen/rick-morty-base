from ...base import BaseWorkflowOrchestrator, BaseImportWorkflow
from .characters_import import CharacterImportWorkflow
from ..sync.sync_char_episode import CharacterEpisodeSyncWorkflow
from app.modules.character import CharacterRepository
from .episodes_import import EpisodeImportWorkflow
from app.modules.episode import EpisodeRepository
from .locations_import import LocationImportWorkflow
from ..sync.sync_location_char import LocationCharacterSyncWorkflow 
from app.modules.location import LocationRepository
from app.infrastructure.integrations.rick_morty.client import RickMortyClient
from app.infrastructure.integrations.rick_morty import CharacterMapper, EpisodeMapper, LocationMapper
from app.infrastructure.database.session import SessionLocal

_character_repo = CharacterRepository()
_location_repo = LocationRepository()
_episode_repo = EpisodeRepository()

orchestrator = BaseWorkflowOrchestrator(SessionLocal, {
    "location": LocationImportWorkflow(
        RickMortyClient(), LocationMapper(), _location_repo
    ),
    "characters": CharacterImportWorkflow(
        RickMortyClient(), CharacterMapper(), _character_repo, LocationCharacterSyncWorkflow(_location_repo, _character_repo)
    ),
    "episode": EpisodeImportWorkflow(
        RickMortyClient(), EpisodeMapper(), _episode_repo, CharacterEpisodeSyncWorkflow(_character_repo, _episode_repo)
    ),
})