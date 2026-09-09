from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_compensations_employees_compensations_response_200 import (
    GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    payroll_run_ids: list[str] | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    payroll_run_employee_ids: list[str] | Unset = UNSET,
    payroll_concept_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_payroll_run_ids: list[str] | Unset = UNSET
    if not isinstance(payroll_run_ids, Unset):
        json_payroll_run_ids = payroll_run_ids

    params["payroll_run_ids[]"] = json_payroll_run_ids

    json_cycle_ids: list[str] | Unset = UNSET
    if not isinstance(cycle_ids, Unset):
        json_cycle_ids = cycle_ids

    params["cycle_ids[]"] = json_cycle_ids

    json_payroll_run_employee_ids: list[str] | Unset = UNSET
    if not isinstance(payroll_run_employee_ids, Unset):
        json_payroll_run_employee_ids = payroll_run_employee_ids

    params["payroll_run_employee_ids[]"] = json_payroll_run_employee_ids

    json_payroll_concept_ids: list[str] | Unset = UNSET
    if not isinstance(payroll_concept_ids, Unset):
        json_payroll_concept_ids = payroll_concept_ids

    params["payroll_concept_ids[]"] = json_payroll_concept_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/compensations/employees_compensations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200.from_dict(
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
) -> Response[GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200]:
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
    payroll_run_ids: list[str] | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    payroll_run_employee_ids: list[str] | Unset = UNSET,
    payroll_concept_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200]:
    """Reads all Employees compensations

     Retrieves employee compensations (result_type=compensation)

    Args:
        ids (list[str] | Unset): Employee compensation ids Example: ['1'].
        payroll_run_ids (list[str] | Unset): Filter by payroll run ids, refers to
            compensations/payroll_runs endpoint. Example: ['1'].
        cycle_ids (list[str] | Unset): Filter by parent cycle ids, refers to compensations/cycles
            endpoint. Example: ['1'].
        payroll_run_employee_ids (list[str] | Unset): Filter by employee ids (participants of the
            payroll run) Example: ['1'].
        payroll_concept_ids (list[str] | Unset): Filter by payroll concept ids, refers to
            compensations/concepts endpoint. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        payroll_run_ids=payroll_run_ids,
        cycle_ids=cycle_ids,
        payroll_run_employee_ids=payroll_run_employee_ids,
        payroll_concept_ids=payroll_concept_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    payroll_run_ids: list[str] | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    payroll_run_employee_ids: list[str] | Unset = UNSET,
    payroll_concept_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200 | None:
    """Reads all Employees compensations

     Retrieves employee compensations (result_type=compensation)

    Args:
        ids (list[str] | Unset): Employee compensation ids Example: ['1'].
        payroll_run_ids (list[str] | Unset): Filter by payroll run ids, refers to
            compensations/payroll_runs endpoint. Example: ['1'].
        cycle_ids (list[str] | Unset): Filter by parent cycle ids, refers to compensations/cycles
            endpoint. Example: ['1'].
        payroll_run_employee_ids (list[str] | Unset): Filter by employee ids (participants of the
            payroll run) Example: ['1'].
        payroll_concept_ids (list[str] | Unset): Filter by payroll concept ids, refers to
            compensations/concepts endpoint. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        payroll_run_ids=payroll_run_ids,
        cycle_ids=cycle_ids,
        payroll_run_employee_ids=payroll_run_employee_ids,
        payroll_concept_ids=payroll_concept_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    payroll_run_ids: list[str] | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    payroll_run_employee_ids: list[str] | Unset = UNSET,
    payroll_concept_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200]:
    """Reads all Employees compensations

     Retrieves employee compensations (result_type=compensation)

    Args:
        ids (list[str] | Unset): Employee compensation ids Example: ['1'].
        payroll_run_ids (list[str] | Unset): Filter by payroll run ids, refers to
            compensations/payroll_runs endpoint. Example: ['1'].
        cycle_ids (list[str] | Unset): Filter by parent cycle ids, refers to compensations/cycles
            endpoint. Example: ['1'].
        payroll_run_employee_ids (list[str] | Unset): Filter by employee ids (participants of the
            payroll run) Example: ['1'].
        payroll_concept_ids (list[str] | Unset): Filter by payroll concept ids, refers to
            compensations/concepts endpoint. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        payroll_run_ids=payroll_run_ids,
        cycle_ids=cycle_ids,
        payroll_run_employee_ids=payroll_run_employee_ids,
        payroll_concept_ids=payroll_concept_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    payroll_run_ids: list[str] | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    payroll_run_employee_ids: list[str] | Unset = UNSET,
    payroll_concept_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200 | None:
    """Reads all Employees compensations

     Retrieves employee compensations (result_type=compensation)

    Args:
        ids (list[str] | Unset): Employee compensation ids Example: ['1'].
        payroll_run_ids (list[str] | Unset): Filter by payroll run ids, refers to
            compensations/payroll_runs endpoint. Example: ['1'].
        cycle_ids (list[str] | Unset): Filter by parent cycle ids, refers to compensations/cycles
            endpoint. Example: ['1'].
        payroll_run_employee_ids (list[str] | Unset): Filter by employee ids (participants of the
            payroll run) Example: ['1'].
        payroll_concept_ids (list[str] | Unset): Filter by payroll concept ids, refers to
            compensations/concepts endpoint. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesCompensationsEmployeesCompensationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            payroll_run_ids=payroll_run_ids,
            cycle_ids=cycle_ids,
            payroll_run_employee_ids=payroll_run_employee_ids,
            payroll_concept_ids=payroll_concept_ids,
        )
    ).parsed
