from .base_workflow import BaseWorkflow
from app.infrastructure.integrations.rick_morty.exceptions import APIClientError


class BaseImportWorkflow(BaseWorkflow):
    def __init__(self, client, mapper, repository, resource):
        super().__init__()

        self.client = client
        self.mapper = mapper
        self.repository = repository
        self.resource = resource

    async def run(self, session, mode: str, start=None, end=None, page=None) -> None:
        self.session = session

        if mode == "full":
            return await self._run_full()

        elif mode == "range":
            return await self._run_range(start, end)

        elif mode == "single":
            return await self._run_single(page)

    async def _run_full(self):
        page = 1

        while True:
            result = await self._process_page(page)

            if result == "empty":
                break

            if result == "error":
                continue

            page += 1

    async def _run_range(self, start, end):
        for p in range(start, end + 1):
            await self._process_page(p)

    async def _run_single(self, page):
        await self._process_page(page)

    async def _process_page(self, page):
        try:
            self.logger.warning(f"Processing page {page}")

            data = await self._fetch(page)

            results = data.get("entitiy")

            if not results:
                self.logger.warning(f"Page {page} is empty")
                return "empty"

            mapped = self._map(data)
            await self._save(mapped)

            self.logger.warning(f"Page {page} processed successfully")

            return "success"

        except APIClientError as e:
            self.logger.error(f"API error on page {page}: {e}")
            return "error"

        except Exception:
            self.logger.exception(f"Unexpected error on page {page}")
            raise

    async def _fetch(self, page: int): # raw data
        return await self.client.get(self.resource, page)
    
    def _map(self, data): # raw data -> model
        return self.mapper.transform_to_model(data)
    
    async def _save(self, data): 
        repo = self.repository.bind(self.session)
        await repo.upsert_many(data)