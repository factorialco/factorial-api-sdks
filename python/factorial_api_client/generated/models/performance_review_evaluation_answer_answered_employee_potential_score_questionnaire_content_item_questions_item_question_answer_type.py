from enum import Enum


class PerformanceReviewEvaluationAnswerAnsweredEmployeePotentialScoreQuestionnaireContentItemQuestionsItemQuestionAnswerType(
    str, Enum
):
    MULTIPLE_CHOICE = "multiple_choice"
    NUMBER = "number"
    RATING = "rating"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
