from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_review_process import PerformanceReviewProcess
from ...models.post_api_20251001_resources_performance_review_processes_reopen_body import (
    PostApi20251001ResourcesPerformanceReviewProcessesReopenBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/performance/review_processes/reopen",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PerformanceReviewProcess | None:
    if response.status_code == 200:
        response_200 = PerformanceReviewProcess.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PerformanceReviewProcess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset = UNSET,
) -> Response[PerformanceReviewProcess]:
    """Reopens a Review process

     Reopen a finished review process.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewProcess]
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
    body: PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset = UNSET,
) -> PerformanceReviewProcess | None:
    """Reopens a Review process

     Reopen a finished review process.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewProcess
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset = UNSET,
) -> Response[PerformanceReviewProcess]:
    """Reopens a Review process

     Reopen a finished review process.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewProcess]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset = UNSET,
) -> PerformanceReviewProcess | None:
    """Reopens a Review process

     Reopen a finished review process.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewProcessesReopenBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewProcess
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
