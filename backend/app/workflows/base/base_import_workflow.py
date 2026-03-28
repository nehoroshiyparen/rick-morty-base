from abc import ABC, abstractmethod
from app.infrastructure.integrations.rick_morty.exceptions import APIClientError, APIHTTPError

class BaseImportWorkflow(ABC):
    def __init__(self, client, mapper, repository, resource):
        self.client = client
        self.mapper = mapper
        self.repository = repository
        self.resource = resource

    def run(self, mode: str, start=None, end=None, page=None) -> None:
        if mode == "full":
            return self._run_full()

        elif mode == "range":
            return self._run_range(start, end)

        elif mode == "single":
            return self._run_single(page)

    def _run_full(self):
        page = 1

        while True:
            result = self._process_page(page)

            if result == "empty":
                break

            if result == "error":
                # можно решить: continue или break
                continue

            page += 1

    def _run_range(self, start, end):
        for p in range(start, end + 1):
            self._process_page(p)

    def _run_single(self, page):
        self._process_page(page)

    def _process_page(self, page):
        try:
            data = self._fetch(page)

            results = data.get("results")

            # 👉 конец данных
            if not results:
                return "empty"

            mapped = self._map(data)
            self._save(mapped)

            return "success"

        except APIClientError as e:
            print(e)
            return "error"

    def _fetch(self, page: int): # raw data
        return self.client.get(self.resource, page)
    
    def _map(self, data): # raw data -> model
        return self.mapper.transform(data)
    
    def _save(self, data): 
        return self.repository.upsert_many(data)