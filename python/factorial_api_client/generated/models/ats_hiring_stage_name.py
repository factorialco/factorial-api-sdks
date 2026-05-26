from enum import Enum


class AtsHiringStageName(str, Enum):
    ASSESSMENT = "assessment"
    HIRED = "hired"
    INTERVIEW = "interview"
    NEW = "new"
    OFFER = "offer"
    SCREENING = "screening"

    def __str__(self) -> str:
        return str(self.value)
