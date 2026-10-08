from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_api_20270101_resources_project_management_projects_body import (
    PostApi20270101ResourcesProjectManagementProjectsBody,
)
from ...models.project_management_project import ProjectManagementProject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesProjectManagementProjectsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/project_management/projects",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ProjectManagementProject | None:
    if response.status_code == 201:
        response_201 = ProjectManagementProject.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | ProjectManagementProject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesProjectManagementProjectsBody | Unset = UNSET,
) -> Response[ErrorResponse | ProjectManagementProject]:
    """Creates a Project

     ###### **What does it do?**
    This creates a new project. By default, the project will be created with the status `active`.
    ###### **What body params do you need?**

      - `name`: is mandatory to pass a name of the project.
      - `code`: optional unique code for the project to be identifiable and searchable.
      - `start_date`: optional start date for the project. If given must be in iso-8601 format (YYYY-MM-
    DD).
      - `due_date`: optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD).
      - `status`: a project can have the status `active` or `closed`. By default, the project will be
    created with the status `active`.
      - `employees_assignment`: optional param to define the kind of assignation the project has. Its
    possible values are: [`manual`, `company`]. A project can have `manual` assignation or can be
    defined to be assigned to the whole `company`. Defaults to `manual`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    create projects.

    Args:
        body (PostApi20270101ResourcesProjectManagementProjectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectManagementProject]
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
    body: PostApi20270101ResourcesProjectManagementProjectsBody | Unset = UNSET,
) -> ErrorResponse | ProjectManagementProject | None:
    """Creates a Project

     ###### **What does it do?**
    This creates a new project. By default, the project will be created with the status `active`.
    ###### **What body params do you need?**

      - `name`: is mandatory to pass a name of the project.
      - `code`: optional unique code for the project to be identifiable and searchable.
      - `start_date`: optional start date for the project. If given must be in iso-8601 format (YYYY-MM-
    DD).
      - `due_date`: optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD).
      - `status`: a project can have the status `active` or `closed`. By default, the project will be
    created with the status `active`.
      - `employees_assignment`: optional param to define the kind of assignation the project has. Its
    possible values are: [`manual`, `company`]. A project can have `manual` assignation or can be
    defined to be assigned to the whole `company`. Defaults to `manual`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    create projects.

    Args:
        body (PostApi20270101ResourcesProjectManagementProjectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectManagementProject
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesProjectManagementProjectsBody | Unset = UNSET,
) -> Response[ErrorResponse | ProjectManagementProject]:
    """Creates a Project

     ###### **What does it do?**
    This creates a new project. By default, the project will be created with the status `active`.
    ###### **What body params do you need?**

      - `name`: is mandatory to pass a name of the project.
      - `code`: optional unique code for the project to be identifiable and searchable.
      - `start_date`: optional start date for the project. If given must be in iso-8601 format (YYYY-MM-
    DD).
      - `due_date`: optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD).
      - `status`: a project can have the status `active` or `closed`. By default, the project will be
    created with the status `active`.
      - `employees_assignment`: optional param to define the kind of assignation the project has. Its
    possible values are: [`manual`, `company`]. A project can have `manual` assignation or can be
    defined to be assigned to the whole `company`. Defaults to `manual`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    create projects.

    Args:
        body (PostApi20270101ResourcesProjectManagementProjectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectManagementProject]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesProjectManagementProjectsBody | Unset = UNSET,
) -> ErrorResponse | ProjectManagementProject | None:
    """Creates a Project

     ###### **What does it do?**
    This creates a new project. By default, the project will be created with the status `active`.
    ###### **What body params do you need?**

      - `name`: is mandatory to pass a name of the project.
      - `code`: optional unique code for the project to be identifiable and searchable.
      - `start_date`: optional start date for the project. If given must be in iso-8601 format (YYYY-MM-
    DD).
      - `due_date`: optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD).
      - `status`: a project can have the status `active` or `closed`. By default, the project will be
    created with the status `active`.
      - `employees_assignment`: optional param to define the kind of assignation the project has. Its
    possible values are: [`manual`, `company`]. A project can have `manual` assignation or can be
    defined to be assigned to the whole `company`. Defaults to `manual`.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    create projects.

    Args:
        body (PostApi20270101ResourcesProjectManagementProjectsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectManagementProject
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
