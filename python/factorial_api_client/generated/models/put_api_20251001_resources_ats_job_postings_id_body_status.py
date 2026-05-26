from enum import Enum


class PutApi20251001ResourcesAtsJobPostingsIdBodyStatus(str, Enum):
    ARCHIVED = "archived"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    PUBLISHED = "published"
    UNLISTED = "unlisted"

    def __str__(self) -> str:
        return str(self.value)
