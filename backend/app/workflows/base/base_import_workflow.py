from .base_workflow import BaseWorkflow
from app.infrastructure.integrations.rick_morty.exceptions import APIClientError, APIResponseError


class BaseImportWorkflow(BaseWorkflow):
    def __init__(self, client, mapper, repository, resource, sync: BaseWorkflow = None):
        super().__init__()

        self.client = client
        self.mapper = mapper
        self.repository = repository
        self.resource = resource

        self.mapped = []
        self.sync = sync

    async def run(self, session, mode: str, start=None, end=None, page=None) -> None:
        self.session = session
        self.mapped = []

        if mode == "full":
            await self._run_full()

        elif mode == "range":
            await self._run_range(start, end)

        elif mode == "single":
            await self._run_single(page)
        
        if self.sync:
            await self._sync()

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

            results = data.get("results")

            if not results:
                self.logger.warning(f"Page {page} is empty")
                return "empty"

            mapped = self._map(results)
            await self._save(mapped)

            self.logger.warning(f"Page {page} processed successfully")

            self.mapped.extend(mapped)
            return "success"

        except APIResponseError as e:
            if e.status_code == 404:
                self.logger.warning(f"Page {page} does not exist. Stopping.")
                return "empty"

            self.logger.error(f"API error on page {page}: {e}")
            return "error"

        except APIClientError as e:
            self.logger.error(f"API error on page {page}: {e}")
            return "error"

        except Exception:
            self.logger.exception(f"Unexpected error on page {page}")
            raise

    async def _fetch(self, page: int): # raw data
        return await self.client.get(self.resource, page)

    def _map(self, results: list) -> list: # list of raw dicts -> list of mapped dicts
        return [self.mapper.transform_to_model(item) for item in results]

    async def _save(self, mapped: list) -> None:
        entities = [item["entity"] for item in mapped]
        repo = self.repository.bind(self.session)
        await repo.upsert_many(entities)

    async def _sync(self):
        await self.sync.run(self.session, self.mapped)