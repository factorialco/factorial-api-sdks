from enum import Enum


class PostApi20261001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyBodyQuestionnaireContentItemType(
    str, Enum
):
    QUESTION = "question"
    SECTION = "section"

    def __str__(self) -> str:
        return str(self.value)
