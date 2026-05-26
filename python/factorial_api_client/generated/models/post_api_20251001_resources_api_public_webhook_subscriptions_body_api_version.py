from enum import Enum


class PostApi20251001ResourcesApiPublicWebhookSubscriptionsBodyApiVersion(str, Enum):
    VALUE_0 = "2024-10-01"
    VALUE_1 = "2025-01-01"
    VALUE_2 = "2025-04-01"
    VALUE_3 = "2025-07-01"
    VALUE_4 = "2025-10-01"

    def __str__(self) -> str:
        return str(self.value)
