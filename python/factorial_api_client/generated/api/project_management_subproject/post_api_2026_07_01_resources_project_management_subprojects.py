from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260701_resources_project_management_subprojects_body import (
    PostApi20260701ResourcesProjectManagementSubprojectsBody,
)
from ...models.project_management_subproject import ProjectManagementSubproject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/project_management/subprojects",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementSubproject | None:
    if response.status_code == 201:
        response_201 = ProjectManagementSubproject.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementSubproject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset = UNSET,
) -> Response[ProjectManagementSubproject]:
    """Creates a Subproject

     ###### **What does it do?**
    This creates a new subproject.
    ###### **Is it related to other entities?**
    A subproject is always related to a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        body (PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementSubproject]
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
    body: PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset = UNSET,
) -> ProjectManagementSubproject | None:
    """Creates a Subproject

     ###### **What does it do?**
    This creates a new subproject.
    ###### **Is it related to other entities?**
    A subproject is always related to a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        body (PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementSubproject
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset = UNSET,
) -> Response[ProjectManagementSubproject]:
    """Creates a Subproject

     ###### **What does it do?**
    This creates a new subproject.
    ###### **Is it related to other entities?**
    A subproject is always related to a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        body (PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementSubproject]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset = UNSET,
) -> ProjectManagementSubproject | None:
    """Creates a Subproject

     ###### **What does it do?**
    This creates a new subproject.
    ###### **Is it related to other entities?**
    A subproject is always related to a project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        body (PostApi20260701ResourcesProjectManagementSubprojectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementSubproject
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
