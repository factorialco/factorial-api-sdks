from enum import Enum


class AtsJobPostingStatus(str, Enum):
    ARCHIVED = "archived"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    PUBLISHED = "published"
    UNLISTED = "unlisted"

    def __str__(self) -> str:
        return str(self.value)
