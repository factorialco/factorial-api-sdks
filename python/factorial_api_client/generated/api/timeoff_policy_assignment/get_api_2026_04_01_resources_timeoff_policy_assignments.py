from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_timeoff_policy_assignments_response_200 import (
    GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    timeoff_policy_ids: list[int] | Unset = UNSET,
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

    json_timeoff_policy_ids: list[int] | Unset = UNSET
    if not isinstance(timeoff_policy_ids, Unset):
        json_timeoff_policy_ids = timeoff_policy_ids

    params["timeoff_policy_ids[]"] = json_timeoff_policy_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/timeoff/policy_assignments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200]:
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
    timeoff_policy_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200]:
    """Reads all Policy assignments

     Read Time off Policy Assignments

    Args:
        ids (list[int] | Unset): An array of time off policy assignment ids Example: [1, 2].
        employee_ids (list[int] | Unset): Filter policy assignments by employee ids Example: [1,
            2].
        timeoff_policy_ids (list[int] | Unset): Filter policy assignments by time off policy ids
            Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        timeoff_policy_ids=timeoff_policy_ids,
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
    timeoff_policy_ids: list[int] | Unset = UNSET,
) -> GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200 | None:
    """Reads all Policy assignments

     Read Time off Policy Assignments

    Args:
        ids (list[int] | Unset): An array of time off policy assignment ids Example: [1, 2].
        employee_ids (list[int] | Unset): Filter policy assignments by employee ids Example: [1,
            2].
        timeoff_policy_ids (list[int] | Unset): Filter policy assignments by time off policy ids
            Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        timeoff_policy_ids=timeoff_policy_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    timeoff_policy_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200]:
    """Reads all Policy assignments

     Read Time off Policy Assignments

    Args:
        ids (list[int] | Unset): An array of time off policy assignment ids Example: [1, 2].
        employee_ids (list[int] | Unset): Filter policy assignments by employee ids Example: [1,
            2].
        timeoff_policy_ids (list[int] | Unset): Filter policy assignments by time off policy ids
            Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        timeoff_policy_ids=timeoff_policy_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    timeoff_policy_ids: list[int] | Unset = UNSET,
) -> GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200 | None:
    """Reads all Policy assignments

     Read Time off Policy Assignments

    Args:
        ids (list[int] | Unset): An array of time off policy assignment ids Example: [1, 2].
        employee_ids (list[int] | Unset): Filter policy assignments by employee ids Example: [1,
            2].
        timeoff_policy_ids (list[int] | Unset): Filter policy assignments by time off policy ids
            Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTimeoffPolicyAssignmentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            timeoff_policy_ids=timeoff_policy_ids,
        )
    ).parsed
