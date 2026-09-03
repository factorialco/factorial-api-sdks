from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_compensations_concepts_categories import (
    GetApi20261001ResourcesCompensationsConceptsCategories,
)
from ...models.get_api_20261001_resources_compensations_concepts_response_200 import (
    GetApi20261001ResourcesCompensationsConceptsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20261001ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_categories: str | Unset = UNSET
    if not isinstance(categories, Unset):
        json_categories = categories.value

    params["categories[]"] = json_categories

    params["with_active_status"] = with_active_status

    params["enabled"] = enabled

    params["default"] = default

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/compensations/concepts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesCompensationsConceptsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesCompensationsConceptsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesCompensationsConceptsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20261001ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesCompensationsConceptsResponse200]:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20261001ResourcesCompensationsConceptsCategories | Unset): Filter by
            concept categories Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): When true, returns only default concepts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesCompensationsConceptsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
        enabled=enabled,
        default=default,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20261001ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> GetApi20261001ResourcesCompensationsConceptsResponse200 | None:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20261001ResourcesCompensationsConceptsCategories | Unset): Filter by
            concept categories Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): When true, returns only default concepts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesCompensationsConceptsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
        enabled=enabled,
        default=default,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20261001ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesCompensationsConceptsResponse200]:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20261001ResourcesCompensationsConceptsCategories | Unset): Filter by
            concept categories Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): When true, returns only default concepts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesCompensationsConceptsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
        enabled=enabled,
        default=default,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20261001ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> GetApi20261001ResourcesCompensationsConceptsResponse200 | None:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20261001ResourcesCompensationsConceptsCategories | Unset): Filter by
            concept categories Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): When true, returns only default concepts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesCompensationsConceptsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            categories=categories,
            with_active_status=with_active_status,
            enabled=enabled,
            default=default,
        )
    ).parsed
