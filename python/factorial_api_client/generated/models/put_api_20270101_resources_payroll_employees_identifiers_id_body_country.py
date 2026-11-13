from enum import Enum


class PutApi20270101ResourcesPayrollEmployeesIdentifiersIdBodyCountry(str, Enum):
    DE = "de"
    IT = "it"
    PT = "pt"

    def __str__(self) -> str:
        return str(self.value)
