from .api_http_error import APIHTTPError

class APIResponseError(APIHTTPError):
    """Bad HTTP response (4xx, 5xx)"""