from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_project_task import ProjectManagementProjectTask
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/project_management/project_tasks/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementProjectTask | None:
    if response.status_code == 200:
        response_200 = ProjectManagementProjectTask.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementProjectTask]:
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
) -> Response[ProjectManagementProjectTask]:
    """Reads a single Project task

     ###### **What does it do?**
    This reads the data of projects tasks, and retrieves the information based on permissions:

      - If the user can see all company projects for everybody, the endpoint will return a list with the
    tasks from the related projects.
      - If the user can create projects for everybody, the endpoint will return a list with the tasks
    from the related projects.
      - If the user has any role (editor or owner) on the project, the endpoint will return a list with
    the tasks from the related projects where the user has that role.
      - If those conditions are not matched, the endpoint will return an empty list.

    ###### **What params does it accept?**

      - `ids`: retrieve only the projects tasks that matches the ids passed in the request.
      - `project_ids`: retrieve only the projects tasks from the projects that matched the ids passed in
    the request.
      - `subproject_ids`: retrieve only the projects tasks from the subprojects that matched the ids
    passed in the request.
      - `completed`: boolean - retrieve only the projects tasks with the status completed.
      - `overdue`: boolean - retrieve only the projects tasks that are overdue.
      - `search`:  retrieve only the projects tasks that their name match with the content passed as
    argument.
      - `due_status`: retrieve only the project tasks that their due status match with the content
    passed as argument.
      - `client_ids`: retrieve only the projects tasks from the clients that matched the ids passed in
    the request.

    ###### **Who can use it?**

      Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProjectTask]
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
) -> ProjectManagementProjectTask | None:
    """Reads a single Project task

     ###### **What does it do?**
    This reads the data of projects tasks, and retrieves the information based on permissions:

      - If the user can see all company projects for everybody, the endpoint will return a list with the
    tasks from the related projects.
      - If the user can create projects for everybody, the endpoint will return a list with the tasks
    from the related projects.
      - If the user has any role (editor or owner) on the project, the endpoint will return a list with
    the tasks from the related projects where the user has that role.
      - If those conditions are not matched, the endpoint will return an empty list.

    ###### **What params does it accept?**

      - `ids`: retrieve only the projects tasks that matches the ids passed in the request.
      - `project_ids`: retrieve only the projects tasks from the projects that matched the ids passed in
    the request.
      - `subproject_ids`: retrieve only the projects tasks from the subprojects that matched the ids
    passed in the request.
      - `completed`: boolean - retrieve only the projects tasks with the status completed.
      - `overdue`: boolean - retrieve only the projects tasks that are overdue.
      - `search`:  retrieve only the projects tasks that their name match with the content passed as
    argument.
      - `due_status`: retrieve only the project tasks that their due status match with the content
    passed as argument.
      - `client_ids`: retrieve only the projects tasks from the clients that matched the ids passed in
    the request.

    ###### **Who can use it?**

      Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProjectTask
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectManagementProjectTask]:
    """Reads a single Project task

     ###### **What does it do?**
    This reads the data of projects tasks, and retrieves the information based on permissions:

      - If the user can see all company projects for everybody, the endpoint will return a list with the
    tasks from the related projects.
      - If the user can create projects for everybody, the endpoint will return a list with the tasks
    from the related projects.
      - If the user has any role (editor or owner) on the project, the endpoint will return a list with
    the tasks from the related projects where the user has that role.
      - If those conditions are not matched, the endpoint will return an empty list.

    ###### **What params does it accept?**

      - `ids`: retrieve only the projects tasks that matches the ids passed in the request.
      - `project_ids`: retrieve only the projects tasks from the projects that matched the ids passed in
    the request.
      - `subproject_ids`: retrieve only the projects tasks from the subprojects that matched the ids
    passed in the request.
      - `completed`: boolean - retrieve only the projects tasks with the status completed.
      - `overdue`: boolean - retrieve only the projects tasks that are overdue.
      - `search`:  retrieve only the projects tasks that their name match with the content passed as
    argument.
      - `due_status`: retrieve only the project tasks that their due status match with the content
    passed as argument.
      - `client_ids`: retrieve only the projects tasks from the clients that matched the ids passed in
    the request.

    ###### **Who can use it?**

      Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementProjectTask]
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
) -> ProjectManagementProjectTask | None:
    """Reads a single Project task

     ###### **What does it do?**
    This reads the data of projects tasks, and retrieves the information based on permissions:

      - If the user can see all company projects for everybody, the endpoint will return a list with the
    tasks from the related projects.
      - If the user can create projects for everybody, the endpoint will return a list with the tasks
    from the related projects.
      - If the user has any role (editor or owner) on the project, the endpoint will return a list with
    the tasks from the related projects where the user has that role.
      - If those conditions are not matched, the endpoint will return an empty list.

    ###### **What params does it accept?**

      - `ids`: retrieve only the projects tasks that matches the ids passed in the request.
      - `project_ids`: retrieve only the projects tasks from the projects that matched the ids passed in
    the request.
      - `subproject_ids`: retrieve only the projects tasks from the subprojects that matched the ids
    passed in the request.
      - `completed`: boolean - retrieve only the projects tasks with the status completed.
      - `overdue`: boolean - retrieve only the projects tasks that are overdue.
      - `search`:  retrieve only the projects tasks that their name match with the content passed as
    argument.
      - `due_status`: retrieve only the project tasks that their due status match with the content
    passed as argument.
      - `client_ids`: retrieve only the projects tasks from the clients that matched the ids passed in
    the request.

    ###### **Who can use it?**

      Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementProjectTask
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
