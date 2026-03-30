from ...base import BaseImportWorkflow, BaseWorkflow
from app.infrastructure.integrations.rick_morty.types import ResourceType

class CharacterImportWorkflow(BaseImportWorkflow):
    def __init__(self, client, mapper, repository, sync: BaseWorkflow=None):
        super().__init__(
            client=client,
            mapper=mapper,
            repository=repository,
            resource=ResourceType.CHARACTER,
            sync=sync
        )