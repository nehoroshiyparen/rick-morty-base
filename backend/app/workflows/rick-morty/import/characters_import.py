from ...base import BaseImportWorkflow
from app.infrastructure.integrations.rick_morty.types import ResourceType

class CharacterImportWorkflow(BaseImportWorkflow):
    def __init__(self, client, mapper, repository):
        super().__init__(
            client=client,
            mapper=mapper,
            repository=repository,
            resource=ResourceType.CHARACTER
        )