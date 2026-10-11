from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_compensations_payroll_run_participants_response_200 import (
    GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    payroll_run_ids: list[str],
    employee_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_payroll_run_ids = payroll_run_ids

    params["payroll_run_ids[]"] = json_payroll_run_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/compensations/payroll_run_participants",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200.from_dict(
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
) -> Response[
    ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    payroll_run_ids: list[str],
    employee_ids: list[str] | Unset = UNSET,
) -> Response[
    ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200
]:
    """Reads all Payroll run participants

     Returns the participants of each regular payroll run: the employees whose payroll results
    compensations/payroll_results bulk_create accepts. Use it before an import to send results
    only for these employees.

    Off-cycle runs (any payment_type other than regular, see compensations/payroll_runs) are
    rejected. They have no fixed population: most of the company's employees are likely to be
    valid for one, so a list from this endpoint would not provide much value when trying to
    know who an off-cycle payment is for. Knowing which employees to sync is a task the
    integration developer should be responsible for: post them directly to bulk_create, whose
    employee checks always act as a guardrail and reject any employee who isn't valid for the
    run.

    The list is not paginated: every participant is returned in one response. It only
    includes employees the caller is allowed to see.

    Args:
        payroll_run_ids (list[str]): Regular payroll run ids, at most 5, refers to
            compensations/payroll_runs endpoint. The only use case so far requests a single run; the
            limit of 5 leaves margin for future integrations while keeping each request cheap.
            Example: ['1'].
        employee_ids (list[str] | Unset): Only consider these employees, refers to
            employees/employees endpoint. When omitted, every employee the caller can see is
            considered. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200]
    """

    kwargs = _get_kwargs(
        payroll_run_ids=payroll_run_ids,
        employee_ids=employee_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    payroll_run_ids: list[str],
    employee_ids: list[str] | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200 | None:
    """Reads all Payroll run participants

     Returns the participants of each regular payroll run: the employees whose payroll results
    compensations/payroll_results bulk_create accepts. Use it before an import to send results
    only for these employees.

    Off-cycle runs (any payment_type other than regular, see compensations/payroll_runs) are
    rejected. They have no fixed population: most of the company's employees are likely to be
    valid for one, so a list from this endpoint would not provide much value when trying to
    know who an off-cycle payment is for. Knowing which employees to sync is a task the
    integration developer should be responsible for: post them directly to bulk_create, whose
    employee checks always act as a guardrail and reject any employee who isn't valid for the
    run.

    The list is not paginated: every participant is returned in one response. It only
    includes employees the caller is allowed to see.

    Args:
        payroll_run_ids (list[str]): Regular payroll run ids, at most 5, refers to
            compensations/payroll_runs endpoint. The only use case so far requests a single run; the
            limit of 5 leaves margin for future integrations while keeping each request cheap.
            Example: ['1'].
        employee_ids (list[str] | Unset): Only consider these employees, refers to
            employees/employees endpoint. When omitted, every employee the caller can see is
            considered. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200
    """

    return sync_detailed(
        client=client,
        payroll_run_ids=payroll_run_ids,
        employee_ids=employee_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    payroll_run_ids: list[str],
    employee_ids: list[str] | Unset = UNSET,
) -> Response[
    ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200
]:
    """Reads all Payroll run participants

     Returns the participants of each regular payroll run: the employees whose payroll results
    compensations/payroll_results bulk_create accepts. Use it before an import to send results
    only for these employees.

    Off-cycle runs (any payment_type other than regular, see compensations/payroll_runs) are
    rejected. They have no fixed population: most of the company's employees are likely to be
    valid for one, so a list from this endpoint would not provide much value when trying to
    know who an off-cycle payment is for. Knowing which employees to sync is a task the
    integration developer should be responsible for: post them directly to bulk_create, whose
    employee checks always act as a guardrail and reject any employee who isn't valid for the
    run.

    The list is not paginated: every participant is returned in one response. It only
    includes employees the caller is allowed to see.

    Args:
        payroll_run_ids (list[str]): Regular payroll run ids, at most 5, refers to
            compensations/payroll_runs endpoint. The only use case so far requests a single run; the
            limit of 5 leaves margin for future integrations while keeping each request cheap.
            Example: ['1'].
        employee_ids (list[str] | Unset): Only consider these employees, refers to
            employees/employees endpoint. When omitted, every employee the caller can see is
            considered. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200]
    """

    kwargs = _get_kwargs(
        payroll_run_ids=payroll_run_ids,
        employee_ids=employee_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    payroll_run_ids: list[str],
    employee_ids: list[str] | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200 | None:
    """Reads all Payroll run participants

     Returns the participants of each regular payroll run: the employees whose payroll results
    compensations/payroll_results bulk_create accepts. Use it before an import to send results
    only for these employees.

    Off-cycle runs (any payment_type other than regular, see compensations/payroll_runs) are
    rejected. They have no fixed population: most of the company's employees are likely to be
    valid for one, so a list from this endpoint would not provide much value when trying to
    know who an off-cycle payment is for. Knowing which employees to sync is a task the
    integration developer should be responsible for: post them directly to bulk_create, whose
    employee checks always act as a guardrail and reject any employee who isn't valid for the
    run.

    The list is not paginated: every participant is returned in one response. It only
    includes employees the caller is allowed to see.

    Args:
        payroll_run_ids (list[str]): Regular payroll run ids, at most 5, refers to
            compensations/payroll_runs endpoint. The only use case so far requests a single run; the
            limit of 5 leaves margin for future integrations while keeping each request cheap.
            Example: ['1'].
        employee_ids (list[str] | Unset): Only consider these employees, refers to
            employees/employees endpoint. When omitted, every employee the caller can see is
            considered. Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesCompensationsPayrollRunParticipantsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            payroll_run_ids=payroll_run_ids,
            employee_ids=employee_ids,
        )
    ).parsed
