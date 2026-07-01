from enum import Enum


class PutApi20260701ResourcesContractsContractVersionsIdBodyBankHolidayTreatment(str, Enum):
    NON_WORKABLE = "non_workable"
    WORKABLE = "workable"

    def __str__(self) -> str:
        return str(self.value)
