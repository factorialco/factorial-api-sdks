from enum import Enum


class IntegrationsSyncRunStatus(str, Enum):
    ERRORED = "errored"
    RUNNING = "running"
    SUCCEDEDWITHERRORS = "succededwitherrors"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
