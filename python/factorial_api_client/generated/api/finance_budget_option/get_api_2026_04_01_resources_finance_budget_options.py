from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_finance_budget_options_response_200 import (
    GetApi20260401ResourcesFinanceBudgetOptionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    effective_at: str | Unset = UNSET,
    include_inactive: bool,
    include_archived: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["effective_at"] = effective_at

    params["include_inactive"] = include_inactive

    params["include_archived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/finance/budget_options",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesFinanceBudgetOptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesFinanceBudgetOptionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesFinanceBudgetOptionsResponse200]:
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
    employee_ids: list[int] | Unset = UNSET,
    effective_at: str | Unset = UNSET,
    include_inactive: bool,
    include_archived: bool,
) -> Response[GetApi20260401ResourcesFinanceBudgetOptionsResponse200]:
    """Reads all Budget options

     Fetch budget options for the company

    Args:
        ids (list[int] | Unset): Search budget options by ID Example: [1].
        employee_ids (list[int] | Unset): Search budget options by employee IDs Example: [1].
        effective_at (str | Unset): Filter budget options effective at this date Example:
            2021-01-01T00:00:00Z.
        include_inactive (bool): Include inactive budget options
        include_archived (bool): Include archived budget options

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceBudgetOptionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        effective_at=effective_at,
        include_inactive=include_inactive,
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    effective_at: str | Unset = UNSET,
    include_inactive: bool,
    include_archived: bool,
) -> GetApi20260401ResourcesFinanceBudgetOptionsResponse200 | None:
    """Reads all Budget options

     Fetch budget options for the company

    Args:
        ids (list[int] | Unset): Search budget options by ID Example: [1].
        employee_ids (list[int] | Unset): Search budget options by employee IDs Example: [1].
        effective_at (str | Unset): Filter budget options effective at this date Example:
            2021-01-01T00:00:00Z.
        include_inactive (bool): Include inactive budget options
        include_archived (bool): Include archived budget options

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceBudgetOptionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        effective_at=effective_at,
        include_inactive=include_inactive,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    effective_at: str | Unset = UNSET,
    include_inactive: bool,
    include_archived: bool,
) -> Response[GetApi20260401ResourcesFinanceBudgetOptionsResponse200]:
    """Reads all Budget options

     Fetch budget options for the company

    Args:
        ids (list[int] | Unset): Search budget options by ID Example: [1].
        employee_ids (list[int] | Unset): Search budget options by employee IDs Example: [1].
        effective_at (str | Unset): Filter budget options effective at this date Example:
            2021-01-01T00:00:00Z.
        include_inactive (bool): Include inactive budget options
        include_archived (bool): Include archived budget options

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceBudgetOptionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        effective_at=effective_at,
        include_inactive=include_inactive,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    effective_at: str | Unset = UNSET,
    include_inactive: bool,
    include_archived: bool,
) -> GetApi20260401ResourcesFinanceBudgetOptionsResponse200 | None:
    """Reads all Budget options

     Fetch budget options for the company

    Args:
        ids (list[int] | Unset): Search budget options by ID Example: [1].
        employee_ids (list[int] | Unset): Search budget options by employee IDs Example: [1].
        effective_at (str | Unset): Filter budget options effective at this date Example:
            2021-01-01T00:00:00Z.
        include_inactive (bool): Include inactive budget options
        include_archived (bool): Include archived budget options

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceBudgetOptionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            effective_at=effective_at,
            include_inactive=include_inactive,
            include_archived=include_archived,
        )
    ).parsed
