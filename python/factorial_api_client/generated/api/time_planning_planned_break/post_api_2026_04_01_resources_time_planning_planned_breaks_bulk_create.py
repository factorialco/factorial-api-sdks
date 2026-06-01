from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260401_resources_time_planning_planned_breaks_bulk_create_body import (
    PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody,
)
from ...models.time_planning_planned_break import TimePlanningPlannedBreak
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/time_planning/planned_breaks/bulk_create",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TimePlanningPlannedBreak] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TimePlanningPlannedBreak.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TimePlanningPlannedBreak]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset = UNSET,
) -> Response[list[TimePlanningPlannedBreak]]:
    """Bulk creates a Planned break

     Bulk creates a Planned break

    Args:
        body (PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimePlanningPlannedBreak]]
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
    body: PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset = UNSET,
) -> list[TimePlanningPlannedBreak] | None:
    """Bulk creates a Planned break

     Bulk creates a Planned break

    Args:
        body (PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimePlanningPlannedBreak]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset = UNSET,
) -> Response[list[TimePlanningPlannedBreak]]:
    """Bulk creates a Planned break

     Bulk creates a Planned break

    Args:
        body (PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimePlanningPlannedBreak]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset = UNSET,
) -> list[TimePlanningPlannedBreak] | None:
    """Bulk creates a Planned break

     Bulk creates a Planned break

    Args:
        body (PostApi20260401ResourcesTimePlanningPlannedBreaksBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimePlanningPlannedBreak]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
