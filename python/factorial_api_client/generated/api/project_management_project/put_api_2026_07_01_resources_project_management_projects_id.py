from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_project import ProjectManagementProject
from ...models.put_api_20260701_resources_project_management_projects_id_body import (
    PutApi20260701ResourcesProjectManagementProjectsIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-07-01/resources/project_management/projects/{id}".format(
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset = UNSET,
) -> Response[ProjectManagementProject]:
    """Updates a Project

     ###### **What does it do?**
    This updates a project with the given params.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        id (str):
        body (PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProject]
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
    body: PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset = UNSET,
) -> ProjectManagementProject | None:
    """Updates a Project

     ###### **What does it do?**
    This updates a project with the given params.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        id (str):
        body (PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProject
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
    body: PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset = UNSET,
) -> Response[ProjectManagementProject]:
    """Updates a Project

     ###### **What does it do?**
    This updates a project with the given params.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        id (str):
        body (PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProject]
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
    body: PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset = UNSET,
) -> ProjectManagementProject | None:
    """Updates a Project

     ###### **What does it do?**
    This updates a project with the given params.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the
    project.

    Args:
        id (str):
        body (PutApi20260701ResourcesProjectManagementProjectsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProject
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
