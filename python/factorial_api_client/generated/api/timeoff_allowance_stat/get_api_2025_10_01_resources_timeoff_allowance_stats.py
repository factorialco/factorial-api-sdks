from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_timeoff_allowance_stats_response_200 import (
    GetApi20251001ResourcesTimeoffAllowanceStatsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    allowance_ids: list[int] | Unset = UNSET,
    reference_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_allowance_ids: list[int] | Unset = UNSET
    if not isinstance(allowance_ids, Unset):
        json_allowance_ids = allowance_ids

    params["allowance_ids[]"] = json_allowance_ids

    params["reference_date"] = reference_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/timeoff/allowance_stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesTimeoffAllowanceStatsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesTimeoffAllowanceStatsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesTimeoffAllowanceStatsResponse200]:
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
    employee_ids: list[int] | Unset = UNSET,
    allowance_ids: list[int] | Unset = UNSET,
    reference_date: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesTimeoffAllowanceStatsResponse200]:
    """Reads all Allowance stats

     Retrieves the employee time off counters for a specific allowance with a reference date

    Args:
        ids (list[str] | Unset): A virtual ID for the allowance stat, composed of
            employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. Example:
            1/2/2023-10-01.
        employee_ids (list[int] | Unset): Get the allowance stats for specific employees Example:
            [1].
        allowance_ids (list[int] | Unset): Filter the stats by these allowance IDs Example: [1,
            2].
        reference_date (str | Unset): The reference date to calculate the allowance stats. If not
            provided, it will use today's date. Example: 2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesTimeoffAllowanceStatsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        allowance_ids=allowance_ids,
        reference_date=reference_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    allowance_ids: list[int] | Unset = UNSET,
    reference_date: str | Unset = UNSET,
) -> GetApi20251001ResourcesTimeoffAllowanceStatsResponse200 | None:
    """Reads all Allowance stats

     Retrieves the employee time off counters for a specific allowance with a reference date

    Args:
        ids (list[str] | Unset): A virtual ID for the allowance stat, composed of
            employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. Example:
            1/2/2023-10-01.
        employee_ids (list[int] | Unset): Get the allowance stats for specific employees Example:
            [1].
        allowance_ids (list[int] | Unset): Filter the stats by these allowance IDs Example: [1,
            2].
        reference_date (str | Unset): The reference date to calculate the allowance stats. If not
            provided, it will use today's date. Example: 2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesTimeoffAllowanceStatsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        allowance_ids=allowance_ids,
        reference_date=reference_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    allowance_ids: list[int] | Unset = UNSET,
    reference_date: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesTimeoffAllowanceStatsResponse200]:
    """Reads all Allowance stats

     Retrieves the employee time off counters for a specific allowance with a reference date

    Args:
        ids (list[str] | Unset): A virtual ID for the allowance stat, composed of
            employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. Example:
            1/2/2023-10-01.
        employee_ids (list[int] | Unset): Get the allowance stats for specific employees Example:
            [1].
        allowance_ids (list[int] | Unset): Filter the stats by these allowance IDs Example: [1,
            2].
        reference_date (str | Unset): The reference date to calculate the allowance stats. If not
            provided, it will use today's date. Example: 2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesTimeoffAllowanceStatsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        allowance_ids=allowance_ids,
        reference_date=reference_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    allowance_ids: list[int] | Unset = UNSET,
    reference_date: str | Unset = UNSET,
) -> GetApi20251001ResourcesTimeoffAllowanceStatsResponse200 | None:
    """Reads all Allowance stats

     Retrieves the employee time off counters for a specific allowance with a reference date

    Args:
        ids (list[str] | Unset): A virtual ID for the allowance stat, composed of
            employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. Example:
            1/2/2023-10-01.
        employee_ids (list[int] | Unset): Get the allowance stats for specific employees Example:
            [1].
        allowance_ids (list[int] | Unset): Filter the stats by these allowance IDs Example: [1,
            2].
        reference_date (str | Unset): The reference date to calculate the allowance stats. If not
            provided, it will use today's date. Example: 2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesTimeoffAllowanceStatsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            allowance_ids=allowance_ids,
            reference_date=reference_date,
        )
    ).parsed
