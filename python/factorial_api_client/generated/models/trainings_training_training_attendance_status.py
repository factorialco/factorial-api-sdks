from enum import Enum


class TrainingsTrainingTrainingAttendanceStatus(str, Enum):
    COMPLETED = "completed"
    MISSING = "missing"
    NOTASSIGNED = "notassigned"
    NOTSTARTED = "notstarted"
    PARTIALLYCOMPLETED = "partiallycompleted"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
