from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expenses_expensable import ExpensesExpensable
from ...models.post_api_20260701_resources_expenses_expensables_update_reimbursable_amount_body import (
    PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/expenses/expensables/update_reimbursable_amount",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExpensesExpensable | None:
    if response.status_code == 200:
        response_200 = ExpensesExpensable.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExpensesExpensable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset = UNSET,
) -> Response[ExpensesExpensable]:
    """Update reimbursable amount on an expensable

     Update the reimbursable amount on an expensable. Only expense-type expensables with reimbursable
    payment are supported.

    Args:
        body (PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpensesExpensable]
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
    body: PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset = UNSET,
) -> ExpensesExpensable | None:
    """Update reimbursable amount on an expensable

     Update the reimbursable amount on an expensable. Only expense-type expensables with reimbursable
    payment are supported.

    Args:
        body (PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpensesExpensable
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset = UNSET,
) -> Response[ExpensesExpensable]:
    """Update reimbursable amount on an expensable

     Update the reimbursable amount on an expensable. Only expense-type expensables with reimbursable
    payment are supported.

    Args:
        body (PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpensesExpensable]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset = UNSET,
) -> ExpensesExpensable | None:
    """Update reimbursable amount on an expensable

     Update the reimbursable amount on an expensable. Only expense-type expensables with reimbursable
    payment are supported.

    Args:
        body (PostApi20260701ResourcesExpensesExpensablesUpdateReimbursableAmountBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpensesExpensable
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
