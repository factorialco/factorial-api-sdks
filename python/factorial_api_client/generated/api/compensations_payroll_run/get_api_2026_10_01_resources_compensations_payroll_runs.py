from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_compensations_payroll_runs_payment_types import (
    GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes,
)
from ...models.get_api_20261001_resources_compensations_payroll_runs_response_200 import (
    GetApi20261001ResourcesCompensationsPayrollRunsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    payment_types: GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["from"] = from_

    params["to"] = to

    params["company_id"] = company_id

    json_cycle_ids: list[str] | Unset = UNSET
    if not isinstance(cycle_ids, Unset):
        json_cycle_ids = cycle_ids

    params["cycle_ids[]"] = json_cycle_ids

    json_statuses: list[str] | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses

    params["statuses[]"] = json_statuses

    json_payment_types: str | Unset = UNSET
    if not isinstance(payment_types, Unset):
        json_payment_types = payment_types.value

    params["payment_types[]"] = json_payment_types

    params["include_hidden"] = include_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/compensations/payroll_runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesCompensationsPayrollRunsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesCompensationsPayrollRunsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesCompensationsPayrollRunsResponse200]:
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
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    payment_types: GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesCompensationsPayrollRunsResponse200]:
    """Reads all Payroll runs

     Retrieves payroll runs

    Args:
        ids (list[str] | Unset): Filter by payroll run ids Example: ['1'].
        from_ (str | Unset): Lower bound for the run end date (ends_on >= from) Example:
            2026-01-01.
        to (str | Unset): Upper bound for the run start date (starts_on <= to) Example:
            2026-12-31.
        company_id (str | Unset): Filter by company id (single) Example: 1.
        cycle_ids (list[str] | Unset): Filter by parent cycle ids Example: ['1'].
        statuses (list[str] | Unset): Filter by run statuses Example: ['open'].
        payment_types (GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset):
            Filter by payment types (regular, extra_pay) Example: ['regular'].
        include_hidden (bool | Unset): Include hidden cycles' runs in the response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesCompensationsPayrollRunsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        from_=from_,
        to=to,
        company_id=company_id,
        cycle_ids=cycle_ids,
        statuses=statuses,
        payment_types=payment_types,
        include_hidden=include_hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    payment_types: GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
) -> GetApi20261001ResourcesCompensationsPayrollRunsResponse200 | None:
    """Reads all Payroll runs

     Retrieves payroll runs

    Args:
        ids (list[str] | Unset): Filter by payroll run ids Example: ['1'].
        from_ (str | Unset): Lower bound for the run end date (ends_on >= from) Example:
            2026-01-01.
        to (str | Unset): Upper bound for the run start date (starts_on <= to) Example:
            2026-12-31.
        company_id (str | Unset): Filter by company id (single) Example: 1.
        cycle_ids (list[str] | Unset): Filter by parent cycle ids Example: ['1'].
        statuses (list[str] | Unset): Filter by run statuses Example: ['open'].
        payment_types (GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset):
            Filter by payment types (regular, extra_pay) Example: ['regular'].
        include_hidden (bool | Unset): Include hidden cycles' runs in the response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesCompensationsPayrollRunsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        from_=from_,
        to=to,
        company_id=company_id,
        cycle_ids=cycle_ids,
        statuses=statuses,
        payment_types=payment_types,
        include_hidden=include_hidden,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    payment_types: GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesCompensationsPayrollRunsResponse200]:
    """Reads all Payroll runs

     Retrieves payroll runs

    Args:
        ids (list[str] | Unset): Filter by payroll run ids Example: ['1'].
        from_ (str | Unset): Lower bound for the run end date (ends_on >= from) Example:
            2026-01-01.
        to (str | Unset): Upper bound for the run start date (starts_on <= to) Example:
            2026-12-31.
        company_id (str | Unset): Filter by company id (single) Example: 1.
        cycle_ids (list[str] | Unset): Filter by parent cycle ids Example: ['1'].
        statuses (list[str] | Unset): Filter by run statuses Example: ['open'].
        payment_types (GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset):
            Filter by payment types (regular, extra_pay) Example: ['regular'].
        include_hidden (bool | Unset): Include hidden cycles' runs in the response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesCompensationsPayrollRunsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        from_=from_,
        to=to,
        company_id=company_id,
        cycle_ids=cycle_ids,
        statuses=statuses,
        payment_types=payment_types,
        include_hidden=include_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cycle_ids: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    payment_types: GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
) -> GetApi20261001ResourcesCompensationsPayrollRunsResponse200 | None:
    """Reads all Payroll runs

     Retrieves payroll runs

    Args:
        ids (list[str] | Unset): Filter by payroll run ids Example: ['1'].
        from_ (str | Unset): Lower bound for the run end date (ends_on >= from) Example:
            2026-01-01.
        to (str | Unset): Upper bound for the run start date (starts_on <= to) Example:
            2026-12-31.
        company_id (str | Unset): Filter by company id (single) Example: 1.
        cycle_ids (list[str] | Unset): Filter by parent cycle ids Example: ['1'].
        statuses (list[str] | Unset): Filter by run statuses Example: ['open'].
        payment_types (GetApi20261001ResourcesCompensationsPayrollRunsPaymentTypes | Unset):
            Filter by payment types (regular, extra_pay) Example: ['regular'].
        include_hidden (bool | Unset): Include hidden cycles' runs in the response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesCompensationsPayrollRunsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            from_=from_,
            to=to,
            company_id=company_id,
            cycle_ids=cycle_ids,
            statuses=statuses,
            payment_types=payment_types,
            include_hidden=include_hidden,
        )
    ).parsed
