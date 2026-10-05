from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_teams_memberships_response_200 import (
    GetApi20261001ResourcesTeamsMembershipsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    lead: bool | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    with_source_attribution: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["lead"] = lead

    json_team_ids: list[str] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids[]"] = json_team_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["with_source_attribution"] = with_source_attribution

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/teams/memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesTeamsMembershipsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesTeamsMembershipsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesTeamsMembershipsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    lead: bool | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    with_source_attribution: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTeamsMembershipsResponse200]:
    """Reads all Memberships

     Get all memberships.

    Args:
        ids (list[str] | Unset): Return only the memberships with these ids. Example: ['1', '2',
            '3'].
        lead (bool | Unset): Whether the employee is a lead of the team or not Example: True.
        team_ids (list[str] | Unset): Return only the memberships of these teams. Example: ['3',
            '5', '7'].
        employee_ids (list[str] | Unset): Return only the memberships of these employees. Example:
            ['10', '12', '13'].
        with_source_attribution (bool | Unset): Populate `direct`, `source_team_ids` and
            `parent_team_ids` on each returned membership (nested teams). Only honoured when filtering
            by a single `employee_ids` value without `team_ids` — the read that attributes one
            employee's own memberships, and the only one that resolves `direct`. Reads filtered by a
            single team already return `source_team_ids`/`parent_team_ids` without this flag (`direct`
            stays null there); bulk reads ignore it entirely. Unsupported filter combinations return
            `200` with empty attribution rather than an error. Attribution is resolved per employee
            and is significantly more expensive than a plain read: intended for per-profile lookups,
            not bulk synchronization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTeamsMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        lead=lead,
        team_ids=team_ids,
        employee_ids=employee_ids,
        with_source_attribution=with_source_attribution,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    lead: bool | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    with_source_attribution: bool | Unset = UNSET,
) -> GetApi20261001ResourcesTeamsMembershipsResponse200 | None:
    """Reads all Memberships

     Get all memberships.

    Args:
        ids (list[str] | Unset): Return only the memberships with these ids. Example: ['1', '2',
            '3'].
        lead (bool | Unset): Whether the employee is a lead of the team or not Example: True.
        team_ids (list[str] | Unset): Return only the memberships of these teams. Example: ['3',
            '5', '7'].
        employee_ids (list[str] | Unset): Return only the memberships of these employees. Example:
            ['10', '12', '13'].
        with_source_attribution (bool | Unset): Populate `direct`, `source_team_ids` and
            `parent_team_ids` on each returned membership (nested teams). Only honoured when filtering
            by a single `employee_ids` value without `team_ids` — the read that attributes one
            employee's own memberships, and the only one that resolves `direct`. Reads filtered by a
            single team already return `source_team_ids`/`parent_team_ids` without this flag (`direct`
            stays null there); bulk reads ignore it entirely. Unsupported filter combinations return
            `200` with empty attribution rather than an error. Attribution is resolved per employee
            and is significantly more expensive than a plain read: intended for per-profile lookups,
            not bulk synchronization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTeamsMembershipsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        lead=lead,
        team_ids=team_ids,
        employee_ids=employee_ids,
        with_source_attribution=with_source_attribution,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    lead: bool | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    with_source_attribution: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTeamsMembershipsResponse200]:
    """Reads all Memberships

     Get all memberships.

    Args:
        ids (list[str] | Unset): Return only the memberships with these ids. Example: ['1', '2',
            '3'].
        lead (bool | Unset): Whether the employee is a lead of the team or not Example: True.
        team_ids (list[str] | Unset): Return only the memberships of these teams. Example: ['3',
            '5', '7'].
        employee_ids (list[str] | Unset): Return only the memberships of these employees. Example:
            ['10', '12', '13'].
        with_source_attribution (bool | Unset): Populate `direct`, `source_team_ids` and
            `parent_team_ids` on each returned membership (nested teams). Only honoured when filtering
            by a single `employee_ids` value without `team_ids` — the read that attributes one
            employee's own memberships, and the only one that resolves `direct`. Reads filtered by a
            single team already return `source_team_ids`/`parent_team_ids` without this flag (`direct`
            stays null there); bulk reads ignore it entirely. Unsupported filter combinations return
            `200` with empty attribution rather than an error. Attribution is resolved per employee
            and is significantly more expensive than a plain read: intended for per-profile lookups,
            not bulk synchronization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTeamsMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        lead=lead,
        team_ids=team_ids,
        employee_ids=employee_ids,
        with_source_attribution=with_source_attribution,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    lead: bool | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    with_source_attribution: bool | Unset = UNSET,
) -> GetApi20261001ResourcesTeamsMembershipsResponse200 | None:
    """Reads all Memberships

     Get all memberships.

    Args:
        ids (list[str] | Unset): Return only the memberships with these ids. Example: ['1', '2',
            '3'].
        lead (bool | Unset): Whether the employee is a lead of the team or not Example: True.
        team_ids (list[str] | Unset): Return only the memberships of these teams. Example: ['3',
            '5', '7'].
        employee_ids (list[str] | Unset): Return only the memberships of these employees. Example:
            ['10', '12', '13'].
        with_source_attribution (bool | Unset): Populate `direct`, `source_team_ids` and
            `parent_team_ids` on each returned membership (nested teams). Only honoured when filtering
            by a single `employee_ids` value without `team_ids` — the read that attributes one
            employee's own memberships, and the only one that resolves `direct`. Reads filtered by a
            single team already return `source_team_ids`/`parent_team_ids` without this flag (`direct`
            stays null there); bulk reads ignore it entirely. Unsupported filter combinations return
            `200` with empty attribution rather than an error. Attribution is resolved per employee
            and is significantly more expensive than a plain read: intended for per-profile lookups,
            not bulk synchronization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTeamsMembershipsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            lead=lead,
            team_ids=team_ids,
            employee_ids=employee_ids,
            with_source_attribution=with_source_attribution,
        )
    ).parsed
