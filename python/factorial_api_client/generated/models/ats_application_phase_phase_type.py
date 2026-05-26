from enum import Enum


class AtsApplicationPhasePhaseType(str, Enum):
    ASSESSMENT = "assessment"
    HIRED = "hired"
    INITIAL = "initial"
    INTERVIEW = "interview"
    NORMAL = "normal"
    OFFER = "offer"
    SCREENING = "screening"

    def __str__(self) -> str:
        return str(self.value)
