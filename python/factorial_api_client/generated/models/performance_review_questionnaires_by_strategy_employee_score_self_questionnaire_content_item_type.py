from enum import Enum


class PerformanceReviewQuestionnairesByStrategyEmployeeScoreSelfQuestionnaireContentItemType(
    str, Enum
):
    QUESTION = "question"
    SECTION = "section"

    def __str__(self) -> str:
        return str(self.value)
