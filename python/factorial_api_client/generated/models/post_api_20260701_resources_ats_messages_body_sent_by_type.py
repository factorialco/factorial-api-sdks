from enum import Enum


class PostApi20260701ResourcesAtsMessagesBodySentByType(str, Enum):
    CANDIDATE = "candidate"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
