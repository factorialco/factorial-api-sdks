from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_ats_applications_response_200 import (
    GetApi20251001ResourcesAtsApplicationsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_id: int | Unset = UNSET,
    qualified: bool | Unset = UNSET,
    ats_application_phase_id: int | Unset = UNSET,
    ats_candidate_ids: list[int] | Unset = UNSET,
    ats_rejection_reason_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    ats_tags_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["ats_job_posting_id"] = ats_job_posting_id

    params["qualified"] = qualified

    params["ats_application_phase_id"] = ats_application_phase_id

    json_ats_candidate_ids: list[int] | Unset = UNSET
    if not isinstance(ats_candidate_ids, Unset):
        json_ats_candidate_ids = ats_candidate_ids

    params["ats_candidate_ids[]"] = json_ats_candidate_ids

    json_ats_rejection_reason_ids: list[int] | Unset = UNSET
    if not isinstance(ats_rejection_reason_ids, Unset):
        json_ats_rejection_reason_ids = ats_rejection_reason_ids

    params["ats_rejection_reason_ids[]"] = json_ats_rejection_reason_ids

    params["search"] = search

    json_ats_tags_ids: list[int] | Unset = UNSET
    if not isinstance(ats_tags_ids, Unset):
        json_ats_tags_ids = ats_tags_ids

    params["ats_tags_ids[]"] = json_ats_tags_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/ats/applications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesAtsApplicationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesAtsApplicationsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesAtsApplicationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_id: int | Unset = UNSET,
    qualified: bool | Unset = UNSET,
    ats_application_phase_id: int | Unset = UNSET,
    ats_candidate_ids: list[int] | Unset = UNSET,
    ats_rejection_reason_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    ats_tags_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesAtsApplicationsResponse200]:
    """Reads all Applications

     Reads all Applications

    Args:
        ids (list[int] | Unset): Application ids to retrieve Example: [1, 2].
        ats_job_posting_id (int | Unset): Application job posting id to retrieve Example: 1.
        qualified (bool | Unset): Retrieve applications by their qualified status Example: True.
        ats_application_phase_id (int | Unset): Application phase id Example: 1.
        ats_candidate_ids (list[int] | Unset): Application candidates ids Example: [1, 2].
        ats_rejection_reason_ids (list[int] | Unset): Application rejection reason ids Example:
            [1, 2].
        search (str | Unset): Application search Example: application.
        ats_tags_ids (list[int] | Unset): Application tag ids Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesAtsApplicationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        ats_job_posting_id=ats_job_posting_id,
        qualified=qualified,
        ats_application_phase_id=ats_application_phase_id,
        ats_candidate_ids=ats_candidate_ids,
        ats_rejection_reason_ids=ats_rejection_reason_ids,
        search=search,
        ats_tags_ids=ats_tags_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_id: int | Unset = UNSET,
    qualified: bool | Unset = UNSET,
    ats_application_phase_id: int | Unset = UNSET,
    ats_candidate_ids: list[int] | Unset = UNSET,
    ats_rejection_reason_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    ats_tags_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesAtsApplicationsResponse200 | None:
    """Reads all Applications

     Reads all Applications

    Args:
        ids (list[int] | Unset): Application ids to retrieve Example: [1, 2].
        ats_job_posting_id (int | Unset): Application job posting id to retrieve Example: 1.
        qualified (bool | Unset): Retrieve applications by their qualified status Example: True.
        ats_application_phase_id (int | Unset): Application phase id Example: 1.
        ats_candidate_ids (list[int] | Unset): Application candidates ids Example: [1, 2].
        ats_rejection_reason_ids (list[int] | Unset): Application rejection reason ids Example:
            [1, 2].
        search (str | Unset): Application search Example: application.
        ats_tags_ids (list[int] | Unset): Application tag ids Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesAtsApplicationsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        ats_job_posting_id=ats_job_posting_id,
        qualified=qualified,
        ats_application_phase_id=ats_application_phase_id,
        ats_candidate_ids=ats_candidate_ids,
        ats_rejection_reason_ids=ats_rejection_reason_ids,
        search=search,
        ats_tags_ids=ats_tags_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_id: int | Unset = UNSET,
    qualified: bool | Unset = UNSET,
    ats_application_phase_id: int | Unset = UNSET,
    ats_candidate_ids: list[int] | Unset = UNSET,
    ats_rejection_reason_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    ats_tags_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesAtsApplicationsResponse200]:
    """Reads all Applications

     Reads all Applications

    Args:
        ids (list[int] | Unset): Application ids to retrieve Example: [1, 2].
        ats_job_posting_id (int | Unset): Application job posting id to retrieve Example: 1.
        qualified (bool | Unset): Retrieve applications by their qualified status Example: True.
        ats_application_phase_id (int | Unset): Application phase id Example: 1.
        ats_candidate_ids (list[int] | Unset): Application candidates ids Example: [1, 2].
        ats_rejection_reason_ids (list[int] | Unset): Application rejection reason ids Example:
            [1, 2].
        search (str | Unset): Application search Example: application.
        ats_tags_ids (list[int] | Unset): Application tag ids Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesAtsApplicationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        ats_job_posting_id=ats_job_posting_id,
        qualified=qualified,
        ats_application_phase_id=ats_application_phase_id,
        ats_candidate_ids=ats_candidate_ids,
        ats_rejection_reason_ids=ats_rejection_reason_ids,
        search=search,
        ats_tags_ids=ats_tags_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_id: int | Unset = UNSET,
    qualified: bool | Unset = UNSET,
    ats_application_phase_id: int | Unset = UNSET,
    ats_candidate_ids: list[int] | Unset = UNSET,
    ats_rejection_reason_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    ats_tags_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesAtsApplicationsResponse200 | None:
    """Reads all Applications

     Reads all Applications

    Args:
        ids (list[int] | Unset): Application ids to retrieve Example: [1, 2].
        ats_job_posting_id (int | Unset): Application job posting id to retrieve Example: 1.
        qualified (bool | Unset): Retrieve applications by their qualified status Example: True.
        ats_application_phase_id (int | Unset): Application phase id Example: 1.
        ats_candidate_ids (list[int] | Unset): Application candidates ids Example: [1, 2].
        ats_rejection_reason_ids (list[int] | Unset): Application rejection reason ids Example:
            [1, 2].
        search (str | Unset): Application search Example: application.
        ats_tags_ids (list[int] | Unset): Application tag ids Example: [1, 2].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesAtsApplicationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            ats_job_posting_id=ats_job_posting_id,
            qualified=qualified,
            ats_application_phase_id=ats_application_phase_id,
            ats_candidate_ids=ats_candidate_ids,
            ats_rejection_reason_ids=ats_rejection_reason_ids,
            search=search,
            ats_tags_ids=ats_tags_ids,
        )
    ).parsed
