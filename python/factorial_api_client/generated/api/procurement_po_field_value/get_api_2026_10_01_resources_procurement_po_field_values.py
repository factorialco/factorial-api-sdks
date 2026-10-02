from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_procurement_po_field_values_response_200 import (
    GetApi20261001ResourcesProcurementPoFieldValuesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    purchase_order_ids: list[str] | Unset = UNSET,
    line_item_ids: list[str] | Unset = UNSET,
    exclude_line_items: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_purchase_order_ids: list[str] | Unset = UNSET
    if not isinstance(purchase_order_ids, Unset):
        json_purchase_order_ids = purchase_order_ids

    params["purchase_order_ids[]"] = json_purchase_order_ids

    json_line_item_ids: list[str] | Unset = UNSET
    if not isinstance(line_item_ids, Unset):
        json_line_item_ids = line_item_ids

    params["line_item_ids[]"] = json_line_item_ids

    params["exclude_line_items"] = exclude_line_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/procurement/po_field_values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesProcurementPoFieldValuesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesProcurementPoFieldValuesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesProcurementPoFieldValuesResponse200]:
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
    purchase_order_ids: list[str] | Unset = UNSET,
    line_item_ids: list[str] | Unset = UNSET,
    exclude_line_items: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProcurementPoFieldValuesResponse200]:
    """Reads all Po field values

     Fetch field values for a purchase order.

    Args:
        ids (list[str] | Unset): An array of field value IDs to filter by. Example: ['1'].
        purchase_order_ids (list[str] | Unset): An array of purchase order IDs to filter values
            for. Example: ['1'].
        line_item_ids (list[str] | Unset): Restrict results to values belonging to these line
            items. Header-level values (not associated with any line item) are never returned when
            this is set. Mutually exclusive with `exclude_line_items=true` — combining both returns no
            results. Example: ['1'].
        exclude_line_items (bool | Unset): When true, excludes per-line values and returns only
            values not associated with any line item (i.e. header-level). Mutually exclusive with
            `line_item_ids`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProcurementPoFieldValuesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        purchase_order_ids=purchase_order_ids,
        line_item_ids=line_item_ids,
        exclude_line_items=exclude_line_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    purchase_order_ids: list[str] | Unset = UNSET,
    line_item_ids: list[str] | Unset = UNSET,
    exclude_line_items: bool | Unset = UNSET,
) -> GetApi20261001ResourcesProcurementPoFieldValuesResponse200 | None:
    """Reads all Po field values

     Fetch field values for a purchase order.

    Args:
        ids (list[str] | Unset): An array of field value IDs to filter by. Example: ['1'].
        purchase_order_ids (list[str] | Unset): An array of purchase order IDs to filter values
            for. Example: ['1'].
        line_item_ids (list[str] | Unset): Restrict results to values belonging to these line
            items. Header-level values (not associated with any line item) are never returned when
            this is set. Mutually exclusive with `exclude_line_items=true` — combining both returns no
            results. Example: ['1'].
        exclude_line_items (bool | Unset): When true, excludes per-line values and returns only
            values not associated with any line item (i.e. header-level). Mutually exclusive with
            `line_item_ids`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProcurementPoFieldValuesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        purchase_order_ids=purchase_order_ids,
        line_item_ids=line_item_ids,
        exclude_line_items=exclude_line_items,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    purchase_order_ids: list[str] | Unset = UNSET,
    line_item_ids: list[str] | Unset = UNSET,
    exclude_line_items: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProcurementPoFieldValuesResponse200]:
    """Reads all Po field values

     Fetch field values for a purchase order.

    Args:
        ids (list[str] | Unset): An array of field value IDs to filter by. Example: ['1'].
        purchase_order_ids (list[str] | Unset): An array of purchase order IDs to filter values
            for. Example: ['1'].
        line_item_ids (list[str] | Unset): Restrict results to values belonging to these line
            items. Header-level values (not associated with any line item) are never returned when
            this is set. Mutually exclusive with `exclude_line_items=true` — combining both returns no
            results. Example: ['1'].
        exclude_line_items (bool | Unset): When true, excludes per-line values and returns only
            values not associated with any line item (i.e. header-level). Mutually exclusive with
            `line_item_ids`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProcurementPoFieldValuesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        purchase_order_ids=purchase_order_ids,
        line_item_ids=line_item_ids,
        exclude_line_items=exclude_line_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    purchase_order_ids: list[str] | Unset = UNSET,
    line_item_ids: list[str] | Unset = UNSET,
    exclude_line_items: bool | Unset = UNSET,
) -> GetApi20261001ResourcesProcurementPoFieldValuesResponse200 | None:
    """Reads all Po field values

     Fetch field values for a purchase order.

    Args:
        ids (list[str] | Unset): An array of field value IDs to filter by. Example: ['1'].
        purchase_order_ids (list[str] | Unset): An array of purchase order IDs to filter values
            for. Example: ['1'].
        line_item_ids (list[str] | Unset): Restrict results to values belonging to these line
            items. Header-level values (not associated with any line item) are never returned when
            this is set. Mutually exclusive with `exclude_line_items=true` — combining both returns no
            results. Example: ['1'].
        exclude_line_items (bool | Unset): When true, excludes per-line values and returns only
            values not associated with any line item (i.e. header-level). Mutually exclusive with
            `line_item_ids`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProcurementPoFieldValuesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            purchase_order_ids=purchase_order_ids,
            line_item_ids=line_item_ids,
            exclude_line_items=exclude_line_items,
        )
    ).parsed
