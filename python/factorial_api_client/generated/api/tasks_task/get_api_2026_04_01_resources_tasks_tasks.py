from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_tasks_tasks_category import (
    GetApi20260401ResourcesTasksTasksCategory,
)
from ...models.get_api_20260401_resources_tasks_tasks_response_200 import (
    GetApi20260401ResourcesTasksTasksResponse200,
)
from ...models.get_api_20260401_resources_tasks_tasks_task_status import (
    GetApi20260401ResourcesTasksTasksTaskStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    assignee_id: int | Unset = UNSET,
    due_on: str | Unset = UNSET,
    already_due: bool | Unset = UNSET,
    task_status: GetApi20260401ResourcesTasksTasksTaskStatus | Unset = UNSET,
    involvee_id: int | Unset = UNSET,
    category: GetApi20260401ResourcesTasksTasksCategory | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["company_id"] = company_id

    params["assignee_id"] = assignee_id

    params["due_on"] = due_on

    params["already_due"] = already_due

    json_task_status: str | Unset = UNSET
    if not isinstance(task_status, Unset):
        json_task_status = task_status.value

    params["task_status"] = json_task_status

    params["involvee_id"] = involvee_id

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/tasks/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesTasksTasksResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesTasksTasksResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesTasksTasksResponse200]:
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
    company_id: int | Unset = UNSET,
    assignee_id: int | Unset = UNSET,
    due_on: str | Unset = UNSET,
    already_due: bool | Unset = UNSET,
    task_status: GetApi20260401ResourcesTasksTasksTaskStatus | Unset = UNSET,
    involvee_id: int | Unset = UNSET,
    category: GetApi20260401ResourcesTasksTasksCategory | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTasksTasksResponse200]:
    """Reads all Tasks

     This endpoint retrieves all tasks created.

    Args:
        ids (list[int] | Unset): retrieve only the tasks that match the IDs passed in the request.
            Example: [1, 2, 3].
        company_id (int | Unset): retrieve the tasks that have a company_id associated Example: 1.
        assignee_id (int | Unset): retrieve the tasks that have an assignee_id associated,
            assignee_id references to employee_id. Example: 1.
        due_on (str | Unset): filter by tasks that have a due date. Example: 2024-06-06.
        already_due (bool | Unset): filter by tasks that have expired or are still due. Example:
            True.
        task_status (GetApi20260401ResourcesTasksTasksTaskStatus | Unset): filter by tasks that
            with an especific status (todo | in_progress | done | discarded). Example: todo.
        involvee_id (int | Unset): retrieve tasks where the user is affectee or assignee Example:
            1.
        category (GetApi20260401ResourcesTasksTasksCategory | Unset): filter by tasks that have a
            specific category Example: benefits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTasksTasksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        assignee_id=assignee_id,
        due_on=due_on,
        already_due=already_due,
        task_status=task_status,
        involvee_id=involvee_id,
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    assignee_id: int | Unset = UNSET,
    due_on: str | Unset = UNSET,
    already_due: bool | Unset = UNSET,
    task_status: GetApi20260401ResourcesTasksTasksTaskStatus | Unset = UNSET,
    involvee_id: int | Unset = UNSET,
    category: GetApi20260401ResourcesTasksTasksCategory | Unset = UNSET,
) -> GetApi20260401ResourcesTasksTasksResponse200 | None:
    """Reads all Tasks

     This endpoint retrieves all tasks created.

    Args:
        ids (list[int] | Unset): retrieve only the tasks that match the IDs passed in the request.
            Example: [1, 2, 3].
        company_id (int | Unset): retrieve the tasks that have a company_id associated Example: 1.
        assignee_id (int | Unset): retrieve the tasks that have an assignee_id associated,
            assignee_id references to employee_id. Example: 1.
        due_on (str | Unset): filter by tasks that have a due date. Example: 2024-06-06.
        already_due (bool | Unset): filter by tasks that have expired or are still due. Example:
            True.
        task_status (GetApi20260401ResourcesTasksTasksTaskStatus | Unset): filter by tasks that
            with an especific status (todo | in_progress | done | discarded). Example: todo.
        involvee_id (int | Unset): retrieve tasks where the user is affectee or assignee Example:
            1.
        category (GetApi20260401ResourcesTasksTasksCategory | Unset): filter by tasks that have a
            specific category Example: benefits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTasksTasksResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_id=company_id,
        assignee_id=assignee_id,
        due_on=due_on,
        already_due=already_due,
        task_status=task_status,
        involvee_id=involvee_id,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    assignee_id: int | Unset = UNSET,
    due_on: str | Unset = UNSET,
    already_due: bool | Unset = UNSET,
    task_status: GetApi20260401ResourcesTasksTasksTaskStatus | Unset = UNSET,
    involvee_id: int | Unset = UNSET,
    category: GetApi20260401ResourcesTasksTasksCategory | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTasksTasksResponse200]:
    """Reads all Tasks

     This endpoint retrieves all tasks created.

    Args:
        ids (list[int] | Unset): retrieve only the tasks that match the IDs passed in the request.
            Example: [1, 2, 3].
        company_id (int | Unset): retrieve the tasks that have a company_id associated Example: 1.
        assignee_id (int | Unset): retrieve the tasks that have an assignee_id associated,
            assignee_id references to employee_id. Example: 1.
        due_on (str | Unset): filter by tasks that have a due date. Example: 2024-06-06.
        already_due (bool | Unset): filter by tasks that have expired or are still due. Example:
            True.
        task_status (GetApi20260401ResourcesTasksTasksTaskStatus | Unset): filter by tasks that
            with an especific status (todo | in_progress | done | discarded). Example: todo.
        involvee_id (int | Unset): retrieve tasks where the user is affectee or assignee Example:
            1.
        category (GetApi20260401ResourcesTasksTasksCategory | Unset): filter by tasks that have a
            specific category Example: benefits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTasksTasksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        assignee_id=assignee_id,
        due_on=due_on,
        already_due=already_due,
        task_status=task_status,
        involvee_id=involvee_id,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    assignee_id: int | Unset = UNSET,
    due_on: str | Unset = UNSET,
    already_due: bool | Unset = UNSET,
    task_status: GetApi20260401ResourcesTasksTasksTaskStatus | Unset = UNSET,
    involvee_id: int | Unset = UNSET,
    category: GetApi20260401ResourcesTasksTasksCategory | Unset = UNSET,
) -> GetApi20260401ResourcesTasksTasksResponse200 | None:
    """Reads all Tasks

     This endpoint retrieves all tasks created.

    Args:
        ids (list[int] | Unset): retrieve only the tasks that match the IDs passed in the request.
            Example: [1, 2, 3].
        company_id (int | Unset): retrieve the tasks that have a company_id associated Example: 1.
        assignee_id (int | Unset): retrieve the tasks that have an assignee_id associated,
            assignee_id references to employee_id. Example: 1.
        due_on (str | Unset): filter by tasks that have a due date. Example: 2024-06-06.
        already_due (bool | Unset): filter by tasks that have expired or are still due. Example:
            True.
        task_status (GetApi20260401ResourcesTasksTasksTaskStatus | Unset): filter by tasks that
            with an especific status (todo | in_progress | done | discarded). Example: todo.
        involvee_id (int | Unset): retrieve tasks where the user is affectee or assignee Example:
            1.
        category (GetApi20260401ResourcesTasksTasksCategory | Unset): filter by tasks that have a
            specific category Example: benefits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTasksTasksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_id=company_id,
            assignee_id=assignee_id,
            due_on=due_on,
            already_due=already_due,
            task_status=task_status,
            involvee_id=involvee_id,
            category=category,
        )
    ).parsed
