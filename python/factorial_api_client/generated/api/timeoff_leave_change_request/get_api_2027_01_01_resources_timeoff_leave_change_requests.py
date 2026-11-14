from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_timeoff_leave_change_requests_response_200 import (
    GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    pending: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_leave_ids: list[str] | Unset = UNSET
    if not isinstance(leave_ids, Unset):
        json_leave_ids = leave_ids

    params["leave_ids[]"] = json_leave_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["pending"] = pending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/timeoff/leave_change_requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200]:
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
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    pending: bool | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200]:
    """Reads leave change requests

     Returns the change requests on the leaves the caller can see.

    Args:
        ids (list[str] | Unset): Return only the change requests with these ids. Example: ['1'].
        leave_ids (list[str] | Unset): Return only the change requests on these leaves. Example:
            ['1'].
        employee_ids (list[str] | Unset): Return only the change requests of these employees.
            Example: ['1'].
        pending (bool | Unset): Set to true to return only the requests still awaiting a decision.
            Passing false has no effect. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        leave_ids=leave_ids,
        employee_ids=employee_ids,
        pending=pending,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    pending: bool | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200 | None:
    """Reads leave change requests

     Returns the change requests on the leaves the caller can see.

    Args:
        ids (list[str] | Unset): Return only the change requests with these ids. Example: ['1'].
        leave_ids (list[str] | Unset): Return only the change requests on these leaves. Example:
            ['1'].
        employee_ids (list[str] | Unset): Return only the change requests of these employees.
            Example: ['1'].
        pending (bool | Unset): Set to true to return only the requests still awaiting a decision.
            Passing false has no effect. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        leave_ids=leave_ids,
        employee_ids=employee_ids,
        pending=pending,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    pending: bool | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200]:
    """Reads leave change requests

     Returns the change requests on the leaves the caller can see.

    Args:
        ids (list[str] | Unset): Return only the change requests with these ids. Example: ['1'].
        leave_ids (list[str] | Unset): Return only the change requests on these leaves. Example:
            ['1'].
        employee_ids (list[str] | Unset): Return only the change requests of these employees.
            Example: ['1'].
        pending (bool | Unset): Set to true to return only the requests still awaiting a decision.
            Passing false has no effect. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        leave_ids=leave_ids,
        employee_ids=employee_ids,
        pending=pending,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    pending: bool | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200 | None:
    """Reads leave change requests

     Returns the change requests on the leaves the caller can see.

    Args:
        ids (list[str] | Unset): Return only the change requests with these ids. Example: ['1'].
        leave_ids (list[str] | Unset): Return only the change requests on these leaves. Example:
            ['1'].
        employee_ids (list[str] | Unset): Return only the change requests of these employees.
            Example: ['1'].
        pending (bool | Unset): Set to true to return only the requests still awaiting a decision.
            Passing false has no effect. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesTimeoffLeaveChangeRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            leave_ids=leave_ids,
            employee_ids=employee_ids,
            pending=pending,
        )
    ).parsed
