from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_ats_evaluation_forms_response_200 import (
    GetApi20260401ResourcesAtsEvaluationFormsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_ids: list[int] | Unset = UNSET,
    template: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_ats_job_posting_ids: list[int] | Unset = UNSET
    if not isinstance(ats_job_posting_ids, Unset):
        json_ats_job_posting_ids = ats_job_posting_ids

    params["ats_job_posting_ids[]"] = json_ats_job_posting_ids

    params["template"] = template

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/ats/evaluation_forms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesAtsEvaluationFormsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesAtsEvaluationFormsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesAtsEvaluationFormsResponse200]:
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
    ats_job_posting_ids: list[int] | Unset = UNSET,
    template: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesAtsEvaluationFormsResponse200]:
    """Reads all Evaluation forms

     Reads all Evaluation forms

    Args:
        ids (list[int] | Unset): List of IDs of the evaluation forms to be fetched. Example: [1,
            2, 3].
        ats_job_posting_ids (list[int] | Unset): List of IDs of the job postings to filter the
            evaluation forms by. Example: [1, 2, 3].
        template (bool | Unset): If true, only the evaluation forms that are templates will be
            fetched. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesAtsEvaluationFormsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        ats_job_posting_ids=ats_job_posting_ids,
        template=template,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_ids: list[int] | Unset = UNSET,
    template: bool | Unset = UNSET,
) -> GetApi20260401ResourcesAtsEvaluationFormsResponse200 | None:
    """Reads all Evaluation forms

     Reads all Evaluation forms

    Args:
        ids (list[int] | Unset): List of IDs of the evaluation forms to be fetched. Example: [1,
            2, 3].
        ats_job_posting_ids (list[int] | Unset): List of IDs of the job postings to filter the
            evaluation forms by. Example: [1, 2, 3].
        template (bool | Unset): If true, only the evaluation forms that are templates will be
            fetched. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesAtsEvaluationFormsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        ats_job_posting_ids=ats_job_posting_ids,
        template=template,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_ids: list[int] | Unset = UNSET,
    template: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesAtsEvaluationFormsResponse200]:
    """Reads all Evaluation forms

     Reads all Evaluation forms

    Args:
        ids (list[int] | Unset): List of IDs of the evaluation forms to be fetched. Example: [1,
            2, 3].
        ats_job_posting_ids (list[int] | Unset): List of IDs of the job postings to filter the
            evaluation forms by. Example: [1, 2, 3].
        template (bool | Unset): If true, only the evaluation forms that are templates will be
            fetched. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesAtsEvaluationFormsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        ats_job_posting_ids=ats_job_posting_ids,
        template=template,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    ats_job_posting_ids: list[int] | Unset = UNSET,
    template: bool | Unset = UNSET,
) -> GetApi20260401ResourcesAtsEvaluationFormsResponse200 | None:
    """Reads all Evaluation forms

     Reads all Evaluation forms

    Args:
        ids (list[int] | Unset): List of IDs of the evaluation forms to be fetched. Example: [1,
            2, 3].
        ats_job_posting_ids (list[int] | Unset): List of IDs of the job postings to filter the
            evaluation forms by. Example: [1, 2, 3].
        template (bool | Unset): If true, only the evaluation forms that are templates will be
            fetched. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesAtsEvaluationFormsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            ats_job_posting_ids=ats_job_posting_ids,
            template=template,
        )
    ).parsed
