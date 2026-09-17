from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_contracts_reference_contracts_response_200 import (
    GetApi20261001ResourcesContractsReferenceContractsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employee_ids: list[str] | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_job_catalog_tree_node_uuids = job_catalog_tree_node_uuids

    params["job_catalog_tree_node_uuids[]"] = json_job_catalog_tree_node_uuids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/contracts/reference_contracts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesContractsReferenceContractsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesContractsReferenceContractsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesContractsReferenceContractsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
) -> Response[GetApi20261001ResourcesContractsReferenceContractsResponse200]:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree.
            Example: ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesContractsReferenceContractsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
) -> GetApi20261001ResourcesContractsReferenceContractsResponse200 | None:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree.
            Example: ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesContractsReferenceContractsResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
        job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
) -> Response[GetApi20261001ResourcesContractsReferenceContractsResponse200]:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree.
            Example: ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesContractsReferenceContractsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
) -> GetApi20261001ResourcesContractsReferenceContractsResponse200 | None:
    """Reads all Reference contracts

     Reads all Reference Contracts. The reference contract is the contract that applies today. If no
    contract applies today, we will return the nearest upcoming contract. If there are no upcoming
    contracts, we will provide the most recent past contract.

    Args:
        employee_ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree.
            Example: ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesContractsReferenceContractsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
            job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
        )
    ).parsed
