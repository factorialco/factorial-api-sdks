from enum import Enum


class GetApi20270101ResourcesFinanceContactsContactType(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
