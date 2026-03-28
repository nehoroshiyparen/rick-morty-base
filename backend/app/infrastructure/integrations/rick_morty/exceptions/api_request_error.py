from .api_client_error import APIClientError

class APIRequestError(APIClientError):
    """Network / connection error"""