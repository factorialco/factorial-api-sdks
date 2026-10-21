from enum import Enum


class PostApi20270101ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemType(
    str, Enum
):
    QUESTION = "question"
    SECTION = "section"

    def __str__(self) -> str:
        return str(self.value)
