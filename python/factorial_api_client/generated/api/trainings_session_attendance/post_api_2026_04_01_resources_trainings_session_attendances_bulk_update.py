from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260401_resources_trainings_session_attendances_bulk_update_body import (
    PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody,
)
from ...models.trainings_session_attendance import TrainingsSessionAttendance
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/trainings/session_attendances/bulk_update",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TrainingsSessionAttendance] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TrainingsSessionAttendance.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TrainingsSessionAttendance]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset = UNSET,
) -> Response[list[TrainingsSessionAttendance]]:
    """Bulk update session attendances

     Updates the status or completed duration of multiple session attendances. When status is set to
    completed, completed_duration is automatically set to session duration. When only completed_duration
    is provided, attendances must already be in completed status.

    Args:
        body (PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TrainingsSessionAttendance]]
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
    body: PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset = UNSET,
) -> list[TrainingsSessionAttendance] | None:
    """Bulk update session attendances

     Updates the status or completed duration of multiple session attendances. When status is set to
    completed, completed_duration is automatically set to session duration. When only completed_duration
    is provided, attendances must already be in completed status.

    Args:
        body (PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TrainingsSessionAttendance]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset = UNSET,
) -> Response[list[TrainingsSessionAttendance]]:
    """Bulk update session attendances

     Updates the status or completed duration of multiple session attendances. When status is set to
    completed, completed_duration is automatically set to session duration. When only completed_duration
    is provided, attendances must already be in completed status.

    Args:
        body (PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TrainingsSessionAttendance]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset = UNSET,
) -> list[TrainingsSessionAttendance] | None:
    """Bulk update session attendances

     Updates the status or completed duration of multiple session attendances. When status is set to
    completed, completed_duration is automatically set to session duration. When only completed_duration
    is provided, attendances must already be in completed status.

    Args:
        body (PostApi20260401ResourcesTrainingsSessionAttendancesBulkUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TrainingsSessionAttendance]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
