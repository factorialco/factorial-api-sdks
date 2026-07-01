from enum import Enum


class PutApi20260701ResourcesAtsApplicationsIdBodyAuthorType(str, Enum):
    ACCESS = "access"
    COMPANY = "company"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
