from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_job_catalog_tree_nodes_node_type import (
    GetApi20260701ResourcesJobCatalogTreeNodesNodeType,
)
from ...models.get_api_20260701_resources_job_catalog_tree_nodes_response_200 import (
    GetApi20260701ResourcesJobCatalogTreeNodesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    uuids: list[str] | Unset = UNSET,
    node_type: GetApi20260701ResourcesJobCatalogTreeNodesNodeType,
    ancestor_uuids: list[str] | Unset = UNSET,
    include_full_path: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_uuids: list[str] | Unset = UNSET
    if not isinstance(uuids, Unset):
        json_uuids = uuids

    params["uuids[]"] = json_uuids

    json_node_type = node_type.value
    params["node_type"] = json_node_type

    json_ancestor_uuids: list[str] | Unset = UNSET
    if not isinstance(ancestor_uuids, Unset):
        json_ancestor_uuids = ancestor_uuids

    params["ancestor_uuids[]"] = json_ancestor_uuids

    params["include_full_path"] = include_full_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/job_catalog/tree_nodes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesJobCatalogTreeNodesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesJobCatalogTreeNodesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesJobCatalogTreeNodesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    uuids: list[str] | Unset = UNSET,
    node_type: GetApi20260701ResourcesJobCatalogTreeNodesNodeType,
    ancestor_uuids: list[str] | Unset = UNSET,
    include_full_path: bool | Unset = UNSET,
) -> Response[GetApi20260701ResourcesJobCatalogTreeNodesResponse200]:
    """Reads all Tree nodes

     Fetch Job Catalog Tree Node. For now only admins can see all the nodes' information, regular users
    won't have access to the nodes' information. In general there are four node types level, function,
    role and family.

    Args:
        uuids (list[str] | Unset): List of Job Catalog node UUIDs to fetch. Must reference nodes
            of a single type. Example: ['jobcatalog_treelevel-331', 'jobcatalog_treelevel-412'].
        node_type (GetApi20260701ResourcesJobCatalogTreeNodesNodeType): Node type scope for the
            query. Required with IDs, ancestor filters, or name search. Accepted values:
            jobcatalog_treelevel, jobcatalog_treefunction, jobcatalog_treerole, jobcatalog_treefamily.
            Example: jobcatalog_treelevel.
        ancestor_uuids (list[str] | Unset): Return nodes that descend from any of these ancestor
            UUIDs (single node type only). Example: ['jobcatalog_treefamily-018',
            'jobcatalog_treefamily-225'].
        include_full_path (bool | Unset): When true, includes each node's ordered ancestor path up
            to the root. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesJobCatalogTreeNodesResponse200]
    """

    kwargs = _get_kwargs(
        uuids=uuids,
        node_type=node_type,
        ancestor_uuids=ancestor_uuids,
        include_full_path=include_full_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uuids: list[str] | Unset = UNSET,
    node_type: GetApi20260701ResourcesJobCatalogTreeNodesNodeType,
    ancestor_uuids: list[str] | Unset = UNSET,
    include_full_path: bool | Unset = UNSET,
) -> GetApi20260701ResourcesJobCatalogTreeNodesResponse200 | None:
    """Reads all Tree nodes

     Fetch Job Catalog Tree Node. For now only admins can see all the nodes' information, regular users
    won't have access to the nodes' information. In general there are four node types level, function,
    role and family.

    Args:
        uuids (list[str] | Unset): List of Job Catalog node UUIDs to fetch. Must reference nodes
            of a single type. Example: ['jobcatalog_treelevel-331', 'jobcatalog_treelevel-412'].
        node_type (GetApi20260701ResourcesJobCatalogTreeNodesNodeType): Node type scope for the
            query. Required with IDs, ancestor filters, or name search. Accepted values:
            jobcatalog_treelevel, jobcatalog_treefunction, jobcatalog_treerole, jobcatalog_treefamily.
            Example: jobcatalog_treelevel.
        ancestor_uuids (list[str] | Unset): Return nodes that descend from any of these ancestor
            UUIDs (single node type only). Example: ['jobcatalog_treefamily-018',
            'jobcatalog_treefamily-225'].
        include_full_path (bool | Unset): When true, includes each node's ordered ancestor path up
            to the root. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesJobCatalogTreeNodesResponse200
    """

    return sync_detailed(
        client=client,
        uuids=uuids,
        node_type=node_type,
        ancestor_uuids=ancestor_uuids,
        include_full_path=include_full_path,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uuids: list[str] | Unset = UNSET,
    node_type: GetApi20260701ResourcesJobCatalogTreeNodesNodeType,
    ancestor_uuids: list[str] | Unset = UNSET,
    include_full_path: bool | Unset = UNSET,
) -> Response[GetApi20260701ResourcesJobCatalogTreeNodesResponse200]:
    """Reads all Tree nodes

     Fetch Job Catalog Tree Node. For now only admins can see all the nodes' information, regular users
    won't have access to the nodes' information. In general there are four node types level, function,
    role and family.

    Args:
        uuids (list[str] | Unset): List of Job Catalog node UUIDs to fetch. Must reference nodes
            of a single type. Example: ['jobcatalog_treelevel-331', 'jobcatalog_treelevel-412'].
        node_type (GetApi20260701ResourcesJobCatalogTreeNodesNodeType): Node type scope for the
            query. Required with IDs, ancestor filters, or name search. Accepted values:
            jobcatalog_treelevel, jobcatalog_treefunction, jobcatalog_treerole, jobcatalog_treefamily.
            Example: jobcatalog_treelevel.
        ancestor_uuids (list[str] | Unset): Return nodes that descend from any of these ancestor
            UUIDs (single node type only). Example: ['jobcatalog_treefamily-018',
            'jobcatalog_treefamily-225'].
        include_full_path (bool | Unset): When true, includes each node's ordered ancestor path up
            to the root. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesJobCatalogTreeNodesResponse200]
    """

    kwargs = _get_kwargs(
        uuids=uuids,
        node_type=node_type,
        ancestor_uuids=ancestor_uuids,
        include_full_path=include_full_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uuids: list[str] | Unset = UNSET,
    node_type: GetApi20260701ResourcesJobCatalogTreeNodesNodeType,
    ancestor_uuids: list[str] | Unset = UNSET,
    include_full_path: bool | Unset = UNSET,
) -> GetApi20260701ResourcesJobCatalogTreeNodesResponse200 | None:
    """Reads all Tree nodes

     Fetch Job Catalog Tree Node. For now only admins can see all the nodes' information, regular users
    won't have access to the nodes' information. In general there are four node types level, function,
    role and family.

    Args:
        uuids (list[str] | Unset): List of Job Catalog node UUIDs to fetch. Must reference nodes
            of a single type. Example: ['jobcatalog_treelevel-331', 'jobcatalog_treelevel-412'].
        node_type (GetApi20260701ResourcesJobCatalogTreeNodesNodeType): Node type scope for the
            query. Required with IDs, ancestor filters, or name search. Accepted values:
            jobcatalog_treelevel, jobcatalog_treefunction, jobcatalog_treerole, jobcatalog_treefamily.
            Example: jobcatalog_treelevel.
        ancestor_uuids (list[str] | Unset): Return nodes that descend from any of these ancestor
            UUIDs (single node type only). Example: ['jobcatalog_treefamily-018',
            'jobcatalog_treefamily-225'].
        include_full_path (bool | Unset): When true, includes each node's ordered ancestor path up
            to the root. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesJobCatalogTreeNodesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            uuids=uuids,
            node_type=node_type,
            ancestor_uuids=ancestor_uuids,
            include_full_path=include_full_path,
        )
    ).parsed
