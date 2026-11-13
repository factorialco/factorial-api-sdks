from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_contracts_contract_versions_response_200 import (
    GetApi20270101ResourcesContractsContractVersionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    date: str | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
    updated_at_gteq: str | Unset = UNSET,
    updated_at_lteq: str | Unset = UNSET,
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

    params["date"] = date

    json_job_catalog_tree_node_uuids = job_catalog_tree_node_uuids

    params["job_catalog_tree_node_uuids[]"] = json_job_catalog_tree_node_uuids

    params["updated_at_gteq"] = updated_at_gteq

    params["updated_at_lteq"] = updated_at_lteq

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/contracts/contract_versions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesContractsContractVersionsResponse200.from_dict(
            response.json()
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
) -> Response[ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200]:
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
    date: str | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
    updated_at_gteq: str | Unset = UNSET,
    updated_at_lteq: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200]:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[str] | Unset): Return only the contract versions with these ids. Example: ['1',
            '2'].
        employee_ids (list[str] | Unset): Return only the contract versions of these employees.
            Example: ['1', '2'].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree. As
            only level nodes are accepted and persisted, so filtering with other node types will
            return no results. Refer to job_catalog/tree_nodes endpoint. Example:
            ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].
        updated_at_gteq (str | Unset): Filter contract versions updated on or after this timestamp
            (ISO 8601).
             Example: 2024-01-01T00:00:00.000Z.
        updated_at_lteq (str | Unset): Filter contract versions updated on or before this
            timestamp (ISO 8601).
             Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        date=date,
        job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
        updated_at_gteq=updated_at_gteq,
        updated_at_lteq=updated_at_lteq,
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
    date: str | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
    updated_at_gteq: str | Unset = UNSET,
    updated_at_lteq: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200 | None:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[str] | Unset): Return only the contract versions with these ids. Example: ['1',
            '2'].
        employee_ids (list[str] | Unset): Return only the contract versions of these employees.
            Example: ['1', '2'].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree. As
            only level nodes are accepted and persisted, so filtering with other node types will
            return no results. Refer to job_catalog/tree_nodes endpoint. Example:
            ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].
        updated_at_gteq (str | Unset): Filter contract versions updated on or after this timestamp
            (ISO 8601).
             Example: 2024-01-01T00:00:00.000Z.
        updated_at_lteq (str | Unset): Filter contract versions updated on or before this
            timestamp (ISO 8601).
             Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        date=date,
        job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
        updated_at_gteq=updated_at_gteq,
        updated_at_lteq=updated_at_lteq,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    date: str | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
    updated_at_gteq: str | Unset = UNSET,
    updated_at_lteq: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200]:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[str] | Unset): Return only the contract versions with these ids. Example: ['1',
            '2'].
        employee_ids (list[str] | Unset): Return only the contract versions of these employees.
            Example: ['1', '2'].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree. As
            only level nodes are accepted and persisted, so filtering with other node types will
            return no results. Refer to job_catalog/tree_nodes endpoint. Example:
            ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].
        updated_at_gteq (str | Unset): Filter contract versions updated on or after this timestamp
            (ISO 8601).
             Example: 2024-01-01T00:00:00.000Z.
        updated_at_lteq (str | Unset): Filter contract versions updated on or before this
            timestamp (ISO 8601).
             Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        date=date,
        job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
        updated_at_gteq=updated_at_gteq,
        updated_at_lteq=updated_at_lteq,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    date: str | Unset = UNSET,
    job_catalog_tree_node_uuids: list[str],
    updated_at_gteq: str | Unset = UNSET,
    updated_at_lteq: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200 | None:
    """Reads all Contract versions

     Reads all Contract versions

    Args:
        ids (list[str] | Unset): Return only the contract versions with these ids. Example: ['1',
            '2'].
        employee_ids (list[str] | Unset): Return only the contract versions of these employees.
            Example: ['1', '2'].
        date (str | Unset): filters contracts of employees with effective_on date less or equal
            than the given date. Example: 2024-10-06.
        job_catalog_tree_node_uuids (list[str]): the uuid of nodes in the job catalog tree. As
            only level nodes are accepted and persisted, so filtering with other node types will
            return no results. Refer to job_catalog/tree_nodes endpoint. Example:
            ['jobcatalog_treelevel-14', 'jobcatalog_treelevel-15'].
        updated_at_gteq (str | Unset): Filter contract versions updated on or after this timestamp
            (ISO 8601).
             Example: 2024-01-01T00:00:00.000Z.
        updated_at_lteq (str | Unset): Filter contract versions updated on or before this
            timestamp (ISO 8601).
             Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesContractsContractVersionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            date=date,
            job_catalog_tree_node_uuids=job_catalog_tree_node_uuids,
            updated_at_gteq=updated_at_gteq,
            updated_at_lteq=updated_at_lteq,
        )
    ).parsed
