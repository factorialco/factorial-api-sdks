from enum import Enum


class PutApi20270101ResourcesAtsJobPostingsIdBodyWorkplaceType(str, Enum):
    HYBRID = "hybrid"
    ONSITE = "onsite"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
