from abc import abstractmethod
from .base_workflow import BaseWorkflow

class BaseSyncWorkflow(BaseWorkflow):
    def __init__(self):
        super().__init__()

    async def run(self, session, mapped_data):
        self.session = session

        prepared = await self._prepare_data(mapped_data)
        return await self._save(prepared)
    
    @abstractmethod
    async def _prepare_data(self, mapped_data):
        pass

    @abstractmethod
    async def _save(self, data):
        pass