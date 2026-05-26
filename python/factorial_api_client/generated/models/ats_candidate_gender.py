from enum import Enum


class AtsCandidateGender(str, Enum):
    FEMALE = "female"
    MALE = "male"
    OTHER = "other"
    UNANSWERED = "unanswered"

    def __str__(self) -> str:
        return str(self.value)
