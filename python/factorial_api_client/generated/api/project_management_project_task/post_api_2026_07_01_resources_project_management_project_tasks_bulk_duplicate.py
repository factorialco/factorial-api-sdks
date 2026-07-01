from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260701_resources_project_management_project_tasks_bulk_duplicate_body import (
    PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody,
)
from ...models.project_management_project_task import ProjectManagementProjectTask
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/project_management/project_tasks/bulk_duplicate",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ProjectManagementProjectTask] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProjectManagementProjectTask.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ProjectManagementProjectTask]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset = UNSET,
) -> Response[list[ProjectManagementProjectTask]]:
    """Bulk duplicates a Project task

     ###### **What does it do?**
    This will create new project tasks with the same attributes as the project task ids passed as an
    argument.
    ###### **What params does it accept?**

      - `ids`: Project task ids

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        body (PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProjectManagementProjectTask]]
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
    body: PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset = UNSET,
) -> list[ProjectManagementProjectTask] | None:
    """Bulk duplicates a Project task

     ###### **What does it do?**
    This will create new project tasks with the same attributes as the project task ids passed as an
    argument.
    ###### **What params does it accept?**

      - `ids`: Project task ids

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        body (PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProjectManagementProjectTask]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset = UNSET,
) -> Response[list[ProjectManagementProjectTask]]:
    """Bulk duplicates a Project task

     ###### **What does it do?**
    This will create new project tasks with the same attributes as the project task ids passed as an
    argument.
    ###### **What params does it accept?**

      - `ids`: Project task ids

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        body (PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProjectManagementProjectTask]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset = UNSET,
) -> list[ProjectManagementProjectTask] | None:
    """Bulk duplicates a Project task

     ###### **What does it do?**
    This will create new project tasks with the same attributes as the project task ids passed as an
    argument.
    ###### **What params does it accept?**

      - `ids`: Project task ids

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        body (PostApi20260701ResourcesProjectManagementProjectTasksBulkDuplicateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProjectManagementProjectTask]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
