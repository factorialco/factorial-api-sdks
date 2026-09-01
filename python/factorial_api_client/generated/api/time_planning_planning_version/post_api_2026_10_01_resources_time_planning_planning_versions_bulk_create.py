from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20261001_resources_time_planning_planning_versions_bulk_create_body import (
    PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody,
)
from ...models.time_planning_planning_version import TimePlanningPlanningVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-10-01/resources/time_planning/planning_versions/bulk_create",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TimePlanningPlanningVersion] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TimePlanningPlanningVersion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TimePlanningPlanningVersion]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset = UNSET,
) -> Response[list[TimePlanningPlanningVersion]]:
    """Bulk creates a Planning version

     Bulk creates a Planning version

    Args:
        body (PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimePlanningPlanningVersion]]
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
    body: PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset = UNSET,
) -> list[TimePlanningPlanningVersion] | None:
    """Bulk creates a Planning version

     Bulk creates a Planning version

    Args:
        body (PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimePlanningPlanningVersion]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset = UNSET,
) -> Response[list[TimePlanningPlanningVersion]]:
    """Bulk creates a Planning version

     Bulk creates a Planning version

    Args:
        body (PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimePlanningPlanningVersion]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset = UNSET,
) -> list[TimePlanningPlanningVersion] | None:
    """Bulk creates a Planning version

     Bulk creates a Planning version

    Args:
        body (PostApi20261001ResourcesTimePlanningPlanningVersionsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimePlanningPlanningVersion]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
