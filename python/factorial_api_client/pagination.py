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

# The pagination params (`after_id`, `limit`) are not in the OpenAPI spec but
# work at runtime, so the generated functions don't accept them. Callers pass a
# `fetcher(after_id)` closure that performs the request; the generated client
# builds those closures with `fetch_page` / `fetch_page_async` below, which
# replicate the generated `sync_detailed` / `asyncio_detailed` flow
# (`_get_kwargs` → httpx request → `_build_response`) and inject the pagination
# params into the query string.


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


def fetch_page(
    module: Any,
    client: Any,
    after_id: str | None = None,
    limit: int | None = None,
    **params: Any,
) -> Any:
    """
    Call a generated list-endpoint module with pagination params injected.

    ``after_id`` and ``limit`` are not in the OpenAPI spec, so the generated
    ``sync_detailed`` functions do not accept them. This helper replicates
    ``sync_detailed`` (``_get_kwargs`` → httpx request → ``_build_response``)
    and adds the pagination params to the query string.

    Args:
        module: A generated endpoint module exposing ``_get_kwargs`` and
                ``_build_response``.
        client: The ``AuthenticatedClient``.
        after_id: Opaque cursor (``meta.end_cursor`` of the previous page).
        limit: Page size (the API caps it at 100).
        **params: The endpoint's own query params, passed to ``_get_kwargs``.

    Returns:
        The ``Response`` object, as returned by ``sync_detailed``.
    """
    kwargs = module._get_kwargs(**params)
    query = kwargs.setdefault("params", {})
    if after_id is not None:
        query["after_id"] = after_id
    if limit is not None:
        query["limit"] = limit
    response = client.get_httpx_client().request(**kwargs)
    return module._build_response(client=client, response=response)


async def fetch_page_async(
    module: Any,
    client: Any,
    after_id: str | None = None,
    limit: int | None = None,
    **params: Any,
) -> Any:
    """Async variant of :func:`fetch_page` (see its docstring)."""
    kwargs = module._get_kwargs(**params)
    query = kwargs.setdefault("params", {})
    if after_id is not None:
        query["after_id"] = after_id
    if limit is not None:
        query["limit"] = limit
    response = await client.get_async_httpx_client().request(**kwargs)
    return module._build_response(client=client, response=response)


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
