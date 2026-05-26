from enum import Enum


class GetApi20251001ResourcesFinanceContactsContactType(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
