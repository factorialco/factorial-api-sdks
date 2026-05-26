from enum import Enum


class GetApi20251001ResourcesPayrollEmployeesIdentifiersCountry(str, Enum):
    DE = "de"
    IT = "it"
    PT = "pt"

    def __str__(self) -> str:
        return str(self.value)
