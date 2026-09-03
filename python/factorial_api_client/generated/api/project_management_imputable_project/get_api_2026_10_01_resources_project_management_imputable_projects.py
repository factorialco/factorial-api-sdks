from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_project_management_imputable_projects_response_200 import (
    GetApi20261001ResourcesProjectManagementImputableProjectsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["name_or_code"] = name_or_code

    params["only_active"] = only_active

    params["assigned"] = assigned

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/project_management/imputable_projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesProjectManagementImputableProjectsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20261001ResourcesProjectManagementImputableProjectsResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesProjectManagementImputableProjectsResponse200]:
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
    name_or_code: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProjectManagementImputableProjectsResponse200]:
    """Reads all Imputable projects

     Reads all Imputable projects

    Args:
        ids (list[str] | Unset): Retrieve only the imputable projects that match the ids provided
            in the request. Example: ['314159', '271828'].
        name_or_code (str | Unset): Retrieve only the imputable projects that match the name or
            code passed in the request. Example: DS.
        only_active (bool | Unset): If true, retrieve only active imputable projects. Example:
            True.
        assigned (bool | Unset): If true, retrieve only imputable projects that have at least one
            assigned project worker.
        employee_ids (list[str] | Unset): Retrieve only the imputable projects in which the
            employees passed in the request are project workers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProjectManagementImputableProjectsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        name_or_code=name_or_code,
        only_active=only_active,
        assigned=assigned,
        employee_ids=employee_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesProjectManagementImputableProjectsResponse200 | None:
    """Reads all Imputable projects

     Reads all Imputable projects

    Args:
        ids (list[str] | Unset): Retrieve only the imputable projects that match the ids provided
            in the request. Example: ['314159', '271828'].
        name_or_code (str | Unset): Retrieve only the imputable projects that match the name or
            code passed in the request. Example: DS.
        only_active (bool | Unset): If true, retrieve only active imputable projects. Example:
            True.
        assigned (bool | Unset): If true, retrieve only imputable projects that have at least one
            assigned project worker.
        employee_ids (list[str] | Unset): Retrieve only the imputable projects in which the
            employees passed in the request are project workers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProjectManagementImputableProjectsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        name_or_code=name_or_code,
        only_active=only_active,
        assigned=assigned,
        employee_ids=employee_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProjectManagementImputableProjectsResponse200]:
    """Reads all Imputable projects

     Reads all Imputable projects

    Args:
        ids (list[str] | Unset): Retrieve only the imputable projects that match the ids provided
            in the request. Example: ['314159', '271828'].
        name_or_code (str | Unset): Retrieve only the imputable projects that match the name or
            code passed in the request. Example: DS.
        only_active (bool | Unset): If true, retrieve only active imputable projects. Example:
            True.
        assigned (bool | Unset): If true, retrieve only imputable projects that have at least one
            assigned project worker.
        employee_ids (list[str] | Unset): Retrieve only the imputable projects in which the
            employees passed in the request are project workers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProjectManagementImputableProjectsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        name_or_code=name_or_code,
        only_active=only_active,
        assigned=assigned,
        employee_ids=employee_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    assigned: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesProjectManagementImputableProjectsResponse200 | None:
    """Reads all Imputable projects

     Reads all Imputable projects

    Args:
        ids (list[str] | Unset): Retrieve only the imputable projects that match the ids provided
            in the request. Example: ['314159', '271828'].
        name_or_code (str | Unset): Retrieve only the imputable projects that match the name or
            code passed in the request. Example: DS.
        only_active (bool | Unset): If true, retrieve only active imputable projects. Example:
            True.
        assigned (bool | Unset): If true, retrieve only imputable projects that have at least one
            assigned project worker.
        employee_ids (list[str] | Unset): Retrieve only the imputable projects in which the
            employees passed in the request are project workers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProjectManagementImputableProjectsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            name_or_code=name_or_code,
            only_active=only_active,
            assigned=assigned,
            employee_ids=employee_ids,
        )
    ).parsed
