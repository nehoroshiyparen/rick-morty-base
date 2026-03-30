from abc import abstractmethod
from .base_workflow import BaseWorkflow

class BaseSyncWorkflow(BaseWorkflow):
    def __init__(self):
        super().__init__()

    async def run(self, session, mapped_data: list) -> None:
        self.session = session
        self.logger.warning("Syncing...")
        prepared = await self._prepare_data(mapped_data)
        await self._save(prepared)
        self.logger.warning("Synced successfully!")

    @abstractmethod
    async def _prepare_data(self, mapped_data):
        pass

    @abstractmethod
    async def _save(self, data):
        pass