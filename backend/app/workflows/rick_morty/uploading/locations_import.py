from ...base import BaseImportWorkflow, BaseWorkflow
from app.infrastructure.integrations.rick_morty.types import ResourceType

class LocationImportWorkflow(BaseImportWorkflow):
    def __init__(self, client, mapper, repository, sync: BaseWorkflow=None):
        super().__init__(
            client=client,
            mapper=mapper,
            repository=repository,
            resource=ResourceType.LOCATION,
            sync=sync
        )