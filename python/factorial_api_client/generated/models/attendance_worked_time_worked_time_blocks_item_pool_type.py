from enum import Enum


class AttendanceWorkedTimeWorkedTimeBlocksItemPoolType(str, Enum):
    BALANCE = "balance"
    BUFFER = "buffer"
    COMPLEMENTARY_BUFFER = "complementary_buffer"
    DISCARDED = "discarded"
    PAYROLL = "payroll"
    TIMEOFF = "timeoff"
    VIRTUAL_PAYROLL = "virtual_payroll"
    VIRTUAL_TIMEOFF = "virtual_timeoff"

    def __str__(self) -> str:
        return str(self.value)
