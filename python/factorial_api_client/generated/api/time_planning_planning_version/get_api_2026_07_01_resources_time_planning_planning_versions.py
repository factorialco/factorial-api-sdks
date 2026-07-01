from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_time_planning_planning_versions_planning_tool import (
    GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool,
)
from ...models.get_api_20260701_resources_time_planning_planning_versions_response_200 import (
    GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employee_ids: list[str] | Unset = UNSET,
    for_shifts: bool | Unset = UNSET,
    only_active: bool,
    planning_tool: GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset = UNSET,
    schedule_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["for_shifts"] = for_shifts

    params["only_active"] = only_active

    json_planning_tool: str | Unset = UNSET
    if not isinstance(planning_tool, Unset):
        json_planning_tool = planning_tool.value

    params["planning_tool"] = json_planning_tool

    json_schedule_ids: list[str] | Unset = UNSET
    if not isinstance(schedule_ids, Unset):
        json_schedule_ids = schedule_ids

    params["schedule_ids[]"] = json_schedule_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/time_planning/planning_versions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200]:
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
    for_shifts: bool | Unset = UNSET,
    only_active: bool,
    planning_tool: GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset = UNSET,
    schedule_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200]:
    """Reads all Planning versions

     Reads all Planning versions

    Args:
        employee_ids (list[str] | Unset): List of employee identifiers Example: ['1', '2', '3'].
        for_shifts (bool | Unset): Filter by shift management planning tool Example: True.
        only_active (bool): Filter by active planning versions only
        planning_tool (GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset):
            Type of planning tool (shift_management, work_schedules, contract_hours) Example:
            shift_management.
        schedule_ids (list[str] | Unset): List of work schedule identifiers to include Example:
            ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        for_shifts=for_shifts,
        only_active=only_active,
        planning_tool=planning_tool,
        schedule_ids=schedule_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    for_shifts: bool | Unset = UNSET,
    only_active: bool,
    planning_tool: GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset = UNSET,
    schedule_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200 | None:
    """Reads all Planning versions

     Reads all Planning versions

    Args:
        employee_ids (list[str] | Unset): List of employee identifiers Example: ['1', '2', '3'].
        for_shifts (bool | Unset): Filter by shift management planning tool Example: True.
        only_active (bool): Filter by active planning versions only
        planning_tool (GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset):
            Type of planning tool (shift_management, work_schedules, contract_hours) Example:
            shift_management.
        schedule_ids (list[str] | Unset): List of work schedule identifiers to include Example:
            ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
        for_shifts=for_shifts,
        only_active=only_active,
        planning_tool=planning_tool,
        schedule_ids=schedule_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    for_shifts: bool | Unset = UNSET,
    only_active: bool,
    planning_tool: GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset = UNSET,
    schedule_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200]:
    """Reads all Planning versions

     Reads all Planning versions

    Args:
        employee_ids (list[str] | Unset): List of employee identifiers Example: ['1', '2', '3'].
        for_shifts (bool | Unset): Filter by shift management planning tool Example: True.
        only_active (bool): Filter by active planning versions only
        planning_tool (GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset):
            Type of planning tool (shift_management, work_schedules, contract_hours) Example:
            shift_management.
        schedule_ids (list[str] | Unset): List of work schedule identifiers to include Example:
            ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        for_shifts=for_shifts,
        only_active=only_active,
        planning_tool=planning_tool,
        schedule_ids=schedule_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    for_shifts: bool | Unset = UNSET,
    only_active: bool,
    planning_tool: GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset = UNSET,
    schedule_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200 | None:
    """Reads all Planning versions

     Reads all Planning versions

    Args:
        employee_ids (list[str] | Unset): List of employee identifiers Example: ['1', '2', '3'].
        for_shifts (bool | Unset): Filter by shift management planning tool Example: True.
        only_active (bool): Filter by active planning versions only
        planning_tool (GetApi20260701ResourcesTimePlanningPlanningVersionsPlanningTool | Unset):
            Type of planning tool (shift_management, work_schedules, contract_hours) Example:
            shift_management.
        schedule_ids (list[str] | Unset): List of work schedule identifiers to include Example:
            ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTimePlanningPlanningVersionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
            for_shifts=for_shifts,
            only_active=only_active,
            planning_tool=planning_tool,
            schedule_ids=schedule_ids,
        )
    ).parsed
