from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_procurement_purchase_orders_response_200 import (
    GetApi20270101ResourcesProcurementPurchaseOrdersResponse200,
)
from ...models.get_api_20270101_resources_procurement_purchase_orders_status import (
    GetApi20270101ResourcesProcurementPurchaseOrdersStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    purchase_request_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset = UNSET,
    vendor_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_purchase_request_ids: list[str] | Unset = UNSET
    if not isinstance(purchase_request_ids, Unset):
        json_purchase_request_ids = purchase_request_ids

    params["purchase_request_ids[]"] = json_purchase_request_ids

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_vendor_ids: list[str] | Unset = UNSET
    if not isinstance(vendor_ids, Unset):
        json_vendor_ids = vendor_ids

    params["vendor_ids[]"] = json_vendor_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/procurement/purchase_orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesProcurementPurchaseOrdersResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200]:
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
    purchase_request_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset = UNSET,
    vendor_ids: list[str] | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200]:
    """Reads all Purchase orders

     Fetch one or all purchase orders for the company.

    Args:
        ids (list[str] | Unset): An array of purchase order IDs to filter by. Example: ['678432'].
        purchase_request_ids (list[str] | Unset): An array of purchase request IDs to filter by.
            Example: ['5678'].
        status (GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset): Status to filter
            by. Example: pending.
        vendor_ids (list[str] | Unset): Vendor IDs to filter by. Example: ['9012'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        purchase_request_ids=purchase_request_ids,
        status=status,
        vendor_ids=vendor_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    purchase_request_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset = UNSET,
    vendor_ids: list[str] | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200 | None:
    """Reads all Purchase orders

     Fetch one or all purchase orders for the company.

    Args:
        ids (list[str] | Unset): An array of purchase order IDs to filter by. Example: ['678432'].
        purchase_request_ids (list[str] | Unset): An array of purchase request IDs to filter by.
            Example: ['5678'].
        status (GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset): Status to filter
            by. Example: pending.
        vendor_ids (list[str] | Unset): Vendor IDs to filter by. Example: ['9012'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        purchase_request_ids=purchase_request_ids,
        status=status,
        vendor_ids=vendor_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    purchase_request_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset = UNSET,
    vendor_ids: list[str] | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200]:
    """Reads all Purchase orders

     Fetch one or all purchase orders for the company.

    Args:
        ids (list[str] | Unset): An array of purchase order IDs to filter by. Example: ['678432'].
        purchase_request_ids (list[str] | Unset): An array of purchase request IDs to filter by.
            Example: ['5678'].
        status (GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset): Status to filter
            by. Example: pending.
        vendor_ids (list[str] | Unset): Vendor IDs to filter by. Example: ['9012'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        purchase_request_ids=purchase_request_ids,
        status=status,
        vendor_ids=vendor_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    purchase_request_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset = UNSET,
    vendor_ids: list[str] | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200 | None:
    """Reads all Purchase orders

     Fetch one or all purchase orders for the company.

    Args:
        ids (list[str] | Unset): An array of purchase order IDs to filter by. Example: ['678432'].
        purchase_request_ids (list[str] | Unset): An array of purchase request IDs to filter by.
            Example: ['5678'].
        status (GetApi20270101ResourcesProcurementPurchaseOrdersStatus | Unset): Status to filter
            by. Example: pending.
        vendor_ids (list[str] | Unset): Vendor IDs to filter by. Example: ['9012'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProcurementPurchaseOrdersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            purchase_request_ids=purchase_request_ids,
            status=status,
            vendor_ids=vendor_ids,
        )
    ).parsed
