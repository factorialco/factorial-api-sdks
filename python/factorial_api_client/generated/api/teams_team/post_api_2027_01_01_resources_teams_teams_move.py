from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20270101_resources_teams_teams_move_body import (
    PostApi20270101ResourcesTeamsTeamsMoveBody,
)
from ...models.teams_team import TeamsTeam
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesTeamsTeamsMoveBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/teams/teams/move",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TeamsTeam | None:
    if response.status_code == 200:
        response_200 = TeamsTeam.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TeamsTeam]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesTeamsTeamsMoveBody | Unset = UNSET,
) -> Response[TeamsTeam]:
    """Moves a Team

     Move a team under a different parent team, or to the root of the hierarchy. Requires the nested
    teams feature — companies without it get a forbidden error — plus permission to manage the moved
    team and both parents involved; the hierarchy is capped at 4 levels. The team keeps its direct
    members; inherited memberships are re-propagated asynchronously to the new ancestors.

    Args:
        body (PostApi20270101ResourcesTeamsTeamsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamsTeam]
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
    body: PostApi20270101ResourcesTeamsTeamsMoveBody | Unset = UNSET,
) -> TeamsTeam | None:
    """Moves a Team

     Move a team under a different parent team, or to the root of the hierarchy. Requires the nested
    teams feature — companies without it get a forbidden error — plus permission to manage the moved
    team and both parents involved; the hierarchy is capped at 4 levels. The team keeps its direct
    members; inherited memberships are re-propagated asynchronously to the new ancestors.

    Args:
        body (PostApi20270101ResourcesTeamsTeamsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamsTeam
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesTeamsTeamsMoveBody | Unset = UNSET,
) -> Response[TeamsTeam]:
    """Moves a Team

     Move a team under a different parent team, or to the root of the hierarchy. Requires the nested
    teams feature — companies without it get a forbidden error — plus permission to manage the moved
    team and both parents involved; the hierarchy is capped at 4 levels. The team keeps its direct
    members; inherited memberships are re-propagated asynchronously to the new ancestors.

    Args:
        body (PostApi20270101ResourcesTeamsTeamsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamsTeam]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesTeamsTeamsMoveBody | Unset = UNSET,
) -> TeamsTeam | None:
    """Moves a Team

     Move a team under a different parent team, or to the root of the hierarchy. Requires the nested
    teams feature — companies without it get a forbidden error — plus permission to manage the moved
    team and both parents involved; the hierarchy is capped at 4 levels. The team keeps its direct
    members; inherited memberships are re-propagated asynchronously to the new ancestors.

    Args:
        body (PostApi20270101ResourcesTeamsTeamsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamsTeam
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
