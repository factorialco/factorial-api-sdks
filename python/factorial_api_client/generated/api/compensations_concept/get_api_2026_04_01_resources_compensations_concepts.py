from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_compensations_concepts_categories import (
    GetApi20260401ResourcesCompensationsConceptsCategories,
)
from ...models.get_api_20260401_resources_compensations_concepts_response_200 import (
    GetApi20260401ResourcesCompensationsConceptsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    categories: GetApi20260401ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_categories: str | Unset = UNSET
    if not isinstance(categories, Unset):
        json_categories = categories.value

    params["categories[]"] = json_categories

    params["with_active_status"] = with_active_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/compensations/concepts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesCompensationsConceptsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesCompensationsConceptsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesCompensationsConceptsResponse200]:
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
    categories: GetApi20260401ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesCompensationsConceptsResponse200]:
    """Reads all Concepts

     Reads all Concepts

    Args:
        ids (list[int] | Unset): The ids of the concepts Example: [1].
        categories (GetApi20260401ResourcesCompensationsConceptsCategories | Unset): The
            categories of the concept Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): Whether to return only active concepts Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesCompensationsConceptsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    categories: GetApi20260401ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
) -> GetApi20260401ResourcesCompensationsConceptsResponse200 | None:
    """Reads all Concepts

     Reads all Concepts

    Args:
        ids (list[int] | Unset): The ids of the concepts Example: [1].
        categories (GetApi20260401ResourcesCompensationsConceptsCategories | Unset): The
            categories of the concept Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): Whether to return only active concepts Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesCompensationsConceptsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    categories: GetApi20260401ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesCompensationsConceptsResponse200]:
    """Reads all Concepts

     Reads all Concepts

    Args:
        ids (list[int] | Unset): The ids of the concepts Example: [1].
        categories (GetApi20260401ResourcesCompensationsConceptsCategories | Unset): The
            categories of the concept Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): Whether to return only active concepts Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesCompensationsConceptsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    categories: GetApi20260401ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
) -> GetApi20260401ResourcesCompensationsConceptsResponse200 | None:
    """Reads all Concepts

     Reads all Concepts

    Args:
        ids (list[int] | Unset): The ids of the concepts Example: [1].
        categories (GetApi20260401ResourcesCompensationsConceptsCategories | Unset): The
            categories of the concept Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): Whether to return only active concepts Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesCompensationsConceptsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            categories=categories,
            with_active_status=with_active_status,
        )
    ).parsed
