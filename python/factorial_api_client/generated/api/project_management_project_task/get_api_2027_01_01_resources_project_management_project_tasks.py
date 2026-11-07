from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_project_management_project_tasks_due_status import (
    GetApi20270101ResourcesProjectManagementProjectTasksDueStatus,
)
from ...models.get_api_20270101_resources_project_management_project_tasks_response_200 import (
    GetApi20270101ResourcesProjectManagementProjectTasksResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str],
    project_ids: list[str],
    subproject_ids: list[str],
    task_ids: list[str] | Unset = UNSET,
    completed: bool,
    overdue: bool,
    search: str,
    due_status: GetApi20270101ResourcesProjectManagementProjectTasksDueStatus,
    client_ids: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids[]"] = json_ids

    json_project_ids = project_ids

    params["project_ids[]"] = json_project_ids

    json_subproject_ids = subproject_ids

    params["subproject_ids[]"] = json_subproject_ids

    json_task_ids: list[str] | Unset = UNSET
    if not isinstance(task_ids, Unset):
        json_task_ids = task_ids

    params["task_ids[]"] = json_task_ids

    params["completed"] = completed

    params["overdue"] = overdue

    params["search"] = search

    json_due_status = due_status.value
    params["due_status"] = json_due_status

    json_client_ids = client_ids

    params["client_ids[]"] = json_client_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/project_management/project_tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesProjectManagementProjectTasksResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    project_ids: list[str],
    subproject_ids: list[str],
    task_ids: list[str] | Unset = UNSET,
    completed: bool,
    overdue: bool,
    search: str,
    due_status: GetApi20270101ResourcesProjectManagementProjectTasksDueStatus,
    client_ids: list[str],
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200]:
    """Reads all Project tasks

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
        ids (list[str]): Retrieve only the projects tasks that matches the ids passed in the
            request. Example: ['314159', '271828'].
        project_ids (list[str]): Retrieve only the projects tasks from the projects that matched
            the ids passed in the request. Example: ['314159', '271828'].
        subproject_ids (list[str]): Retrieve only the projects tasks from the subprojects that
            matched the ids passed in the request. Example: ['314159', '271828'].
        task_ids (list[str] | Unset):
        completed (bool): Retrieve only the projects tasks with the status completed. Example:
            True.
        overdue (bool): Retrieve only the projects tasks that are overdue. Example: True.
        search (str): Retrieve only the projects tasks that their name match with the content
            passed as argument. Example: Project Name.
        due_status (GetApi20270101ResourcesProjectManagementProjectTasksDueStatus): Retrieve only
            the project tasks that their due status match with the content passed as argument.
            Example: due_in_future.
        client_ids (list[str]): Retrieve only the projects tasks from the clients that matched the
            ids passed in the request. Example: ['314159', '271828'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        task_ids=task_ids,
        completed=completed,
        overdue=overdue,
        search=search,
        due_status=due_status,
        client_ids=client_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    project_ids: list[str],
    subproject_ids: list[str],
    task_ids: list[str] | Unset = UNSET,
    completed: bool,
    overdue: bool,
    search: str,
    due_status: GetApi20270101ResourcesProjectManagementProjectTasksDueStatus,
    client_ids: list[str],
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200 | None:
    """Reads all Project tasks

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
        ids (list[str]): Retrieve only the projects tasks that matches the ids passed in the
            request. Example: ['314159', '271828'].
        project_ids (list[str]): Retrieve only the projects tasks from the projects that matched
            the ids passed in the request. Example: ['314159', '271828'].
        subproject_ids (list[str]): Retrieve only the projects tasks from the subprojects that
            matched the ids passed in the request. Example: ['314159', '271828'].
        task_ids (list[str] | Unset):
        completed (bool): Retrieve only the projects tasks with the status completed. Example:
            True.
        overdue (bool): Retrieve only the projects tasks that are overdue. Example: True.
        search (str): Retrieve only the projects tasks that their name match with the content
            passed as argument. Example: Project Name.
        due_status (GetApi20270101ResourcesProjectManagementProjectTasksDueStatus): Retrieve only
            the project tasks that their due status match with the content passed as argument.
            Example: due_in_future.
        client_ids (list[str]): Retrieve only the projects tasks from the clients that matched the
            ids passed in the request. Example: ['314159', '271828'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        task_ids=task_ids,
        completed=completed,
        overdue=overdue,
        search=search,
        due_status=due_status,
        client_ids=client_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    project_ids: list[str],
    subproject_ids: list[str],
    task_ids: list[str] | Unset = UNSET,
    completed: bool,
    overdue: bool,
    search: str,
    due_status: GetApi20270101ResourcesProjectManagementProjectTasksDueStatus,
    client_ids: list[str],
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200]:
    """Reads all Project tasks

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
        ids (list[str]): Retrieve only the projects tasks that matches the ids passed in the
            request. Example: ['314159', '271828'].
        project_ids (list[str]): Retrieve only the projects tasks from the projects that matched
            the ids passed in the request. Example: ['314159', '271828'].
        subproject_ids (list[str]): Retrieve only the projects tasks from the subprojects that
            matched the ids passed in the request. Example: ['314159', '271828'].
        task_ids (list[str] | Unset):
        completed (bool): Retrieve only the projects tasks with the status completed. Example:
            True.
        overdue (bool): Retrieve only the projects tasks that are overdue. Example: True.
        search (str): Retrieve only the projects tasks that their name match with the content
            passed as argument. Example: Project Name.
        due_status (GetApi20270101ResourcesProjectManagementProjectTasksDueStatus): Retrieve only
            the project tasks that their due status match with the content passed as argument.
            Example: due_in_future.
        client_ids (list[str]): Retrieve only the projects tasks from the clients that matched the
            ids passed in the request. Example: ['314159', '271828'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        task_ids=task_ids,
        completed=completed,
        overdue=overdue,
        search=search,
        due_status=due_status,
        client_ids=client_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str],
    project_ids: list[str],
    subproject_ids: list[str],
    task_ids: list[str] | Unset = UNSET,
    completed: bool,
    overdue: bool,
    search: str,
    due_status: GetApi20270101ResourcesProjectManagementProjectTasksDueStatus,
    client_ids: list[str],
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200 | None:
    """Reads all Project tasks

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
        ids (list[str]): Retrieve only the projects tasks that matches the ids passed in the
            request. Example: ['314159', '271828'].
        project_ids (list[str]): Retrieve only the projects tasks from the projects that matched
            the ids passed in the request. Example: ['314159', '271828'].
        subproject_ids (list[str]): Retrieve only the projects tasks from the subprojects that
            matched the ids passed in the request. Example: ['314159', '271828'].
        task_ids (list[str] | Unset):
        completed (bool): Retrieve only the projects tasks with the status completed. Example:
            True.
        overdue (bool): Retrieve only the projects tasks that are overdue. Example: True.
        search (str): Retrieve only the projects tasks that their name match with the content
            passed as argument. Example: Project Name.
        due_status (GetApi20270101ResourcesProjectManagementProjectTasksDueStatus): Retrieve only
            the project tasks that their due status match with the content passed as argument.
            Example: due_in_future.
        client_ids (list[str]): Retrieve only the projects tasks from the clients that matched the
            ids passed in the request. Example: ['314159', '271828'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProjectManagementProjectTasksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            project_ids=project_ids,
            subproject_ids=subproject_ids,
            task_ids=task_ids,
            completed=completed,
            overdue=overdue,
            search=search,
            due_status=due_status,
            client_ids=client_ids,
        )
    ).parsed
