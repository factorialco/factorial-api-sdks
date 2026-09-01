from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_ats_feedbacks_response_200 import (
    GetApi20261001ResourcesAtsFeedbacksResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    ats_application_ids: list[str] | Unset = UNSET,
    ats_candidate_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_ats_application_ids: list[str] | Unset = UNSET
    if not isinstance(ats_application_ids, Unset):
        json_ats_application_ids = ats_application_ids

    params["ats_application_ids[]"] = json_ats_application_ids

    params["ats_candidate_id"] = ats_candidate_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/ats/feedbacks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesAtsFeedbacksResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesAtsFeedbacksResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesAtsFeedbacksResponse200]:
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
    ats_application_ids: list[str] | Unset = UNSET,
    ats_candidate_id: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesAtsFeedbacksResponse200]:
    """Reads all Feedbacks

     This endpoint retrieves all feedbacks associated with a candidate's applications.

    Args:
        ids (list[str] | Unset): retrieve only the feedbacks that match the IDs passed in the
            request. Example: ['1', '2', '3'].
        ats_application_ids (list[str] | Unset): filter feedbacks based on multiple application
            IDs. Example: ['1', '2', '3'].
        ats_candidate_id (str | Unset): fetch feedbacks related to a specific candidate. Example:
            [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAtsFeedbacksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        ats_application_ids=ats_application_ids,
        ats_candidate_id=ats_candidate_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    ats_application_ids: list[str] | Unset = UNSET,
    ats_candidate_id: str | Unset = UNSET,
) -> GetApi20261001ResourcesAtsFeedbacksResponse200 | None:
    """Reads all Feedbacks

     This endpoint retrieves all feedbacks associated with a candidate's applications.

    Args:
        ids (list[str] | Unset): retrieve only the feedbacks that match the IDs passed in the
            request. Example: ['1', '2', '3'].
        ats_application_ids (list[str] | Unset): filter feedbacks based on multiple application
            IDs. Example: ['1', '2', '3'].
        ats_candidate_id (str | Unset): fetch feedbacks related to a specific candidate. Example:
            [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAtsFeedbacksResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        ats_application_ids=ats_application_ids,
        ats_candidate_id=ats_candidate_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    ats_application_ids: list[str] | Unset = UNSET,
    ats_candidate_id: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesAtsFeedbacksResponse200]:
    """Reads all Feedbacks

     This endpoint retrieves all feedbacks associated with a candidate's applications.

    Args:
        ids (list[str] | Unset): retrieve only the feedbacks that match the IDs passed in the
            request. Example: ['1', '2', '3'].
        ats_application_ids (list[str] | Unset): filter feedbacks based on multiple application
            IDs. Example: ['1', '2', '3'].
        ats_candidate_id (str | Unset): fetch feedbacks related to a specific candidate. Example:
            [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAtsFeedbacksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        ats_application_ids=ats_application_ids,
        ats_candidate_id=ats_candidate_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    ats_application_ids: list[str] | Unset = UNSET,
    ats_candidate_id: str | Unset = UNSET,
) -> GetApi20261001ResourcesAtsFeedbacksResponse200 | None:
    """Reads all Feedbacks

     This endpoint retrieves all feedbacks associated with a candidate's applications.

    Args:
        ids (list[str] | Unset): retrieve only the feedbacks that match the IDs passed in the
            request. Example: ['1', '2', '3'].
        ats_application_ids (list[str] | Unset): filter feedbacks based on multiple application
            IDs. Example: ['1', '2', '3'].
        ats_candidate_id (str | Unset): fetch feedbacks related to a specific candidate. Example:
            [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAtsFeedbacksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            ats_application_ids=ats_application_ids,
            ats_candidate_id=ats_candidate_id,
        )
    ).parsed
