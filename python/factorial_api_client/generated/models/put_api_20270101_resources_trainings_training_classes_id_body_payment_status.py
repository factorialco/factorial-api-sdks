from enum import Enum


class PutApi20270101ResourcesTrainingsTrainingClassesIdBodyPaymentStatus(str, Enum):
    PAID = "paid"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
