def normalize_character(data: dict) -> dict:
    data = data.copy()
    data["status"] = data["status"].capitalize()
    data["gender"] = data["gender"].capitalize()
    return data