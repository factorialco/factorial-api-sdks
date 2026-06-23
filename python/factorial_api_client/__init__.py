"""
factorial-api-client — Python SDK for the Factorial API.

Quick start::

    from factorial_api_client import FactorialClient

    client = FactorialClient(api_key="YOUR_KEY")

    # Synchronous
    employees = client.employees.employee.list()
    for emp in client.employees.employee.paginate(max_items=50):
        print(emp.full_name)
    all_employees = client.employees.employee.all()

    # Async
    import asyncio
    async def main():
        async for emp in client.employees.employee.paginate_async(max_items=50):
            print(emp.full_name)
    asyncio.run(main())
"""

from factorial_api_client.client import FactorialClient
from factorial_api_client.pagination import collect_all, paginate, paginate_async

# The per-event payload aliases (e.g. AtsApplicationCreateWebhook) are generated
# into factorial_api_client.webhooks and re-exported here so handlers can do
# `from factorial_api_client import AtsApplicationCreateWebhook`.
from factorial_api_client.webhooks import *  # noqa: E402,F401,F403
from factorial_api_client.webhooks import (
    WEBHOOK_CATALOG,
    WEBHOOK_PAYLOAD_TYPES,
    WebhookCatalogEntry,
    WebhookSubscriptionType,
)
from factorial_api_client.webhooks import __all__ as _webhook_all

__all__ = [
    "FactorialClient",
    "paginate",
    "paginate_async",
    "collect_all",
    "WEBHOOK_CATALOG",
    "WEBHOOK_PAYLOAD_TYPES",
    "WebhookCatalogEntry",
    "WebhookSubscriptionType",
    *_webhook_all,
]
