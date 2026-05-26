from enum import Enum


class PostApi20251001ResourcesPayrollFamilySituationsBodyCivilStatus(str, Enum):
    CIVIL_PARTNERSHIP = "civil_partnership"
    COHABITATING = "cohabitating"
    DIVORCED = "divorced"
    MARRIED = "married"
    NOT_APPLICABLE = "not_applicable"
    SEPARATED = "separated"
    SINGLE = "single"
    UNKNOWN = "unknown"
    WIDOW = "widow"

    def __str__(self) -> str:
        return str(self.value)
