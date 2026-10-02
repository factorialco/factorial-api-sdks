from enum import Enum


class PostApi20261001ResourcesTasksTasksBulkUpdateBodyTasksItemIdentifier(str, Enum):
    INBOX = "inbox"
    PROJECT = "project"
    SHARED_AND_SINGLE = "shared_and_single"
    SINGLE = "single"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
