from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_project_management_subproject_workers_response_200 import (
    GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    subproject_id: str | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    project_id: str | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["subproject_id"] = subproject_id

    json_subproject_ids: list[str] | Unset = UNSET
    if not isinstance(subproject_ids, Unset):
        json_subproject_ids = subproject_ids

    params["subproject_ids[]"] = json_subproject_ids

    params["project_id"] = project_id

    json_project_ids: list[str] | Unset = UNSET
    if not isinstance(project_ids, Unset):
        json_project_ids = project_ids

    params["project_ids[]"] = json_project_ids

    params["employee_id"] = employee_id

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["assigned"] = assigned

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/project_management/subproject_workers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200.from_dict(
                response.json()
            )
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
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200]:
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
    subproject_id: str | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    project_id: str | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200]:
    """Reads all Subproject workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of subproject workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A subproject_worker is always related to a subproject and a project worker.
    ###### **Who can use it?**
    Only companies in the phase assignment beta who have enabled the `projects_with_subprojects`
    feature. Users only get the subproject workers of the project workers they can already see.

    Args:
        ids (list[str] | Unset): Retrieve only the subproject workers that matches the ids
            provided in the request. Example: ['51234', '2'].
        subproject_id (str | Unset): Retrieve only the subproject workers of the subproject_id
            provided in the request. Example: 314.
        subproject_ids (list[str] | Unset): Retrieve only the subproject workers that matches the
            subproject_ids provided in the request. Example: ['314', '315'].
        project_id (str | Unset): Retrieve only the subproject workers whose subproject belongs to
            the project_id provided in the request. Example: 314159.
        project_ids (list[str] | Unset): Retrieve only the subproject workers whose subproject
            belongs to the project_ids provided in the request. Example: ['314159', '33'].
        employee_id (str | Unset): Retrieve only the subproject workers that are related to the
            employee_id provided in the request. Example: 21.
        employee_ids (list[str] | Unset): Retrieve only the subproject workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve subproject workers that are assigned if true or in not-
            assigned status if false. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        subproject_id=subproject_id,
        subproject_ids=subproject_ids,
        project_id=project_id,
        project_ids=project_ids,
        employee_id=employee_id,
        employee_ids=employee_ids,
        assigned=assigned,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    subproject_id: str | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    project_id: str | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200 | None:
    """Reads all Subproject workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of subproject workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A subproject_worker is always related to a subproject and a project worker.
    ###### **Who can use it?**
    Only companies in the phase assignment beta who have enabled the `projects_with_subprojects`
    feature. Users only get the subproject workers of the project workers they can already see.

    Args:
        ids (list[str] | Unset): Retrieve only the subproject workers that matches the ids
            provided in the request. Example: ['51234', '2'].
        subproject_id (str | Unset): Retrieve only the subproject workers of the subproject_id
            provided in the request. Example: 314.
        subproject_ids (list[str] | Unset): Retrieve only the subproject workers that matches the
            subproject_ids provided in the request. Example: ['314', '315'].
        project_id (str | Unset): Retrieve only the subproject workers whose subproject belongs to
            the project_id provided in the request. Example: 314159.
        project_ids (list[str] | Unset): Retrieve only the subproject workers whose subproject
            belongs to the project_ids provided in the request. Example: ['314159', '33'].
        employee_id (str | Unset): Retrieve only the subproject workers that are related to the
            employee_id provided in the request. Example: 21.
        employee_ids (list[str] | Unset): Retrieve only the subproject workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve subproject workers that are assigned if true or in not-
            assigned status if false. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        subproject_id=subproject_id,
        subproject_ids=subproject_ids,
        project_id=project_id,
        project_ids=project_ids,
        employee_id=employee_id,
        employee_ids=employee_ids,
        assigned=assigned,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    subproject_id: str | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    project_id: str | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200]:
    """Reads all Subproject workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of subproject workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A subproject_worker is always related to a subproject and a project worker.
    ###### **Who can use it?**
    Only companies in the phase assignment beta who have enabled the `projects_with_subprojects`
    feature. Users only get the subproject workers of the project workers they can already see.

    Args:
        ids (list[str] | Unset): Retrieve only the subproject workers that matches the ids
            provided in the request. Example: ['51234', '2'].
        subproject_id (str | Unset): Retrieve only the subproject workers of the subproject_id
            provided in the request. Example: 314.
        subproject_ids (list[str] | Unset): Retrieve only the subproject workers that matches the
            subproject_ids provided in the request. Example: ['314', '315'].
        project_id (str | Unset): Retrieve only the subproject workers whose subproject belongs to
            the project_id provided in the request. Example: 314159.
        project_ids (list[str] | Unset): Retrieve only the subproject workers whose subproject
            belongs to the project_ids provided in the request. Example: ['314159', '33'].
        employee_id (str | Unset): Retrieve only the subproject workers that are related to the
            employee_id provided in the request. Example: 21.
        employee_ids (list[str] | Unset): Retrieve only the subproject workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve subproject workers that are assigned if true or in not-
            assigned status if false. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        subproject_id=subproject_id,
        subproject_ids=subproject_ids,
        project_id=project_id,
        project_ids=project_ids,
        employee_id=employee_id,
        employee_ids=employee_ids,
        assigned=assigned,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    subproject_id: str | Unset = UNSET,
    subproject_ids: list[str] | Unset = UNSET,
    project_id: str | Unset = UNSET,
    project_ids: list[str] | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200 | None:
    """Reads all Subproject workers

     ###### **What does it do?**
    This endpoint reads and retrieves a list of subproject workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A subproject_worker is always related to a subproject and a project worker.
    ###### **Who can use it?**
    Only companies in the phase assignment beta who have enabled the `projects_with_subprojects`
    feature. Users only get the subproject workers of the project workers they can already see.

    Args:
        ids (list[str] | Unset): Retrieve only the subproject workers that matches the ids
            provided in the request. Example: ['51234', '2'].
        subproject_id (str | Unset): Retrieve only the subproject workers of the subproject_id
            provided in the request. Example: 314.
        subproject_ids (list[str] | Unset): Retrieve only the subproject workers that matches the
            subproject_ids provided in the request. Example: ['314', '315'].
        project_id (str | Unset): Retrieve only the subproject workers whose subproject belongs to
            the project_id provided in the request. Example: 314159.
        project_ids (list[str] | Unset): Retrieve only the subproject workers whose subproject
            belongs to the project_ids provided in the request. Example: ['314159', '33'].
        employee_id (str | Unset): Retrieve only the subproject workers that are related to the
            employee_id provided in the request. Example: 21.
        employee_ids (list[str] | Unset): Retrieve only the subproject workers that are related to
            the employee_ids provided in the request. Example: ['21', '22'].
        assigned (bool | Unset): Retrieve subproject workers that are assigned if true or in not-
            assigned status if false. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProjectManagementSubprojectWorkersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            subproject_id=subproject_id,
            subproject_ids=subproject_ids,
            project_id=project_id,
            project_ids=project_ids,
            employee_id=employee_id,
            employee_ids=employee_ids,
            assigned=assigned,
        )
    ).parsed
