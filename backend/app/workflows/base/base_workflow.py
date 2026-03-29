from abc import ABC, abstractmethod
import logging

class BaseWorkflow(ABC):
    def __init__(self):
        self.session = None
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def run(self, session, mode="full", **kwargs):
        pass