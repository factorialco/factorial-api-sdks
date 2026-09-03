from enum import Enum


class PutApi20261001ResourcesTasksTasksIdBodyStatus(str, Enum):
    DISCARDED = "discarded"
    DONE = "done"
    IN_PROGRESS = "in_progress"
    TODO = "todo"

    def __str__(self) -> str:
        return str(self.value)
