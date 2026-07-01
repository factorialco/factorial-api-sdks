from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_ats_job_postings_response_200 import (
    GetApi20260701ResourcesAtsJobPostingsResponse200,
)
from ...models.get_api_20260701_resources_ats_job_postings_status import (
    GetApi20260701ResourcesAtsJobPostingsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    status: GetApi20260701ResourcesAtsJobPostingsStatus | Unset = UNSET,
    team_id: str | Unset = UNSET,
    location_id: str | Unset = UNSET,
    legal_entity_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["team_id"] = team_id

    params["location_id"] = location_id

    params["legal_entity_id"] = legal_entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/ats/job_postings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesAtsJobPostingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesAtsJobPostingsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesAtsJobPostingsResponse200]:
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
    status: GetApi20260701ResourcesAtsJobPostingsStatus | Unset = UNSET,
    team_id: str | Unset = UNSET,
    location_id: str | Unset = UNSET,
    legal_entity_id: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesAtsJobPostingsResponse200]:
    """Reads all Job postings

     Reads all Job postings

    Args:
        ids (list[str] | Unset):
        status (GetApi20260701ResourcesAtsJobPostingsStatus | Unset):
        team_id (str | Unset):
        location_id (str | Unset):
        legal_entity_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAtsJobPostingsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        status=status,
        team_id=team_id,
        location_id=location_id,
        legal_entity_id=legal_entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    status: GetApi20260701ResourcesAtsJobPostingsStatus | Unset = UNSET,
    team_id: str | Unset = UNSET,
    location_id: str | Unset = UNSET,
    legal_entity_id: str | Unset = UNSET,
) -> GetApi20260701ResourcesAtsJobPostingsResponse200 | None:
    """Reads all Job postings

     Reads all Job postings

    Args:
        ids (list[str] | Unset):
        status (GetApi20260701ResourcesAtsJobPostingsStatus | Unset):
        team_id (str | Unset):
        location_id (str | Unset):
        legal_entity_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAtsJobPostingsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        status=status,
        team_id=team_id,
        location_id=location_id,
        legal_entity_id=legal_entity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    status: GetApi20260701ResourcesAtsJobPostingsStatus | Unset = UNSET,
    team_id: str | Unset = UNSET,
    location_id: str | Unset = UNSET,
    legal_entity_id: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesAtsJobPostingsResponse200]:
    """Reads all Job postings

     Reads all Job postings

    Args:
        ids (list[str] | Unset):
        status (GetApi20260701ResourcesAtsJobPostingsStatus | Unset):
        team_id (str | Unset):
        location_id (str | Unset):
        legal_entity_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAtsJobPostingsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        status=status,
        team_id=team_id,
        location_id=location_id,
        legal_entity_id=legal_entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    status: GetApi20260701ResourcesAtsJobPostingsStatus | Unset = UNSET,
    team_id: str | Unset = UNSET,
    location_id: str | Unset = UNSET,
    legal_entity_id: str | Unset = UNSET,
) -> GetApi20260701ResourcesAtsJobPostingsResponse200 | None:
    """Reads all Job postings

     Reads all Job postings

    Args:
        ids (list[str] | Unset):
        status (GetApi20260701ResourcesAtsJobPostingsStatus | Unset):
        team_id (str | Unset):
        location_id (str | Unset):
        legal_entity_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAtsJobPostingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            status=status,
            team_id=team_id,
            location_id=location_id,
            legal_entity_id=legal_entity_id,
        )
    ).parsed
