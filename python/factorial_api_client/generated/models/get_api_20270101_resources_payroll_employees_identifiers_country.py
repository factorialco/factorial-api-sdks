from enum import Enum


class GetApi20270101ResourcesPayrollEmployeesIdentifiersCountry(str, Enum):
    DE = "de"
    IT = "it"
    PT = "pt"

    def __str__(self) -> str:
        return str(self.value)
