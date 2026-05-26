from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_performance_review_evaluations_response_200 import (
    GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200,
)
from ...models.get_api_20251001_resources_performance_review_evaluations_reviewer_strategies import (
    GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies,
)
from ...models.get_api_20251001_resources_performance_review_evaluations_with_targets_managed_by_filter import (
    GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    performance_review_process_ids: list[int] | Unset = UNSET,
    published: bool | Unset = UNSET,
    reviewer_ids: list[int] | Unset = UNSET,
    reviewer_strategies: GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
    | Unset = UNSET,
    target_access_ids: list[int] | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
    with_targets_managed_by_filter: GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter
    | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_performance_review_process_ids: list[int] | Unset = UNSET
    if not isinstance(performance_review_process_ids, Unset):
        json_performance_review_process_ids = performance_review_process_ids

    params["performance_review_process_ids[]"] = json_performance_review_process_ids

    params["published"] = published

    json_reviewer_ids: list[int] | Unset = UNSET
    if not isinstance(reviewer_ids, Unset):
        json_reviewer_ids = reviewer_ids

    params["reviewer_ids[]"] = json_reviewer_ids

    json_reviewer_strategies: str | Unset = UNSET
    if not isinstance(reviewer_strategies, Unset):
        json_reviewer_strategies = reviewer_strategies.value

    params["reviewer_strategies[]"] = json_reviewer_strategies

    json_target_access_ids: list[int] | Unset = UNSET
    if not isinstance(target_access_ids, Unset):
        json_target_access_ids = target_access_ids

    params["target_access_ids[]"] = json_target_access_ids

    json_review_process_target_ids: list[str] | Unset = UNSET
    if not isinstance(review_process_target_ids, Unset):
        json_review_process_target_ids = review_process_target_ids

    params["review_process_target_ids[]"] = json_review_process_target_ids

    json_with_targets_managed_by_filter: dict[str, Any] | Unset = UNSET
    if not isinstance(with_targets_managed_by_filter, Unset):
        json_with_targets_managed_by_filter = with_targets_managed_by_filter.to_dict()
    if not isinstance(json_with_targets_managed_by_filter, Unset):
        params.update(json_with_targets_managed_by_filter)

    json_exclude_ids: list[int] | Unset = UNSET
    if not isinstance(exclude_ids, Unset):
        json_exclude_ids = exclude_ids

    params["exclude_ids[]"] = json_exclude_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/performance/review_evaluations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200]:
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
    performance_review_process_ids: list[int] | Unset = UNSET,
    published: bool | Unset = UNSET,
    reviewer_ids: list[int] | Unset = UNSET,
    reviewer_strategies: GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
    | Unset = UNSET,
    target_access_ids: list[int] | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
    with_targets_managed_by_filter: GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter
    | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200]:
    r"""Reads all Review evaluations

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        ids (list[int] | Unset): Filter by evaluation IDs Example: [1, 2, 3].
        performance_review_process_ids (list[int] | Unset): Filter by review process IDs Example:
            [1, 2, 3].
        published (bool | Unset): Only published or unpublished evaluations Example: True.
        reviewer_ids (list[int] | Unset): Filter by reviewer access IDs Example: [1, 2, 3].
        reviewer_strategies (GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
            | Unset): Filter by reviewer strategies Example: ['manager', 'peer'].
        target_access_ids (list[int] | Unset): Filter by participant access IDs Example: [1, 2,
            3].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs.
            Composite key format: review_process_id-target_access_id Example: ['1-1', '1-2', '1-3'].
        with_targets_managed_by_filter
            (GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter | Unset):
            Only evaluations where the participant is managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.
        exclude_ids (list[int] | Unset): Exclude evaluations by IDs Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        performance_review_process_ids=performance_review_process_ids,
        published=published,
        reviewer_ids=reviewer_ids,
        reviewer_strategies=reviewer_strategies,
        target_access_ids=target_access_ids,
        review_process_target_ids=review_process_target_ids,
        with_targets_managed_by_filter=with_targets_managed_by_filter,
        exclude_ids=exclude_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    performance_review_process_ids: list[int] | Unset = UNSET,
    published: bool | Unset = UNSET,
    reviewer_ids: list[int] | Unset = UNSET,
    reviewer_strategies: GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
    | Unset = UNSET,
    target_access_ids: list[int] | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
    with_targets_managed_by_filter: GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter
    | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200 | None:
    r"""Reads all Review evaluations

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        ids (list[int] | Unset): Filter by evaluation IDs Example: [1, 2, 3].
        performance_review_process_ids (list[int] | Unset): Filter by review process IDs Example:
            [1, 2, 3].
        published (bool | Unset): Only published or unpublished evaluations Example: True.
        reviewer_ids (list[int] | Unset): Filter by reviewer access IDs Example: [1, 2, 3].
        reviewer_strategies (GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
            | Unset): Filter by reviewer strategies Example: ['manager', 'peer'].
        target_access_ids (list[int] | Unset): Filter by participant access IDs Example: [1, 2,
            3].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs.
            Composite key format: review_process_id-target_access_id Example: ['1-1', '1-2', '1-3'].
        with_targets_managed_by_filter
            (GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter | Unset):
            Only evaluations where the participant is managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.
        exclude_ids (list[int] | Unset): Exclude evaluations by IDs Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        performance_review_process_ids=performance_review_process_ids,
        published=published,
        reviewer_ids=reviewer_ids,
        reviewer_strategies=reviewer_strategies,
        target_access_ids=target_access_ids,
        review_process_target_ids=review_process_target_ids,
        with_targets_managed_by_filter=with_targets_managed_by_filter,
        exclude_ids=exclude_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    performance_review_process_ids: list[int] | Unset = UNSET,
    published: bool | Unset = UNSET,
    reviewer_ids: list[int] | Unset = UNSET,
    reviewer_strategies: GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
    | Unset = UNSET,
    target_access_ids: list[int] | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
    with_targets_managed_by_filter: GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter
    | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200]:
    r"""Reads all Review evaluations

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        ids (list[int] | Unset): Filter by evaluation IDs Example: [1, 2, 3].
        performance_review_process_ids (list[int] | Unset): Filter by review process IDs Example:
            [1, 2, 3].
        published (bool | Unset): Only published or unpublished evaluations Example: True.
        reviewer_ids (list[int] | Unset): Filter by reviewer access IDs Example: [1, 2, 3].
        reviewer_strategies (GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
            | Unset): Filter by reviewer strategies Example: ['manager', 'peer'].
        target_access_ids (list[int] | Unset): Filter by participant access IDs Example: [1, 2,
            3].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs.
            Composite key format: review_process_id-target_access_id Example: ['1-1', '1-2', '1-3'].
        with_targets_managed_by_filter
            (GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter | Unset):
            Only evaluations where the participant is managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.
        exclude_ids (list[int] | Unset): Exclude evaluations by IDs Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        performance_review_process_ids=performance_review_process_ids,
        published=published,
        reviewer_ids=reviewer_ids,
        reviewer_strategies=reviewer_strategies,
        target_access_ids=target_access_ids,
        review_process_target_ids=review_process_target_ids,
        with_targets_managed_by_filter=with_targets_managed_by_filter,
        exclude_ids=exclude_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    performance_review_process_ids: list[int] | Unset = UNSET,
    published: bool | Unset = UNSET,
    reviewer_ids: list[int] | Unset = UNSET,
    reviewer_strategies: GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
    | Unset = UNSET,
    target_access_ids: list[int] | Unset = UNSET,
    review_process_target_ids: list[str] | Unset = UNSET,
    with_targets_managed_by_filter: GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter
    | Unset = UNSET,
    exclude_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200 | None:
    r"""Reads all Review evaluations

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        ids (list[int] | Unset): Filter by evaluation IDs Example: [1, 2, 3].
        performance_review_process_ids (list[int] | Unset): Filter by review process IDs Example:
            [1, 2, 3].
        published (bool | Unset): Only published or unpublished evaluations Example: True.
        reviewer_ids (list[int] | Unset): Filter by reviewer access IDs Example: [1, 2, 3].
        reviewer_strategies (GetApi20251001ResourcesPerformanceReviewEvaluationsReviewerStrategies
            | Unset): Filter by reviewer strategies Example: ['manager', 'peer'].
        target_access_ids (list[int] | Unset): Filter by participant access IDs Example: [1, 2,
            3].
        review_process_target_ids (list[str] | Unset): Filter by review process target IDs.
            Composite key format: review_process_id-target_access_id Example: ['1-1', '1-2', '1-3'].
        with_targets_managed_by_filter
            (GetApi20251001ResourcesPerformanceReviewEvaluationsWithTargetsManagedByFilter | Unset):
            Only evaluations where the participant is managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.
        exclude_ids (list[int] | Unset): Exclude evaluations by IDs Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesPerformanceReviewEvaluationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            performance_review_process_ids=performance_review_process_ids,
            published=published,
            reviewer_ids=reviewer_ids,
            reviewer_strategies=reviewer_strategies,
            target_access_ids=target_access_ids,
            review_process_target_ids=review_process_target_ids,
            with_targets_managed_by_filter=with_targets_managed_by_filter,
            exclude_ids=exclude_ids,
        )
    ).parsed
