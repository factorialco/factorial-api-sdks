from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_project_management_rates_resource_kind import (
    GetApi20261001ResourcesProjectManagementRatesResourceKind,
)
from ...models.get_api_20261001_resources_project_management_rates_response_200 import (
    GetApi20261001ResourcesProjectManagementRatesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    resource_ids: list[str] | Unset = UNSET,
    resource_kind: GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset = UNSET,
    reference_rate_id: str | Unset = UNSET,
    role_or_level: str | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    quote_id: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    without_project: bool | Unset = UNSET,
    without_quote: bool | Unset = UNSET,
    record_type: str | Unset = UNSET,
    reference_rate_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["company_id"] = company_id

    params["project_id"] = project_id

    json_resource_ids: list[str] | Unset = UNSET
    if not isinstance(resource_ids, Unset):
        json_resource_ids = resource_ids

    params["resource_ids[]"] = json_resource_ids

    json_resource_kind: str | Unset = UNSET
    if not isinstance(resource_kind, Unset):
        json_resource_kind = resource_kind.value

    params["resource_kind"] = json_resource_kind

    params["reference_rate_id"] = reference_rate_id

    params["role_or_level"] = role_or_level

    params["employee_name"] = employee_name

    params["quote_id"] = quote_id

    params["only_active"] = only_active

    params["without_project"] = without_project

    params["without_quote"] = without_quote

    params["record_type"] = record_type

    json_reference_rate_ids: list[str] | Unset = UNSET
    if not isinstance(reference_rate_ids, Unset):
        json_reference_rate_ids = reference_rate_ids

    params["reference_rate_ids[]"] = json_reference_rate_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/project_management/rates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesProjectManagementRatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesProjectManagementRatesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesProjectManagementRatesResponse200]:
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
    company_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    resource_ids: list[str] | Unset = UNSET,
    resource_kind: GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset = UNSET,
    reference_rate_id: str | Unset = UNSET,
    role_or_level: str | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    quote_id: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    without_project: bool | Unset = UNSET,
    without_quote: bool | Unset = UNSET,
    record_type: str | Unset = UNSET,
    reference_rate_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProjectManagementRatesResponse200]:
    """Reads all Rates

     Read rates

    Args:
        ids (list[str] | Unset): Filter rates by IDs Example: ['1', '2', '3'].
        company_id (str | Unset): Filter rates by company ID Example: 123.
        project_id (str | Unset): Filter rates by project ID Example: 456.
        resource_ids (list[str] | Unset): Filter rates by canonical resource identity (numeric id
            or tree node uuid) Example: ['789', 'jobcatalog_treelevel-13'].
        resource_kind (GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset): Filter
            rates by the kind of resource they apply to. Example: project_worker.
        reference_rate_id (str | Unset): Filter rates by reference rate ID Example: 42.
        role_or_level (str | Unset): Filter rates by job catalog role or level name Example:
            Senior Engineer.
        employee_name (str | Unset): Filter rates by employee name Example: John Doe.
        quote_id (str | Unset): Filter rates by quote ID Example: 99.
        only_active (bool | Unset): If true, retrieve only currently active rates. Example: True.
        without_project (bool | Unset): If true, retrieve only rates that are not linked to a
            project.
        without_quote (bool | Unset): If true, retrieve only rates that are not linked to a quote.
        record_type (str | Unset): Filter rates by record type Example:
            ProjectManagement::Project.
        reference_rate_ids (list[str] | Unset): Filter rates by reference rate IDs Example: [1, 2,
            3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProjectManagementRatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        project_id=project_id,
        resource_ids=resource_ids,
        resource_kind=resource_kind,
        reference_rate_id=reference_rate_id,
        role_or_level=role_or_level,
        employee_name=employee_name,
        quote_id=quote_id,
        only_active=only_active,
        without_project=without_project,
        without_quote=without_quote,
        record_type=record_type,
        reference_rate_ids=reference_rate_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    resource_ids: list[str] | Unset = UNSET,
    resource_kind: GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset = UNSET,
    reference_rate_id: str | Unset = UNSET,
    role_or_level: str | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    quote_id: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    without_project: bool | Unset = UNSET,
    without_quote: bool | Unset = UNSET,
    record_type: str | Unset = UNSET,
    reference_rate_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesProjectManagementRatesResponse200 | None:
    """Reads all Rates

     Read rates

    Args:
        ids (list[str] | Unset): Filter rates by IDs Example: ['1', '2', '3'].
        company_id (str | Unset): Filter rates by company ID Example: 123.
        project_id (str | Unset): Filter rates by project ID Example: 456.
        resource_ids (list[str] | Unset): Filter rates by canonical resource identity (numeric id
            or tree node uuid) Example: ['789', 'jobcatalog_treelevel-13'].
        resource_kind (GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset): Filter
            rates by the kind of resource they apply to. Example: project_worker.
        reference_rate_id (str | Unset): Filter rates by reference rate ID Example: 42.
        role_or_level (str | Unset): Filter rates by job catalog role or level name Example:
            Senior Engineer.
        employee_name (str | Unset): Filter rates by employee name Example: John Doe.
        quote_id (str | Unset): Filter rates by quote ID Example: 99.
        only_active (bool | Unset): If true, retrieve only currently active rates. Example: True.
        without_project (bool | Unset): If true, retrieve only rates that are not linked to a
            project.
        without_quote (bool | Unset): If true, retrieve only rates that are not linked to a quote.
        record_type (str | Unset): Filter rates by record type Example:
            ProjectManagement::Project.
        reference_rate_ids (list[str] | Unset): Filter rates by reference rate IDs Example: [1, 2,
            3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProjectManagementRatesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_id=company_id,
        project_id=project_id,
        resource_ids=resource_ids,
        resource_kind=resource_kind,
        reference_rate_id=reference_rate_id,
        role_or_level=role_or_level,
        employee_name=employee_name,
        quote_id=quote_id,
        only_active=only_active,
        without_project=without_project,
        without_quote=without_quote,
        record_type=record_type,
        reference_rate_ids=reference_rate_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    resource_ids: list[str] | Unset = UNSET,
    resource_kind: GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset = UNSET,
    reference_rate_id: str | Unset = UNSET,
    role_or_level: str | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    quote_id: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    without_project: bool | Unset = UNSET,
    without_quote: bool | Unset = UNSET,
    record_type: str | Unset = UNSET,
    reference_rate_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProjectManagementRatesResponse200]:
    """Reads all Rates

     Read rates

    Args:
        ids (list[str] | Unset): Filter rates by IDs Example: ['1', '2', '3'].
        company_id (str | Unset): Filter rates by company ID Example: 123.
        project_id (str | Unset): Filter rates by project ID Example: 456.
        resource_ids (list[str] | Unset): Filter rates by canonical resource identity (numeric id
            or tree node uuid) Example: ['789', 'jobcatalog_treelevel-13'].
        resource_kind (GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset): Filter
            rates by the kind of resource they apply to. Example: project_worker.
        reference_rate_id (str | Unset): Filter rates by reference rate ID Example: 42.
        role_or_level (str | Unset): Filter rates by job catalog role or level name Example:
            Senior Engineer.
        employee_name (str | Unset): Filter rates by employee name Example: John Doe.
        quote_id (str | Unset): Filter rates by quote ID Example: 99.
        only_active (bool | Unset): If true, retrieve only currently active rates. Example: True.
        without_project (bool | Unset): If true, retrieve only rates that are not linked to a
            project.
        without_quote (bool | Unset): If true, retrieve only rates that are not linked to a quote.
        record_type (str | Unset): Filter rates by record type Example:
            ProjectManagement::Project.
        reference_rate_ids (list[str] | Unset): Filter rates by reference rate IDs Example: [1, 2,
            3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProjectManagementRatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        project_id=project_id,
        resource_ids=resource_ids,
        resource_kind=resource_kind,
        reference_rate_id=reference_rate_id,
        role_or_level=role_or_level,
        employee_name=employee_name,
        quote_id=quote_id,
        only_active=only_active,
        without_project=without_project,
        without_quote=without_quote,
        record_type=record_type,
        reference_rate_ids=reference_rate_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    resource_ids: list[str] | Unset = UNSET,
    resource_kind: GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset = UNSET,
    reference_rate_id: str | Unset = UNSET,
    role_or_level: str | Unset = UNSET,
    employee_name: str | Unset = UNSET,
    quote_id: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    without_project: bool | Unset = UNSET,
    without_quote: bool | Unset = UNSET,
    record_type: str | Unset = UNSET,
    reference_rate_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesProjectManagementRatesResponse200 | None:
    """Reads all Rates

     Read rates

    Args:
        ids (list[str] | Unset): Filter rates by IDs Example: ['1', '2', '3'].
        company_id (str | Unset): Filter rates by company ID Example: 123.
        project_id (str | Unset): Filter rates by project ID Example: 456.
        resource_ids (list[str] | Unset): Filter rates by canonical resource identity (numeric id
            or tree node uuid) Example: ['789', 'jobcatalog_treelevel-13'].
        resource_kind (GetApi20261001ResourcesProjectManagementRatesResourceKind | Unset): Filter
            rates by the kind of resource they apply to. Example: project_worker.
        reference_rate_id (str | Unset): Filter rates by reference rate ID Example: 42.
        role_or_level (str | Unset): Filter rates by job catalog role or level name Example:
            Senior Engineer.
        employee_name (str | Unset): Filter rates by employee name Example: John Doe.
        quote_id (str | Unset): Filter rates by quote ID Example: 99.
        only_active (bool | Unset): If true, retrieve only currently active rates. Example: True.
        without_project (bool | Unset): If true, retrieve only rates that are not linked to a
            project.
        without_quote (bool | Unset): If true, retrieve only rates that are not linked to a quote.
        record_type (str | Unset): Filter rates by record type Example:
            ProjectManagement::Project.
        reference_rate_ids (list[str] | Unset): Filter rates by reference rate IDs Example: [1, 2,
            3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProjectManagementRatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_id=company_id,
            project_id=project_id,
            resource_ids=resource_ids,
            resource_kind=resource_kind,
            reference_rate_id=reference_rate_id,
            role_or_level=role_or_level,
            employee_name=employee_name,
            quote_id=quote_id,
            only_active=only_active,
            without_project=without_project,
            without_quote=without_quote,
            record_type=record_type,
            reference_rate_ids=reference_rate_ids,
        )
    ).parsed
