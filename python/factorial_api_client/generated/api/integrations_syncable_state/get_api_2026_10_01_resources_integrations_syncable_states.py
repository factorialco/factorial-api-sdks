from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_integrations_syncable_states_response_200 import (
    GetApi20261001ResourcesIntegrationsSyncableStatesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    syncable_ids: list[str] | Unset = UNSET,
    resource_syncable_type: str | Unset = UNSET,
    integration_uuid: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_syncable_ids: list[str] | Unset = UNSET
    if not isinstance(syncable_ids, Unset):
        json_syncable_ids = syncable_ids

    params["syncable_ids[]"] = json_syncable_ids

    params["resource_syncable_type"] = resource_syncable_type

    params["integration_uuid"] = integration_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/integrations/syncable_states",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesIntegrationsSyncableStatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesIntegrationsSyncableStatesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesIntegrationsSyncableStatesResponse200]:
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
    syncable_ids: list[str] | Unset = UNSET,
    resource_syncable_type: str | Unset = UNSET,
    integration_uuid: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesIntegrationsSyncableStatesResponse200]:
    """Reads all Syncable states

     Reads all Syncable states

    Args:
        ids (list[str] | Unset): Filter syncable states by their identifiers Example: ['1'].
        syncable_ids (list[str] | Unset): Filter syncable states by the identifiers of the linked
            API resource, identified by resource_syncable_type field Example: ['1'].
        resource_syncable_type (str | Unset): The resource type of the linked records, in
            "namespace/resource" form. Required when filtering by syncable_ids. Example:
            compensations/payroll_run_employees_compensation.
        integration_uuid (str | Unset): Filter syncable states by the UUID of the marketplace
            integration Example: 123e4567-e89b-12d3-a456-426614174000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesIntegrationsSyncableStatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        syncable_ids=syncable_ids,
        resource_syncable_type=resource_syncable_type,
        integration_uuid=integration_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    syncable_ids: list[str] | Unset = UNSET,
    resource_syncable_type: str | Unset = UNSET,
    integration_uuid: str | Unset = UNSET,
) -> GetApi20261001ResourcesIntegrationsSyncableStatesResponse200 | None:
    """Reads all Syncable states

     Reads all Syncable states

    Args:
        ids (list[str] | Unset): Filter syncable states by their identifiers Example: ['1'].
        syncable_ids (list[str] | Unset): Filter syncable states by the identifiers of the linked
            API resource, identified by resource_syncable_type field Example: ['1'].
        resource_syncable_type (str | Unset): The resource type of the linked records, in
            "namespace/resource" form. Required when filtering by syncable_ids. Example:
            compensations/payroll_run_employees_compensation.
        integration_uuid (str | Unset): Filter syncable states by the UUID of the marketplace
            integration Example: 123e4567-e89b-12d3-a456-426614174000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesIntegrationsSyncableStatesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        syncable_ids=syncable_ids,
        resource_syncable_type=resource_syncable_type,
        integration_uuid=integration_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    syncable_ids: list[str] | Unset = UNSET,
    resource_syncable_type: str | Unset = UNSET,
    integration_uuid: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesIntegrationsSyncableStatesResponse200]:
    """Reads all Syncable states

     Reads all Syncable states

    Args:
        ids (list[str] | Unset): Filter syncable states by their identifiers Example: ['1'].
        syncable_ids (list[str] | Unset): Filter syncable states by the identifiers of the linked
            API resource, identified by resource_syncable_type field Example: ['1'].
        resource_syncable_type (str | Unset): The resource type of the linked records, in
            "namespace/resource" form. Required when filtering by syncable_ids. Example:
            compensations/payroll_run_employees_compensation.
        integration_uuid (str | Unset): Filter syncable states by the UUID of the marketplace
            integration Example: 123e4567-e89b-12d3-a456-426614174000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesIntegrationsSyncableStatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        syncable_ids=syncable_ids,
        resource_syncable_type=resource_syncable_type,
        integration_uuid=integration_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    syncable_ids: list[str] | Unset = UNSET,
    resource_syncable_type: str | Unset = UNSET,
    integration_uuid: str | Unset = UNSET,
) -> GetApi20261001ResourcesIntegrationsSyncableStatesResponse200 | None:
    """Reads all Syncable states

     Reads all Syncable states

    Args:
        ids (list[str] | Unset): Filter syncable states by their identifiers Example: ['1'].
        syncable_ids (list[str] | Unset): Filter syncable states by the identifiers of the linked
            API resource, identified by resource_syncable_type field Example: ['1'].
        resource_syncable_type (str | Unset): The resource type of the linked records, in
            "namespace/resource" form. Required when filtering by syncable_ids. Example:
            compensations/payroll_run_employees_compensation.
        integration_uuid (str | Unset): Filter syncable states by the UUID of the marketplace
            integration Example: 123e4567-e89b-12d3-a456-426614174000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesIntegrationsSyncableStatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            syncable_ids=syncable_ids,
            resource_syncable_type=resource_syncable_type,
            integration_uuid=integration_uuid,
        )
    ).parsed
