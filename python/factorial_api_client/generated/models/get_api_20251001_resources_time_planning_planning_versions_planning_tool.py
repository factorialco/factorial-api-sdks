from enum import Enum


class GetApi20251001ResourcesTimePlanningPlanningVersionsPlanningTool(str, Enum):
    CONTRACT_HOURS = "contract_hours"
    SHIFT_MANAGEMENT = "shift_management"
    WORK_SCHEDULE = "work_schedule"

    def __str__(self) -> str:
        return str(self.value)
