from enum import Enum


class HolidaysCompanyHolidayHalfDay(str, Enum):
    BEGINNING_OF_DAY = "beginning_of_day"
    END_OF_DAY = "end_of_day"

    def __str__(self) -> str:
        return str(self.value)
