from enum import Enum


class GetApi20260401ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus(str, Enum):
    CANBEINITIATED = "canbeinitiated"
    HASBOUNCEDEMAILAGREEMENT = "hasbouncedemailagreement"
    HASCANCELLEDAGREEMENT = "hascancelledagreement"
    HASDECLINEDAGREEMENT = "hasdeclinedagreement"
    HASERRORAGREEMENT = "haserroragreement"
    HASESIGNEDAGREEMENT = "hasesignedagreement"
    HASEXPIREDAGREEMENT = "hasexpiredagreement"
    HASPARTIALLYESIGNEDAGREEMENT = "haspartiallyesignedagreement"
    HASPENDINGAGREEMENT = "haspendingagreement"
    HASPENDINGESIGNATURESAGREEMENT = "haspendingesignaturesagreement"
    HASSIGNEDAGREEMENT = "hassignedagreement"
    NOTINITIATED = "notinitiated"

    def __str__(self) -> str:
        return str(self.value)
