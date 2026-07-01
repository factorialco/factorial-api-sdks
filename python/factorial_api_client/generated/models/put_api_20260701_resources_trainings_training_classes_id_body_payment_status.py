from enum import Enum


class PutApi20260701ResourcesTrainingsTrainingClassesIdBodyPaymentStatus(str, Enum):
    PAID = "paid"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
