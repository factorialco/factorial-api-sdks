from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_contracts_reference_contracts_response_200 import (
    GetApi20251001ResourcesContractsReferenceContractsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employee_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/contracts/reference_contracts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesContractsReferenceContractsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesContractsReferenceContractsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesContractsReferenceContractsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesContractsReferenceContractsResponse200]:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesContractsReferenceContractsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesContractsReferenceContractsResponse200 | None:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesContractsReferenceContractsResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesContractsReferenceContractsResponse200]:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesContractsReferenceContractsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesContractsReferenceContractsResponse200 | None:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[int] | Unset): filter by employee ids. Example: [1, 2, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesContractsReferenceContractsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
        )
    ).parsed
