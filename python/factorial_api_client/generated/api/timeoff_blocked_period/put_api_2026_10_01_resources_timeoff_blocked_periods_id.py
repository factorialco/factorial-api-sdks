from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_20261001_resources_timeoff_blocked_periods_id_body import (
    PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody,
)
from ...models.timeoff_blocked_periods_policy import TimeoffBlockedPeriodsPolicy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-10-01/resources/timeoff/blocked_periods/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TimeoffBlockedPeriodsPolicy | None:
    if response.status_code == 200:
        response_200 = TimeoffBlockedPeriodsPolicy.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TimeoffBlockedPeriodsPolicy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset = UNSET,
) -> Response[TimeoffBlockedPeriodsPolicy]:
    """Updates a Blocked period

     Updates a blocked period

    Args:
        id (str):
        body (PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeoffBlockedPeriodsPolicy]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset = UNSET,
) -> TimeoffBlockedPeriodsPolicy | None:
    """Updates a Blocked period

     Updates a blocked period

    Args:
        id (str):
        body (PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeoffBlockedPeriodsPolicy
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset = UNSET,
) -> Response[TimeoffBlockedPeriodsPolicy]:
    """Updates a Blocked period

     Updates a blocked period

    Args:
        id (str):
        body (PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeoffBlockedPeriodsPolicy]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset = UNSET,
) -> TimeoffBlockedPeriodsPolicy | None:
    """Updates a Blocked period

     Updates a blocked period

    Args:
        id (str):
        body (PutApi20261001ResourcesTimeoffBlockedPeriodsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeoffBlockedPeriodsPolicy
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
