def extract_id(url: str) -> int:
    return int(url.rstrip("/").split("/")[-1])