from enum import Enum


class PerformanceReviewProcessStartValidationErrors(str, Enum):
    INVALID_DEADLINE = "invalid_deadline"
    INVALID_SECTION_WEIGHTS_SUM = "invalid_section_weights_sum"
    MISSING_DEADLINE = "missing_deadline"
    MISSING_POTENTIAL_REVIEWERS = "missing_potential_reviewers"
    MISSING_QUESTIONS = "missing_questions"
    MISSING_REVIEWER_STRATEGY = "missing_reviewer_strategy"
    MISSING_TARGET_STRATEGY = "missing_target_strategy"
    MISSING_TARGET_STRATEGY_MEMBERS = "missing_target_strategy_members"
    MISSING_TITLE = "missing_title"

    def __str__(self) -> str:
        return str(self.value)
