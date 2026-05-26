from enum import Enum


class ContractsContractVersionRequestStatus(str, Enum):
    APPROVED = "approved"
    PENDING = "pending"
    REJECTED = "rejected"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
