from enum import Enum


class PerformanceReviewProcessStatus(str, Enum):
    ACTIVE = "active"
    DRAFT = "draft"
    FINISHED = "finished"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
