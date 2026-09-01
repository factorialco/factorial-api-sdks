from enum import Enum


class PerformanceReviewEvaluationAnswerAnsweredQuestionnaireWithSectionsContentItemType(str, Enum):
    ANSWERED_QUESTION = "answered_question"
    ANSWERED_SECTION = "answered_section"

    def __str__(self) -> str:
        return str(self.value)
