from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.procurement_purchase_order import ProcurementPurchaseOrder
from ...models.put_api_20270101_resources_procurement_purchase_orders_id_body import (
    PutApi20270101ResourcesProcurementPurchaseOrdersIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2027-01-01/resources/procurement/purchase_orders/{id}".format(
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
) -> ErrorResponse | ProcurementPurchaseOrder | None:
    if response.status_code == 200:
        response_200 = ProcurementPurchaseOrder.from_dict(response.json())

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
) -> Response[ErrorResponse | ProcurementPurchaseOrder]:
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
    body: PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> Response[ErrorResponse | ProcurementPurchaseOrder]:
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
        body (PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProcurementPurchaseOrder]
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
    body: PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> ErrorResponse | ProcurementPurchaseOrder | None:
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
        body (PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProcurementPurchaseOrder
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
    body: PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> Response[ErrorResponse | ProcurementPurchaseOrder]:
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
        body (PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProcurementPurchaseOrder]
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
    body: PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset = UNSET,
) -> ErrorResponse | ProcurementPurchaseOrder | None:
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
        body (PutApi20270101ResourcesProcurementPurchaseOrdersIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProcurementPurchaseOrder
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
