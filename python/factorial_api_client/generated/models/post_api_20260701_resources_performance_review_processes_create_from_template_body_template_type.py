from enum import Enum


class PostApi20260701ResourcesPerformanceReviewProcessesCreateFromTemplateBodyTemplateType(
    str, Enum
):
    CUSTOM = "custom"
    PREDEFINED = "predefined"

    def __str__(self) -> str:
        return str(self.value)
