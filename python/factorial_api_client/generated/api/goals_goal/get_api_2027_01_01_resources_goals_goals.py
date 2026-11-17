from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_goals_goals_frequency import (
    GetApi20270101ResourcesGoalsGoalsFrequency,
)
from ...models.get_api_20270101_resources_goals_goals_overlaps_period import (
    GetApi20270101ResourcesGoalsGoalsOverlapsPeriod,
)
from ...models.get_api_20270101_resources_goals_goals_people_group_criteria import (
    GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria,
)
from ...models.get_api_20270101_resources_goals_goals_response_200 import (
    GetApi20270101ResourcesGoalsGoalsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    assignee_ids: list[str] | Unset = UNSET,
    manager_ids: list[str] | Unset = UNSET,
    indirect_manager_ids: list[str] | Unset = UNSET,
    assignee_search: str | Unset = UNSET,
    people_group_ids: list[str] | Unset = UNSET,
    people_group_criteria: GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset = UNSET,
    individual: bool | Unset = UNSET,
    individual_top_level: bool | Unset = UNSET,
    performance_agreement_ids: list[str] | Unset = UNSET,
    parent_ids: list[str] | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    eligible_parent_for_id: str | Unset = UNSET,
    eligible_child_for_id: str | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    overlaps_period: GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset = UNSET,
    ends_closest_to: str | Unset = UNSET,
    frequency: GetApi20270101ResourcesGoalsGoalsFrequency | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_assignee_ids: list[str] | Unset = UNSET
    if not isinstance(assignee_ids, Unset):
        json_assignee_ids = assignee_ids

    params["assignee_ids[]"] = json_assignee_ids

    json_manager_ids: list[str] | Unset = UNSET
    if not isinstance(manager_ids, Unset):
        json_manager_ids = manager_ids

    params["manager_ids[]"] = json_manager_ids

    json_indirect_manager_ids: list[str] | Unset = UNSET
    if not isinstance(indirect_manager_ids, Unset):
        json_indirect_manager_ids = indirect_manager_ids

    params["indirect_manager_ids[]"] = json_indirect_manager_ids

    params["assignee_search"] = assignee_search

    json_people_group_ids: list[str] | Unset = UNSET
    if not isinstance(people_group_ids, Unset):
        json_people_group_ids = people_group_ids

    params["people_group_ids[]"] = json_people_group_ids

    json_people_group_criteria: dict[str, Any] | Unset = UNSET
    if not isinstance(people_group_criteria, Unset):
        json_people_group_criteria = people_group_criteria.to_dict()
    if not isinstance(json_people_group_criteria, Unset):
        params.update(json_people_group_criteria)

    params["individual"] = individual

    params["individual_top_level"] = individual_top_level

    json_performance_agreement_ids: list[str] | Unset = UNSET
    if not isinstance(performance_agreement_ids, Unset):
        json_performance_agreement_ids = performance_agreement_ids

    params["performance_agreement_ids[]"] = json_performance_agreement_ids

    json_parent_ids: list[str] | Unset = UNSET
    if not isinstance(parent_ids, Unset):
        json_parent_ids = parent_ids

    params["parent_ids[]"] = json_parent_ids

    params["only_root"] = only_root

    params["eligible_parent_for_id"] = eligible_parent_for_id

    params["eligible_child_for_id"] = eligible_child_for_id

    params["start_on"] = start_on

    params["end_on"] = end_on

    json_overlaps_period: dict[str, Any] | Unset = UNSET
    if not isinstance(overlaps_period, Unset):
        json_overlaps_period = overlaps_period.to_dict()
    if not isinstance(json_overlaps_period, Unset):
        params.update(json_overlaps_period)

    params["ends_closest_to"] = ends_closest_to

    json_frequency: str | Unset = UNSET
    if not isinstance(frequency, Unset):
        json_frequency = frequency.value

    params["frequency"] = json_frequency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/goals/goals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesGoalsGoalsResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200]:
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
    assignee_ids: list[str] | Unset = UNSET,
    manager_ids: list[str] | Unset = UNSET,
    indirect_manager_ids: list[str] | Unset = UNSET,
    assignee_search: str | Unset = UNSET,
    people_group_ids: list[str] | Unset = UNSET,
    people_group_criteria: GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset = UNSET,
    individual: bool | Unset = UNSET,
    individual_top_level: bool | Unset = UNSET,
    performance_agreement_ids: list[str] | Unset = UNSET,
    parent_ids: list[str] | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    eligible_parent_for_id: str | Unset = UNSET,
    eligible_child_for_id: str | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    overlaps_period: GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset = UNSET,
    ends_closest_to: str | Unset = UNSET,
    frequency: GetApi20270101ResourcesGoalsGoalsFrequency | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200]:
    """Reads all Goals

     Retrieves goals

    Args:
        ids (list[str] | Unset): Goal ids Example: ['1'].
        assignee_ids (list[str] | Unset): Goals assigned to any of these employees Example: ['1'].
        manager_ids (list[str] | Unset): Goals assigned to the active direct reports of any of
            these employees Example: ['1'].
        indirect_manager_ids (list[str] | Unset): Goals assigned to active employees two or more
            levels below any of these employees in the reporting line Example: ['1'].
        assignee_search (str | Unset): Goals assigned to an employee whose name matches this text
            Example: Jane.
        people_group_ids (list[str] | Unset): Goals assigned to any of these people groups
            Example: ['1'].
        people_group_criteria (GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset):
            Goals whose audience matches these people group criteria, sent as nested query keys such
            as people_group_criteria[team_ids][]=1 or people_group_criteria[any_team]=true
        individual (bool | Unset): When true, only goals assigned to a single employee; when
            false, only goals assigned to a group Example: True.
        individual_top_level (bool | Unset): When true, only individual goals without a parent
            goal, ordered by assignee name
        performance_agreement_ids (list[str] | Unset): Goals linked to any of these performance
            agreements Example: ['1'].
        parent_ids (list[str] | Unset): Sub-goals of any of these goals Example: ['1'].
        only_root (bool | Unset): When true, only goals without a parent goal
        eligible_parent_for_id (str | Unset): Goals that can become the parent of this goal
            Example: 1.
        eligible_child_for_id (str | Unset): Goals that can become a sub-goal of this goal
            Example: 1.
        start_on (str | Unset): Goals that start on this date Example: 2026-01-01.
        end_on (str | Unset): Goals that end on this date Example: 2026-12-31.
        overlaps_period (GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset): Goals whose
            dates overlap this period
        ends_closest_to (str | Unset): Orders the goals by how close their end date is to this
            date Example: 2026-12-31.
        frequency (GetApi20270101ResourcesGoalsGoalsFrequency | Unset): Goals measured with this
            frequency (yearly, half_yearly, quarterly or monthly) Example: quarterly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        assignee_ids=assignee_ids,
        manager_ids=manager_ids,
        indirect_manager_ids=indirect_manager_ids,
        assignee_search=assignee_search,
        people_group_ids=people_group_ids,
        people_group_criteria=people_group_criteria,
        individual=individual,
        individual_top_level=individual_top_level,
        performance_agreement_ids=performance_agreement_ids,
        parent_ids=parent_ids,
        only_root=only_root,
        eligible_parent_for_id=eligible_parent_for_id,
        eligible_child_for_id=eligible_child_for_id,
        start_on=start_on,
        end_on=end_on,
        overlaps_period=overlaps_period,
        ends_closest_to=ends_closest_to,
        frequency=frequency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    assignee_ids: list[str] | Unset = UNSET,
    manager_ids: list[str] | Unset = UNSET,
    indirect_manager_ids: list[str] | Unset = UNSET,
    assignee_search: str | Unset = UNSET,
    people_group_ids: list[str] | Unset = UNSET,
    people_group_criteria: GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset = UNSET,
    individual: bool | Unset = UNSET,
    individual_top_level: bool | Unset = UNSET,
    performance_agreement_ids: list[str] | Unset = UNSET,
    parent_ids: list[str] | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    eligible_parent_for_id: str | Unset = UNSET,
    eligible_child_for_id: str | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    overlaps_period: GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset = UNSET,
    ends_closest_to: str | Unset = UNSET,
    frequency: GetApi20270101ResourcesGoalsGoalsFrequency | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200 | None:
    """Reads all Goals

     Retrieves goals

    Args:
        ids (list[str] | Unset): Goal ids Example: ['1'].
        assignee_ids (list[str] | Unset): Goals assigned to any of these employees Example: ['1'].
        manager_ids (list[str] | Unset): Goals assigned to the active direct reports of any of
            these employees Example: ['1'].
        indirect_manager_ids (list[str] | Unset): Goals assigned to active employees two or more
            levels below any of these employees in the reporting line Example: ['1'].
        assignee_search (str | Unset): Goals assigned to an employee whose name matches this text
            Example: Jane.
        people_group_ids (list[str] | Unset): Goals assigned to any of these people groups
            Example: ['1'].
        people_group_criteria (GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset):
            Goals whose audience matches these people group criteria, sent as nested query keys such
            as people_group_criteria[team_ids][]=1 or people_group_criteria[any_team]=true
        individual (bool | Unset): When true, only goals assigned to a single employee; when
            false, only goals assigned to a group Example: True.
        individual_top_level (bool | Unset): When true, only individual goals without a parent
            goal, ordered by assignee name
        performance_agreement_ids (list[str] | Unset): Goals linked to any of these performance
            agreements Example: ['1'].
        parent_ids (list[str] | Unset): Sub-goals of any of these goals Example: ['1'].
        only_root (bool | Unset): When true, only goals without a parent goal
        eligible_parent_for_id (str | Unset): Goals that can become the parent of this goal
            Example: 1.
        eligible_child_for_id (str | Unset): Goals that can become a sub-goal of this goal
            Example: 1.
        start_on (str | Unset): Goals that start on this date Example: 2026-01-01.
        end_on (str | Unset): Goals that end on this date Example: 2026-12-31.
        overlaps_period (GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset): Goals whose
            dates overlap this period
        ends_closest_to (str | Unset): Orders the goals by how close their end date is to this
            date Example: 2026-12-31.
        frequency (GetApi20270101ResourcesGoalsGoalsFrequency | Unset): Goals measured with this
            frequency (yearly, half_yearly, quarterly or monthly) Example: quarterly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        assignee_ids=assignee_ids,
        manager_ids=manager_ids,
        indirect_manager_ids=indirect_manager_ids,
        assignee_search=assignee_search,
        people_group_ids=people_group_ids,
        people_group_criteria=people_group_criteria,
        individual=individual,
        individual_top_level=individual_top_level,
        performance_agreement_ids=performance_agreement_ids,
        parent_ids=parent_ids,
        only_root=only_root,
        eligible_parent_for_id=eligible_parent_for_id,
        eligible_child_for_id=eligible_child_for_id,
        start_on=start_on,
        end_on=end_on,
        overlaps_period=overlaps_period,
        ends_closest_to=ends_closest_to,
        frequency=frequency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    assignee_ids: list[str] | Unset = UNSET,
    manager_ids: list[str] | Unset = UNSET,
    indirect_manager_ids: list[str] | Unset = UNSET,
    assignee_search: str | Unset = UNSET,
    people_group_ids: list[str] | Unset = UNSET,
    people_group_criteria: GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset = UNSET,
    individual: bool | Unset = UNSET,
    individual_top_level: bool | Unset = UNSET,
    performance_agreement_ids: list[str] | Unset = UNSET,
    parent_ids: list[str] | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    eligible_parent_for_id: str | Unset = UNSET,
    eligible_child_for_id: str | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    overlaps_period: GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset = UNSET,
    ends_closest_to: str | Unset = UNSET,
    frequency: GetApi20270101ResourcesGoalsGoalsFrequency | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200]:
    """Reads all Goals

     Retrieves goals

    Args:
        ids (list[str] | Unset): Goal ids Example: ['1'].
        assignee_ids (list[str] | Unset): Goals assigned to any of these employees Example: ['1'].
        manager_ids (list[str] | Unset): Goals assigned to the active direct reports of any of
            these employees Example: ['1'].
        indirect_manager_ids (list[str] | Unset): Goals assigned to active employees two or more
            levels below any of these employees in the reporting line Example: ['1'].
        assignee_search (str | Unset): Goals assigned to an employee whose name matches this text
            Example: Jane.
        people_group_ids (list[str] | Unset): Goals assigned to any of these people groups
            Example: ['1'].
        people_group_criteria (GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset):
            Goals whose audience matches these people group criteria, sent as nested query keys such
            as people_group_criteria[team_ids][]=1 or people_group_criteria[any_team]=true
        individual (bool | Unset): When true, only goals assigned to a single employee; when
            false, only goals assigned to a group Example: True.
        individual_top_level (bool | Unset): When true, only individual goals without a parent
            goal, ordered by assignee name
        performance_agreement_ids (list[str] | Unset): Goals linked to any of these performance
            agreements Example: ['1'].
        parent_ids (list[str] | Unset): Sub-goals of any of these goals Example: ['1'].
        only_root (bool | Unset): When true, only goals without a parent goal
        eligible_parent_for_id (str | Unset): Goals that can become the parent of this goal
            Example: 1.
        eligible_child_for_id (str | Unset): Goals that can become a sub-goal of this goal
            Example: 1.
        start_on (str | Unset): Goals that start on this date Example: 2026-01-01.
        end_on (str | Unset): Goals that end on this date Example: 2026-12-31.
        overlaps_period (GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset): Goals whose
            dates overlap this period
        ends_closest_to (str | Unset): Orders the goals by how close their end date is to this
            date Example: 2026-12-31.
        frequency (GetApi20270101ResourcesGoalsGoalsFrequency | Unset): Goals measured with this
            frequency (yearly, half_yearly, quarterly or monthly) Example: quarterly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        assignee_ids=assignee_ids,
        manager_ids=manager_ids,
        indirect_manager_ids=indirect_manager_ids,
        assignee_search=assignee_search,
        people_group_ids=people_group_ids,
        people_group_criteria=people_group_criteria,
        individual=individual,
        individual_top_level=individual_top_level,
        performance_agreement_ids=performance_agreement_ids,
        parent_ids=parent_ids,
        only_root=only_root,
        eligible_parent_for_id=eligible_parent_for_id,
        eligible_child_for_id=eligible_child_for_id,
        start_on=start_on,
        end_on=end_on,
        overlaps_period=overlaps_period,
        ends_closest_to=ends_closest_to,
        frequency=frequency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    assignee_ids: list[str] | Unset = UNSET,
    manager_ids: list[str] | Unset = UNSET,
    indirect_manager_ids: list[str] | Unset = UNSET,
    assignee_search: str | Unset = UNSET,
    people_group_ids: list[str] | Unset = UNSET,
    people_group_criteria: GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset = UNSET,
    individual: bool | Unset = UNSET,
    individual_top_level: bool | Unset = UNSET,
    performance_agreement_ids: list[str] | Unset = UNSET,
    parent_ids: list[str] | Unset = UNSET,
    only_root: bool | Unset = UNSET,
    eligible_parent_for_id: str | Unset = UNSET,
    eligible_child_for_id: str | Unset = UNSET,
    start_on: str | Unset = UNSET,
    end_on: str | Unset = UNSET,
    overlaps_period: GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset = UNSET,
    ends_closest_to: str | Unset = UNSET,
    frequency: GetApi20270101ResourcesGoalsGoalsFrequency | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200 | None:
    """Reads all Goals

     Retrieves goals

    Args:
        ids (list[str] | Unset): Goal ids Example: ['1'].
        assignee_ids (list[str] | Unset): Goals assigned to any of these employees Example: ['1'].
        manager_ids (list[str] | Unset): Goals assigned to the active direct reports of any of
            these employees Example: ['1'].
        indirect_manager_ids (list[str] | Unset): Goals assigned to active employees two or more
            levels below any of these employees in the reporting line Example: ['1'].
        assignee_search (str | Unset): Goals assigned to an employee whose name matches this text
            Example: Jane.
        people_group_ids (list[str] | Unset): Goals assigned to any of these people groups
            Example: ['1'].
        people_group_criteria (GetApi20270101ResourcesGoalsGoalsPeopleGroupCriteria | Unset):
            Goals whose audience matches these people group criteria, sent as nested query keys such
            as people_group_criteria[team_ids][]=1 or people_group_criteria[any_team]=true
        individual (bool | Unset): When true, only goals assigned to a single employee; when
            false, only goals assigned to a group Example: True.
        individual_top_level (bool | Unset): When true, only individual goals without a parent
            goal, ordered by assignee name
        performance_agreement_ids (list[str] | Unset): Goals linked to any of these performance
            agreements Example: ['1'].
        parent_ids (list[str] | Unset): Sub-goals of any of these goals Example: ['1'].
        only_root (bool | Unset): When true, only goals without a parent goal
        eligible_parent_for_id (str | Unset): Goals that can become the parent of this goal
            Example: 1.
        eligible_child_for_id (str | Unset): Goals that can become a sub-goal of this goal
            Example: 1.
        start_on (str | Unset): Goals that start on this date Example: 2026-01-01.
        end_on (str | Unset): Goals that end on this date Example: 2026-12-31.
        overlaps_period (GetApi20270101ResourcesGoalsGoalsOverlapsPeriod | Unset): Goals whose
            dates overlap this period
        ends_closest_to (str | Unset): Orders the goals by how close their end date is to this
            date Example: 2026-12-31.
        frequency (GetApi20270101ResourcesGoalsGoalsFrequency | Unset): Goals measured with this
            frequency (yearly, half_yearly, quarterly or monthly) Example: quarterly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesGoalsGoalsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            assignee_ids=assignee_ids,
            manager_ids=manager_ids,
            indirect_manager_ids=indirect_manager_ids,
            assignee_search=assignee_search,
            people_group_ids=people_group_ids,
            people_group_criteria=people_group_criteria,
            individual=individual,
            individual_top_level=individual_top_level,
            performance_agreement_ids=performance_agreement_ids,
            parent_ids=parent_ids,
            only_root=only_root,
            eligible_parent_for_id=eligible_parent_for_id,
            eligible_child_for_id=eligible_child_for_id,
            start_on=start_on,
            end_on=end_on,
            overlaps_period=overlaps_period,
            ends_closest_to=ends_closest_to,
            frequency=frequency,
        )
    ).parsed
