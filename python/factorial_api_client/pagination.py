"""
Pagination helpers for the Factorial API client.

The Factorial API uses cursor-based pagination via `after_id` / `end_cursor`.
All list endpoints return:
  { data: [...], meta: { end_cursor, has_next_page, ... } }

The generated `sync_detailed` / `asyncio_detailed` functions return a
`Response[T]` object with `.parsed` containing the response model.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator, Callable, Generator
from typing import Any, TypeVar

T = TypeVar("T")

# The pagination params are not in the OpenAPI spec but work at runtime.
# We inject them via httpx's `params` extra kwarg mechanism.
# The generated _get_kwargs puts them in the `params` dict — but since the
# generated functions don't accept after_id/limit, we use a different approach:
# callers pass a `fetcher` closure that accepts `after_id: str | None` and
# returns the Response object from *_detailed().
#
# The fetcher is responsible for injecting after_id into the request.
# Since the generated code doesn't support extra params natively, callers can
# use sync_detailed(client=..., **other_params) and the extra pagination params
# must be passed via the client's base URL or by monkey-patching.
#
# Simplest approach: callers pass a fetcher(after_id) that calls the generated
# function. We extract meta from response.parsed.meta.


def _extract_page(response: Any) -> tuple[list[Any], str | None, bool]:
    """Extract (items, end_cursor, has_next_page) from a Response object."""
    parsed = response.parsed
    if parsed is None:
        return [], None, False

    data = getattr(parsed, "data", None) or []
    meta = getattr(parsed, "meta", None)
    if meta is None:
        return data, None, False

    end_cursor = getattr(meta, "end_cursor", None)
    # Unset sentinel check
    if hasattr(end_cursor, "__class__") and end_cursor.__class__.__name__ == "Unset":
        end_cursor = None
    has_next = getattr(meta, "has_next_page", False)
    return data, end_cursor, has_next


def paginate(
    fetcher: Callable[[str | None], Any],
    *,
    max_items: int | None = None,
) -> Generator[Any, None, None]:
    """
    Synchronous cursor-paginated generator.

    Args:
        fetcher: A callable that accepts ``after_id: str | None`` and returns
                 the ``Response`` object from a ``*_detailed()`` generated function.
        max_items: Stop after yielding this many items total (across all pages).

    Yields:
        Individual items from the ``data`` field of each page.
    """
    after_id: str | None = None
    yielded = 0

    while True:
        response = fetcher(after_id)
        items, end_cursor, has_next = _extract_page(response)

        for item in items:
            if max_items is not None and yielded >= max_items:
                return
            yield item
            yielded += 1

        if not has_next or not end_cursor:
            break
        after_id = end_cursor


async def paginate_async(
    fetcher: Callable[[str | None], Any],
    *,
    max_items: int | None = None,
) -> AsyncGenerator[Any, None]:
    """
    Asynchronous cursor-paginated generator.

    Args:
        fetcher: A coroutine callable that accepts ``after_id: str | None`` and
                 returns the ``Response`` object from a ``*_detailed()`` function.
        max_items: Stop after yielding this many items total.

    Yields:
        Individual items from the ``data`` field of each page.
    """
    after_id: str | None = None
    yielded = 0

    while True:
        response = await fetcher(after_id)
        items, end_cursor, has_next = _extract_page(response)

        for item in items:
            if max_items is not None and yielded >= max_items:
                return
            yield item
            yielded += 1

        if not has_next or not end_cursor:
            break
        after_id = end_cursor


def collect_all(
    fetcher: Callable[[str | None], Any],
    *,
    max_items: int | None = None,
) -> list[Any]:
    """
    Synchronously collect all pages into a flat list.

    Args:
        fetcher: A callable that accepts ``after_id: str | None``.
        max_items: Cap the total number of items returned.

    Returns:
        A list of all items across all pages.
    """
    return list(paginate(fetcher, max_items=max_items))
