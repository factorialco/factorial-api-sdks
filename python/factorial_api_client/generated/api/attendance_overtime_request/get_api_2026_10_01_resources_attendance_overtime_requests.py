from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_attendance_overtime_requests_response_200 import (
    GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200,
)
from ...models.get_api_20261001_resources_attendance_overtime_requests_status import (
    GetApi20261001ResourcesAttendanceOvertimeRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    status: GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
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
        "url": "/api/2026-10-01/resources/attendance/overtime_requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200]:
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
    status: GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> Response[GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200]:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset):
        employee_ids (list[str] | Unset):
        start_on (str | Unset):
        end_on (str | Unset):
        status (GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset):
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200]
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
    status: GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200 | None:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset):
        employee_ids (list[str] | Unset):
        start_on (str | Unset):
        end_on (str | Unset):
        status (GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset):
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200
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
    status: GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> Response[GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200]:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset):
        employee_ids (list[str] | Unset):
        start_on (str | Unset):
        end_on (str | Unset):
        status (GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset):
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200]
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
    status: GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset = UNSET,
    include_approval_flow: bool,
) -> GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200 | None:
    """Reads all Overtime requests

     Reads all Overtime requests

    Args:
        ids (list[str] | Unset):
        employee_ids (list[str] | Unset):
        start_on (str | Unset):
        end_on (str | Unset):
        status (GetApi20261001ResourcesAttendanceOvertimeRequestsStatus | Unset):
        include_approval_flow (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceOvertimeRequestsResponse200
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
