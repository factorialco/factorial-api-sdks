from enum import Enum


class ContractsContractSchedule(str, Enum):
    EXPIRED = "expired"
    ONGOING = "ongoing"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
