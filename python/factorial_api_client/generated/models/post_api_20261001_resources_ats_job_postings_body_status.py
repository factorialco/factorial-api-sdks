from enum import Enum


class PostApi20261001ResourcesAtsJobPostingsBodyStatus(str, Enum):
    ARCHIVED = "archived"
    CANCELLED = "cancelled"
    DELETED = "deleted"
    DRAFT = "draft"
    PUBLISHED = "published"
    UNLISTED = "unlisted"

    def __str__(self) -> str:
        return str(self.value)
