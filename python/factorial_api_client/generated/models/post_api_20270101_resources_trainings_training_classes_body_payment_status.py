from enum import Enum


class PostApi20270101ResourcesTrainingsTrainingClassesBodyPaymentStatus(str, Enum):
    PAID = "paid"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
