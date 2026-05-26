from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_work_schedule_schedules_response_200 import (
    GetApi20260401ResourcesWorkScheduleSchedulesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    with_employee_ids: bool,
    with_periods: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["with_employee_ids"] = with_employee_ids

    params["with_periods"] = with_periods

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/work_schedule/schedules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesWorkScheduleSchedulesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesWorkScheduleSchedulesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesWorkScheduleSchedulesResponse200]:
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
    with_employee_ids: bool,
    with_periods: bool,
) -> Response[GetApi20260401ResourcesWorkScheduleSchedulesResponse200]:
    """Reads all Schedules

     Reads all Schedules

    Args:
        ids (list[int] | Unset):
        with_employee_ids (bool):
        with_periods (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesWorkScheduleSchedulesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        with_employee_ids=with_employee_ids,
        with_periods=with_periods,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    with_employee_ids: bool,
    with_periods: bool,
) -> GetApi20260401ResourcesWorkScheduleSchedulesResponse200 | None:
    """Reads all Schedules

     Reads all Schedules

    Args:
        ids (list[int] | Unset):
        with_employee_ids (bool):
        with_periods (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesWorkScheduleSchedulesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        with_employee_ids=with_employee_ids,
        with_periods=with_periods,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    with_employee_ids: bool,
    with_periods: bool,
) -> Response[GetApi20260401ResourcesWorkScheduleSchedulesResponse200]:
    """Reads all Schedules

     Reads all Schedules

    Args:
        ids (list[int] | Unset):
        with_employee_ids (bool):
        with_periods (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesWorkScheduleSchedulesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        with_employee_ids=with_employee_ids,
        with_periods=with_periods,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    with_employee_ids: bool,
    with_periods: bool,
) -> GetApi20260401ResourcesWorkScheduleSchedulesResponse200 | None:
    """Reads all Schedules

     Reads all Schedules

    Args:
        ids (list[int] | Unset):
        with_employee_ids (bool):
        with_periods (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesWorkScheduleSchedulesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            with_employee_ids=with_employee_ids,
            with_periods=with_periods,
        )
    ).parsed
