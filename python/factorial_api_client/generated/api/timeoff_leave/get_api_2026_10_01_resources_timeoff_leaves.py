from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_timeoff_leaves_response_200 import (
    GetApi20261001ResourcesTimeoffLeavesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    leave_type_id: list[str] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    include_duration_by_day: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
    forced_finish_on: str | Unset = UNSET,
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

    json_leave_type_id: list[str] | Unset = UNSET
    if not isinstance(leave_type_id, Unset):
        json_leave_type_id = leave_type_id

    params["leave_type_id[]"] = json_leave_type_id

    params["to"] = to

    params["from"] = from_

    params["only_active"] = only_active

    params["include_deleted_leaves"] = include_deleted_leaves

    params["approved"] = approved

    params["include_pending"] = include_pending

    params["include_leave_type"] = include_leave_type

    params["include_duration"] = include_duration

    params["include_duration_by_day"] = include_duration_by_day

    params["type_is_workable"] = type_is_workable

    params["type_is_payable"] = type_is_payable

    params["forced_finish_on"] = forced_finish_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/timeoff/leaves",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesTimeoffLeavesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesTimeoffLeavesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesTimeoffLeavesResponse200]:
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
    leave_type_id: list[str] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    include_duration_by_day: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
    forced_finish_on: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTimeoffLeavesResponse200]:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[str] | Unset): The leave ids to retrieve Example: ['1'].
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        leave_type_id (list[str] | Unset): The leave type id to retrieve Example: ['36'].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        include_duration_by_day (bool | Unset): Retrieve the per-day breakdown of the leave's
            duration (`duration_by_day_attributes`)
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves
        forced_finish_on (str | Unset): Caps the per-day duration walk at this date. For endless
            leaves (`finish_on = nil`) it pins the walk end; for closed leaves whose `finish_on` sits
            past this date it truncates the walk. Never extends a leave past its real `finish_on`.
            Must fall inside the read window (from/to or overlaps_range_from/overlaps_range_to).
            Example: 2028-09-30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTimeoffLeavesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        leave_type_id=leave_type_id,
        to=to,
        from_=from_,
        only_active=only_active,
        include_deleted_leaves=include_deleted_leaves,
        approved=approved,
        include_pending=include_pending,
        include_leave_type=include_leave_type,
        include_duration=include_duration,
        include_duration_by_day=include_duration_by_day,
        type_is_workable=type_is_workable,
        type_is_payable=type_is_payable,
        forced_finish_on=forced_finish_on,
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
    leave_type_id: list[str] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    include_duration_by_day: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
    forced_finish_on: str | Unset = UNSET,
) -> GetApi20261001ResourcesTimeoffLeavesResponse200 | None:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[str] | Unset): The leave ids to retrieve Example: ['1'].
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        leave_type_id (list[str] | Unset): The leave type id to retrieve Example: ['36'].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        include_duration_by_day (bool | Unset): Retrieve the per-day breakdown of the leave's
            duration (`duration_by_day_attributes`)
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves
        forced_finish_on (str | Unset): Caps the per-day duration walk at this date. For endless
            leaves (`finish_on = nil`) it pins the walk end; for closed leaves whose `finish_on` sits
            past this date it truncates the walk. Never extends a leave past its real `finish_on`.
            Must fall inside the read window (from/to or overlaps_range_from/overlaps_range_to).
            Example: 2028-09-30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTimeoffLeavesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        leave_type_id=leave_type_id,
        to=to,
        from_=from_,
        only_active=only_active,
        include_deleted_leaves=include_deleted_leaves,
        approved=approved,
        include_pending=include_pending,
        include_leave_type=include_leave_type,
        include_duration=include_duration,
        include_duration_by_day=include_duration_by_day,
        type_is_workable=type_is_workable,
        type_is_payable=type_is_payable,
        forced_finish_on=forced_finish_on,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    leave_type_id: list[str] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    include_duration_by_day: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
    forced_finish_on: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTimeoffLeavesResponse200]:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[str] | Unset): The leave ids to retrieve Example: ['1'].
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        leave_type_id (list[str] | Unset): The leave type id to retrieve Example: ['36'].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        include_duration_by_day (bool | Unset): Retrieve the per-day breakdown of the leave's
            duration (`duration_by_day_attributes`)
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves
        forced_finish_on (str | Unset): Caps the per-day duration walk at this date. For endless
            leaves (`finish_on = nil`) it pins the walk end; for closed leaves whose `finish_on` sits
            past this date it truncates the walk. Never extends a leave past its real `finish_on`.
            Must fall inside the read window (from/to or overlaps_range_from/overlaps_range_to).
            Example: 2028-09-30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTimeoffLeavesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        leave_type_id=leave_type_id,
        to=to,
        from_=from_,
        only_active=only_active,
        include_deleted_leaves=include_deleted_leaves,
        approved=approved,
        include_pending=include_pending,
        include_leave_type=include_leave_type,
        include_duration=include_duration,
        include_duration_by_day=include_duration_by_day,
        type_is_workable=type_is_workable,
        type_is_payable=type_is_payable,
        forced_finish_on=forced_finish_on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    leave_type_id: list[str] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    include_duration_by_day: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
    forced_finish_on: str | Unset = UNSET,
) -> GetApi20261001ResourcesTimeoffLeavesResponse200 | None:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[str] | Unset): The leave ids to retrieve Example: ['1'].
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        leave_type_id (list[str] | Unset): The leave type id to retrieve Example: ['36'].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        include_duration_by_day (bool | Unset): Retrieve the per-day breakdown of the leave's
            duration (`duration_by_day_attributes`)
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves
        forced_finish_on (str | Unset): Caps the per-day duration walk at this date. For endless
            leaves (`finish_on = nil`) it pins the walk end; for closed leaves whose `finish_on` sits
            past this date it truncates the walk. Never extends a leave past its real `finish_on`.
            Must fall inside the read window (from/to or overlaps_range_from/overlaps_range_to).
            Example: 2028-09-30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTimeoffLeavesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            leave_type_id=leave_type_id,
            to=to,
            from_=from_,
            only_active=only_active,
            include_deleted_leaves=include_deleted_leaves,
            approved=approved,
            include_pending=include_pending,
            include_leave_type=include_leave_type,
            include_duration=include_duration,
            include_duration_by_day=include_duration_by_day,
            type_is_workable=type_is_workable,
            type_is_payable=type_is_payable,
            forced_finish_on=forced_finish_on,
        )
    ).parsed
