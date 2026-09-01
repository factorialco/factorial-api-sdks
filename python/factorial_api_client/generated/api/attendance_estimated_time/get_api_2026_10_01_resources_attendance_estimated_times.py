from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_attendance_estimated_times_response_200 import (
    GetApi20261001ResourcesAttendanceEstimatedTimesResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start_on: str,
    end_on: str,
    employee_ids: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start_on"] = start_on

    params["end_on"] = end_on

    json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/attendance/estimated_times",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesAttendanceEstimatedTimesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesAttendanceEstimatedTimesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesAttendanceEstimatedTimesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_on: str,
    end_on: str,
    employee_ids: list[str],
) -> Response[GetApi20261001ResourcesAttendanceEstimatedTimesResponse200]:
    """Reads all Estimated times

     Get information about estimated data for a given date range and a bunch of employees.

    Args:
        start_on (str):
        end_on (str):
        employee_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceEstimatedTimesResponse200]
    """

    kwargs = _get_kwargs(
        start_on=start_on,
        end_on=end_on,
        employee_ids=employee_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_on: str,
    end_on: str,
    employee_ids: list[str],
) -> GetApi20261001ResourcesAttendanceEstimatedTimesResponse200 | None:
    """Reads all Estimated times

     Get information about estimated data for a given date range and a bunch of employees.

    Args:
        start_on (str):
        end_on (str):
        employee_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceEstimatedTimesResponse200
    """

    return sync_detailed(
        client=client,
        start_on=start_on,
        end_on=end_on,
        employee_ids=employee_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_on: str,
    end_on: str,
    employee_ids: list[str],
) -> Response[GetApi20261001ResourcesAttendanceEstimatedTimesResponse200]:
    """Reads all Estimated times

     Get information about estimated data for a given date range and a bunch of employees.

    Args:
        start_on (str):
        end_on (str):
        employee_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceEstimatedTimesResponse200]
    """

    kwargs = _get_kwargs(
        start_on=start_on,
        end_on=end_on,
        employee_ids=employee_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_on: str,
    end_on: str,
    employee_ids: list[str],
) -> GetApi20261001ResourcesAttendanceEstimatedTimesResponse200 | None:
    """Reads all Estimated times

     Get information about estimated data for a given date range and a bunch of employees.

    Args:
        start_on (str):
        end_on (str):
        employee_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceEstimatedTimesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            start_on=start_on,
            end_on=end_on,
            employee_ids=employee_ids,
        )
    ).parsed
