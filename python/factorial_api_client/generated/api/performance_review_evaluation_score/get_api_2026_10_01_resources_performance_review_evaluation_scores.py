from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_performance_review_evaluation_scores_response_200 import (
    GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200,
)
from ...models.get_api_20261001_resources_performance_review_evaluation_scores_reviewer_strategies import (
    GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    review_process_ids: list[str] | Unset = UNSET,
    review_evaluation_ids: list[str] | Unset = UNSET,
    target_access_ids: list[str] | Unset = UNSET,
    reviewer_strategies: GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies
    | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_review_process_ids: list[str] | Unset = UNSET
    if not isinstance(review_process_ids, Unset):
        json_review_process_ids = review_process_ids

    params["review_process_ids[]"] = json_review_process_ids

    json_review_evaluation_ids: list[str] | Unset = UNSET
    if not isinstance(review_evaluation_ids, Unset):
        json_review_evaluation_ids = review_evaluation_ids

    params["review_evaluation_ids[]"] = json_review_evaluation_ids

    json_target_access_ids: list[str] | Unset = UNSET
    if not isinstance(target_access_ids, Unset):
        json_target_access_ids = target_access_ids

    params["target_access_ids[]"] = json_target_access_ids

    json_reviewer_strategies: str | Unset = UNSET
    if not isinstance(reviewer_strategies, Unset):
        json_reviewer_strategies = reviewer_strategies.value

    params["reviewer_strategies[]"] = json_reviewer_strategies

    json_review_process_target_ids: list[str] | Unset = UNSET
    if not isinstance(review_process_target_ids, Unset):
        json_review_process_target_ids = review_process_target_ids

    params["review_process_target_ids[]"] = json_review_process_target_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/performance/review_evaluation_scores",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200.from_dict(
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
) -> Response[GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200]:
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
    review_process_ids: list[str] | Unset = UNSET,
    review_evaluation_ids: list[str] | Unset = UNSET,
    target_access_ids: list[str] | Unset = UNSET,
    reviewer_strategies: GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies
    | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200]:
    """Reads all Review evaluation scores

     Retrieves the published evaluation scores of performance reviews.

    Args:
        ids (list[str] | Unset): Filter by evaluation score IDs Example: ['1', '2', '3'].
        review_process_ids (list[str] | Unset): Filter by review process IDs Example: ['1', '2',
            '3'].
        review_evaluation_ids (list[str] | Unset): Filter by evaluation IDs Example: ['1', '2',
            '3'].
        target_access_ids (list[str] | Unset): Filter by employee access IDs Example: ['1', '2',
            '3'].
        reviewer_strategies
            (GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies | Unset):
            Filter by who scored the employee Example: ['self', 'manager'].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs
            Example: ['1-1', '1-2', '1-3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        review_process_ids=review_process_ids,
        review_evaluation_ids=review_evaluation_ids,
        target_access_ids=target_access_ids,
        reviewer_strategies=reviewer_strategies,
        review_process_target_ids=review_process_target_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    review_process_ids: list[str] | Unset = UNSET,
    review_evaluation_ids: list[str] | Unset = UNSET,
    target_access_ids: list[str] | Unset = UNSET,
    reviewer_strategies: GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies
    | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200 | None:
    """Reads all Review evaluation scores

     Retrieves the published evaluation scores of performance reviews.

    Args:
        ids (list[str] | Unset): Filter by evaluation score IDs Example: ['1', '2', '3'].
        review_process_ids (list[str] | Unset): Filter by review process IDs Example: ['1', '2',
            '3'].
        review_evaluation_ids (list[str] | Unset): Filter by evaluation IDs Example: ['1', '2',
            '3'].
        target_access_ids (list[str] | Unset): Filter by employee access IDs Example: ['1', '2',
            '3'].
        reviewer_strategies
            (GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies | Unset):
            Filter by who scored the employee Example: ['self', 'manager'].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs
            Example: ['1-1', '1-2', '1-3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        review_process_ids=review_process_ids,
        review_evaluation_ids=review_evaluation_ids,
        target_access_ids=target_access_ids,
        reviewer_strategies=reviewer_strategies,
        review_process_target_ids=review_process_target_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    review_process_ids: list[str] | Unset = UNSET,
    review_evaluation_ids: list[str] | Unset = UNSET,
    target_access_ids: list[str] | Unset = UNSET,
    reviewer_strategies: GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies
    | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200]:
    """Reads all Review evaluation scores

     Retrieves the published evaluation scores of performance reviews.

    Args:
        ids (list[str] | Unset): Filter by evaluation score IDs Example: ['1', '2', '3'].
        review_process_ids (list[str] | Unset): Filter by review process IDs Example: ['1', '2',
            '3'].
        review_evaluation_ids (list[str] | Unset): Filter by evaluation IDs Example: ['1', '2',
            '3'].
        target_access_ids (list[str] | Unset): Filter by employee access IDs Example: ['1', '2',
            '3'].
        reviewer_strategies
            (GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies | Unset):
            Filter by who scored the employee Example: ['self', 'manager'].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs
            Example: ['1-1', '1-2', '1-3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        review_process_ids=review_process_ids,
        review_evaluation_ids=review_evaluation_ids,
        target_access_ids=target_access_ids,
        reviewer_strategies=reviewer_strategies,
        review_process_target_ids=review_process_target_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    review_process_ids: list[str] | Unset = UNSET,
    review_evaluation_ids: list[str] | Unset = UNSET,
    target_access_ids: list[str] | Unset = UNSET,
    reviewer_strategies: GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies
    | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200 | None:
    """Reads all Review evaluation scores

     Retrieves the published evaluation scores of performance reviews.

    Args:
        ids (list[str] | Unset): Filter by evaluation score IDs Example: ['1', '2', '3'].
        review_process_ids (list[str] | Unset): Filter by review process IDs Example: ['1', '2',
            '3'].
        review_evaluation_ids (list[str] | Unset): Filter by evaluation IDs Example: ['1', '2',
            '3'].
        target_access_ids (list[str] | Unset): Filter by employee access IDs Example: ['1', '2',
            '3'].
        reviewer_strategies
            (GetApi20261001ResourcesPerformanceReviewEvaluationScoresReviewerStrategies | Unset):
            Filter by who scored the employee Example: ['self', 'manager'].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs
            Example: ['1-1', '1-2', '1-3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesPerformanceReviewEvaluationScoresResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            review_process_ids=review_process_ids,
            review_evaluation_ids=review_evaluation_ids,
            target_access_ids=target_access_ids,
            reviewer_strategies=reviewer_strategies,
            review_process_target_ids=review_process_target_ids,
        )
    ).parsed
