from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_review_process_target import PerformanceReviewProcessTarget
from ...models.post_api_20251001_resources_performance_review_process_targets_add_peers_body import (
    PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/performance/review_process_targets/add_peers",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PerformanceReviewProcessTarget | None:
    if response.status_code == 200:
        response_200 = PerformanceReviewProcessTarget.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PerformanceReviewProcessTarget]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset = UNSET,
) -> Response[PerformanceReviewProcessTarget]:
    """Add peers a Review process target

     Assign peers to evaluate a specific participant.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewProcessTarget]
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
    body: PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset = UNSET,
) -> PerformanceReviewProcessTarget | None:
    """Add peers a Review process target

     Assign peers to evaluate a specific participant.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewProcessTarget
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset = UNSET,
) -> Response[PerformanceReviewProcessTarget]:
    """Add peers a Review process target

     Assign peers to evaluate a specific participant.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewProcessTarget]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset = UNSET,
) -> PerformanceReviewProcessTarget | None:
    """Add peers a Review process target

     Assign peers to evaluate a specific participant.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessTargetsAddPeersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewProcessTarget
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
