from enum import Enum


class GetApi20251001ResourcesAtsJobPostingsStatus(str, Enum):
    ARCHIVED = "archived"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    PUBLISHED = "published"
    UNLISTED = "unlisted"

    def __str__(self) -> str:
        return str(self.value)
