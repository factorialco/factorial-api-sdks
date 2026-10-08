from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_attendance_worked_times_response_200 import (
    GetApi20270101ResourcesAttendanceWorkedTimesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    include_time_range_category: bool,
    include_non_attendable_employees: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["start_on"] = start_on

    params["end_on"] = end_on

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["include_time_range_category"] = include_time_range_category

    params["include_non_attendable_employees"] = include_non_attendable_employees

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/attendance/worked_times",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesAttendanceWorkedTimesResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200]:
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
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    include_time_range_category: bool,
    include_non_attendable_employees: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200]:
    """Reads all Worked times

     Reads all Worked times

    Args:
        ids (list[str] | Unset): Composite worked time id combining the employee_id and date,
            formatted as <employee_id>_<YYYY-MM-DD>. Example: ['1_2024-07-01'].
        start_on (str | Unset): Start of the date range to fetch worked times for (inclusive).
            Required together with end_on. Example: 2024-07-01.
        end_on (str | Unset): End of the date range to fetch worked times for (inclusive).
            Required together with start_on. Example: 2024-07-07.
        employee_ids (list[str] | Unset): Employee IDs to filter the date-range query by. When
            omitted, all attendable employees are returned. Example: ['1'].
        include_time_range_category (bool): Whether to include the time range category on each
            worked time block.
        include_non_attendable_employees (bool): Whether to include employees excluded from
            attendance (attendable=false) in the result. Forced to true when filtering by a single
            employee, so their historical worked time is returned even if they are no longer
            attendable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        start_on=start_on,
        end_on=end_on,
        employee_ids=employee_ids,
        include_time_range_category=include_time_range_category,
        include_non_attendable_employees=include_non_attendable_employees,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    include_time_range_category: bool,
    include_non_attendable_employees: bool,
) -> ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200 | None:
    """Reads all Worked times

     Reads all Worked times

    Args:
        ids (list[str] | Unset): Composite worked time id combining the employee_id and date,
            formatted as <employee_id>_<YYYY-MM-DD>. Example: ['1_2024-07-01'].
        start_on (str | Unset): Start of the date range to fetch worked times for (inclusive).
            Required together with end_on. Example: 2024-07-01.
        end_on (str | Unset): End of the date range to fetch worked times for (inclusive).
            Required together with start_on. Example: 2024-07-07.
        employee_ids (list[str] | Unset): Employee IDs to filter the date-range query by. When
            omitted, all attendable employees are returned. Example: ['1'].
        include_time_range_category (bool): Whether to include the time range category on each
            worked time block.
        include_non_attendable_employees (bool): Whether to include employees excluded from
            attendance (attendable=false) in the result. Forced to true when filtering by a single
            employee, so their historical worked time is returned even if they are no longer
            attendable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        start_on=start_on,
        end_on=end_on,
        employee_ids=employee_ids,
        include_time_range_category=include_time_range_category,
        include_non_attendable_employees=include_non_attendable_employees,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    include_time_range_category: bool,
    include_non_attendable_employees: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200]:
    """Reads all Worked times

     Reads all Worked times

    Args:
        ids (list[str] | Unset): Composite worked time id combining the employee_id and date,
            formatted as <employee_id>_<YYYY-MM-DD>. Example: ['1_2024-07-01'].
        start_on (str | Unset): Start of the date range to fetch worked times for (inclusive).
            Required together with end_on. Example: 2024-07-01.
        end_on (str | Unset): End of the date range to fetch worked times for (inclusive).
            Required together with start_on. Example: 2024-07-07.
        employee_ids (list[str] | Unset): Employee IDs to filter the date-range query by. When
            omitted, all attendable employees are returned. Example: ['1'].
        include_time_range_category (bool): Whether to include the time range category on each
            worked time block.
        include_non_attendable_employees (bool): Whether to include employees excluded from
            attendance (attendable=false) in the result. Forced to true when filtering by a single
            employee, so their historical worked time is returned even if they are no longer
            attendable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        start_on=start_on,
        end_on=end_on,
        employee_ids=employee_ids,
        include_time_range_category=include_time_range_category,
        include_non_attendable_employees=include_non_attendable_employees,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    include_time_range_category: bool,
    include_non_attendable_employees: bool,
) -> ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200 | None:
    """Reads all Worked times

     Reads all Worked times

    Args:
        ids (list[str] | Unset): Composite worked time id combining the employee_id and date,
            formatted as <employee_id>_<YYYY-MM-DD>. Example: ['1_2024-07-01'].
        start_on (str | Unset): Start of the date range to fetch worked times for (inclusive).
            Required together with end_on. Example: 2024-07-01.
        end_on (str | Unset): End of the date range to fetch worked times for (inclusive).
            Required together with start_on. Example: 2024-07-07.
        employee_ids (list[str] | Unset): Employee IDs to filter the date-range query by. When
            omitted, all attendable employees are returned. Example: ['1'].
        include_time_range_category (bool): Whether to include the time range category on each
            worked time block.
        include_non_attendable_employees (bool): Whether to include employees excluded from
            attendance (attendable=false) in the result. Forced to true when filtering by a single
            employee, so their historical worked time is returned even if they are no longer
            attendable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesAttendanceWorkedTimesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            start_on=start_on,
            end_on=end_on,
            employee_ids=employee_ids,
            include_time_range_category=include_time_range_category,
            include_non_attendable_employees=include_non_attendable_employees,
        )
    ).parsed
