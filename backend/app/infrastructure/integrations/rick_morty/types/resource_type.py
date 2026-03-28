from enum import Enum

class ResourceType(str, Enum):
    CHARACTER = "character"
    LOCATION = "location"
    EPISODE = "episode"