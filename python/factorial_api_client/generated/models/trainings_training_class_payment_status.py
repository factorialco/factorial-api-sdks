from enum import Enum


class TrainingsTrainingClassPaymentStatus(str, Enum):
    PAID = "paid"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
