from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_attendance_overtime_requests_response_200 import (
    GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200,
)
from ...models.get_api_20270101_resources_attendance_overtime_requests_status import (
    GetApi20270101ResourcesAttendanceOvertimeRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    status: GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["start_on"] = start_on

    params["end_on"] = end_on

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["include_approval_flow"] = include_approval_flow

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/attendance/overtime_requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200]:
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
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    status: GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200]:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset): Return only the overtime requests with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the overtime requests of these employees.
            Example: ['1'].
        start_on (str | Unset): Return only the requests for an overtime day on or after this
            date. Given without `end_on` it matches that single day. Example: 2024-01-01.
        end_on (str | Unset): Return only the requests for an overtime day on or before this date.
            Given without `start_on` it matches every request up to that day. Example: 2024-01-31.
        status (GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset): Return only the
            requests in this state: `pending` (the state of a newly created request), `approved`,
            `rejected` or `none`. Example: pending.
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        status=status,
        include_approval_flow=include_approval_flow,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    status: GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200 | None:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset): Return only the overtime requests with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the overtime requests of these employees.
            Example: ['1'].
        start_on (str | Unset): Return only the requests for an overtime day on or after this
            date. Given without `end_on` it matches that single day. Example: 2024-01-01.
        end_on (str | Unset): Return only the requests for an overtime day on or before this date.
            Given without `start_on` it matches every request up to that day. Example: 2024-01-31.
        status (GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset): Return only the
            requests in this state: `pending` (the state of a newly created request), `approved`,
            `rejected` or `none`. Example: pending.
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        status=status,
        include_approval_flow=include_approval_flow,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    status: GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200]:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset): Return only the overtime requests with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the overtime requests of these employees.
            Example: ['1'].
        start_on (str | Unset): Return only the requests for an overtime day on or after this
            date. Given without `end_on` it matches that single day. Example: 2024-01-01.
        end_on (str | Unset): Return only the requests for an overtime day on or before this date.
            Given without `start_on` it matches every request up to that day. Example: 2024-01-31.
        status (GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset): Return only the
            requests in this state: `pending` (the state of a newly created request), `approved`,
            `rejected` or `none`. Example: pending.
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        status=status,
        include_approval_flow=include_approval_flow,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    status: GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200 | None:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset): Return only the overtime requests with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the overtime requests of these employees.
            Example: ['1'].
        start_on (str | Unset): Return only the requests for an overtime day on or after this
            date. Given without `end_on` it matches that single day. Example: 2024-01-01.
        end_on (str | Unset): Return only the requests for an overtime day on or before this date.
            Given without `start_on` it matches every request up to that day. Example: 2024-01-31.
        status (GetApi20270101ResourcesAttendanceOvertimeRequestsStatus | Unset): Return only the
            requests in this state: `pending` (the state of a newly created request), `approved`,
            `rejected` or `none`. Example: pending.
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesAttendanceOvertimeRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            start_on=start_on,
            end_on=end_on,
            status=status,
            include_approval_flow=include_approval_flow,
        )
    ).parsed
