from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_attendance_open_shifts_response_200 import (
    GetApi20261001ResourcesAttendanceOpenShiftsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employee_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/attendance/open_shifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesAttendanceOpenShiftsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesAttendanceOpenShiftsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesAttendanceOpenShiftsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesAttendanceOpenShiftsResponse200]:
    """Reads all Open shifts

     Returns the currently open shifts. If `employee_ids` is provided, results are
    filtered to those employees. If `employee_ids` is omitted, callers holding the
    SeeAttendancePeriods permission (e.g. admin API keys) receive every open shift
    in the company; other callers receive only their own open shift.

    Args:
        employee_ids (list[str] | Unset): Optional. Employee ids to filter the open shifts by.
            When omitted,
            callers holding the SeeAttendancePeriods permission receive all open
            shifts in the company; other callers receive only their own open shift.
             Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceOpenShiftsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesAttendanceOpenShiftsResponse200 | None:
    """Reads all Open shifts

     Returns the currently open shifts. If `employee_ids` is provided, results are
    filtered to those employees. If `employee_ids` is omitted, callers holding the
    SeeAttendancePeriods permission (e.g. admin API keys) receive every open shift
    in the company; other callers receive only their own open shift.

    Args:
        employee_ids (list[str] | Unset): Optional. Employee ids to filter the open shifts by.
            When omitted,
            callers holding the SeeAttendancePeriods permission receive all open
            shifts in the company; other callers receive only their own open shift.
             Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceOpenShiftsResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesAttendanceOpenShiftsResponse200]:
    """Reads all Open shifts

     Returns the currently open shifts. If `employee_ids` is provided, results are
    filtered to those employees. If `employee_ids` is omitted, callers holding the
    SeeAttendancePeriods permission (e.g. admin API keys) receive every open shift
    in the company; other callers receive only their own open shift.

    Args:
        employee_ids (list[str] | Unset): Optional. Employee ids to filter the open shifts by.
            When omitted,
            callers holding the SeeAttendancePeriods permission receive all open
            shifts in the company; other callers receive only their own open shift.
             Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceOpenShiftsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesAttendanceOpenShiftsResponse200 | None:
    """Reads all Open shifts

     Returns the currently open shifts. If `employee_ids` is provided, results are
    filtered to those employees. If `employee_ids` is omitted, callers holding the
    SeeAttendancePeriods permission (e.g. admin API keys) receive every open shift
    in the company; other callers receive only their own open shift.

    Args:
        employee_ids (list[str] | Unset): Optional. Employee ids to filter the open shifts by.
            When omitted,
            callers holding the SeeAttendancePeriods permission receive all open
            shifts in the company; other callers receive only their own open shift.
             Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceOpenShiftsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
        )
    ).parsed
