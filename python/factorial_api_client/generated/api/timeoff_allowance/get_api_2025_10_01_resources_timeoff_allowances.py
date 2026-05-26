from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_timeoff_allowances_response_200 import (
    GetApi20251001ResourcesTimeoffAllowancesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    timeoff_policy_id: int | Unset = UNSET,
    by_overtime: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["timeoff_policy_id"] = timeoff_policy_id

    params["by_overtime"] = by_overtime

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/timeoff/allowances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesTimeoffAllowancesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesTimeoffAllowancesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesTimeoffAllowancesResponse200]:
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
    timeoff_policy_id: int | Unset = UNSET,
    by_overtime: bool | Unset = UNSET,
) -> Response[GetApi20251001ResourcesTimeoffAllowancesResponse200]:
    """Reads all Allowances

     Retrieves allowances

    Args:
        ids (list[int] | Unset): An array of allowance ids to look for Example: [1, 2].
        timeoff_policy_id (int | Unset): Filter allowances by Time off policy id Example: 1.
        by_overtime (bool | Unset): Filter by only overtime allowances Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesTimeoffAllowancesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        timeoff_policy_id=timeoff_policy_id,
        by_overtime=by_overtime,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    timeoff_policy_id: int | Unset = UNSET,
    by_overtime: bool | Unset = UNSET,
) -> GetApi20251001ResourcesTimeoffAllowancesResponse200 | None:
    """Reads all Allowances

     Retrieves allowances

    Args:
        ids (list[int] | Unset): An array of allowance ids to look for Example: [1, 2].
        timeoff_policy_id (int | Unset): Filter allowances by Time off policy id Example: 1.
        by_overtime (bool | Unset): Filter by only overtime allowances Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesTimeoffAllowancesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        timeoff_policy_id=timeoff_policy_id,
        by_overtime=by_overtime,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    timeoff_policy_id: int | Unset = UNSET,
    by_overtime: bool | Unset = UNSET,
) -> Response[GetApi20251001ResourcesTimeoffAllowancesResponse200]:
    """Reads all Allowances

     Retrieves allowances

    Args:
        ids (list[int] | Unset): An array of allowance ids to look for Example: [1, 2].
        timeoff_policy_id (int | Unset): Filter allowances by Time off policy id Example: 1.
        by_overtime (bool | Unset): Filter by only overtime allowances Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesTimeoffAllowancesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        timeoff_policy_id=timeoff_policy_id,
        by_overtime=by_overtime,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    timeoff_policy_id: int | Unset = UNSET,
    by_overtime: bool | Unset = UNSET,
) -> GetApi20251001ResourcesTimeoffAllowancesResponse200 | None:
    """Reads all Allowances

     Retrieves allowances

    Args:
        ids (list[int] | Unset): An array of allowance ids to look for Example: [1, 2].
        timeoff_policy_id (int | Unset): Filter allowances by Time off policy id Example: 1.
        by_overtime (bool | Unset): Filter by only overtime allowances Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesTimeoffAllowancesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            timeoff_policy_id=timeoff_policy_id,
            by_overtime=by_overtime,
        )
    ).parsed
