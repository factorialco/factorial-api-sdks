from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.procurement_purchase_order import ProcurementPurchaseOrder
from ...models.put_api_20261001_resources_procurement_purchase_orders_id_body import (
    PutApi20261001ResourcesProcurementPurchaseOrdersIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-10-01/resources/procurement/purchase_orders/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProcurementPurchaseOrder | None:
    if response.status_code == 200:
        response_200 = ProcurementPurchaseOrder.from_dict(response.json())

        return response_200

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> Response[ProcurementPurchaseOrder]:
    r"""Updates a Purchase order

     Update a purchase order with PUT semantics: read the purchase order, modify it, and send the
    complete resource back. Template fields are addressed by their stable field_key and validated
    against the template version the purchase order was created with. Line items are addressed by id.
    Omission semantics: `status`, `date` and `deadline` omitted or null keep their current value;
    `header_field_values_by_key` and `line_items_by_key` omitted keep the current values, while an empty
    array `[]` deletes them all (full replace). Within a sent block, what you send is what remains.
    Errors: validation problems are a 422 with `{\"errors\": {<field_key>: [messages]}}`
    (unknown/computed/predefined keys, missing required fields, unresolvable reference values, foreign
    line-item ids, mixing by_key and legacy addressing). A vendor_id or legal_entity_id that does not
    exist or is not visible to the credential is rejected by the platform resource check with a 400
    (`{\"errors\": [{\"error\": ...}]}`). Lifecycle conflicts are a 409: purchase orders in `closed` or
    `processing` (still being generated — retry later) status cannot be updated. `processing` is not
    accepted as a new status (422). Purchase orders without a template only accept data edits while in
    `draft` status (409 afterwards).

    Args:
        id (str):
        body (PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPurchaseOrder]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> ProcurementPurchaseOrder | None:
    r"""Updates a Purchase order

     Update a purchase order with PUT semantics: read the purchase order, modify it, and send the
    complete resource back. Template fields are addressed by their stable field_key and validated
    against the template version the purchase order was created with. Line items are addressed by id.
    Omission semantics: `status`, `date` and `deadline` omitted or null keep their current value;
    `header_field_values_by_key` and `line_items_by_key` omitted keep the current values, while an empty
    array `[]` deletes them all (full replace). Within a sent block, what you send is what remains.
    Errors: validation problems are a 422 with `{\"errors\": {<field_key>: [messages]}}`
    (unknown/computed/predefined keys, missing required fields, unresolvable reference values, foreign
    line-item ids, mixing by_key and legacy addressing). A vendor_id or legal_entity_id that does not
    exist or is not visible to the credential is rejected by the platform resource check with a 400
    (`{\"errors\": [{\"error\": ...}]}`). Lifecycle conflicts are a 409: purchase orders in `closed` or
    `processing` (still being generated — retry later) status cannot be updated. `processing` is not
    accepted as a new status (422). Purchase orders without a template only accept data edits while in
    `draft` status (409 afterwards).

    Args:
        id (str):
        body (PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPurchaseOrder
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> Response[ProcurementPurchaseOrder]:
    r"""Updates a Purchase order

     Update a purchase order with PUT semantics: read the purchase order, modify it, and send the
    complete resource back. Template fields are addressed by their stable field_key and validated
    against the template version the purchase order was created with. Line items are addressed by id.
    Omission semantics: `status`, `date` and `deadline` omitted or null keep their current value;
    `header_field_values_by_key` and `line_items_by_key` omitted keep the current values, while an empty
    array `[]` deletes them all (full replace). Within a sent block, what you send is what remains.
    Errors: validation problems are a 422 with `{\"errors\": {<field_key>: [messages]}}`
    (unknown/computed/predefined keys, missing required fields, unresolvable reference values, foreign
    line-item ids, mixing by_key and legacy addressing). A vendor_id or legal_entity_id that does not
    exist or is not visible to the credential is rejected by the platform resource check with a 400
    (`{\"errors\": [{\"error\": ...}]}`). Lifecycle conflicts are a 409: purchase orders in `closed` or
    `processing` (still being generated — retry later) status cannot be updated. `processing` is not
    accepted as a new status (422). Purchase orders without a template only accept data edits while in
    `draft` status (409 afterwards).

    Args:
        id (str):
        body (PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPurchaseOrder]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> ProcurementPurchaseOrder | None:
    r"""Updates a Purchase order

     Update a purchase order with PUT semantics: read the purchase order, modify it, and send the
    complete resource back. Template fields are addressed by their stable field_key and validated
    against the template version the purchase order was created with. Line items are addressed by id.
    Omission semantics: `status`, `date` and `deadline` omitted or null keep their current value;
    `header_field_values_by_key` and `line_items_by_key` omitted keep the current values, while an empty
    array `[]` deletes them all (full replace). Within a sent block, what you send is what remains.
    Errors: validation problems are a 422 with `{\"errors\": {<field_key>: [messages]}}`
    (unknown/computed/predefined keys, missing required fields, unresolvable reference values, foreign
    line-item ids, mixing by_key and legacy addressing). A vendor_id or legal_entity_id that does not
    exist or is not visible to the credential is rejected by the platform resource check with a 400
    (`{\"errors\": [{\"error\": ...}]}`). Lifecycle conflicts are a 409: purchase orders in `closed` or
    `processing` (still being generated — retry later) status cannot be updated. `processing` is not
    accepted as a new status (422). Purchase orders without a template only accept data edits while in
    `draft` status (409 afterwards).

    Args:
        id (str):
        body (PutApi20261001ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPurchaseOrder
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
