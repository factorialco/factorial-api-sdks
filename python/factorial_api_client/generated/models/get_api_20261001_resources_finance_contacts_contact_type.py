from enum import Enum


class GetApi20261001ResourcesFinanceContactsContactType(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
