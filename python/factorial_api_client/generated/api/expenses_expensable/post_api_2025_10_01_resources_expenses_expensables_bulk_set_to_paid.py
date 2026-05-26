from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expenses_expensable import ExpensesExpensable
from ...models.post_api_20251001_resources_expenses_expensables_bulk_set_to_paid_body import (
    PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/expenses/expensables/bulk_set_to_paid",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ExpensesExpensable] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExpensesExpensable.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ExpensesExpensable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset = UNSET,
) -> Response[list[ExpensesExpensable]]:
    """Bulk set to paids an Expensable

     Bulk set to paids an Expensable

    Args:
        body (PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ExpensesExpensable]]
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
    body: PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset = UNSET,
) -> list[ExpensesExpensable] | None:
    """Bulk set to paids an Expensable

     Bulk set to paids an Expensable

    Args:
        body (PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ExpensesExpensable]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset = UNSET,
) -> Response[list[ExpensesExpensable]]:
    """Bulk set to paids an Expensable

     Bulk set to paids an Expensable

    Args:
        body (PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ExpensesExpensable]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset = UNSET,
) -> list[ExpensesExpensable] | None:
    """Bulk set to paids an Expensable

     Bulk set to paids an Expensable

    Args:
        body (PostApi20251001ResourcesExpensesExpensablesBulkSetToPaidBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ExpensesExpensable]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
