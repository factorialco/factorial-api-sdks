from enum import Enum


class ProjectManagementProjectEmployeesAssignment(str, Enum):
    COMPANY = "company"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
