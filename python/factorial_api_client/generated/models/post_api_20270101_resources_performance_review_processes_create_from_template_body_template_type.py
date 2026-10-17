from enum import Enum


class PostApi20270101ResourcesPerformanceReviewProcessesCreateFromTemplateBodyTemplateType(
    str, Enum
):
    CUSTOM = "custom"
    PREDEFINED = "predefined"

    def __str__(self) -> str:
        return str(self.value)
