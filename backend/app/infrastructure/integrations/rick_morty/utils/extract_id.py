from typing import Any

def extract_id(url: str | Any) -> int:
    url_str = str(url)
    return int(url_str.rstrip("/").split("/")[-1])