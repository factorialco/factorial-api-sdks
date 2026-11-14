from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_project_management_subprojects_response_200 import (
    GetApi20270101ResourcesProjectManagementSubprojectsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    include_no_subproject: bool | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
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

    params["name"] = name

    params["include_no_subproject"] = include_no_subproject

    params["include_inputed_minutes"] = include_inputed_minutes

    params["include_cost"] = include_cost

    params["updated_after"] = updated_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/project_management/subprojects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesProjectManagementSubprojectsResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200]:
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
    name: str | Unset = UNSET,
    include_no_subproject: bool | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200]:
    r"""Reads all Subprojects

     ###### **What does it do?**
    This reads all subprojects created
    ###### **What params does it accept?**

      - `ids`: retrieve only the subprojects that matches the ids passed in the request.\n
      - `include_inputed_minutes`: if `true` we will perform the minutes calculations and will be return
    the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE`
    so it will return `inputed_minutes: 0` and no minutes calculations will be performed.
      - `updated_after`: this parameter is needed to filter subprojects created or updated after a date.

    ###### **Is it related to other entities?**
    A subproject is always related to a project, so you can use the query params to list only the
    subprojects that are related to a specific project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with the
    permission of read subprojects.

    Args:
        ids (list[str] | Unset): Retrieve only the subprojects that matches the ids passed in the
            request. Example: ['314'].
        project_ids (list[str] | Unset): Retrieve only the subprojects that belongs to the project
            ids passed in the request. Example: ['11'].
        name (str | Unset): Retrieve only the subprojects that matches the name passed in the
            request. Example: Subproject name.
        include_no_subproject (bool | Unset):
        include_inputed_minutes (bool | Unset): If `true` we will perform the minutes calculations
            and will be return the total `inputed_minutes`. If the param is not passed in the request,
            its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If `true` we will perform the cost calculations and will be
            return the total `labor_cost_cents`. If the param is not passed in the request, its
            default value is `FALSE` so it will return `labor_cost_cents: 0` and no cost calculations
            will be performed. Example: True.
        updated_after (str | Unset): Retrieve only the subprojects that were updated after the
            date passed in the request. Example: 1993-08-23.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_ids=project_ids,
        name=name,
        include_no_subproject=include_no_subproject,
        include_inputed_minutes=include_inputed_minutes,
        include_cost=include_cost,
        updated_after=updated_after,
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
    name: str | Unset = UNSET,
    include_no_subproject: bool | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200 | None:
    r"""Reads all Subprojects

     ###### **What does it do?**
    This reads all subprojects created
    ###### **What params does it accept?**

      - `ids`: retrieve only the subprojects that matches the ids passed in the request.\n
      - `include_inputed_minutes`: if `true` we will perform the minutes calculations and will be return
    the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE`
    so it will return `inputed_minutes: 0` and no minutes calculations will be performed.
      - `updated_after`: this parameter is needed to filter subprojects created or updated after a date.

    ###### **Is it related to other entities?**
    A subproject is always related to a project, so you can use the query params to list only the
    subprojects that are related to a specific project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with the
    permission of read subprojects.

    Args:
        ids (list[str] | Unset): Retrieve only the subprojects that matches the ids passed in the
            request. Example: ['314'].
        project_ids (list[str] | Unset): Retrieve only the subprojects that belongs to the project
            ids passed in the request. Example: ['11'].
        name (str | Unset): Retrieve only the subprojects that matches the name passed in the
            request. Example: Subproject name.
        include_no_subproject (bool | Unset):
        include_inputed_minutes (bool | Unset): If `true` we will perform the minutes calculations
            and will be return the total `inputed_minutes`. If the param is not passed in the request,
            its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If `true` we will perform the cost calculations and will be
            return the total `labor_cost_cents`. If the param is not passed in the request, its
            default value is `FALSE` so it will return `labor_cost_cents: 0` and no cost calculations
            will be performed. Example: True.
        updated_after (str | Unset): Retrieve only the subprojects that were updated after the
            date passed in the request. Example: 1993-08-23.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        project_ids=project_ids,
        name=name,
        include_no_subproject=include_no_subproject,
        include_inputed_minutes=include_inputed_minutes,
        include_cost=include_cost,
        updated_after=updated_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    include_no_subproject: bool | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200]:
    r"""Reads all Subprojects

     ###### **What does it do?**
    This reads all subprojects created
    ###### **What params does it accept?**

      - `ids`: retrieve only the subprojects that matches the ids passed in the request.\n
      - `include_inputed_minutes`: if `true` we will perform the minutes calculations and will be return
    the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE`
    so it will return `inputed_minutes: 0` and no minutes calculations will be performed.
      - `updated_after`: this parameter is needed to filter subprojects created or updated after a date.

    ###### **Is it related to other entities?**
    A subproject is always related to a project, so you can use the query params to list only the
    subprojects that are related to a specific project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with the
    permission of read subprojects.

    Args:
        ids (list[str] | Unset): Retrieve only the subprojects that matches the ids passed in the
            request. Example: ['314'].
        project_ids (list[str] | Unset): Retrieve only the subprojects that belongs to the project
            ids passed in the request. Example: ['11'].
        name (str | Unset): Retrieve only the subprojects that matches the name passed in the
            request. Example: Subproject name.
        include_no_subproject (bool | Unset):
        include_inputed_minutes (bool | Unset): If `true` we will perform the minutes calculations
            and will be return the total `inputed_minutes`. If the param is not passed in the request,
            its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If `true` we will perform the cost calculations and will be
            return the total `labor_cost_cents`. If the param is not passed in the request, its
            default value is `FALSE` so it will return `labor_cost_cents: 0` and no cost calculations
            will be performed. Example: True.
        updated_after (str | Unset): Retrieve only the subprojects that were updated after the
            date passed in the request. Example: 1993-08-23.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_ids=project_ids,
        name=name,
        include_no_subproject=include_no_subproject,
        include_inputed_minutes=include_inputed_minutes,
        include_cost=include_cost,
        updated_after=updated_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    include_no_subproject: bool | Unset = UNSET,
    include_inputed_minutes: bool | Unset = UNSET,
    include_cost: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200 | None:
    r"""Reads all Subprojects

     ###### **What does it do?**
    This reads all subprojects created
    ###### **What params does it accept?**

      - `ids`: retrieve only the subprojects that matches the ids passed in the request.\n
      - `include_inputed_minutes`: if `true` we will perform the minutes calculations and will be return
    the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE`
    so it will return `inputed_minutes: 0` and no minutes calculations will be performed.
      - `updated_after`: this parameter is needed to filter subprojects created or updated after a date.

    ###### **Is it related to other entities?**
    A subproject is always related to a project, so you can use the query params to list only the
    subprojects that are related to a specific project.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with the
    permission of read subprojects.

    Args:
        ids (list[str] | Unset): Retrieve only the subprojects that matches the ids passed in the
            request. Example: ['314'].
        project_ids (list[str] | Unset): Retrieve only the subprojects that belongs to the project
            ids passed in the request. Example: ['11'].
        name (str | Unset): Retrieve only the subprojects that matches the name passed in the
            request. Example: Subproject name.
        include_no_subproject (bool | Unset):
        include_inputed_minutes (bool | Unset): If `true` we will perform the minutes calculations
            and will be return the total `inputed_minutes`. If the param is not passed in the request,
            its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes
            calculations will be performed. Example: True.
        include_cost (bool | Unset): If `true` we will perform the cost calculations and will be
            return the total `labor_cost_cents`. If the param is not passed in the request, its
            default value is `FALSE` so it will return `labor_cost_cents: 0` and no cost calculations
            will be performed. Example: True.
        updated_after (str | Unset): Retrieve only the subprojects that were updated after the
            date passed in the request. Example: 1993-08-23.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            project_ids=project_ids,
            name=name,
            include_no_subproject=include_no_subproject,
            include_inputed_minutes=include_inputed_minutes,
            include_cost=include_cost,
            updated_after=updated_after,
        )
    ).parsed
