from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_job_catalog_node_attributes_attribute_types import (
    GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes,
)
from ...models.get_api_20260701_resources_job_catalog_node_attributes_response_200 import (
    GetApi20260701ResourcesJobCatalogNodeAttributesResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    node_uuid: str,
    attribute_types: GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["node_uuid"] = node_uuid

    json_attribute_types = attribute_types.value
    params["attribute_types[]"] = json_attribute_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/job_catalog/node_attributes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesJobCatalogNodeAttributesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesJobCatalogNodeAttributesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesJobCatalogNodeAttributesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    node_uuid: str,
    attribute_types: GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes,
) -> Response[GetApi20260701ResourcesJobCatalogNodeAttributesResponse200]:
    """Reads all Node attributes

     Fetch Attributes for a node (Family, Function, role or level) in the Job Catalog Tree

    Args:
        node_uuid (str): Preferred identifier of the node to fetch attributes for. Required unless
            `node_id` + `node_type` are provided. Example: jobcatalog_treelevel-331.
        attribute_types (GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes): Restrict
            the response to attributes of these classes (e.g., competency, salary_range). Example:
            ['competency', 'salary_range'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesJobCatalogNodeAttributesResponse200]
    """

    kwargs = _get_kwargs(
        node_uuid=node_uuid,
        attribute_types=attribute_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    node_uuid: str,
    attribute_types: GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes,
) -> GetApi20260701ResourcesJobCatalogNodeAttributesResponse200 | None:
    """Reads all Node attributes

     Fetch Attributes for a node (Family, Function, role or level) in the Job Catalog Tree

    Args:
        node_uuid (str): Preferred identifier of the node to fetch attributes for. Required unless
            `node_id` + `node_type` are provided. Example: jobcatalog_treelevel-331.
        attribute_types (GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes): Restrict
            the response to attributes of these classes (e.g., competency, salary_range). Example:
            ['competency', 'salary_range'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesJobCatalogNodeAttributesResponse200
    """

    return sync_detailed(
        client=client,
        node_uuid=node_uuid,
        attribute_types=attribute_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    node_uuid: str,
    attribute_types: GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes,
) -> Response[GetApi20260701ResourcesJobCatalogNodeAttributesResponse200]:
    """Reads all Node attributes

     Fetch Attributes for a node (Family, Function, role or level) in the Job Catalog Tree

    Args:
        node_uuid (str): Preferred identifier of the node to fetch attributes for. Required unless
            `node_id` + `node_type` are provided. Example: jobcatalog_treelevel-331.
        attribute_types (GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes): Restrict
            the response to attributes of these classes (e.g., competency, salary_range). Example:
            ['competency', 'salary_range'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesJobCatalogNodeAttributesResponse200]
    """

    kwargs = _get_kwargs(
        node_uuid=node_uuid,
        attribute_types=attribute_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    node_uuid: str,
    attribute_types: GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes,
) -> GetApi20260701ResourcesJobCatalogNodeAttributesResponse200 | None:
    """Reads all Node attributes

     Fetch Attributes for a node (Family, Function, role or level) in the Job Catalog Tree

    Args:
        node_uuid (str): Preferred identifier of the node to fetch attributes for. Required unless
            `node_id` + `node_type` are provided. Example: jobcatalog_treelevel-331.
        attribute_types (GetApi20260701ResourcesJobCatalogNodeAttributesAttributeTypes): Restrict
            the response to attributes of these classes (e.g., competency, salary_range). Example:
            ['competency', 'salary_range'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesJobCatalogNodeAttributesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            node_uuid=node_uuid,
            attribute_types=attribute_types,
        )
    ).parsed
