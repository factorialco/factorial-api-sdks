from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_api_20270101_resources_shift_management_shifts_publish_body import (
    PostApi20270101ResourcesShiftManagementShiftsPublishBody,
)
from ...models.shift_management_shift import ShiftManagementShift
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/shift_management/shifts/publish",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | list[ShiftManagementShift] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ShiftManagementShift.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ErrorResponse | list[ShiftManagementShift]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset = UNSET,
) -> Response[ErrorResponse | list[ShiftManagementShift]]:
    r"""Publishes draft shifts

     Publishes the draft shifts and rest days of the selected employees between two dates, so employees
    can see them. It publishes the same set as the \"Publish\" action of the shifts planner, and
    optionally notifies the employees. If the filters match no employee, nothing is published. Only the
    drafts included in the request are checked for conflicts, against each other and against the
    employee's leaves and rest days. A draft that overlaps a shift that is already published is not
    detected. When a conflict blocks the publish, nothing is published and the 409 response lists each
    conflict in messages.shift_conflicts as a JSON string with shift_id, employee_id,
    conflicting_shift_ids, conflicting_leave_ids and conflicting_rest_day_ids. With skip_conflicts, the
    employees with conflicts are left out instead. Returns the shifts that were published. Up to 31 days
    can be published per request.

    Args:
        body (PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[ShiftManagementShift]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset = UNSET,
) -> ErrorResponse | list[ShiftManagementShift] | None:
    r"""Publishes draft shifts

     Publishes the draft shifts and rest days of the selected employees between two dates, so employees
    can see them. It publishes the same set as the \"Publish\" action of the shifts planner, and
    optionally notifies the employees. If the filters match no employee, nothing is published. Only the
    drafts included in the request are checked for conflicts, against each other and against the
    employee's leaves and rest days. A draft that overlaps a shift that is already published is not
    detected. When a conflict blocks the publish, nothing is published and the 409 response lists each
    conflict in messages.shift_conflicts as a JSON string with shift_id, employee_id,
    conflicting_shift_ids, conflicting_leave_ids and conflicting_rest_day_ids. With skip_conflicts, the
    employees with conflicts are left out instead. Returns the shifts that were published. Up to 31 days
    can be published per request.

    Args:
        body (PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[ShiftManagementShift]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset = UNSET,
) -> Response[ErrorResponse | list[ShiftManagementShift]]:
    r"""Publishes draft shifts

     Publishes the draft shifts and rest days of the selected employees between two dates, so employees
    can see them. It publishes the same set as the \"Publish\" action of the shifts planner, and
    optionally notifies the employees. If the filters match no employee, nothing is published. Only the
    drafts included in the request are checked for conflicts, against each other and against the
    employee's leaves and rest days. A draft that overlaps a shift that is already published is not
    detected. When a conflict blocks the publish, nothing is published and the 409 response lists each
    conflict in messages.shift_conflicts as a JSON string with shift_id, employee_id,
    conflicting_shift_ids, conflicting_leave_ids and conflicting_rest_day_ids. With skip_conflicts, the
    employees with conflicts are left out instead. Returns the shifts that were published. Up to 31 days
    can be published per request.

    Args:
        body (PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[ShiftManagementShift]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset = UNSET,
) -> ErrorResponse | list[ShiftManagementShift] | None:
    r"""Publishes draft shifts

     Publishes the draft shifts and rest days of the selected employees between two dates, so employees
    can see them. It publishes the same set as the \"Publish\" action of the shifts planner, and
    optionally notifies the employees. If the filters match no employee, nothing is published. Only the
    drafts included in the request are checked for conflicts, against each other and against the
    employee's leaves and rest days. A draft that overlaps a shift that is already published is not
    detected. When a conflict blocks the publish, nothing is published and the 409 response lists each
    conflict in messages.shift_conflicts as a JSON string with shift_id, employee_id,
    conflicting_shift_ids, conflicting_leave_ids and conflicting_rest_day_ids. With skip_conflicts, the
    employees with conflicts are left out instead. Returns the shifts that were published. Up to 31 days
    can be published per request.

    Args:
        body (PostApi20270101ResourcesShiftManagementShiftsPublishBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[ShiftManagementShift]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
