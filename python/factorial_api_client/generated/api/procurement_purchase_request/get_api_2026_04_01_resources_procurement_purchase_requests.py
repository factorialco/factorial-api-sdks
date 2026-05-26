from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_procurement_purchase_requests_response_200 import (
    GetApi20260401ResourcesProcurementPurchaseRequestsResponse200,
)
from ...models.get_api_20260401_resources_procurement_purchase_requests_status import (
    GetApi20260401ResourcesProcurementPurchaseRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    requester_employee_ids: list[int] | Unset = UNSET,
    type_ids: list[int] | Unset = UNSET,
    status: GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_requester_employee_ids: list[int] | Unset = UNSET
    if not isinstance(requester_employee_ids, Unset):
        json_requester_employee_ids = requester_employee_ids

    params["requester_employee_ids[]"] = json_requester_employee_ids

    json_type_ids: list[int] | Unset = UNSET
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
        "url": "/api/2026-04-01/resources/procurement/purchase_requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesProcurementPurchaseRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesProcurementPurchaseRequestsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesProcurementPurchaseRequestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    requester_employee_ids: list[int] | Unset = UNSET,
    type_ids: list[int] | Unset = UNSET,
    status: GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> Response[GetApi20260401ResourcesProcurementPurchaseRequestsResponse200]:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[int] | Unset): An array of purchase request IDs to filter by. Example: [678432].
        requester_employee_ids (list[int] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: [20].
        type_ids (list[int] | Unset): An array of purchase type IDs to filter by. Example:
            [12353].
        status (GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesProcurementPurchaseRequestsResponse200]
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
    ids: list[int] | Unset = UNSET,
    requester_employee_ids: list[int] | Unset = UNSET,
    type_ids: list[int] | Unset = UNSET,
    status: GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> GetApi20260401ResourcesProcurementPurchaseRequestsResponse200 | None:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[int] | Unset): An array of purchase request IDs to filter by. Example: [678432].
        requester_employee_ids (list[int] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: [20].
        type_ids (list[int] | Unset): An array of purchase type IDs to filter by. Example:
            [12353].
        status (GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesProcurementPurchaseRequestsResponse200
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
    ids: list[int] | Unset = UNSET,
    requester_employee_ids: list[int] | Unset = UNSET,
    type_ids: list[int] | Unset = UNSET,
    status: GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> Response[GetApi20260401ResourcesProcurementPurchaseRequestsResponse200]:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[int] | Unset): An array of purchase request IDs to filter by. Example: [678432].
        requester_employee_ids (list[int] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: [20].
        type_ids (list[int] | Unset): An array of purchase type IDs to filter by. Example:
            [12353].
        status (GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesProcurementPurchaseRequestsResponse200]
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
    ids: list[int] | Unset = UNSET,
    requester_employee_ids: list[int] | Unset = UNSET,
    type_ids: list[int] | Unset = UNSET,
    status: GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset = UNSET,
) -> GetApi20260401ResourcesProcurementPurchaseRequestsResponse200 | None:
    """Reads all Purchase requests

     Fetch one or all purchase requests for the company.

    Args:
        ids (list[int] | Unset): An array of purchase request IDs to filter by. Example: [678432].
        requester_employee_ids (list[int] | Unset): An array of employee IDs to filter by as the
            purchase requester requesters. Example: [20].
        type_ids (list[int] | Unset): An array of purchase type IDs to filter by. Example:
            [12353].
        status (GetApi20260401ResourcesProcurementPurchaseRequestsStatus | Unset): Status to
            filter by. Example: pending.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesProcurementPurchaseRequestsResponse200
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
