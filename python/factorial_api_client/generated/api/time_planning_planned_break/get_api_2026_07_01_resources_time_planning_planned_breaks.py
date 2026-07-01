from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_time_planning_planned_breaks_response_200 import (
    GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ids: list[str],
    paid: bool,
    default_shift_ids: list[str],
    shift_ids: list[str],
    day_configuration_ids: list[str],
    shift_configuration_ids: list[str],
    active_break_configuration: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids[]"] = json_ids

    params["paid"] = paid

    json_default_shift_ids = default_shift_ids

    params["default_shift_ids[]"] = json_default_shift_ids

    json_shift_ids = shift_ids

    params["shift_ids[]"] = json_shift_ids

    json_day_configuration_ids = day_configuration_ids

    params["day_configuration_ids[]"] = json_day_configuration_ids

    json_shift_configuration_ids = shift_configuration_ids

    params["shift_configuration_ids[]"] = json_shift_configuration_ids

    params["active_break_configuration"] = active_break_configuration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/time_planning/planned_breaks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    paid: bool,
    default_shift_ids: list[str],
    shift_ids: list[str],
    day_configuration_ids: list[str],
    shift_configuration_ids: list[str],
    active_break_configuration: bool,
) -> Response[GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200]:
    """Reads all Planned breaks

     Reads all Planned breaks

    Args:
        ids (list[str]): List of planned break identifiers
        paid (bool): Filter by paid or unpaid breaks
        default_shift_ids (list[str]): List of default shift identifiers
        shift_ids (list[str]): List of shift identifiers
        day_configuration_ids (list[str]): List of day configuration identifiers
        shift_configuration_ids (list[str]): List of shift configuration identifiers
        active_break_configuration (bool): Filter by active break configurations only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        paid=paid,
        default_shift_ids=default_shift_ids,
        shift_ids=shift_ids,
        day_configuration_ids=day_configuration_ids,
        shift_configuration_ids=shift_configuration_ids,
        active_break_configuration=active_break_configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    paid: bool,
    default_shift_ids: list[str],
    shift_ids: list[str],
    day_configuration_ids: list[str],
    shift_configuration_ids: list[str],
    active_break_configuration: bool,
) -> GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200 | None:
    """Reads all Planned breaks

     Reads all Planned breaks

    Args:
        ids (list[str]): List of planned break identifiers
        paid (bool): Filter by paid or unpaid breaks
        default_shift_ids (list[str]): List of default shift identifiers
        shift_ids (list[str]): List of shift identifiers
        day_configuration_ids (list[str]): List of day configuration identifiers
        shift_configuration_ids (list[str]): List of shift configuration identifiers
        active_break_configuration (bool): Filter by active break configurations only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        paid=paid,
        default_shift_ids=default_shift_ids,
        shift_ids=shift_ids,
        day_configuration_ids=day_configuration_ids,
        shift_configuration_ids=shift_configuration_ids,
        active_break_configuration=active_break_configuration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    paid: bool,
    default_shift_ids: list[str],
    shift_ids: list[str],
    day_configuration_ids: list[str],
    shift_configuration_ids: list[str],
    active_break_configuration: bool,
) -> Response[GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200]:
    """Reads all Planned breaks

     Reads all Planned breaks

    Args:
        ids (list[str]): List of planned break identifiers
        paid (bool): Filter by paid or unpaid breaks
        default_shift_ids (list[str]): List of default shift identifiers
        shift_ids (list[str]): List of shift identifiers
        day_configuration_ids (list[str]): List of day configuration identifiers
        shift_configuration_ids (list[str]): List of shift configuration identifiers
        active_break_configuration (bool): Filter by active break configurations only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        paid=paid,
        default_shift_ids=default_shift_ids,
        shift_ids=shift_ids,
        day_configuration_ids=day_configuration_ids,
        shift_configuration_ids=shift_configuration_ids,
        active_break_configuration=active_break_configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    paid: bool,
    default_shift_ids: list[str],
    shift_ids: list[str],
    day_configuration_ids: list[str],
    shift_configuration_ids: list[str],
    active_break_configuration: bool,
) -> GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200 | None:
    """Reads all Planned breaks

     Reads all Planned breaks

    Args:
        ids (list[str]): List of planned break identifiers
        paid (bool): Filter by paid or unpaid breaks
        default_shift_ids (list[str]): List of default shift identifiers
        shift_ids (list[str]): List of shift identifiers
        day_configuration_ids (list[str]): List of day configuration identifiers
        shift_configuration_ids (list[str]): List of shift configuration identifiers
        active_break_configuration (bool): Filter by active break configurations only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTimePlanningPlannedBreaksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            paid=paid,
            default_shift_ids=default_shift_ids,
            shift_ids=shift_ids,
            day_configuration_ids=day_configuration_ids,
            shift_configuration_ids=shift_configuration_ids,
            active_break_configuration=active_break_configuration,
        )
    ).parsed
