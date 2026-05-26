from enum import Enum


class PostApi20251001ResourcesPayrollEmployeesIdentifiersBodyCountry(str, Enum):
    DE = "de"
    IT = "it"
    PT = "pt"

    def __str__(self) -> str:
        return str(self.value)
