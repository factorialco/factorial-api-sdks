from enum import Enum


class PostApi20260401ResourcesProjectManagementProjectsChangeStatusBodyStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
