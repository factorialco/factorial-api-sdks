from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_attendance_shifts_response_200 import (
    GetApi20260701ResourcesAttendanceShiftsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    half_day: bool,
    workable: bool | Unset = UNSET,
    latest_shift: bool | Unset = UNSET,
    sort_created_at_asc: bool,
    breaks_with_time_configuration: bool | Unset = UNSET,
    last_working_shift: bool | Unset = UNSET,
    updated_at: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["start_on"] = start_on

    params["end_on"] = end_on

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["half_day"] = half_day

    params["workable"] = workable

    params["latest_shift"] = latest_shift

    params["sort_created_at_asc"] = sort_created_at_asc

    params["breaks_with_time_configuration"] = breaks_with_time_configuration

    params["last_working_shift"] = last_working_shift

    params["updated_at"] = updated_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/attendance/shifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesAttendanceShiftsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesAttendanceShiftsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesAttendanceShiftsResponse200]:
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
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    half_day: bool,
    workable: bool | Unset = UNSET,
    latest_shift: bool | Unset = UNSET,
    sort_created_at_asc: bool,
    breaks_with_time_configuration: bool | Unset = UNSET,
    last_working_shift: bool | Unset = UNSET,
    updated_at: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesAttendanceShiftsResponse200]:
    """Reads all Shifts

     Reads all Shifts

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        start_on (str | Unset): filter by shift that starts after or including this date. Example:
            2023-09-30.
        end_on (str | Unset): filter by shift that ends before or including this date. Example:
            2023-10-01.
        ids (list[str] | Unset): filter by ids. Example: ['1', '2', '3'].
        half_day (bool): Flag to filter half day shifts
        workable (bool | Unset): Flag to filter shifts in workable days Example: True.
        latest_shift (bool | Unset): Flag to filter only the latest shift for each employee
            Example: True.
        sort_created_at_asc (bool): Flag to sort by created_at asc Example: True.
        breaks_with_time_configuration (bool | Unset): Flag to include breaks with time
            configuration Example: True.
        last_working_shift (bool | Unset): Filter by last working shift Example: True.
        updated_at (str | Unset): Filter shifts by the date they were last updated Example:
            2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAttendanceShiftsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        ids=ids,
        half_day=half_day,
        workable=workable,
        latest_shift=latest_shift,
        sort_created_at_asc=sort_created_at_asc,
        breaks_with_time_configuration=breaks_with_time_configuration,
        last_working_shift=last_working_shift,
        updated_at=updated_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    half_day: bool,
    workable: bool | Unset = UNSET,
    latest_shift: bool | Unset = UNSET,
    sort_created_at_asc: bool,
    breaks_with_time_configuration: bool | Unset = UNSET,
    last_working_shift: bool | Unset = UNSET,
    updated_at: str | Unset = UNSET,
) -> GetApi20260701ResourcesAttendanceShiftsResponse200 | None:
    """Reads all Shifts

     Reads all Shifts

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        start_on (str | Unset): filter by shift that starts after or including this date. Example:
            2023-09-30.
        end_on (str | Unset): filter by shift that ends before or including this date. Example:
            2023-10-01.
        ids (list[str] | Unset): filter by ids. Example: ['1', '2', '3'].
        half_day (bool): Flag to filter half day shifts
        workable (bool | Unset): Flag to filter shifts in workable days Example: True.
        latest_shift (bool | Unset): Flag to filter only the latest shift for each employee
            Example: True.
        sort_created_at_asc (bool): Flag to sort by created_at asc Example: True.
        breaks_with_time_configuration (bool | Unset): Flag to include breaks with time
            configuration Example: True.
        last_working_shift (bool | Unset): Filter by last working shift Example: True.
        updated_at (str | Unset): Filter shifts by the date they were last updated Example:
            2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAttendanceShiftsResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        ids=ids,
        half_day=half_day,
        workable=workable,
        latest_shift=latest_shift,
        sort_created_at_asc=sort_created_at_asc,
        breaks_with_time_configuration=breaks_with_time_configuration,
        last_working_shift=last_working_shift,
        updated_at=updated_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    half_day: bool,
    workable: bool | Unset = UNSET,
    latest_shift: bool | Unset = UNSET,
    sort_created_at_asc: bool,
    breaks_with_time_configuration: bool | Unset = UNSET,
    last_working_shift: bool | Unset = UNSET,
    updated_at: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesAttendanceShiftsResponse200]:
    """Reads all Shifts

     Reads all Shifts

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        start_on (str | Unset): filter by shift that starts after or including this date. Example:
            2023-09-30.
        end_on (str | Unset): filter by shift that ends before or including this date. Example:
            2023-10-01.
        ids (list[str] | Unset): filter by ids. Example: ['1', '2', '3'].
        half_day (bool): Flag to filter half day shifts
        workable (bool | Unset): Flag to filter shifts in workable days Example: True.
        latest_shift (bool | Unset): Flag to filter only the latest shift for each employee
            Example: True.
        sort_created_at_asc (bool): Flag to sort by created_at asc Example: True.
        breaks_with_time_configuration (bool | Unset): Flag to include breaks with time
            configuration Example: True.
        last_working_shift (bool | Unset): Filter by last working shift Example: True.
        updated_at (str | Unset): Filter shifts by the date they were last updated Example:
            2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAttendanceShiftsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        ids=ids,
        half_day=half_day,
        workable=workable,
        latest_shift=latest_shift,
        sort_created_at_asc=sort_created_at_asc,
        breaks_with_time_configuration=breaks_with_time_configuration,
        last_working_shift=last_working_shift,
        updated_at=updated_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    half_day: bool,
    workable: bool | Unset = UNSET,
    latest_shift: bool | Unset = UNSET,
    sort_created_at_asc: bool,
    breaks_with_time_configuration: bool | Unset = UNSET,
    last_working_shift: bool | Unset = UNSET,
    updated_at: str | Unset = UNSET,
) -> GetApi20260701ResourcesAttendanceShiftsResponse200 | None:
    """Reads all Shifts

     Reads all Shifts

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        start_on (str | Unset): filter by shift that starts after or including this date. Example:
            2023-09-30.
        end_on (str | Unset): filter by shift that ends before or including this date. Example:
            2023-10-01.
        ids (list[str] | Unset): filter by ids. Example: ['1', '2', '3'].
        half_day (bool): Flag to filter half day shifts
        workable (bool | Unset): Flag to filter shifts in workable days Example: True.
        latest_shift (bool | Unset): Flag to filter only the latest shift for each employee
            Example: True.
        sort_created_at_asc (bool): Flag to sort by created_at asc Example: True.
        breaks_with_time_configuration (bool | Unset): Flag to include breaks with time
            configuration Example: True.
        last_working_shift (bool | Unset): Filter by last working shift Example: True.
        updated_at (str | Unset): Filter shifts by the date they were last updated Example:
            2023-10-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAttendanceShiftsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
            start_on=start_on,
            end_on=end_on,
            ids=ids,
            half_day=half_day,
            workable=workable,
            latest_shift=latest_shift,
            sort_created_at_asc=sort_created_at_asc,
            breaks_with_time_configuration=breaks_with_time_configuration,
            last_working_shift=last_working_shift,
            updated_at=updated_at,
        )
    ).parsed
