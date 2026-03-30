from .api_client_error import APIClientError

class APIHTTPError(APIClientError):
    def __init__(self, status_code: int, message: str, url: str | None = None):
        self.status_code = status_code
        self.url = url

        full_message = f"[{status_code}] {message}"
        if url:
            full_message += f" | {url}"

        super().__init__(full_message)