from enum import Enum


class GetApi20260401ResourcesTasksTasksCategory(str, Enum):
    BENEFITS = "benefits"
    COMPENSATION = "compensation"
    COMPLAINTS = "complaints"
    DOCUMENTS = "documents"
    ENGAGEMENT = "engagement"
    FINANCE = "finance"
    ORGANIZATION = "organization"
    PERFORMANCE = "performance"
    POLICIES = "policies"
    RECRUITMENT = "recruitment"
    SOFTWARE = "software"
    SPENDING = "spending"
    SURVEYS = "surveys"
    TIMEOFF = "timeoff"
    TIME_PLANNING = "time_planning"
    TIME_TRACKING = "time_tracking"
    TRAINING = "training"

    def __str__(self) -> str:
        return str(self.value)
