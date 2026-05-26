from enum import Enum


class PostApi20260401ResourcesDocumentsDocumentsBodySpace(str, Enum):
    COMPANY_INTERNAL = "company_internal"
    COMPANY_PUBLIC = "company_public"
    EMPLOYEE_MY_DOCUMENTS = "employee_my_documents"
    PENDING_TO_ASSIGN = "pending_to_assign"
    PENDING_TO_DESTROY = "pending_to_destroy"

    def __str__(self) -> str:
        return str(self.value)
