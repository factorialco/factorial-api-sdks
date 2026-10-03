from enum import Enum


class PerformanceReviewQuestionnairesByStrategyPeersQuestionnaireContentItemType(str, Enum):
    QUESTION = "question"
    SECTION = "section"

    def __str__(self) -> str:
        return str(self.value)
