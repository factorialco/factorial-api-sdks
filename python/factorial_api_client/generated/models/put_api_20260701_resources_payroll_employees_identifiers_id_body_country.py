from enum import Enum


class PutApi20260701ResourcesPayrollEmployeesIdentifiersIdBodyCountry(str, Enum):
    DE = "de"
    IT = "it"
    PT = "pt"

    def __str__(self) -> str:
        return str(self.value)
