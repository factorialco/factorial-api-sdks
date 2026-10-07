from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compensations_payroll_result import CompensationsPayrollResult
from ...models.post_api_20270101_resources_compensations_payroll_results_bulk_create_body import (
    PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/compensations/payroll_results/bulk_create",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[CompensationsPayrollResult] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CompensationsPayrollResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[CompensationsPayrollResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset = UNSET,
) -> Response[list[CompensationsPayrollResult]]:
    r"""Bulk creates a Payroll result

     Imports payroll result amounts for employees of an existing payroll run, for example the
    figures returned by an external payroll provider. Only Factorial ids are accepted.

    The import is atomic: the whole request is validated before anything is written, and any
    error rejects it entirely. A 4xx or 5xx response means nothing was written, so a failed
    request can be retried as is.

    The request is rejected when:
    - it has no results, an employee entry has no items, it carries more than 1,000 amounts,
      or it repeats an employee or a concept for the same employee
    - the payroll run, an employee or a payroll concept does not exist in the company
    - an employee is not part of the payroll run, that is, is not one of the employees
      Factorial lists in that run. On regular runs the employee's contract must cover the run
      period, they must not have been terminated more than 60 days before the run starts and,
      when the run's cycle is limited to a people group, they must belong to it. Off-cycle
      runs only apply the people group and a 365-day termination window. The error lists
      these employees in `errors.employee_ids`, so they can be removed and the rest resent.
      From API version 2027-01-01, compensations/payroll_run_participants returns the
      employees of a regular run that are accepted, so they can be checked beforehand.
    - a concept is a base salary concept or is disabled
    - an employee entry does not include the company's net_pay concept (find its id with
      compensations/concepts)
    - an amount is outside the signed 32-bit integer range

    Re-posting an (employee, concept) pair replaces its amount and keeps the row id. Pairs not
    included in the request are left untouched; there is no delete. Split larger payrolls into
    requests of up to 1,000 amounts, keeping all of an employee's items in the same request.
    Requires the \"Import payroll results\" permission.

    Args:
        body (PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CompensationsPayrollResult]]
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
    body: PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset = UNSET,
) -> list[CompensationsPayrollResult] | None:
    r"""Bulk creates a Payroll result

     Imports payroll result amounts for employees of an existing payroll run, for example the
    figures returned by an external payroll provider. Only Factorial ids are accepted.

    The import is atomic: the whole request is validated before anything is written, and any
    error rejects it entirely. A 4xx or 5xx response means nothing was written, so a failed
    request can be retried as is.

    The request is rejected when:
    - it has no results, an employee entry has no items, it carries more than 1,000 amounts,
      or it repeats an employee or a concept for the same employee
    - the payroll run, an employee or a payroll concept does not exist in the company
    - an employee is not part of the payroll run, that is, is not one of the employees
      Factorial lists in that run. On regular runs the employee's contract must cover the run
      period, they must not have been terminated more than 60 days before the run starts and,
      when the run's cycle is limited to a people group, they must belong to it. Off-cycle
      runs only apply the people group and a 365-day termination window. The error lists
      these employees in `errors.employee_ids`, so they can be removed and the rest resent.
      From API version 2027-01-01, compensations/payroll_run_participants returns the
      employees of a regular run that are accepted, so they can be checked beforehand.
    - a concept is a base salary concept or is disabled
    - an employee entry does not include the company's net_pay concept (find its id with
      compensations/concepts)
    - an amount is outside the signed 32-bit integer range

    Re-posting an (employee, concept) pair replaces its amount and keeps the row id. Pairs not
    included in the request are left untouched; there is no delete. Split larger payrolls into
    requests of up to 1,000 amounts, keeping all of an employee's items in the same request.
    Requires the \"Import payroll results\" permission.

    Args:
        body (PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CompensationsPayrollResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset = UNSET,
) -> Response[list[CompensationsPayrollResult]]:
    r"""Bulk creates a Payroll result

     Imports payroll result amounts for employees of an existing payroll run, for example the
    figures returned by an external payroll provider. Only Factorial ids are accepted.

    The import is atomic: the whole request is validated before anything is written, and any
    error rejects it entirely. A 4xx or 5xx response means nothing was written, so a failed
    request can be retried as is.

    The request is rejected when:
    - it has no results, an employee entry has no items, it carries more than 1,000 amounts,
      or it repeats an employee or a concept for the same employee
    - the payroll run, an employee or a payroll concept does not exist in the company
    - an employee is not part of the payroll run, that is, is not one of the employees
      Factorial lists in that run. On regular runs the employee's contract must cover the run
      period, they must not have been terminated more than 60 days before the run starts and,
      when the run's cycle is limited to a people group, they must belong to it. Off-cycle
      runs only apply the people group and a 365-day termination window. The error lists
      these employees in `errors.employee_ids`, so they can be removed and the rest resent.
      From API version 2027-01-01, compensations/payroll_run_participants returns the
      employees of a regular run that are accepted, so they can be checked beforehand.
    - a concept is a base salary concept or is disabled
    - an employee entry does not include the company's net_pay concept (find its id with
      compensations/concepts)
    - an amount is outside the signed 32-bit integer range

    Re-posting an (employee, concept) pair replaces its amount and keeps the row id. Pairs not
    included in the request are left untouched; there is no delete. Split larger payrolls into
    requests of up to 1,000 amounts, keeping all of an employee's items in the same request.
    Requires the \"Import payroll results\" permission.

    Args:
        body (PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CompensationsPayrollResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset = UNSET,
) -> list[CompensationsPayrollResult] | None:
    r"""Bulk creates a Payroll result

     Imports payroll result amounts for employees of an existing payroll run, for example the
    figures returned by an external payroll provider. Only Factorial ids are accepted.

    The import is atomic: the whole request is validated before anything is written, and any
    error rejects it entirely. A 4xx or 5xx response means nothing was written, so a failed
    request can be retried as is.

    The request is rejected when:
    - it has no results, an employee entry has no items, it carries more than 1,000 amounts,
      or it repeats an employee or a concept for the same employee
    - the payroll run, an employee or a payroll concept does not exist in the company
    - an employee is not part of the payroll run, that is, is not one of the employees
      Factorial lists in that run. On regular runs the employee's contract must cover the run
      period, they must not have been terminated more than 60 days before the run starts and,
      when the run's cycle is limited to a people group, they must belong to it. Off-cycle
      runs only apply the people group and a 365-day termination window. The error lists
      these employees in `errors.employee_ids`, so they can be removed and the rest resent.
      From API version 2027-01-01, compensations/payroll_run_participants returns the
      employees of a regular run that are accepted, so they can be checked beforehand.
    - a concept is a base salary concept or is disabled
    - an employee entry does not include the company's net_pay concept (find its id with
      compensations/concepts)
    - an amount is outside the signed 32-bit integer range

    Re-posting an (employee, concept) pair replaces its amount and keeps the row id. Pairs not
    included in the request are left untouched; there is no delete. Split larger payrolls into
    requests of up to 1,000 amounts, keeping all of an employee's items in the same request.
    Requires the \"Import payroll results\" permission.

    Args:
        body (PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CompensationsPayrollResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
