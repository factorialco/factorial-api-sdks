from enum import Enum


class GetApi20251001ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus(str, Enum):
    CANBEINITIATED = "canbeinitiated"
    HASPENDINGAGREEMENT = "haspendingagreement"
    HASSIGNEDAGREEMENT = "hassignedagreement"
    NOTINITIATED = "notinitiated"

    def __str__(self) -> str:
        return str(self.value)
