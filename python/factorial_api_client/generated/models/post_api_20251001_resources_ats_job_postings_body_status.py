from enum import Enum


class PostApi20251001ResourcesAtsJobPostingsBodyStatus(str, Enum):
    ARCHIVED = "archived"
    CANCELLED = "cancelled"
    DRAFT = "draft"
    PUBLISHED = "published"
    UNLISTED = "unlisted"

    def __str__(self) -> str:
        return str(self.value)
