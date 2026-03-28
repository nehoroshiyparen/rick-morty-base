import httpx
from .types import ResourceType
from .exceptions import APIResponseError, APIDecodeError, APIRequestError

class RickMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=10.0
        )

    async def get(self, resource: ResourceType, page: int):
        try:
            response = await self.client.get(
            f"/{resource.value}",
            params={"page": page}
        )
        except httpx.RequestError as e:
            raise APIRequestError(f"Network error: {str(e)}") from e
        
        if response.status_code >= 400:
            raise APIResponseError(
                f"HTTP {response.status_code}: {response.text}"
            )

        try:
            return response.json()
        except Exception as e:
            raise APIDecodeError("Invalid JSON response") from e