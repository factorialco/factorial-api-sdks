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

__all__ = [
    "FactorialClient",
    "paginate",
    "paginate_async",
    "collect_all",
]
