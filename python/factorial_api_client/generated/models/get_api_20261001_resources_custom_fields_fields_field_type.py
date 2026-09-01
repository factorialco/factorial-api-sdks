from enum import Enum


class GetApi20261001ResourcesCustomFieldsFieldsFieldType(str, Enum):
    CENTS = "cents"
    CHECKBOX = "checkbox"
    DATE = "date"
    LONG_TEXT = "long_text"
    MONEY = "money"
    MULTIPLE_CHOICE = "multiple_choice"
    RATING = "rating"
    SINGLE_CHOICE = "single_choice"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
