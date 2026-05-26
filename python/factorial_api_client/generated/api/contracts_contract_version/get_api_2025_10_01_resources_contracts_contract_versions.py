from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_contracts_contract_versions_response_200 import (
    GetApi20251001ResourcesContractsContractVersionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/contracts/contract_versions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesContractsContractVersionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesContractsContractVersionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesContractsContractVersionsResponse200]:
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
    employee_ids: list[int] | Unset = UNSET,
    date: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesContractsContractVersionsResponse200]:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[int] | Unset): list of contract version identifiers. Example: [1, 2].
        employee_ids (list[int] | Unset): list of employee identifiers, refers to
            /employees/employees endpoint. Example: [1, 2].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesContractsContractVersionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    date: str | Unset = UNSET,
) -> GetApi20251001ResourcesContractsContractVersionsResponse200 | None:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[int] | Unset): list of contract version identifiers. Example: [1, 2].
        employee_ids (list[int] | Unset): list of employee identifiers, refers to
            /employees/employees endpoint. Example: [1, 2].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesContractsContractVersionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    date: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesContractsContractVersionsResponse200]:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[int] | Unset): list of contract version identifiers. Example: [1, 2].
        employee_ids (list[int] | Unset): list of employee identifiers, refers to
            /employees/employees endpoint. Example: [1, 2].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesContractsContractVersionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    date: str | Unset = UNSET,
) -> GetApi20251001ResourcesContractsContractVersionsResponse200 | None:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[int] | Unset): list of contract version identifiers. Example: [1, 2].
        employee_ids (list[int] | Unset): list of employee identifiers, refers to
            /employees/employees endpoint. Example: [1, 2].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesContractsContractVersionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            date=date,
        )
    ).parsed
