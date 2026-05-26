from enum import Enum


class PutApi20260401ResourcesProjectManagementProjectTasksIdBodyStatus(str, Enum):
    DISCARDED = "discarded"
    DONE = "done"
    IN_PROGRESS = "in_progress"
    TODO = "todo"

    def __str__(self) -> str:
        return str(self.value)
