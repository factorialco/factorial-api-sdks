from enum import Enum


class PostApi20251001ResourcesAtsQuestionsBodyQuestionType(str, Enum):
    FILE = "file"
    LONG_TEXT = "long_text"
    MULTIPLE_CHOICE = "multiple_choice"
    SINGLE_CHOICE = "single_choice"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
