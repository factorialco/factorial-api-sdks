from enum import Enum


class PostApi20260401ResourcesTrainingsSessionsBodyModality(str, Enum):
    INPERSON = "inperson"
    MIXED = "mixed"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
