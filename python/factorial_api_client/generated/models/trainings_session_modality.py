from enum import Enum


class TrainingsSessionModality(str, Enum):
    INPERSON = "inperson"
    MIXED = "mixed"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
