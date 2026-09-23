from enum import Enum


class GetApi20261001ResourcesPerformanceReviewEvaluationsReviewerStrategies(str, Enum):
    DIRECT_REPORTS = "direct_reports"
    MANAGER = "manager"
    PEERS = "peers"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
