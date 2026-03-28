from api_client_error import APIClientError

class APIDecodeError(APIClientError):
    """Invalid JSON / schema mismatch"""