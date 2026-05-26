from enum import Enum


class PerformanceReviewEvaluationStatus(str, Enum):
    PENDING = "pending"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
