import httpx
from .types import ResourceType
from .exceptions import APIResponseError, APIDecodeError, APIRequestError
import asyncio

class RickMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=10.0
        )

    async def get(self, resource: ResourceType, page: int, retries=3):
        last_exc = None

        for attempt in range(retries):
            try:
                response = await self.client.get(
                    f"/{resource.value}",
                    params={"page": page}
                )

                if response.status_code == 429:
                    await asyncio.sleep(2 ** attempt)
                    continue

                if response.status_code >= 500:
                    await asyncio.sleep(2 ** attempt)
                    continue

                if response.status_code >= 400:
                    raise APIResponseError(
                        status_code=response.status_code,
                        message=response.text,
                        url=str(response.url)
                    )

                return response.json()

            except httpx.RequestError as e:
                last_exc = e
                await asyncio.sleep(2 ** attempt)

        raise APIRequestError(f"Failed after retries: {last_exc}")