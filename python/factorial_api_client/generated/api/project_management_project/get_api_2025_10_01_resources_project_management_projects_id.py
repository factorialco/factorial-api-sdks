from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_project import ProjectManagementProject
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/project_management/projects/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

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
) -> Response[ProjectManagementProject]:
    """Reads a single Project

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProject]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ProjectManagementProject | None:
    """Reads a single Project

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProject
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectManagementProject]:
    """Reads a single Project

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProject]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ProjectManagementProject | None:
    """Reads a single Project

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        id (str):

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
        )
    ).parsed
