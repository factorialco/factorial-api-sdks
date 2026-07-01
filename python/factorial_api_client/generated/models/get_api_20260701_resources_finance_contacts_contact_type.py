from enum import Enum


class GetApi20260701ResourcesFinanceContactsContactType(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
