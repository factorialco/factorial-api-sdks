from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_project_management_project_workers_response_200 import (
    GetApi20260701ResourcesProjectManagementProjectWorkersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    no_subproject: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    project_active: bool | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    include_labor_cost: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_project_ids: list[str] | Unset = UNSET
    if not isinstance(project_ids, Unset):
        json_project_ids = project_ids

    params["project_ids[]"] = json_project_ids

    json_subproject_ids: list[str] | Unset = UNSET
    if not isinstance(subproject_ids, Unset):
        json_subproject_ids = subproject_ids

    params["subproject_ids[]"] = json_subproject_ids

    params["no_subproject"] = no_subproject

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["assigned"] = assigned

    params["project_active"] = project_active

    params["employee_name"] = employee_name

    params["include_inputed_minutes"] = include_inputed_minutes

    params["include_cost"] = include_cost

    params["updated_after"] = updated_after

    params["include_labor_cost"] = include_labor_cost

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/project_management/project_workers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesProjectManagementProjectWorkersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesProjectManagementProjectWorkersResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesProjectManagementProjectWorkersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    no_subproject: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    project_active: bool | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    include_labor_cost: bool | Unset = UNSET,
) -> Response[GetApi20260701ResourcesProjectManagementProjectWorkersResponse200]:
    """Reads all Project workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        ids (list[str] | Unset): Retrieve only the project workers that matches the ids provided
            in the request. Example: ['92732', '2'].
        project_ids (list[str] | Unset): Retrieve only the project workers that matches the
            project_ids provided in the request. Example: ['314159', '33'].
        subproject_ids (list[str] | Unset): Retrieve only the project workers that matches the
            subproject_ids provided in the request. Example: ['5', '6'].
        no_subproject (bool | Unset): Retrieve the project workers that are not assigned to any
            subproject (can be combined with subproject_ids).
        employee_ids (list[str] | Unset): Retrieve only the project workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve project workers that are assigned if true or in not-
            assigned status if false. Example: True.
        project_active (bool | Unset): Retrieve the project workers that are assigned to active
            projects if turew or closed projects if false. Example: True.
        employee_name (str | Unset): Retrieve only the project workers that matches the given
            employee's name provided in the request. Example: John D.
        include_inputed_minutes (bool | Unset): If true we will perform the minutes calculations
            and will be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If true, costs of the project worker will be included to the
            response. Example: True.
        updated_after (str | Unset): Retrieve only the project workers that were created or
            updated after the date provided in the request. Example: 1993-08-23.
        include_labor_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesProjectManagementProjectWorkersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        no_subproject=no_subproject,
        employee_ids=employee_ids,
        assigned=assigned,
        project_active=project_active,
        employee_name=employee_name,
        include_inputed_minutes=include_inputed_minutes,
        include_cost=include_cost,
        updated_after=updated_after,
        include_labor_cost=include_labor_cost,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    no_subproject: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    project_active: bool | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    include_labor_cost: bool | Unset = UNSET,
) -> GetApi20260701ResourcesProjectManagementProjectWorkersResponse200 | None:
    """Reads all Project workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        ids (list[str] | Unset): Retrieve only the project workers that matches the ids provided
            in the request. Example: ['92732', '2'].
        project_ids (list[str] | Unset): Retrieve only the project workers that matches the
            project_ids provided in the request. Example: ['314159', '33'].
        subproject_ids (list[str] | Unset): Retrieve only the project workers that matches the
            subproject_ids provided in the request. Example: ['5', '6'].
        no_subproject (bool | Unset): Retrieve the project workers that are not assigned to any
            subproject (can be combined with subproject_ids).
        employee_ids (list[str] | Unset): Retrieve only the project workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve project workers that are assigned if true or in not-
            assigned status if false. Example: True.
        project_active (bool | Unset): Retrieve the project workers that are assigned to active
            projects if turew or closed projects if false. Example: True.
        employee_name (str | Unset): Retrieve only the project workers that matches the given
            employee's name provided in the request. Example: John D.
        include_inputed_minutes (bool | Unset): If true we will perform the minutes calculations
            and will be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If true, costs of the project worker will be included to the
            response. Example: True.
        updated_after (str | Unset): Retrieve only the project workers that were created or
            updated after the date provided in the request. Example: 1993-08-23.
        include_labor_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesProjectManagementProjectWorkersResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        no_subproject=no_subproject,
        employee_ids=employee_ids,
        assigned=assigned,
        project_active=project_active,
        employee_name=employee_name,
        include_inputed_minutes=include_inputed_minutes,
        include_cost=include_cost,
        updated_after=updated_after,
        include_labor_cost=include_labor_cost,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    no_subproject: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    project_active: bool | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    include_labor_cost: bool | Unset = UNSET,
) -> Response[GetApi20260701ResourcesProjectManagementProjectWorkersResponse200]:
    """Reads all Project workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        ids (list[str] | Unset): Retrieve only the project workers that matches the ids provided
            in the request. Example: ['92732', '2'].
        project_ids (list[str] | Unset): Retrieve only the project workers that matches the
            project_ids provided in the request. Example: ['314159', '33'].
        subproject_ids (list[str] | Unset): Retrieve only the project workers that matches the
            subproject_ids provided in the request. Example: ['5', '6'].
        no_subproject (bool | Unset): Retrieve the project workers that are not assigned to any
            subproject (can be combined with subproject_ids).
        employee_ids (list[str] | Unset): Retrieve only the project workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve project workers that are assigned if true or in not-
            assigned status if false. Example: True.
        project_active (bool | Unset): Retrieve the project workers that are assigned to active
            projects if turew or closed projects if false. Example: True.
        employee_name (str | Unset): Retrieve only the project workers that matches the given
            employee's name provided in the request. Example: John D.
        include_inputed_minutes (bool | Unset): If true we will perform the minutes calculations
            and will be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If true, costs of the project worker will be included to the
            response. Example: True.
        updated_after (str | Unset): Retrieve only the project workers that were created or
            updated after the date provided in the request. Example: 1993-08-23.
        include_labor_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesProjectManagementProjectWorkersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        no_subproject=no_subproject,
        employee_ids=employee_ids,
        assigned=assigned,
        project_active=project_active,
        employee_name=employee_name,
        include_inputed_minutes=include_inputed_minutes,
        include_cost=include_cost,
        updated_after=updated_after,
        include_labor_cost=include_labor_cost,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    no_subproject: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    project_active: bool | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    include_labor_cost: bool | Unset = UNSET,
) -> GetApi20260701ResourcesProjectManagementProjectWorkersResponse200 | None:
    """Reads all Project workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        ids (list[str] | Unset): Retrieve only the project workers that matches the ids provided
            in the request. Example: ['92732', '2'].
        project_ids (list[str] | Unset): Retrieve only the project workers that matches the
            project_ids provided in the request. Example: ['314159', '33'].
        subproject_ids (list[str] | Unset): Retrieve only the project workers that matches the
            subproject_ids provided in the request. Example: ['5', '6'].
        no_subproject (bool | Unset): Retrieve the project workers that are not assigned to any
            subproject (can be combined with subproject_ids).
        employee_ids (list[str] | Unset): Retrieve only the project workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve project workers that are assigned if true or in not-
            assigned status if false. Example: True.
        project_active (bool | Unset): Retrieve the project workers that are assigned to active
            projects if turew or closed projects if false. Example: True.
        employee_name (str | Unset): Retrieve only the project workers that matches the given
            employee's name provided in the request. Example: John D.
        include_inputed_minutes (bool | Unset): If true we will perform the minutes calculations
            and will be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If true, costs of the project worker will be included to the
            response. Example: True.
        updated_after (str | Unset): Retrieve only the project workers that were created or
            updated after the date provided in the request. Example: 1993-08-23.
        include_labor_cost (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesProjectManagementProjectWorkersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            project_ids=project_ids,
            subproject_ids=subproject_ids,
            no_subproject=no_subproject,
            employee_ids=employee_ids,
            assigned=assigned,
            project_active=project_active,
            employee_name=employee_name,
            include_inputed_minutes=include_inputed_minutes,
            include_cost=include_cost,
            updated_after=updated_after,
            include_labor_cost=include_labor_cost,
        )
    ).parsed
