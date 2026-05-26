from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20251001_resources_project_management_projects_soft_delete_body import (
    PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody,
)
from ...models.project_management_project import ProjectManagementProject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/project_management/projects/soft_delete",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementProject | None:
    if response.status_code == 200:
        response_200 = ProjectManagementProject.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementProject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset = UNSET,
) -> Response[ProjectManagementProject]:
    """Soft deletes a Project

     ###### **What does it do?**
    This soft deletes a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    delete projects.

    Args:
        body (PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProject]
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
    body: PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset = UNSET,
) -> ProjectManagementProject | None:
    """Soft deletes a Project

     ###### **What does it do?**
    This soft deletes a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    delete projects.

    Args:
        body (PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProject
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset = UNSET,
) -> Response[ProjectManagementProject]:
    """Soft deletes a Project

     ###### **What does it do?**
    This soft deletes a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    delete projects.

    Args:
        body (PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProject]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset = UNSET,
) -> ProjectManagementProject | None:
    """Soft deletes a Project

     ###### **What does it do?**
    This soft deletes a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    delete projects.

    Args:
        body (PostApi20251001ResourcesProjectManagementProjectsSoftDeleteBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProject
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
