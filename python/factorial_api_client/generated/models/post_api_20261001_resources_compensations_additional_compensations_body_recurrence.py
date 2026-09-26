from enum import Enum


class PostApi20261001ResourcesCompensationsAdditionalCompensationsBodyRecurrence(str, Enum):
    EVERY_10_MONTHS = "every_10_months"
    EVERY_11_MONTHS = "every_11_months"
    EVERY_12_MONTHS = "every_12_months"
    EVERY_2_MONTHS = "every_2_months"
    EVERY_3_MONTHS = "every_3_months"
    EVERY_4_MONTHS = "every_4_months"
    EVERY_5_MONTHS = "every_5_months"
    EVERY_6_MONTHS = "every_6_months"
    EVERY_7_MONTHS = "every_7_months"
    EVERY_8_MONTHS = "every_8_months"
    EVERY_9_MONTHS = "every_9_months"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)
