from enum import Enum


class GetApi20270101ResourcesPerformanceReviewEvaluationScoresReviewerStrategies(str, Enum):
    DIRECT_REPORTS = "direct_reports"
    MANAGER = "manager"
    PEERS = "peers"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
