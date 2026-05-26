from enum import Enum


class DocumentsDocumentSignatureStatus(str, Enum):
    BOUNCED_EMAIL = "bounced_email"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DECLINED = "declined"
    ERROR = "error"
    EXPIRED = "expired"
    PARTIALLY_SIGNED = "partially_signed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
