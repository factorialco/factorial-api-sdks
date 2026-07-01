from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attendance_shift import AttendanceShift
from ...models.post_api_20260701_resources_attendance_shifts_clock_out_body import (
    PostApi20260701ResourcesAttendanceShiftsClockOutBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/attendance/shifts/clock_out",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttendanceShift | None:
    if response.status_code == 200:
        response_200 = AttendanceShift.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttendanceShift]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset = UNSET,
) -> Response[AttendanceShift]:
    """Clocks out a shift

     Completes an open shift by setting the current time as the clock-out. This action only applies to
    shifts that were previously started using clock_in. If you need to clock in directly, consider using
    or subscribing to the [clock-in
    endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-
    attendance-shifts-clock-in)

    Args:
        body (PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttendanceShift]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset = UNSET,
) -> AttendanceShift | None:
    """Clocks out a shift

     Completes an open shift by setting the current time as the clock-out. This action only applies to
    shifts that were previously started using clock_in. If you need to clock in directly, consider using
    or subscribing to the [clock-in
    endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-
    attendance-shifts-clock-in)

    Args:
        body (PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttendanceShift
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset = UNSET,
) -> Response[AttendanceShift]:
    """Clocks out a shift

     Completes an open shift by setting the current time as the clock-out. This action only applies to
    shifts that were previously started using clock_in. If you need to clock in directly, consider using
    or subscribing to the [clock-in
    endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-
    attendance-shifts-clock-in)

    Args:
        body (PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttendanceShift]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset = UNSET,
) -> AttendanceShift | None:
    """Clocks out a shift

     Completes an open shift by setting the current time as the clock-out. This action only applies to
    shifts that were previously started using clock_in. If you need to clock in directly, consider using
    or subscribing to the [clock-in
    endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-
    attendance-shifts-clock-in)

    Args:
        body (PostApi20260701ResourcesAttendanceShiftsClockOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttendanceShift
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
