from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260701_resources_timeoff_allowance_incidences_body import (
    PostApi20260701ResourcesTimeoffAllowanceIncidencesBody,
)
from ...models.timeoff_allowance_incidence import TimeoffAllowanceIncidence
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/timeoff/allowance_incidences",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TimeoffAllowanceIncidence | None:
    if response.status_code == 201:
        response_201 = TimeoffAllowanceIncidence.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TimeoffAllowanceIncidence]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset = UNSET,
) -> Response[TimeoffAllowanceIncidence]:
    """Creates an Allowance incidence

     Creates an allowance incidence, also known as an Allowance Adjustment in the Employee Time off Page.
    They are hours or days added or subtracted from the time off allowance

    Args:
        body (PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeoffAllowanceIncidence]
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
    body: PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset = UNSET,
) -> TimeoffAllowanceIncidence | None:
    """Creates an Allowance incidence

     Creates an allowance incidence, also known as an Allowance Adjustment in the Employee Time off Page.
    They are hours or days added or subtracted from the time off allowance

    Args:
        body (PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeoffAllowanceIncidence
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset = UNSET,
) -> Response[TimeoffAllowanceIncidence]:
    """Creates an Allowance incidence

     Creates an allowance incidence, also known as an Allowance Adjustment in the Employee Time off Page.
    They are hours or days added or subtracted from the time off allowance

    Args:
        body (PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeoffAllowanceIncidence]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset = UNSET,
) -> TimeoffAllowanceIncidence | None:
    """Creates an Allowance incidence

     Creates an allowance incidence, also known as an Allowance Adjustment in the Employee Time off Page.
    They are hours or days added or subtracted from the time off allowance

    Args:
        body (PostApi20260701ResourcesTimeoffAllowanceIncidencesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeoffAllowanceIncidence
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
