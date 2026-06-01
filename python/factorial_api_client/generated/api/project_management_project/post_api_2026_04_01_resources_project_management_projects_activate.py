from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260401_resources_project_management_projects_activate_body import (
    PostApi20260401ResourcesProjectManagementProjectsActivateBody,
)
from ...models.project_management_project import ProjectManagementProject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/project_management/projects/activate",
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
    body: PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset = UNSET,
) -> Response[ProjectManagementProject]:
    """Activates a Project

     ###### **What does it do?**
    This endpoint can be used to set a project as `Active`.
    ###### **What body params do you need?**
      - `id`: mandatory. The id of the project aimed to be activated.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset):

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
    body: PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset = UNSET,
) -> ProjectManagementProject | None:
    """Activates a Project

     ###### **What does it do?**
    This endpoint can be used to set a project as `Active`.
    ###### **What body params do you need?**
      - `id`: mandatory. The id of the project aimed to be activated.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset):

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
    body: PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset = UNSET,
) -> Response[ProjectManagementProject]:
    """Activates a Project

     ###### **What does it do?**
    This endpoint can be used to set a project as `Active`.
    ###### **What body params do you need?**
      - `id`: mandatory. The id of the project aimed to be activated.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset):

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
    body: PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset = UNSET,
) -> ProjectManagementProject | None:
    """Activates a Project

     ###### **What does it do?**
    This endpoint can be used to set a project as `Active`.
    ###### **What body params do you need?**
      - `id`: mandatory. The id of the project aimed to be activated.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectsActivateBody | Unset):

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
