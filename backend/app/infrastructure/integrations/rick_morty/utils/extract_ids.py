from .extract_id import extract_id

def extract_ids(urls: list[str]) -> list[int]:
    return [extract_id(url) for url in urls]