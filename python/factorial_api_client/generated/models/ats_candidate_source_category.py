from enum import Enum


class AtsCandidateSourceCategory(str, Enum):
    AGENCY_OR_EXTERNAL_RECRUITER = "agency_or_external_recruiter"
    EVENT = "event"
    INTERNAL = "internal"
    JOB_BOARD = "job_board"
    MANUALLY_ADDED = "manually_added"
    ORGANIC = "organic"
    REFERRAL = "referral"
    SOCIAL_MEDIA = "social_media"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
