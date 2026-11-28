from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.goals_goal import GoalsGoal
from ...models.post_api_20270101_resources_goals_goals_update_progress_body import (
    PostApi20270101ResourcesGoalsGoalsUpdateProgressBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/goals/goals/update_progress",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GoalsGoal | None:
    if response.status_code == 200:
        response_200 = GoalsGoal.from_dict(response.json())

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
) -> Response[ErrorResponse | GoalsGoal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset = UNSET,
) -> Response[ErrorResponse | GoalsGoal]:
    """Records a goal's progress

     Records a new attainment value for a goal, as the Update progress action does in Factorial.
    Each call adds an entry to the goal's progress history and returns the updated goal.

    A call made with a company API key or a company-level OAuth token must name, in author_id,
    the active employee the update is recorded as. The update is authorized with that
    employee's permissions, so name an employee who may update the goal, such as an admin.
    A call made with a user's OAuth token is recorded as that user; author_id may be left out
    or must name that user.

    The request is refused with 403 when author_id is missing on a company call, does not name
    an active employee of the company, names someone else on a user call, or names an employee
    who may not update the goal. A goal tracked by its sub-goals cannot be updated, because its
    value rolls up from them. A goal without a target value cannot be updated, and a
    qualitative goal only accepts 0 (not achieved) or 100 (achieved).

    Args:
        body (PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoalsGoal]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset = UNSET,
) -> ErrorResponse | GoalsGoal | None:
    """Records a goal's progress

     Records a new attainment value for a goal, as the Update progress action does in Factorial.
    Each call adds an entry to the goal's progress history and returns the updated goal.

    A call made with a company API key or a company-level OAuth token must name, in author_id,
    the active employee the update is recorded as. The update is authorized with that
    employee's permissions, so name an employee who may update the goal, such as an admin.
    A call made with a user's OAuth token is recorded as that user; author_id may be left out
    or must name that user.

    The request is refused with 403 when author_id is missing on a company call, does not name
    an active employee of the company, names someone else on a user call, or names an employee
    who may not update the goal. A goal tracked by its sub-goals cannot be updated, because its
    value rolls up from them. A goal without a target value cannot be updated, and a
    qualitative goal only accepts 0 (not achieved) or 100 (achieved).

    Args:
        body (PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoalsGoal
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset = UNSET,
) -> Response[ErrorResponse | GoalsGoal]:
    """Records a goal's progress

     Records a new attainment value for a goal, as the Update progress action does in Factorial.
    Each call adds an entry to the goal's progress history and returns the updated goal.

    A call made with a company API key or a company-level OAuth token must name, in author_id,
    the active employee the update is recorded as. The update is authorized with that
    employee's permissions, so name an employee who may update the goal, such as an admin.
    A call made with a user's OAuth token is recorded as that user; author_id may be left out
    or must name that user.

    The request is refused with 403 when author_id is missing on a company call, does not name
    an active employee of the company, names someone else on a user call, or names an employee
    who may not update the goal. A goal tracked by its sub-goals cannot be updated, because its
    value rolls up from them. A goal without a target value cannot be updated, and a
    qualitative goal only accepts 0 (not achieved) or 100 (achieved).

    Args:
        body (PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoalsGoal]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset = UNSET,
) -> ErrorResponse | GoalsGoal | None:
    """Records a goal's progress

     Records a new attainment value for a goal, as the Update progress action does in Factorial.
    Each call adds an entry to the goal's progress history and returns the updated goal.

    A call made with a company API key or a company-level OAuth token must name, in author_id,
    the active employee the update is recorded as. The update is authorized with that
    employee's permissions, so name an employee who may update the goal, such as an admin.
    A call made with a user's OAuth token is recorded as that user; author_id may be left out
    or must name that user.

    The request is refused with 403 when author_id is missing on a company call, does not name
    an active employee of the company, names someone else on a user call, or names an employee
    who may not update the goal. A goal tracked by its sub-goals cannot be updated, because its
    value rolls up from them. A goal without a target value cannot be updated, and a
    qualitative goal only accepts 0 (not achieved) or 100 (achieved).

    Args:
        body (PostApi20270101ResourcesGoalsGoalsUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoalsGoal
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
