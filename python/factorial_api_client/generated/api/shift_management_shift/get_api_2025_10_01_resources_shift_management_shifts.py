from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_shift_management_shifts_only_states import (
    GetApi20251001ResourcesShiftManagementShiftsOnlyStates,
)
from ...models.get_api_20251001_resources_shift_management_shifts_response_200 import (
    GetApi20251001ResourcesShiftManagementShiftsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    without_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_without_ids: list[int] | Unset = UNSET
    if not isinstance(without_ids, Unset):
        json_without_ids = without_ids

    params["without_ids[]"] = json_without_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_location_ids: list[int] | Unset = UNSET
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
        "url": "/api/2025-10-01/resources/shift_management/shifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesShiftManagementShiftsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesShiftManagementShiftsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesShiftManagementShiftsResponse200]:
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
    without_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> Response[GetApi20251001ResourcesShiftManagementShiftsResponse200]:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[int] | Unset): List of shift identifiers Example: [1].
        without_ids (list[int] | Unset): List of shift identifiers to exclude Example: [3].
        employee_ids (list[int] | Unset): List of employee identifiers Example: [1].
        location_ids (list[int] | Unset): List of location identifiers Example: [3].
        start_at (str | Unset): Start date to find shifts from Example: 2020-01-01.
        end_at (str | Unset): End date to find shifts to Example: 2020-12-31.
        only_published (bool | Unset): To retrieve only published shifts
        only_states (GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset): List of
            states to filter by Example: ['draft', 'published'].
        split_overnight_shifts (bool | Unset): Whether to split overnight shifts into two shifts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesShiftManagementShiftsResponse200]
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
    ids: list[int] | Unset = UNSET,
    without_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> GetApi20251001ResourcesShiftManagementShiftsResponse200 | None:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[int] | Unset): List of shift identifiers Example: [1].
        without_ids (list[int] | Unset): List of shift identifiers to exclude Example: [3].
        employee_ids (list[int] | Unset): List of employee identifiers Example: [1].
        location_ids (list[int] | Unset): List of location identifiers Example: [3].
        start_at (str | Unset): Start date to find shifts from Example: 2020-01-01.
        end_at (str | Unset): End date to find shifts to Example: 2020-12-31.
        only_published (bool | Unset): To retrieve only published shifts
        only_states (GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset): List of
            states to filter by Example: ['draft', 'published'].
        split_overnight_shifts (bool | Unset): Whether to split overnight shifts into two shifts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesShiftManagementShiftsResponse200
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
    ids: list[int] | Unset = UNSET,
    without_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> Response[GetApi20251001ResourcesShiftManagementShiftsResponse200]:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[int] | Unset): List of shift identifiers Example: [1].
        without_ids (list[int] | Unset): List of shift identifiers to exclude Example: [3].
        employee_ids (list[int] | Unset): List of employee identifiers Example: [1].
        location_ids (list[int] | Unset): List of location identifiers Example: [3].
        start_at (str | Unset): Start date to find shifts from Example: 2020-01-01.
        end_at (str | Unset): End date to find shifts to Example: 2020-12-31.
        only_published (bool | Unset): To retrieve only published shifts
        only_states (GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset): List of
            states to filter by Example: ['draft', 'published'].
        split_overnight_shifts (bool | Unset): Whether to split overnight shifts into two shifts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesShiftManagementShiftsResponse200]
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
    ids: list[int] | Unset = UNSET,
    without_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
    only_published: bool | Unset = UNSET,
    only_states: GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset = UNSET,
    split_overnight_shifts: bool | Unset = UNSET,
) -> GetApi20251001ResourcesShiftManagementShiftsResponse200 | None:
    """Reads all Shifts

     Reads all Shifts

    Args:
        ids (list[int] | Unset): List of shift identifiers Example: [1].
        without_ids (list[int] | Unset): List of shift identifiers to exclude Example: [3].
        employee_ids (list[int] | Unset): List of employee identifiers Example: [1].
        location_ids (list[int] | Unset): List of location identifiers Example: [3].
        start_at (str | Unset): Start date to find shifts from Example: 2020-01-01.
        end_at (str | Unset): End date to find shifts to Example: 2020-12-31.
        only_published (bool | Unset): To retrieve only published shifts
        only_states (GetApi20251001ResourcesShiftManagementShiftsOnlyStates | Unset): List of
            states to filter by Example: ['draft', 'published'].
        split_overnight_shifts (bool | Unset): Whether to split overnight shifts into two shifts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesShiftManagementShiftsResponse200
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
