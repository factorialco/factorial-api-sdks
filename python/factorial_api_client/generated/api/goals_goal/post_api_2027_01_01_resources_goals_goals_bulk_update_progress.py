from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.goals_goal import GoalsGoal
from ...models.post_api_20270101_resources_goals_goals_bulk_update_progress_body import (
    PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/goals/goals/bulk_update_progress",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | list[GoalsGoal] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GoalsGoal.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ErrorResponse | list[GoalsGoal]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset = UNSET,
) -> Response[ErrorResponse | list[GoalsGoal]]:
    """Records the progress of several goals

     Records a new attainment value for up to 200 goals or goal periods in one request, as
    update_progress does for one. All updates are recorded as the same author.

    The request is atomic: it is validated as a whole and any refused item rejects it
    entirely, so nothing is written and the request can be retried as is. It is refused when
    it has no items, has more than 200, or repeats a goal and period. author_id follows the
    same rules as in update_progress.

    Args:
        body (PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[GoalsGoal]]
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
    body: PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset = UNSET,
) -> ErrorResponse | list[GoalsGoal] | None:
    """Records the progress of several goals

     Records a new attainment value for up to 200 goals or goal periods in one request, as
    update_progress does for one. All updates are recorded as the same author.

    The request is atomic: it is validated as a whole and any refused item rejects it
    entirely, so nothing is written and the request can be retried as is. It is refused when
    it has no items, has more than 200, or repeats a goal and period. author_id follows the
    same rules as in update_progress.

    Args:
        body (PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[GoalsGoal]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset = UNSET,
) -> Response[ErrorResponse | list[GoalsGoal]]:
    """Records the progress of several goals

     Records a new attainment value for up to 200 goals or goal periods in one request, as
    update_progress does for one. All updates are recorded as the same author.

    The request is atomic: it is validated as a whole and any refused item rejects it
    entirely, so nothing is written and the request can be retried as is. It is refused when
    it has no items, has more than 200, or repeats a goal and period. author_id follows the
    same rules as in update_progress.

    Args:
        body (PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[GoalsGoal]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset = UNSET,
) -> ErrorResponse | list[GoalsGoal] | None:
    """Records the progress of several goals

     Records a new attainment value for up to 200 goals or goal periods in one request, as
    update_progress does for one. All updates are recorded as the same author.

    The request is atomic: it is validated as a whole and any refused item rejects it
    entirely, so nothing is written and the request can be retried as is. It is refused when
    it has no items, has more than 200, or repeats a goal and period. author_id follows the
    same rules as in update_progress.

    Args:
        body (PostApi20270101ResourcesGoalsGoalsBulkUpdateProgressBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[GoalsGoal]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
