from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_procurement_purchase_requests_response_200 import (
    GetApi20270101ResourcesProcurementPurchaseRequestsResponse200,
)
from ...models.get_api_20270101_resources_procurement_purchase_requests_status import (
    GetApi20270101ResourcesProcurementPurchaseRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    requester_employee_ids: list[str] | Unset = UNSET,
    type_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_requester_employee_ids: list[str] | Unset = UNSET
    if not isinstance(requester_employee_ids, Unset):
        json_requester_employee_ids = requester_employee_ids

    params["requester_employee_ids[]"] = json_requester_employee_ids

    json_type_ids: list[str] | Unset = UNSET
    if not isinstance(type_ids, Unset):
        json_type_ids = type_ids

    params["type_ids[]"] = json_type_ids

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/procurement/purchase_requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesProcurementPurchaseRequestsResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200]:
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
    requester_employee_ids: list[str] | Unset = UNSET,
    type_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200]:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[str] | Unset): An array of purchase request IDs to filter by. Example:
            ['678432'].
        requester_employee_ids (list[str] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: ['20'].
        type_ids (list[str] | Unset): An array of purchase type IDs to filter by. Example:
            ['12353'].
        status (GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        requester_employee_ids=requester_employee_ids,
        type_ids=type_ids,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    requester_employee_ids: list[str] | Unset = UNSET,
    type_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200 | None:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[str] | Unset): An array of purchase request IDs to filter by. Example:
            ['678432'].
        requester_employee_ids (list[str] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: ['20'].
        type_ids (list[str] | Unset): An array of purchase type IDs to filter by. Example:
            ['12353'].
        status (GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        requester_employee_ids=requester_employee_ids,
        type_ids=type_ids,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    requester_employee_ids: list[str] | Unset = UNSET,
    type_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200]:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[str] | Unset): An array of purchase request IDs to filter by. Example:
            ['678432'].
        requester_employee_ids (list[str] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: ['20'].
        type_ids (list[str] | Unset): An array of purchase type IDs to filter by. Example:
            ['12353'].
        status (GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        requester_employee_ids=requester_employee_ids,
        type_ids=type_ids,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    requester_employee_ids: list[str] | Unset = UNSET,
    type_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200 | None:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[str] | Unset): An array of purchase request IDs to filter by. Example:
            ['678432'].
        requester_employee_ids (list[str] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: ['20'].
        type_ids (list[str] | Unset): An array of purchase type IDs to filter by. Example:
            ['12353'].
        status (GetApi20270101ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesProcurementPurchaseRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            requester_employee_ids=requester_employee_ids,
            type_ids=type_ids,
            status=status,
        )
    ).parsed
