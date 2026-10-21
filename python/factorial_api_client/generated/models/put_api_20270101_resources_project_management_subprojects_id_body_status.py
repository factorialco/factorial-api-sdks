from enum import Enum


class PutApi20270101ResourcesProjectManagementSubprojectsIdBodyStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    DRAFT = "draft"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
