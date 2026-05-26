from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_performance_review_process_custom_templates_response_200 import (
    GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    author_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_author_ids: list[int] | Unset = UNSET
    if not isinstance(author_ids, Unset):
        json_author_ids = author_ids

    params["author_ids[]"] = json_author_ids

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/performance/review_process_custom_templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    author_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200]:
    """Reads all Review process custom templates

     Retrieves the templates for the company.

    Args:
        ids (list[int] | Unset): Filter by template IDs Example: [1, 2, 3].
        author_ids (list[int] | Unset): Filter by author IDs Example: [1, 2, 3].
        search (str | Unset): Filter by template name Example: Q1 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        author_ids=author_ids,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    author_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
) -> GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200 | None:
    """Reads all Review process custom templates

     Retrieves the templates for the company.

    Args:
        ids (list[int] | Unset): Filter by template IDs Example: [1, 2, 3].
        author_ids (list[int] | Unset): Filter by author IDs Example: [1, 2, 3].
        search (str | Unset): Filter by template name Example: Q1 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        author_ids=author_ids,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    author_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200]:
    """Reads all Review process custom templates

     Retrieves the templates for the company.

    Args:
        ids (list[int] | Unset): Filter by template IDs Example: [1, 2, 3].
        author_ids (list[int] | Unset): Filter by author IDs Example: [1, 2, 3].
        search (str | Unset): Filter by template name Example: Q1 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        author_ids=author_ids,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    author_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
) -> GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200 | None:
    """Reads all Review process custom templates

     Retrieves the templates for the company.

    Args:
        ids (list[int] | Unset): Filter by template IDs Example: [1, 2, 3].
        author_ids (list[int] | Unset): Filter by author IDs Example: [1, 2, 3].
        search (str | Unset): Filter by template name Example: Q1 2024.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesPerformanceReviewProcessCustomTemplatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            author_ids=author_ids,
            search=search,
        )
    ).parsed
