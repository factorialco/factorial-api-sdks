from enum import Enum


class GetApi20270101ResourcesProcessesProcessesCategories(str, Enum):
    CUSTOM = "custom"
    OFFBOARDING = "offboarding"
    ONBOARDING = "onboarding"
    TRAINING = "training"

    def __str__(self) -> str:
        return str(self.value)
