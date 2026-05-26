from enum import Enum


class PostApi20251001ResourcesContractsContractVersionsBodyBankHolidayTreatment(str, Enum):
    NON_WORKABLE = "non_workable"
    WORKABLE = "workable"

    def __str__(self) -> str:
        return str(self.value)
