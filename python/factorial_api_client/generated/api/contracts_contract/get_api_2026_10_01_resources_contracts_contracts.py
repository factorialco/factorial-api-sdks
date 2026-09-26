from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_contracts_contracts_response_200 import (
    GetApi20261001ResourcesContractsContractsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
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

    params["starts_on"] = starts_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/contracts/contracts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesContractsContractsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesContractsContractsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesContractsContractsResponse200]:
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
    starts_on: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesContractsContractsResponse200]:
    """Reads all Contracts

     Reads all Contracts

    Args:
        ids (list[str] | Unset): Return only the contracts with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the contracts of these employees. Example:
            ['1'].
        starts_on (str | Unset): Return only the contracts starting exactly on this date. This is
            an equality match on the contract's start date, not a lower bound. Example: 2024-07-17.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesContractsContractsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        starts_on=starts_on,
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
    starts_on: str | Unset = UNSET,
) -> GetApi20261001ResourcesContractsContractsResponse200 | None:
    """Reads all Contracts

     Reads all Contracts

    Args:
        ids (list[str] | Unset): Return only the contracts with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the contracts of these employees. Example:
            ['1'].
        starts_on (str | Unset): Return only the contracts starting exactly on this date. This is
            an equality match on the contract's start date, not a lower bound. Example: 2024-07-17.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesContractsContractsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        starts_on=starts_on,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesContractsContractsResponse200]:
    """Reads all Contracts

     Reads all Contracts

    Args:
        ids (list[str] | Unset): Return only the contracts with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the contracts of these employees. Example:
            ['1'].
        starts_on (str | Unset): Return only the contracts starting exactly on this date. This is
            an equality match on the contract's start date, not a lower bound. Example: 2024-07-17.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesContractsContractsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        starts_on=starts_on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
) -> GetApi20261001ResourcesContractsContractsResponse200 | None:
    """Reads all Contracts

     Reads all Contracts

    Args:
        ids (list[str] | Unset): Return only the contracts with these ids. Example: ['1'].
        employee_ids (list[str] | Unset): Return only the contracts of these employees. Example:
            ['1'].
        starts_on (str | Unset): Return only the contracts starting exactly on this date. This is
            an equality match on the contract's start date, not a lower bound. Example: 2024-07-17.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesContractsContractsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            starts_on=starts_on,
        )
    ).parsed
