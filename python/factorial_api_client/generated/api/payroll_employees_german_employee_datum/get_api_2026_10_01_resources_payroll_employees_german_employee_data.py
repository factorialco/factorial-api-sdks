from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_payroll_employees_german_employee_data_response_200 import (
    GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/payroll_employees/german_employee_data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200.from_dict(
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
) -> Response[GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200]:
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
    employee_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200]:
    """Reads all German employee data

     Reads German-specific payroll data records for employees

    Args:
        ids (list[str] | Unset): Filter by identifiers of the German employee data records
            Example: ['1'].
        employee_ids (list[str] | Unset): Filter by employee identifiers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
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
    employee_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200 | None:
    """Reads all German employee data

     Reads German-specific payroll data records for employees

    Args:
        ids (list[str] | Unset): Filter by identifiers of the German employee data records
            Example: ['1'].
        employee_ids (list[str] | Unset): Filter by employee identifiers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200]:
    """Reads all German employee data

     Reads German-specific payroll data records for employees

    Args:
        ids (list[str] | Unset): Filter by identifiers of the German employee data records
            Example: ['1'].
        employee_ids (list[str] | Unset): Filter by employee identifiers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200 | None:
    """Reads all German employee data

     Reads German-specific payroll data records for employees

    Args:
        ids (list[str] | Unset): Filter by identifiers of the German employee data records
            Example: ['1'].
        employee_ids (list[str] | Unset): Filter by employee identifiers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesPayrollEmployeesGermanEmployeeDataResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
        )
    ).parsed
