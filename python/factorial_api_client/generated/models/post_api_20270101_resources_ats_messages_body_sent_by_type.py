from enum import Enum


class PostApi20270101ResourcesAtsMessagesBodySentByType(str, Enum):
    CANDIDATE = "candidate"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
