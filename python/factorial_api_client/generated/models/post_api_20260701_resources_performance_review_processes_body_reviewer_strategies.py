from enum import Enum


class PostApi20260701ResourcesPerformanceReviewProcessesBodyReviewerStrategies(str, Enum):
    DIRECT_REPORTS = "direct_reports"
    MANAGER = "manager"
    PEERS = "peers"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
