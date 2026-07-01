from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260701_resources_timeoff_leaves_approve_all_body import (
    PostApi20260701ResourcesTimeoffLeavesApproveAllBody,
)
from ...models.timeoff_leave import TimeoffLeave
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/timeoff/leaves/approve_all",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TimeoffLeave | None:
    if response.status_code == 200:
        response_200 = TimeoffLeave.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TimeoffLeave]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset = UNSET,
) -> Response[TimeoffLeave]:
    """Approve alls a Leave

     Allows authorized users to approve employee time-off requests by directly approving the leave

    Args:
        body (PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeoffLeave]
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
    body: PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset = UNSET,
) -> TimeoffLeave | None:
    """Approve alls a Leave

     Allows authorized users to approve employee time-off requests by directly approving the leave

    Args:
        body (PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeoffLeave
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset = UNSET,
) -> Response[TimeoffLeave]:
    """Approve alls a Leave

     Allows authorized users to approve employee time-off requests by directly approving the leave

    Args:
        body (PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeoffLeave]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset = UNSET,
) -> TimeoffLeave | None:
    """Approve alls a Leave

     Allows authorized users to approve employee time-off requests by directly approving the leave

    Args:
        body (PostApi20260701ResourcesTimeoffLeavesApproveAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeoffLeave
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
