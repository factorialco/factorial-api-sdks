from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_contracts_compensations_response_200 import (
    GetApi20260701ResourcesContractsCompensationsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    contract_version_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_contract_version_ids: list[str] | Unset = UNSET
    if not isinstance(contract_version_ids, Unset):
        json_contract_version_ids = contract_version_ids

    params["contract_version_ids[]"] = json_contract_version_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/contracts/compensations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesContractsCompensationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesContractsCompensationsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesContractsCompensationsResponse200]:
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
    contract_version_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesContractsCompensationsResponse200]:
    """Reads all Compensations

     Reads all Compensations

    Args:
        ids (list[str] | Unset):
        contract_version_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesContractsCompensationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        contract_version_ids=contract_version_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    contract_version_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesContractsCompensationsResponse200 | None:
    """Reads all Compensations

     Reads all Compensations

    Args:
        ids (list[str] | Unset):
        contract_version_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesContractsCompensationsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        contract_version_ids=contract_version_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    contract_version_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesContractsCompensationsResponse200]:
    """Reads all Compensations

     Reads all Compensations

    Args:
        ids (list[str] | Unset):
        contract_version_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesContractsCompensationsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        contract_version_ids=contract_version_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    contract_version_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesContractsCompensationsResponse200 | None:
    """Reads all Compensations

     Reads all Compensations

    Args:
        ids (list[str] | Unset):
        contract_version_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesContractsCompensationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            contract_version_ids=contract_version_ids,
        )
    ).parsed
