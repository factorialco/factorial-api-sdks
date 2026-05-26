from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_20260401_resources_tasks_tasks_id_body import (
    PutApi20260401ResourcesTasksTasksIdBody,
)
from ...models.tasks_task import TasksTask
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20260401ResourcesTasksTasksIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-04-01/resources/tasks/tasks/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TasksTask | None:
    if response.status_code == 200:
        response_200 = TasksTask.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TasksTask]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260401ResourcesTasksTasksIdBody | Unset = UNSET,
) -> Response[TasksTask]:
    """Updates a Task

     This endpoint updates an existing task.

    Args:
        id (str):
        body (PutApi20260401ResourcesTasksTasksIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TasksTask]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260401ResourcesTasksTasksIdBody | Unset = UNSET,
) -> TasksTask | None:
    """Updates a Task

     This endpoint updates an existing task.

    Args:
        id (str):
        body (PutApi20260401ResourcesTasksTasksIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TasksTask
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260401ResourcesTasksTasksIdBody | Unset = UNSET,
) -> Response[TasksTask]:
    """Updates a Task

     This endpoint updates an existing task.

    Args:
        id (str):
        body (PutApi20260401ResourcesTasksTasksIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TasksTask]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260401ResourcesTasksTasksIdBody | Unset = UNSET,
) -> TasksTask | None:
    """Updates a Task

     This endpoint updates an existing task.

    Args:
        id (str):
        body (PutApi20260401ResourcesTasksTasksIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TasksTask
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
