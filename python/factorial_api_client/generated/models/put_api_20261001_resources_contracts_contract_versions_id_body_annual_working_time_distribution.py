from enum import Enum


class PutApi20261001ResourcesContractsContractVersionsIdBodyAnnualWorkingTimeDistribution(
    str, Enum
):
    LIMIT_DAILY_HOURS = "limit_daily_hours"
    LIMIT_WORKDAYS = "limit_workdays"

    def __str__(self) -> str:
        return str(self.value)
