#!/usr/bin/env python3
"""
test_api.py — Live smoke test for the Factorial Python SDK.

Requires one of:
  FACTORIAL_API_KEY      — sent as x-api-key header
  FACTORIAL_OAUTH_TOKEN  — sent as Authorization: Bearer header

Usage:
    FACTORIAL_API_KEY=xxx uv run python scripts/test_api.py
    FACTORIAL_OAUTH_TOKEN=xxx uv run python scripts/test_api.py
"""

from __future__ import annotations

import asyncio
import os
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1]))

from factorial_api_client import FactorialClient


def test_sync(client: FactorialClient) -> None:
    print("=== Sync tests ===\n")

    # list() — first page
    print("1. employees.employee.list()")
    result = client.employees.employee.list()
    data = getattr(result, "data", result) or []
    print(f"   Got {len(data)} employees on first page")

    # paginate() — stop at 5
    print("\n2. employees.employee.paginate(max_items=5)")
    count = 0
    for emp in client.employees.employee.paginate(max_items=5):
        count += 1
    print(f"   Iterated {count} employees")

    # all() — collect up to 10
    print("\n3. employees.employee.all(max_items=10)")
    all_emps = client.employees.employee.all(max_items=10)
    print(f"   Collected {len(all_emps)} employees")

    print("\nSync tests passed.")


async def test_async(client: FactorialClient) -> None:
    print("\n=== Async tests ===\n")

    # paginate_async() — stop at 5
    print("4. employees.employee.paginate_async(max_items=5)")
    count = 0
    async for emp in await client.employees.employee.paginate_async(max_items=5):
        count += 1
    print(f"   Async iterated {count} employees")

    print("\nAsync tests passed.")


def main() -> None:
    api_key = os.environ.get("FACTORIAL_API_KEY")
    oauth_token = os.environ.get("FACTORIAL_OAUTH_TOKEN")

    if not api_key and not oauth_token:
        print("ERROR: Set FACTORIAL_API_KEY or FACTORIAL_OAUTH_TOKEN environment variable")
        sys.exit(1)

    if api_key:
        print(f"Authenticated via API key")
        client = FactorialClient(api_key=api_key)
    else:
        print(f"Authenticated via OAuth token")
        client = FactorialClient(token=oauth_token)

    test_sync(client)
    asyncio.run(test_async(client))

    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
