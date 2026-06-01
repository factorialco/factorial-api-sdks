from enum import Enum


class TrainingsTrainingStatus(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
