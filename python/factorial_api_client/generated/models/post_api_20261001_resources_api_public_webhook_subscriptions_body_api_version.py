from enum import Enum


class PostApi20261001ResourcesApiPublicWebhookSubscriptionsBodyApiVersion(str, Enum):
    VALUE_0 = "2025-10-01"
    VALUE_1 = "2026-01-01"
    VALUE_2 = "2026-04-01"
    VALUE_3 = "2026-07-01"
    VALUE_4 = "2026-10-01"

    def __str__(self) -> str:
        return str(self.value)
