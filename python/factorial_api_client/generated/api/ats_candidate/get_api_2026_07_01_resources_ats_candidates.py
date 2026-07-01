from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_ats_candidates_response_200 import (
    GetApi20260701ResourcesAtsCandidatesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    source: list[str] | Unset = UNSET,
    remote: bool | Unset = UNSET,
    job_posting_ids: list[str] | Unset = UNSET,
    minimum_average_rating: float | Unset = UNSET,
    active: bool | Unset = UNSET,
    talent_pool: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_emails: list[str] | Unset = UNSET
    if not isinstance(emails, Unset):
        json_emails = emails

    params["emails[]"] = json_emails

    json_team_ids: list[str] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids[]"] = json_team_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["location_ids[]"] = json_location_ids

    json_source: list[str] | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source

    params["source[]"] = json_source

    params["remote"] = remote

    json_job_posting_ids: list[str] | Unset = UNSET
    if not isinstance(job_posting_ids, Unset):
        json_job_posting_ids = job_posting_ids

    params["job_posting_ids[]"] = json_job_posting_ids

    params["minimum_average_rating"] = minimum_average_rating

    params["active"] = active

    params["talent_pool"] = talent_pool

    params["archived"] = archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/ats/candidates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesAtsCandidatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesAtsCandidatesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesAtsCandidatesResponse200]:
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
    emails: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    source: list[str] | Unset = UNSET,
    remote: bool | Unset = UNSET,
    job_posting_ids: list[str] | Unset = UNSET,
    minimum_average_rating: float | Unset = UNSET,
    active: bool | Unset = UNSET,
    talent_pool: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
) -> Response[GetApi20260701ResourcesAtsCandidatesResponse200]:
    """Reads all Candidates

     Fetches candidates data from Factorial. When using administrator-level API Credentials, all
    candidates associated with a company will be returned. When using non-admin level API credentials,
    only candidates that applied to a job for which the user is a hiring manager will be returned.

    Args:
        ids (list[str] | Unset): list of candidate identifiers. Example: ['1', '2', '3'].
        emails (list[str] | Unset): list of candidate emails. Example: ['ana@factorial.com',
            'juan@factorial.com'].
        team_ids (list[str] | Unset): list of team identifiers, refers to teams/teams endpoint.
            Example: ['1', '2', '3'].
        location_ids (list[str] | Unset): list of location identifiers, refers to
            locations/locations endpoint. Example: ['1', '2', '3'].
        source (list[str] | Unset): source of the candidate. Example: email.
        remote (bool | Unset): is the candidate remote? Example: True.
        job_posting_ids (list[str] | Unset): list of job posting identifiers, refers to
            ats/job_postings endpoint. Example: ['1', '2', '3'].
        minimum_average_rating (float | Unset): minimum average rating of the candidate. Example:
            4.
        active (bool | Unset): is the candidate active? Example: True.
        talent_pool (bool | Unset): is the candidate part of talent pool? Example: True.
        archived (bool | Unset): is the candidate archived? Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAtsCandidatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        emails=emails,
        team_ids=team_ids,
        location_ids=location_ids,
        source=source,
        remote=remote,
        job_posting_ids=job_posting_ids,
        minimum_average_rating=minimum_average_rating,
        active=active,
        talent_pool=talent_pool,
        archived=archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    source: list[str] | Unset = UNSET,
    remote: bool | Unset = UNSET,
    job_posting_ids: list[str] | Unset = UNSET,
    minimum_average_rating: float | Unset = UNSET,
    active: bool | Unset = UNSET,
    talent_pool: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
) -> GetApi20260701ResourcesAtsCandidatesResponse200 | None:
    """Reads all Candidates

     Fetches candidates data from Factorial. When using administrator-level API Credentials, all
    candidates associated with a company will be returned. When using non-admin level API credentials,
    only candidates that applied to a job for which the user is a hiring manager will be returned.

    Args:
        ids (list[str] | Unset): list of candidate identifiers. Example: ['1', '2', '3'].
        emails (list[str] | Unset): list of candidate emails. Example: ['ana@factorial.com',
            'juan@factorial.com'].
        team_ids (list[str] | Unset): list of team identifiers, refers to teams/teams endpoint.
            Example: ['1', '2', '3'].
        location_ids (list[str] | Unset): list of location identifiers, refers to
            locations/locations endpoint. Example: ['1', '2', '3'].
        source (list[str] | Unset): source of the candidate. Example: email.
        remote (bool | Unset): is the candidate remote? Example: True.
        job_posting_ids (list[str] | Unset): list of job posting identifiers, refers to
            ats/job_postings endpoint. Example: ['1', '2', '3'].
        minimum_average_rating (float | Unset): minimum average rating of the candidate. Example:
            4.
        active (bool | Unset): is the candidate active? Example: True.
        talent_pool (bool | Unset): is the candidate part of talent pool? Example: True.
        archived (bool | Unset): is the candidate archived? Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAtsCandidatesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        emails=emails,
        team_ids=team_ids,
        location_ids=location_ids,
        source=source,
        remote=remote,
        job_posting_ids=job_posting_ids,
        minimum_average_rating=minimum_average_rating,
        active=active,
        talent_pool=talent_pool,
        archived=archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    source: list[str] | Unset = UNSET,
    remote: bool | Unset = UNSET,
    job_posting_ids: list[str] | Unset = UNSET,
    minimum_average_rating: float | Unset = UNSET,
    active: bool | Unset = UNSET,
    talent_pool: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
) -> Response[GetApi20260701ResourcesAtsCandidatesResponse200]:
    """Reads all Candidates

     Fetches candidates data from Factorial. When using administrator-level API Credentials, all
    candidates associated with a company will be returned. When using non-admin level API credentials,
    only candidates that applied to a job for which the user is a hiring manager will be returned.

    Args:
        ids (list[str] | Unset): list of candidate identifiers. Example: ['1', '2', '3'].
        emails (list[str] | Unset): list of candidate emails. Example: ['ana@factorial.com',
            'juan@factorial.com'].
        team_ids (list[str] | Unset): list of team identifiers, refers to teams/teams endpoint.
            Example: ['1', '2', '3'].
        location_ids (list[str] | Unset): list of location identifiers, refers to
            locations/locations endpoint. Example: ['1', '2', '3'].
        source (list[str] | Unset): source of the candidate. Example: email.
        remote (bool | Unset): is the candidate remote? Example: True.
        job_posting_ids (list[str] | Unset): list of job posting identifiers, refers to
            ats/job_postings endpoint. Example: ['1', '2', '3'].
        minimum_average_rating (float | Unset): minimum average rating of the candidate. Example:
            4.
        active (bool | Unset): is the candidate active? Example: True.
        talent_pool (bool | Unset): is the candidate part of talent pool? Example: True.
        archived (bool | Unset): is the candidate archived? Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAtsCandidatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        emails=emails,
        team_ids=team_ids,
        location_ids=location_ids,
        source=source,
        remote=remote,
        job_posting_ids=job_posting_ids,
        minimum_average_rating=minimum_average_rating,
        active=active,
        talent_pool=talent_pool,
        archived=archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    source: list[str] | Unset = UNSET,
    remote: bool | Unset = UNSET,
    job_posting_ids: list[str] | Unset = UNSET,
    minimum_average_rating: float | Unset = UNSET,
    active: bool | Unset = UNSET,
    talent_pool: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
) -> GetApi20260701ResourcesAtsCandidatesResponse200 | None:
    """Reads all Candidates

     Fetches candidates data from Factorial. When using administrator-level API Credentials, all
    candidates associated with a company will be returned. When using non-admin level API credentials,
    only candidates that applied to a job for which the user is a hiring manager will be returned.

    Args:
        ids (list[str] | Unset): list of candidate identifiers. Example: ['1', '2', '3'].
        emails (list[str] | Unset): list of candidate emails. Example: ['ana@factorial.com',
            'juan@factorial.com'].
        team_ids (list[str] | Unset): list of team identifiers, refers to teams/teams endpoint.
            Example: ['1', '2', '3'].
        location_ids (list[str] | Unset): list of location identifiers, refers to
            locations/locations endpoint. Example: ['1', '2', '3'].
        source (list[str] | Unset): source of the candidate. Example: email.
        remote (bool | Unset): is the candidate remote? Example: True.
        job_posting_ids (list[str] | Unset): list of job posting identifiers, refers to
            ats/job_postings endpoint. Example: ['1', '2', '3'].
        minimum_average_rating (float | Unset): minimum average rating of the candidate. Example:
            4.
        active (bool | Unset): is the candidate active? Example: True.
        talent_pool (bool | Unset): is the candidate part of talent pool? Example: True.
        archived (bool | Unset): is the candidate archived? Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAtsCandidatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            emails=emails,
            team_ids=team_ids,
            location_ids=location_ids,
            source=source,
            remote=remote,
            job_posting_ids=job_posting_ids,
            minimum_average_rating=minimum_average_rating,
            active=active,
            talent_pool=talent_pool,
            archived=archived,
        )
    ).parsed
