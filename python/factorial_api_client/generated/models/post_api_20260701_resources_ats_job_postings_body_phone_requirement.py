from enum import Enum


class PostApi20260701ResourcesAtsJobPostingsBodyPhoneRequirement(str, Enum):
    DO_NOT_ASK = "do_not_ask"
    MANDATORY = "mandatory"
    OPTIONAL = "optional"

    def __str__(self) -> str:
        return str(self.value)
