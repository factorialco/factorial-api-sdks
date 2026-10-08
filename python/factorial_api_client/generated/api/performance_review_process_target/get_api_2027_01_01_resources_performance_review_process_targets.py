from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_performance_review_process_targets_agreement_completion_status import (
    GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus,
)
from ...models.get_api_20270101_resources_performance_review_process_targets_managed_by_filter import (
    GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter,
)
from ...models.get_api_20270101_resources_performance_review_process_targets_response_200 import (
    GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    only_for_peer_assignment: bool | Unset = UNSET,
    without_manager: bool | Unset = UNSET,
    performance_review_process_ids: list[str] | Unset = UNSET,
    agreement_completion_status: GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus
    | Unset = UNSET,
    pending_peer_evaluations: bool | Unset = UNSET,
    managed_by_filter: GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter
    | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_access_ids: list[str] | Unset = UNSET
    if not isinstance(access_ids, Unset):
        json_access_ids = access_ids

    params["access_ids[]"] = json_access_ids

    params["only_for_peer_assignment"] = only_for_peer_assignment

    params["without_manager"] = without_manager

    json_performance_review_process_ids: list[str] | Unset = UNSET
    if not isinstance(performance_review_process_ids, Unset):
        json_performance_review_process_ids = performance_review_process_ids

    params["performance_review_process_ids[]"] = json_performance_review_process_ids

    json_agreement_completion_status: str | Unset = UNSET
    if not isinstance(agreement_completion_status, Unset):
        json_agreement_completion_status = agreement_completion_status.value

    params["agreement_completion_status"] = json_agreement_completion_status

    params["pending_peer_evaluations"] = pending_peer_evaluations

    json_managed_by_filter: dict[str, Any] | Unset = UNSET
    if not isinstance(managed_by_filter, Unset):
        json_managed_by_filter = managed_by_filter.to_dict()
    if not isinstance(json_managed_by_filter, Unset):
        params.update(json_managed_by_filter)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/performance/review_process_targets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200]:
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
    access_ids: list[str] | Unset = UNSET,
    only_for_peer_assignment: bool | Unset = UNSET,
    without_manager: bool | Unset = UNSET,
    performance_review_process_ids: list[str] | Unset = UNSET,
    agreement_completion_status: GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus
    | Unset = UNSET,
    pending_peer_evaluations: bool | Unset = UNSET,
    managed_by_filter: GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter
    | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200]:
    """Reads all Review process targets

     Retrieves the participants of active review processes.

    Args:
        ids (list[str] | Unset): Filter by review process target IDs Example: ['1-1', '1-2',
            '1-3'].
        access_ids (list[str] | Unset): Filter by access IDs Example: ['1', '2', '3'].
        only_for_peer_assignment (bool | Unset): Only participants for peer assignment
        without_manager (bool | Unset): Only participants with no manager assigned
        performance_review_process_ids (list[str] | Unset): Filter by reviewer process IDs
            Example: ['1', '2', '3'].
        agreement_completion_status
            (GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus | Unset):
            Filter by agreement status Example: canbeinitiated.
        pending_peer_evaluations (bool | Unset): Only participants with no peer evaluations
        managed_by_filter (GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter |
            Unset): Only participants managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        access_ids=access_ids,
        only_for_peer_assignment=only_for_peer_assignment,
        without_manager=without_manager,
        performance_review_process_ids=performance_review_process_ids,
        agreement_completion_status=agreement_completion_status,
        pending_peer_evaluations=pending_peer_evaluations,
        managed_by_filter=managed_by_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    only_for_peer_assignment: bool | Unset = UNSET,
    without_manager: bool | Unset = UNSET,
    performance_review_process_ids: list[str] | Unset = UNSET,
    agreement_completion_status: GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus
    | Unset = UNSET,
    pending_peer_evaluations: bool | Unset = UNSET,
    managed_by_filter: GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter
    | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200 | None:
    """Reads all Review process targets

     Retrieves the participants of active review processes.

    Args:
        ids (list[str] | Unset): Filter by review process target IDs Example: ['1-1', '1-2',
            '1-3'].
        access_ids (list[str] | Unset): Filter by access IDs Example: ['1', '2', '3'].
        only_for_peer_assignment (bool | Unset): Only participants for peer assignment
        without_manager (bool | Unset): Only participants with no manager assigned
        performance_review_process_ids (list[str] | Unset): Filter by reviewer process IDs
            Example: ['1', '2', '3'].
        agreement_completion_status
            (GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus | Unset):
            Filter by agreement status Example: canbeinitiated.
        pending_peer_evaluations (bool | Unset): Only participants with no peer evaluations
        managed_by_filter (GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter |
            Unset): Only participants managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        access_ids=access_ids,
        only_for_peer_assignment=only_for_peer_assignment,
        without_manager=without_manager,
        performance_review_process_ids=performance_review_process_ids,
        agreement_completion_status=agreement_completion_status,
        pending_peer_evaluations=pending_peer_evaluations,
        managed_by_filter=managed_by_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    only_for_peer_assignment: bool | Unset = UNSET,
    without_manager: bool | Unset = UNSET,
    performance_review_process_ids: list[str] | Unset = UNSET,
    agreement_completion_status: GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus
    | Unset = UNSET,
    pending_peer_evaluations: bool | Unset = UNSET,
    managed_by_filter: GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter
    | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200]:
    """Reads all Review process targets

     Retrieves the participants of active review processes.

    Args:
        ids (list[str] | Unset): Filter by review process target IDs Example: ['1-1', '1-2',
            '1-3'].
        access_ids (list[str] | Unset): Filter by access IDs Example: ['1', '2', '3'].
        only_for_peer_assignment (bool | Unset): Only participants for peer assignment
        without_manager (bool | Unset): Only participants with no manager assigned
        performance_review_process_ids (list[str] | Unset): Filter by reviewer process IDs
            Example: ['1', '2', '3'].
        agreement_completion_status
            (GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus | Unset):
            Filter by agreement status Example: canbeinitiated.
        pending_peer_evaluations (bool | Unset): Only participants with no peer evaluations
        managed_by_filter (GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter |
            Unset): Only participants managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        access_ids=access_ids,
        only_for_peer_assignment=only_for_peer_assignment,
        without_manager=without_manager,
        performance_review_process_ids=performance_review_process_ids,
        agreement_completion_status=agreement_completion_status,
        pending_peer_evaluations=pending_peer_evaluations,
        managed_by_filter=managed_by_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    only_for_peer_assignment: bool | Unset = UNSET,
    without_manager: bool | Unset = UNSET,
    performance_review_process_ids: list[str] | Unset = UNSET,
    agreement_completion_status: GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus
    | Unset = UNSET,
    pending_peer_evaluations: bool | Unset = UNSET,
    managed_by_filter: GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter
    | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200 | None:
    """Reads all Review process targets

     Retrieves the participants of active review processes.

    Args:
        ids (list[str] | Unset): Filter by review process target IDs Example: ['1-1', '1-2',
            '1-3'].
        access_ids (list[str] | Unset): Filter by access IDs Example: ['1', '2', '3'].
        only_for_peer_assignment (bool | Unset): Only participants for peer assignment
        without_manager (bool | Unset): Only participants with no manager assigned
        performance_review_process_ids (list[str] | Unset): Filter by reviewer process IDs
            Example: ['1', '2', '3'].
        agreement_completion_status
            (GetApi20270101ResourcesPerformanceReviewProcessTargetsAgreementCompletionStatus | Unset):
            Filter by agreement status Example: canbeinitiated.
        pending_peer_evaluations (bool | Unset): Only participants with no peer evaluations
        managed_by_filter (GetApi20270101ResourcesPerformanceReviewProcessTargetsManagedByFilter |
            Unset): Only participants managed by the specified employee ID Example:
            {'manager_employee_id': 1, 'only_direct_reports': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesPerformanceReviewProcessTargetsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            access_ids=access_ids,
            only_for_peer_assignment=only_for_peer_assignment,
            without_manager=without_manager,
            performance_review_process_ids=performance_review_process_ids,
            agreement_completion_status=agreement_completion_status,
            pending_peer_evaluations=pending_peer_evaluations,
            managed_by_filter=managed_by_filter,
        )
    ).parsed
