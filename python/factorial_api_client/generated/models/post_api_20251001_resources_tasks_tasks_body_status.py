from enum import Enum


class PostApi20251001ResourcesTasksTasksBodyStatus(str, Enum):
    DISCARDED = "discarded"
    DONE = "done"
    IN_PROGRESS = "in_progress"
    TODO = "todo"

    def __str__(self) -> str:
        return str(self.value)
