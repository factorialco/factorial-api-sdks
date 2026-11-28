from enum import Enum


class PutApi20270101ResourcesFinanceContactsIdBodyContactTypes(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
