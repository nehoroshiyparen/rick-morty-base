from ...base import BaseWorkflowOrchestrator, BaseSyncWorkflow
from .sync_char_episode import CharacterEpisodeSyncWorkflow
from .sync_location_char import LocationCharacterSyncWorkflow
from app.modules.character import CharacterRepository
from app.modules.episode import EpisodeRepository
from app.modules.location import LocationRepository
from app.infrastructure.database.session import SessionLocal

orchestrator = BaseWorkflowOrchestrator(SessionLocal, {
    "char-episodes": CharacterEpisodeSyncWorkflow(
        CharacterRepository(),
        EpisodeRepository(),
    ),
    "char-locations": LocationCharacterSyncWorkflow(
        LocationRepository(),
        CharacterRepository()
    ),
})