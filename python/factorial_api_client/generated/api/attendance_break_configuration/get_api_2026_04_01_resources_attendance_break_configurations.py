from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_attendance_break_configurations_response_200 import (
    GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    time_settings_break_configuration_ids: list[int] | Unset = UNSET,
    attendance_employees_setting_id: int | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_time_settings_break_configuration_ids: list[int] | Unset = UNSET
    if not isinstance(time_settings_break_configuration_ids, Unset):
        json_time_settings_break_configuration_ids = time_settings_break_configuration_ids

    params["time_settings_break_configuration_ids[]"] = json_time_settings_break_configuration_ids

    params["attendance_employees_setting_id"] = attendance_employees_setting_id

    params["enabled"] = enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/attendance/break_configurations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200]:
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
    time_settings_break_configuration_ids: list[int] | Unset = UNSET,
    attendance_employees_setting_id: int | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200]:
    """Reads all Break configurations

     Reads all Break configurations

    Args:
        ids (list[int] | Unset): The break configuration ids to retrieve Example: [1].
        time_settings_break_configuration_ids (list[int] | Unset): Ids of the time settings break
            configuration Example: [1].
        attendance_employees_setting_id (int | Unset): Id of the attendance employee setting
            Example: 1.
        enabled (bool | Unset): Status of the break configuration if enabled or not

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        time_settings_break_configuration_ids=time_settings_break_configuration_ids,
        attendance_employees_setting_id=attendance_employees_setting_id,
        enabled=enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    time_settings_break_configuration_ids: list[int] | Unset = UNSET,
    attendance_employees_setting_id: int | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200 | None:
    """Reads all Break configurations

     Reads all Break configurations

    Args:
        ids (list[int] | Unset): The break configuration ids to retrieve Example: [1].
        time_settings_break_configuration_ids (list[int] | Unset): Ids of the time settings break
            configuration Example: [1].
        attendance_employees_setting_id (int | Unset): Id of the attendance employee setting
            Example: 1.
        enabled (bool | Unset): Status of the break configuration if enabled or not

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        time_settings_break_configuration_ids=time_settings_break_configuration_ids,
        attendance_employees_setting_id=attendance_employees_setting_id,
        enabled=enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    time_settings_break_configuration_ids: list[int] | Unset = UNSET,
    attendance_employees_setting_id: int | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200]:
    """Reads all Break configurations

     Reads all Break configurations

    Args:
        ids (list[int] | Unset): The break configuration ids to retrieve Example: [1].
        time_settings_break_configuration_ids (list[int] | Unset): Ids of the time settings break
            configuration Example: [1].
        attendance_employees_setting_id (int | Unset): Id of the attendance employee setting
            Example: 1.
        enabled (bool | Unset): Status of the break configuration if enabled or not

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        time_settings_break_configuration_ids=time_settings_break_configuration_ids,
        attendance_employees_setting_id=attendance_employees_setting_id,
        enabled=enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    time_settings_break_configuration_ids: list[int] | Unset = UNSET,
    attendance_employees_setting_id: int | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200 | None:
    """Reads all Break configurations

     Reads all Break configurations

    Args:
        ids (list[int] | Unset): The break configuration ids to retrieve Example: [1].
        time_settings_break_configuration_ids (list[int] | Unset): Ids of the time settings break
            configuration Example: [1].
        attendance_employees_setting_id (int | Unset): Id of the attendance employee setting
            Example: 1.
        enabled (bool | Unset): Status of the break configuration if enabled or not

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesAttendanceBreakConfigurationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            time_settings_break_configuration_ids=time_settings_break_configuration_ids,
            attendance_employees_setting_id=attendance_employees_setting_id,
            enabled=enabled,
        )
    ).parsed
