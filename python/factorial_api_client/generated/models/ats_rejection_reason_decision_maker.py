from enum import Enum


class AtsRejectionReasonDecisionMaker(str, Enum):
    CANDIDATE = "candidate"
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)
