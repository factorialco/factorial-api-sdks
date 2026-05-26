from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_attendance_edit_timesheet_requests_response_200 import (
    GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    shift_id: int | Unset = UNSET,
    pending: bool | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
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

    params["shift_id"] = shift_id

    params["pending"] = pending

    params["start_on"] = start_on

    params["end_on"] = end_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/attendance/edit_timesheet_requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200]:
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
    shift_id: int | Unset = UNSET,
    pending: bool | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200]:
    """Reads all Edit timesheet requests

     Reads all Edit timesheet requests

    Args:
        ids (list[int] | Unset): filter by ids. Example: [1, 2, 3].
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].
        shift_id (int | Unset): filter by shift id. Example: 1.
        pending (bool | Unset): filter by edit timesheet request status. Example: True.
        start_on (str | Unset): filter by edit timesheet requests that were created after or
            including this date. Example: 2022-01-01.
        end_on (str | Unset): filter by edit timesheet requests that were created before or
            including this date. Example: 2022-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        shift_id=shift_id,
        pending=pending,
        start_on=start_on,
        end_on=end_on,
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
    shift_id: int | Unset = UNSET,
    pending: bool | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
) -> GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200 | None:
    """Reads all Edit timesheet requests

     Reads all Edit timesheet requests

    Args:
        ids (list[int] | Unset): filter by ids. Example: [1, 2, 3].
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].
        shift_id (int | Unset): filter by shift id. Example: 1.
        pending (bool | Unset): filter by edit timesheet request status. Example: True.
        start_on (str | Unset): filter by edit timesheet requests that were created after or
            including this date. Example: 2022-01-01.
        end_on (str | Unset): filter by edit timesheet requests that were created before or
            including this date. Example: 2022-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        shift_id=shift_id,
        pending=pending,
        start_on=start_on,
        end_on=end_on,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    shift_id: int | Unset = UNSET,
    pending: bool | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200]:
    """Reads all Edit timesheet requests

     Reads all Edit timesheet requests

    Args:
        ids (list[int] | Unset): filter by ids. Example: [1, 2, 3].
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].
        shift_id (int | Unset): filter by shift id. Example: 1.
        pending (bool | Unset): filter by edit timesheet request status. Example: True.
        start_on (str | Unset): filter by edit timesheet requests that were created after or
            including this date. Example: 2022-01-01.
        end_on (str | Unset): filter by edit timesheet requests that were created before or
            including this date. Example: 2022-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        shift_id=shift_id,
        pending=pending,
        start_on=start_on,
        end_on=end_on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    shift_id: int | Unset = UNSET,
    pending: bool | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
) -> GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200 | None:
    """Reads all Edit timesheet requests

     Reads all Edit timesheet requests

    Args:
        ids (list[int] | Unset): filter by ids. Example: [1, 2, 3].
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].
        shift_id (int | Unset): filter by shift id. Example: 1.
        pending (bool | Unset): filter by edit timesheet request status. Example: True.
        start_on (str | Unset): filter by edit timesheet requests that were created after or
            including this date. Example: 2022-01-01.
        end_on (str | Unset): filter by edit timesheet requests that were created before or
            including this date. Example: 2022-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesAttendanceEditTimesheetRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            shift_id=shift_id,
            pending=pending,
            start_on=start_on,
            end_on=end_on,
        )
    ).parsed
