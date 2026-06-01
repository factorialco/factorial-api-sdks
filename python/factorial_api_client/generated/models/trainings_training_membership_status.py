from enum import Enum


class TrainingsTrainingMembershipStatus(str, Enum):
    COMPLETED = "completed"
    MISSING = "missing"
    NOTASSIGNED = "notassigned"
    NOTSTARTED = "notstarted"
    PARTIALLYCOMPLETED = "partiallycompleted"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
