from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_payroll_employees_identifiers_country import (
    GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry,
)
from ...models.get_api_20260401_resources_payroll_employees_identifiers_response_200 import (
    GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    legal_entities_ids: list[int] | Unset = UNSET,
    country: GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employees_ids: list[int] | Unset = UNSET
    if not isinstance(employees_ids, Unset):
        json_employees_ids = employees_ids

    params["employees_ids[]"] = json_employees_ids

    json_legal_entities_ids: list[int] | Unset = UNSET
    if not isinstance(legal_entities_ids, Unset):
        json_legal_entities_ids = legal_entities_ids

    params["legal_entities_ids[]"] = json_legal_entities_ids

    json_country = country.value
    params["country"] = json_country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/payroll_employees/identifiers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    legal_entities_ids: list[int] | Unset = UNSET,
    country: GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry,
) -> Response[GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200]:
    """Reads all Identifiers

     Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

    Args:
        ids (list[int] | Unset):
        employees_ids (list[int] | Unset): filters by employee identifiers Example: [1, 2, 3].
        legal_entities_ids (list[int] | Unset):
        country (GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry): filters by country
            code pt | it | de Example: it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employees_ids=employees_ids,
        legal_entities_ids=legal_entities_ids,
        country=country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    legal_entities_ids: list[int] | Unset = UNSET,
    country: GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry,
) -> GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200 | None:
    """Reads all Identifiers

     Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

    Args:
        ids (list[int] | Unset):
        employees_ids (list[int] | Unset): filters by employee identifiers Example: [1, 2, 3].
        legal_entities_ids (list[int] | Unset):
        country (GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry): filters by country
            code pt | it | de Example: it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employees_ids=employees_ids,
        legal_entities_ids=legal_entities_ids,
        country=country,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    legal_entities_ids: list[int] | Unset = UNSET,
    country: GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry,
) -> Response[GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200]:
    """Reads all Identifiers

     Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

    Args:
        ids (list[int] | Unset):
        employees_ids (list[int] | Unset): filters by employee identifiers Example: [1, 2, 3].
        legal_entities_ids (list[int] | Unset):
        country (GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry): filters by country
            code pt | it | de Example: it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employees_ids=employees_ids,
        legal_entities_ids=legal_entities_ids,
        country=country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    legal_entities_ids: list[int] | Unset = UNSET,
    country: GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry,
) -> GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200 | None:
    """Reads all Identifiers

     Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

    Args:
        ids (list[int] | Unset):
        employees_ids (list[int] | Unset): filters by employee identifiers Example: [1, 2, 3].
        legal_entities_ids (list[int] | Unset):
        country (GetApi20260401ResourcesPayrollEmployeesIdentifiersCountry): filters by country
            code pt | it | de Example: it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesPayrollEmployeesIdentifiersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employees_ids=employees_ids,
            legal_entities_ids=legal_entities_ids,
            country=country,
        )
    ).parsed
