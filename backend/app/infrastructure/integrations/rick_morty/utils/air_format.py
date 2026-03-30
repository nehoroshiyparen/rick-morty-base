from datetime import datetime

AIR_DATE_FORMAT = "%B %d, %Y"

def parse_air_date(value: str) -> datetime | None:
    if not value:
        return None

    try:
        return datetime.strptime(value, AIR_DATE_FORMAT)
    except ValueError:
        return None