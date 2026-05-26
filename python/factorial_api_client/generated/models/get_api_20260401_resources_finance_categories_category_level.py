from enum import Enum


class GetApi20260401ResourcesFinanceCategoriesCategoryLevel(str, Enum):
    ALL = "all"
    CATEGORY = "category"
    SUBCATEGORY = "subcategory"

    def __str__(self) -> str:
        return str(self.value)
