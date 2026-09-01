from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_trainings_session_access_memberships_response_200 import (
    GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    session_id: str,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["session_id"] = session_id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["search"] = search

    json_team_ids: list[str] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids[]"] = json_team_ids

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status[]"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/trainings/session_access_memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200]:
    """Reads all Session access memberships

     Reads all Session access memberships

    Args:
        session_id (str): Filter memberships by session ID Example: 1.
        ids (list[str] | Unset): Filter memberships by specific IDs Example: ['1', '2', '3'].
        search (str | Unset): Filter memberships by user name Example: John.
        team_ids (list[str] | Unset): ID of the team associated with this membership Example:
            ['1', '2'].
        status (list[str] | Unset): Current status of the session attendance Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        ids=ids,
        search=search,
        team_ids=team_ids,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    session_id: str,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200 | None:
    """Reads all Session access memberships

     Reads all Session access memberships

    Args:
        session_id (str): Filter memberships by session ID Example: 1.
        ids (list[str] | Unset): Filter memberships by specific IDs Example: ['1', '2', '3'].
        search (str | Unset): Filter memberships by user name Example: John.
        team_ids (list[str] | Unset): ID of the team associated with this membership Example:
            ['1', '2'].
        status (list[str] | Unset): Current status of the session attendance Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        ids=ids,
        search=search,
        team_ids=team_ids,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200]:
    """Reads all Session access memberships

     Reads all Session access memberships

    Args:
        session_id (str): Filter memberships by session ID Example: 1.
        ids (list[str] | Unset): Filter memberships by specific IDs Example: ['1', '2', '3'].
        search (str | Unset): Filter memberships by user name Example: John.
        team_ids (list[str] | Unset): ID of the team associated with this membership Example:
            ['1', '2'].
        status (list[str] | Unset): Current status of the session attendance Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        ids=ids,
        search=search,
        team_ids=team_ids,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    session_id: str,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200 | None:
    """Reads all Session access memberships

     Reads all Session access memberships

    Args:
        session_id (str): Filter memberships by session ID Example: 1.
        ids (list[str] | Unset): Filter memberships by specific IDs Example: ['1', '2', '3'].
        search (str | Unset): Filter memberships by user name Example: John.
        team_ids (list[str] | Unset): ID of the team associated with this membership Example:
            ['1', '2'].
        status (list[str] | Unset): Current status of the session attendance Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTrainingsSessionAccessMembershipsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            ids=ids,
            search=search,
            team_ids=team_ids,
            status=status,
        )
    ).parsed
