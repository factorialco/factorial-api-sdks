from enum import Enum


class TrainingsTrainingStatus(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    DRAFT = "draft"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
