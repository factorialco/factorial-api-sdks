from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_api_20270101_resources_teams_memberships_body import (
    PostApi20270101ResourcesTeamsMembershipsBody,
)
from ...models.teams_membership import TeamsMembership
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesTeamsMembershipsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/teams/memberships",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TeamsMembership | None:
    if response.status_code == 201:
        response_201 = TeamsMembership.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | TeamsMembership]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesTeamsMembershipsBody | Unset = UNSET,
) -> Response[ErrorResponse | TeamsMembership]:
    """Creates a Membership

     Assign an employee to a team, meaning create a membership. For companies with nested teams, two
    extra semantics apply. Propagation: memberships are inherited upwards, so after adding an employee
    to a sub-team, inherited membership rows for its ancestor teams are materialized asynchronously —
    rows you did not create will appear in later reads. Reuse: if the employee already has a membership
    row on that team (typically an inherited one), no new row is created — the employee becomes a direct
    member of the team, the `lead` flag is applied when you send one, and the existing row (with its
    existing id) is returned instead of a new resource. Omitting `lead` leaves a reused row's leadership
    as it was, so replaying an addition never demotes a current lead; a genuinely new row is created
    without it. The response is still `201` when an existing row is reused, so compare the returned `id`
    against what you already hold to tell the two cases apart.

    Args:
        body (PostApi20270101ResourcesTeamsMembershipsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TeamsMembership]
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
    body: PostApi20270101ResourcesTeamsMembershipsBody | Unset = UNSET,
) -> ErrorResponse | TeamsMembership | None:
    """Creates a Membership

     Assign an employee to a team, meaning create a membership. For companies with nested teams, two
    extra semantics apply. Propagation: memberships are inherited upwards, so after adding an employee
    to a sub-team, inherited membership rows for its ancestor teams are materialized asynchronously —
    rows you did not create will appear in later reads. Reuse: if the employee already has a membership
    row on that team (typically an inherited one), no new row is created — the employee becomes a direct
    member of the team, the `lead` flag is applied when you send one, and the existing row (with its
    existing id) is returned instead of a new resource. Omitting `lead` leaves a reused row's leadership
    as it was, so replaying an addition never demotes a current lead; a genuinely new row is created
    without it. The response is still `201` when an existing row is reused, so compare the returned `id`
    against what you already hold to tell the two cases apart.

    Args:
        body (PostApi20270101ResourcesTeamsMembershipsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TeamsMembership
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesTeamsMembershipsBody | Unset = UNSET,
) -> Response[ErrorResponse | TeamsMembership]:
    """Creates a Membership

     Assign an employee to a team, meaning create a membership. For companies with nested teams, two
    extra semantics apply. Propagation: memberships are inherited upwards, so after adding an employee
    to a sub-team, inherited membership rows for its ancestor teams are materialized asynchronously —
    rows you did not create will appear in later reads. Reuse: if the employee already has a membership
    row on that team (typically an inherited one), no new row is created — the employee becomes a direct
    member of the team, the `lead` flag is applied when you send one, and the existing row (with its
    existing id) is returned instead of a new resource. Omitting `lead` leaves a reused row's leadership
    as it was, so replaying an addition never demotes a current lead; a genuinely new row is created
    without it. The response is still `201` when an existing row is reused, so compare the returned `id`
    against what you already hold to tell the two cases apart.

    Args:
        body (PostApi20270101ResourcesTeamsMembershipsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TeamsMembership]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesTeamsMembershipsBody | Unset = UNSET,
) -> ErrorResponse | TeamsMembership | None:
    """Creates a Membership

     Assign an employee to a team, meaning create a membership. For companies with nested teams, two
    extra semantics apply. Propagation: memberships are inherited upwards, so after adding an employee
    to a sub-team, inherited membership rows for its ancestor teams are materialized asynchronously —
    rows you did not create will appear in later reads. Reuse: if the employee already has a membership
    row on that team (typically an inherited one), no new row is created — the employee becomes a direct
    member of the team, the `lead` flag is applied when you send one, and the existing row (with its
    existing id) is returned instead of a new resource. Omitting `lead` leaves a reused row's leadership
    as it was, so replaying an addition never demotes a current lead; a genuinely new row is created
    without it. The response is still `201` when an existing row is reused, so compare the returned `id`
    against what you already hold to tell the two cases apart.

    Args:
        body (PostApi20270101ResourcesTeamsMembershipsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TeamsMembership
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
