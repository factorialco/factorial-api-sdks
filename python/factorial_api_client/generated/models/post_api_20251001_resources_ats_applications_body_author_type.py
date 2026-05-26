from enum import Enum


class PostApi20251001ResourcesAtsApplicationsBodyAuthorType(str, Enum):
    ACCESS = "access"
    COMPANY = "company"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
