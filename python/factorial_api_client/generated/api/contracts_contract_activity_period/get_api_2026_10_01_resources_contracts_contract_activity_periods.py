from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_contracts_contract_activity_periods_response_200 import (
    GetApi20261001ResourcesContractsContractActivityPeriodsResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    contract_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["contract_id"] = contract_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/contracts/contract_activity_periods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesContractsContractActivityPeriodsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesContractsContractActivityPeriodsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesContractsContractActivityPeriodsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    contract_id: str,
) -> Response[GetApi20261001ResourcesContractsContractActivityPeriodsResponse200]:
    """List the activity periods of a contract.

     Returns the activity and inactivity periods of a single contract, most recent first. Periods are
    derived from the contract's approved versions, so they reflect the contract as it stands today. A
    contract that does not exist, or that the caller is not allowed to see, returns an empty list.

    Args:
        contract_id (str): The contract whose periods are returned. Required — periods are
            computed per contract rather than stored, so they cannot be listed across a company.
            Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesContractsContractActivityPeriodsResponse200]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    contract_id: str,
) -> GetApi20261001ResourcesContractsContractActivityPeriodsResponse200 | None:
    """List the activity periods of a contract.

     Returns the activity and inactivity periods of a single contract, most recent first. Periods are
    derived from the contract's approved versions, so they reflect the contract as it stands today. A
    contract that does not exist, or that the caller is not allowed to see, returns an empty list.

    Args:
        contract_id (str): The contract whose periods are returned. Required — periods are
            computed per contract rather than stored, so they cannot be listed across a company.
            Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesContractsContractActivityPeriodsResponse200
    """

    return sync_detailed(
        client=client,
        contract_id=contract_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    contract_id: str,
) -> Response[GetApi20261001ResourcesContractsContractActivityPeriodsResponse200]:
    """List the activity periods of a contract.

     Returns the activity and inactivity periods of a single contract, most recent first. Periods are
    derived from the contract's approved versions, so they reflect the contract as it stands today. A
    contract that does not exist, or that the caller is not allowed to see, returns an empty list.

    Args:
        contract_id (str): The contract whose periods are returned. Required — periods are
            computed per contract rather than stored, so they cannot be listed across a company.
            Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesContractsContractActivityPeriodsResponse200]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    contract_id: str,
) -> GetApi20261001ResourcesContractsContractActivityPeriodsResponse200 | None:
    """List the activity periods of a contract.

     Returns the activity and inactivity periods of a single contract, most recent first. Periods are
    derived from the contract's approved versions, so they reflect the contract as it stands today. A
    contract that does not exist, or that the caller is not allowed to see, returns an empty list.

    Args:
        contract_id (str): The contract whose periods are returned. Required — periods are
            computed per contract rather than stored, so they cannot be listed across a company.
            Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesContractsContractActivityPeriodsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            contract_id=contract_id,
        )
    ).parsed
