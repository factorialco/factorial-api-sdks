from enum import Enum


class PostApi20260401ResourcesTimeoffAllowancesBodyCycleStart(str, Enum):
    APR = "apr"
    AUG = "aug"
    DEC = "dec"
    EMPLOYEE_HIRED_DATE = "employee_hired_date"
    FEB = "feb"
    JAN = "jan"
    JUL = "jul"
    JUN = "jun"
    MAR = "mar"
    MAY = "may"
    NOV = "nov"
    OCT = "oct"
    SEP = "sep"

    def __str__(self) -> str:
        return str(self.value)
