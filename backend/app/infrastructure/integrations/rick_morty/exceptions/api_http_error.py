from .api_client_error import APIClientError

class APIHTTPError(APIClientError):
    """HTTP-related errors"""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(message)