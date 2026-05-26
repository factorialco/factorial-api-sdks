from enum import Enum


class AtsJobPostingWorkplaceType(str, Enum):
    HYBRID = "hybrid"
    ONSITE = "onsite"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
