from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260401_resources_tasks_task_files_body import (
    PostApi20260401ResourcesTasksTaskFilesBody,
)
from ...models.tasks_task_file import TasksTaskFile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesTasksTaskFilesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/tasks/task_files",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TasksTaskFile | None:
    if response.status_code == 201:
        response_201 = TasksTaskFile.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TasksTaskFile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTasksTaskFilesBody | Unset = UNSET,
) -> Response[TasksTaskFile]:
    """Creates a Task file

     Creates a Task file

    Args:
        body (PostApi20260401ResourcesTasksTaskFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TasksTaskFile]
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
    body: PostApi20260401ResourcesTasksTaskFilesBody | Unset = UNSET,
) -> TasksTaskFile | None:
    """Creates a Task file

     Creates a Task file

    Args:
        body (PostApi20260401ResourcesTasksTaskFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TasksTaskFile
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTasksTaskFilesBody | Unset = UNSET,
) -> Response[TasksTaskFile]:
    """Creates a Task file

     Creates a Task file

    Args:
        body (PostApi20260401ResourcesTasksTaskFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TasksTaskFile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesTasksTaskFilesBody | Unset = UNSET,
) -> TasksTaskFile | None:
    """Creates a Task file

     Creates a Task file

    Args:
        body (PostApi20260401ResourcesTasksTaskFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TasksTaskFile
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
