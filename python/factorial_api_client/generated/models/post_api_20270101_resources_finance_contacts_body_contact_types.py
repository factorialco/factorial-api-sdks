from enum import Enum


class PostApi20270101ResourcesFinanceContactsBodyContactTypes(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
