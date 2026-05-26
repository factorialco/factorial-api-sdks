from enum import Enum


class PostApi20251001ResourcesPerformanceReviewProcessesBodyTargetStrategy(str, Enum):
    ALL_EMPLOYEES = "all_employees"
    BY_EMPLOYEES = "by_employees"
    BY_LOCATIONS = "by_locations"
    BY_TEAMS = "by_teams"
    MANUAL_SELECTION = "manual_selection"

    def __str__(self) -> str:
        return str(self.value)
