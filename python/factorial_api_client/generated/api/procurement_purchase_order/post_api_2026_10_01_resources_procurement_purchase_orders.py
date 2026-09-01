from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20261001_resources_procurement_purchase_orders_body import (
    PostApi20261001ResourcesProcurementPurchaseOrdersBody,
)
from ...models.procurement_purchase_order import ProcurementPurchaseOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-10-01/resources/procurement/purchase_orders",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProcurementPurchaseOrder | None:
    if response.status_code == 201:
        response_201 = ProcurementPurchaseOrder.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProcurementPurchaseOrder]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset = UNSET,
) -> Response[ProcurementPurchaseOrder]:
    """Creates a Purchase order

     Create a standalone purchase order (e.g. pushed by an ERP integrator), not linked to any purchase
    request. The purchase order is pinned to the company's ACTIVE purchase order template version;
    template fields are addressed by their stable field_key and validated against that version: unknown
    field keys, missing required fields and reference values that do not resolve in the company are all
    rejected with a field-keyed 422. A vendor_id or legal_entity_id that does not exist or is not
    visible to the credential is rejected earlier by the platform resource check (400).

    Args:
        body (PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPurchaseOrder]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset = UNSET,
) -> ProcurementPurchaseOrder | None:
    """Creates a Purchase order

     Create a standalone purchase order (e.g. pushed by an ERP integrator), not linked to any purchase
    request. The purchase order is pinned to the company's ACTIVE purchase order template version;
    template fields are addressed by their stable field_key and validated against that version: unknown
    field keys, missing required fields and reference values that do not resolve in the company are all
    rejected with a field-keyed 422. A vendor_id or legal_entity_id that does not exist or is not
    visible to the credential is rejected earlier by the platform resource check (400).

    Args:
        body (PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPurchaseOrder
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset = UNSET,
) -> Response[ProcurementPurchaseOrder]:
    """Creates a Purchase order

     Create a standalone purchase order (e.g. pushed by an ERP integrator), not linked to any purchase
    request. The purchase order is pinned to the company's ACTIVE purchase order template version;
    template fields are addressed by their stable field_key and validated against that version: unknown
    field keys, missing required fields and reference values that do not resolve in the company are all
    rejected with a field-keyed 422. A vendor_id or legal_entity_id that does not exist or is not
    visible to the credential is rejected earlier by the platform resource check (400).

    Args:
        body (PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPurchaseOrder]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset = UNSET,
) -> ProcurementPurchaseOrder | None:
    """Creates a Purchase order

     Create a standalone purchase order (e.g. pushed by an ERP integrator), not linked to any purchase
    request. The purchase order is pinned to the company's ACTIVE purchase order template version;
    template fields are addressed by their stable field_key and validated against that version: unknown
    field keys, missing required fields and reference values that do not resolve in the company are all
    rejected with a field-keyed 422. A vendor_id or legal_entity_id that does not exist or is not
    visible to the credential is rejected earlier by the platform resource check (400).

    Args:
        body (PostApi20261001ResourcesProcurementPurchaseOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPurchaseOrder
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
