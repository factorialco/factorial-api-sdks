from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_timeoff_leaves_response_200 import (
    GetApi20260401ResourcesTimeoffLeavesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    leave_type_id: list[int] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_leave_type_id: list[int] | Unset = UNSET
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

    params["type_is_workable"] = type_is_workable

    params["type_is_payable"] = type_is_payable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/timeoff/leaves",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesTimeoffLeavesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesTimeoffLeavesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesTimeoffLeavesResponse200]:
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
    employee_ids: list[int] | Unset = UNSET,
    leave_type_id: list[int] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTimeoffLeavesResponse200]:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[int] | Unset): The leave ids to retrieve Example: [1].
        employee_ids (list[int] | Unset): The employee ids to retrieve Example: [1].
        leave_type_id (list[int] | Unset): The leave type id to retrieve Example: [36].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTimeoffLeavesResponse200]
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
        type_is_workable=type_is_workable,
        type_is_payable=type_is_payable,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    leave_type_id: list[int] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
) -> GetApi20260401ResourcesTimeoffLeavesResponse200 | None:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[int] | Unset): The leave ids to retrieve Example: [1].
        employee_ids (list[int] | Unset): The employee ids to retrieve Example: [1].
        leave_type_id (list[int] | Unset): The leave type id to retrieve Example: [36].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTimeoffLeavesResponse200
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
        type_is_workable=type_is_workable,
        type_is_payable=type_is_payable,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    leave_type_id: list[int] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTimeoffLeavesResponse200]:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[int] | Unset): The leave ids to retrieve Example: [1].
        employee_ids (list[int] | Unset): The employee ids to retrieve Example: [1].
        leave_type_id (list[int] | Unset): The leave type id to retrieve Example: [36].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTimeoffLeavesResponse200]
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
        type_is_workable=type_is_workable,
        type_is_payable=type_is_payable,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    leave_type_id: list[int] | Unset = UNSET,
    to: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    include_deleted_leaves: bool,
    approved: bool | Unset = UNSET,
    include_pending: bool | Unset = UNSET,
    include_leave_type: bool | Unset = UNSET,
    include_duration: bool | Unset = UNSET,
    type_is_workable: bool | Unset = UNSET,
    type_is_payable: bool | Unset = UNSET,
) -> GetApi20260401ResourcesTimeoffLeavesResponse200 | None:
    """Reads all Leaves

     Reads all Leaves

    Args:
        ids (list[int] | Unset): The leave ids to retrieve Example: [1].
        employee_ids (list[int] | Unset): The employee ids to retrieve Example: [1].
        leave_type_id (list[int] | Unset): The leave type id to retrieve Example: [36].
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-30.
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2028-09-01.
        only_active (bool | Unset): Retrieve only active leaves
        include_deleted_leaves (bool): Whether to include deleted leaves (not included by default
            if not specified) Example: True.
        approved (bool | Unset): Retrieve approved leaves Example: True.
        include_pending (bool | Unset): Retrieve pending leaves Example: True.
        include_leave_type (bool | Unset): Retrieve leave types
        include_duration (bool | Unset): Retrieve leave duration Example: True.
        type_is_workable (bool | Unset): Retrieve workable leaves
        type_is_payable (bool | Unset): Retrieve payable leaves

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTimeoffLeavesResponse200
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
            type_is_workable=type_is_workable,
            type_is_payable=type_is_payable,
        )
    ).parsed
