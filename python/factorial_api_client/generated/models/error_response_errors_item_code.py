from enum import Enum


class ErrorResponseErrorsItemCode(str, Enum):
    FORBIDDEN = "forbidden"
    INVALID_STATE = "invalid_state"
    MALFORMED_REQUEST = "malformed_request"
    MALFORMED_RESOURCE = "malformed_resource"
    MISSING_RESOURCE = "missing_resource"
    PAYMENT_REQUIRED = "payment_required"
    SERVICE_UNREACHABLE = "service_unreachable"
    UNAUTHORIZED = "unauthorized"
    UNKNOWN_ERROR = "unknown_error"
    VALIDATION_FAILED = "validation_failed"

    def __str__(self) -> str:
        return str(self.value)
