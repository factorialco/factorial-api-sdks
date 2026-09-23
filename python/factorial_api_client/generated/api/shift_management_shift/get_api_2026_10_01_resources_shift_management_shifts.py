from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_shift_management_shifts_only_states import (
    GetApi20261001ResourcesShiftManagementShiftsOnlyStates,
)
from ...models.get_api_20261001_resources_shift_management_shifts_response_200 import (
    GetApi20261001ResourcesShiftManagementShiftsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    without_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_without_ids: list[str] | Unset = UNSET
    if not isinstance(without_ids, Unset):
        json_without_ids = without_ids

    params["without_ids[]"] = json_without_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["location_ids[]"] = json_location_ids

    params["start_at"] = start_at

    params["end_at"] = end_at

    params["only_published"] = only_published

    json_only_states: str | Unset = UNSET
    if not isinstance(only_states, Unset):
        json_only_states = only_states.value

    params["only_states[]"] = json_only_states

    params["split_overnight_shifts"] = split_overnight_shifts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/shift_management/shifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesShiftManagementShiftsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesShiftManagementShiftsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesShiftManagementShiftsResponse200]:
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
    without_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesShiftManagementShiftsResponse200]:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[str] | Unset): Filter shifts by their unique identifiers. Returns only shifts
            matching the provided IDs. If an empty array is provided, returns no results Example:
            ['1'].
        without_ids (list[str] | Unset): Exclude shifts with these identifiers from the results.
            Useful for filtering out specific shifts while keeping others Example: ['3'].
        employee_ids (list[str] | Unset): Filter shifts by employee identifiers. Returns only
            shifts assigned to the specified employees. If not provided, returns shifts for all
            accessible employees Example: ['1'].
        location_ids (list[str] | Unset): Filter shifts by location identifiers. Returns shifts
            that occur at the specified locations. Can be combined with employee_ids for more precise
            filtering Example: ['3'].
        start_at (str | Unset): Filter shifts that end on or after this date. Only the date
            (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00).
            Shifts are included if their end time is at or after the start of the specified day
            Example: 2020-01-01.
        end_at (str | Unset): Filter shifts that start before this date. Only the date (calendar
            day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are
            included if their start time is before the end of the specified day Example: 2020-12-31.
        only_published (bool | Unset): When true, returns only shifts with state 'published'
            (visible to employees). When false, returns shifts in all states (draft, published,
            backup) based on your permissions
        only_states (GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset): Filter
            shifts by their state. Provide an array of states ('draft', 'published', 'backup') to
            include. Can be combined with other filters for precise control Example: ['draft',
            'published'].
        split_overnight_shifts (bool | Unset): When true, shifts that span across midnight
            (overnight shifts) are split into two separate shift objects - one for each calendar day.
            This makes it easier to display shifts in day-based views

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesShiftManagementShiftsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        without_ids=without_ids,
        employee_ids=employee_ids,
        location_ids=location_ids,
        start_at=start_at,
        end_at=end_at,
        only_published=only_published,
        only_states=only_states,
        split_overnight_shifts=split_overnight_shifts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    without_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> GetApi20261001ResourcesShiftManagementShiftsResponse200 | None:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[str] | Unset): Filter shifts by their unique identifiers. Returns only shifts
            matching the provided IDs. If an empty array is provided, returns no results Example:
            ['1'].
        without_ids (list[str] | Unset): Exclude shifts with these identifiers from the results.
            Useful for filtering out specific shifts while keeping others Example: ['3'].
        employee_ids (list[str] | Unset): Filter shifts by employee identifiers. Returns only
            shifts assigned to the specified employees. If not provided, returns shifts for all
            accessible employees Example: ['1'].
        location_ids (list[str] | Unset): Filter shifts by location identifiers. Returns shifts
            that occur at the specified locations. Can be combined with employee_ids for more precise
            filtering Example: ['3'].
        start_at (str | Unset): Filter shifts that end on or after this date. Only the date
            (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00).
            Shifts are included if their end time is at or after the start of the specified day
            Example: 2020-01-01.
        end_at (str | Unset): Filter shifts that start before this date. Only the date (calendar
            day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are
            included if their start time is before the end of the specified day Example: 2020-12-31.
        only_published (bool | Unset): When true, returns only shifts with state 'published'
            (visible to employees). When false, returns shifts in all states (draft, published,
            backup) based on your permissions
        only_states (GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset): Filter
            shifts by their state. Provide an array of states ('draft', 'published', 'backup') to
            include. Can be combined with other filters for precise control Example: ['draft',
            'published'].
        split_overnight_shifts (bool | Unset): When true, shifts that span across midnight
            (overnight shifts) are split into two separate shift objects - one for each calendar day.
            This makes it easier to display shifts in day-based views

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesShiftManagementShiftsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        without_ids=without_ids,
        employee_ids=employee_ids,
        location_ids=location_ids,
        start_at=start_at,
        end_at=end_at,
        only_published=only_published,
        only_states=only_states,
        split_overnight_shifts=split_overnight_shifts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    without_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesShiftManagementShiftsResponse200]:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[str] | Unset): Filter shifts by their unique identifiers. Returns only shifts
            matching the provided IDs. If an empty array is provided, returns no results Example:
            ['1'].
        without_ids (list[str] | Unset): Exclude shifts with these identifiers from the results.
            Useful for filtering out specific shifts while keeping others Example: ['3'].
        employee_ids (list[str] | Unset): Filter shifts by employee identifiers. Returns only
            shifts assigned to the specified employees. If not provided, returns shifts for all
            accessible employees Example: ['1'].
        location_ids (list[str] | Unset): Filter shifts by location identifiers. Returns shifts
            that occur at the specified locations. Can be combined with employee_ids for more precise
            filtering Example: ['3'].
        start_at (str | Unset): Filter shifts that end on or after this date. Only the date
            (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00).
            Shifts are included if their end time is at or after the start of the specified day
            Example: 2020-01-01.
        end_at (str | Unset): Filter shifts that start before this date. Only the date (calendar
            day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are
            included if their start time is before the end of the specified day Example: 2020-12-31.
        only_published (bool | Unset): When true, returns only shifts with state 'published'
            (visible to employees). When false, returns shifts in all states (draft, published,
            backup) based on your permissions
        only_states (GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset): Filter
            shifts by their state. Provide an array of states ('draft', 'published', 'backup') to
            include. Can be combined with other filters for precise control Example: ['draft',
            'published'].
        split_overnight_shifts (bool | Unset): When true, shifts that span across midnight
            (overnight shifts) are split into two separate shift objects - one for each calendar day.
            This makes it easier to display shifts in day-based views

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesShiftManagementShiftsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        without_ids=without_ids,
        employee_ids=employee_ids,
        location_ids=location_ids,
        start_at=start_at,
        end_at=end_at,
        only_published=only_published,
        only_states=only_states,
        split_overnight_shifts=split_overnight_shifts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    without_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> GetApi20261001ResourcesShiftManagementShiftsResponse200 | None:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[str] | Unset): Filter shifts by their unique identifiers. Returns only shifts
            matching the provided IDs. If an empty array is provided, returns no results Example:
            ['1'].
        without_ids (list[str] | Unset): Exclude shifts with these identifiers from the results.
            Useful for filtering out specific shifts while keeping others Example: ['3'].
        employee_ids (list[str] | Unset): Filter shifts by employee identifiers. Returns only
            shifts assigned to the specified employees. If not provided, returns shifts for all
            accessible employees Example: ['1'].
        location_ids (list[str] | Unset): Filter shifts by location identifiers. Returns shifts
            that occur at the specified locations. Can be combined with employee_ids for more precise
            filtering Example: ['3'].
        start_at (str | Unset): Filter shifts that end on or after this date. Only the date
            (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00).
            Shifts are included if their end time is at or after the start of the specified day
            Example: 2020-01-01.
        end_at (str | Unset): Filter shifts that start before this date. Only the date (calendar
            day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are
            included if their start time is before the end of the specified day Example: 2020-12-31.
        only_published (bool | Unset): When true, returns only shifts with state 'published'
            (visible to employees). When false, returns shifts in all states (draft, published,
            backup) based on your permissions
        only_states (GetApi20261001ResourcesShiftManagementShiftsOnlyStates | Unset): Filter
            shifts by their state. Provide an array of states ('draft', 'published', 'backup') to
            include. Can be combined with other filters for precise control Example: ['draft',
            'published'].
        split_overnight_shifts (bool | Unset): When true, shifts that span across midnight
            (overnight shifts) are split into two separate shift objects - one for each calendar day.
            This makes it easier to display shifts in day-based views

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesShiftManagementShiftsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            without_ids=without_ids,
            employee_ids=employee_ids,
            location_ids=location_ids,
            start_at=start_at,
            end_at=end_at,
            only_published=only_published,
            only_states=only_states,
            split_overnight_shifts=split_overnight_shifts,
        )
    ).parsed
