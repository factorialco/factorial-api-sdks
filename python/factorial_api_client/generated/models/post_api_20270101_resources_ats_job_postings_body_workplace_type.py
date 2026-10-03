from enum import Enum


class PostApi20270101ResourcesAtsJobPostingsBodyWorkplaceType(str, Enum):
    HYBRID = "hybrid"
    ONSITE = "onsite"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
