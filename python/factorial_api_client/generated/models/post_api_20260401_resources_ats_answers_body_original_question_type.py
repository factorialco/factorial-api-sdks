from enum import Enum


class PostApi20260401ResourcesAtsAnswersBodyOriginalQuestionType(str, Enum):
    LONG_TEXT = "long_text"
    MULTIPLE_CHOICE = "multiple_choice"
    SINGLE_CHOICE = "single_choice"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
