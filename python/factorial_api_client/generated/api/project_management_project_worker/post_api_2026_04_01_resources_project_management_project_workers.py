from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260401_resources_project_management_project_workers_body import (
    PostApi20260401ResourcesProjectManagementProjectWorkersBody,
)
from ...models.project_management_project_worker import ProjectManagementProjectWorker
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/project_management/project_workers",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementProjectWorker | None:
    if response.status_code == 201:
        response_201 = ProjectManagementProjectWorker.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementProjectWorker]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset = UNSET,
) -> Response[ProjectManagementProjectWorker]:
    """Creates a Project worker

     ###### **What does it do?**
    This creates a new project worker. By default, the project worker will be created with the status
    `assigned`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProjectWorker]
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
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset = UNSET,
) -> ProjectManagementProjectWorker | None:
    """Creates a Project worker

     ###### **What does it do?**
    This creates a new project worker. By default, the project worker will be created with the status
    `assigned`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProjectWorker
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset = UNSET,
) -> Response[ProjectManagementProjectWorker]:
    """Creates a Project worker

     ###### **What does it do?**
    This creates a new project worker. By default, the project worker will be created with the status
    `assigned`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProjectWorker]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset = UNSET,
) -> ProjectManagementProjectWorker | None:
    """Creates a Project worker

     ###### **What does it do?**
    This creates a new project worker. By default, the project worker will be created with the status
    `assigned`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProjectWorker
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
