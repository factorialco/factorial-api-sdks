from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_banking_transactions_response_200 import (
    GetApi20260701ResourcesBankingTransactionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    bank_account_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_bank_account_ids: list[str] | Unset = UNSET
    if not isinstance(bank_account_ids, Unset):
        json_bank_account_ids = bank_account_ids

    params["bank_account_ids[]"] = json_bank_account_ids

    json_card_payment_ids: list[str] | Unset = UNSET
    if not isinstance(card_payment_ids, Unset):
        json_card_payment_ids = card_payment_ids

    params["card_payment_ids[]"] = json_card_payment_ids

    params["from"] = from_

    params["to"] = to

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/banking/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesBankingTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesBankingTransactionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesBankingTransactionsResponse200]:
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
    bank_account_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesBankingTransactionsResponse200]:
    """Reads all Transactions

     Reads all Transactions

    Args:
        ids (list[str] | Unset): An array of transaction IDs to filter by. Example: ['135'].
        bank_account_ids (list[str] | Unset): An array of Factorial Banking Bank Account IDs to
            filter by. Example: ['357'].
        card_payment_ids (list[str] | Unset): An array of Factorial Card Payment IDs to filter by.
            Example: ['135'].
        from_ (str | Unset): Date from which the transactions should be fetched. Example:
            2021-01-01.
        to (str | Unset): Date until which the transactions should be fetched. Example:
            2025-01-01.
        updated_from (str | Unset): Filter transactions updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesBankingTransactionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        bank_account_ids=bank_account_ids,
        card_payment_ids=card_payment_ids,
        from_=from_,
        to=to,
        updated_from=updated_from,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    bank_account_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesBankingTransactionsResponse200 | None:
    """Reads all Transactions

     Reads all Transactions

    Args:
        ids (list[str] | Unset): An array of transaction IDs to filter by. Example: ['135'].
        bank_account_ids (list[str] | Unset): An array of Factorial Banking Bank Account IDs to
            filter by. Example: ['357'].
        card_payment_ids (list[str] | Unset): An array of Factorial Card Payment IDs to filter by.
            Example: ['135'].
        from_ (str | Unset): Date from which the transactions should be fetched. Example:
            2021-01-01.
        to (str | Unset): Date until which the transactions should be fetched. Example:
            2025-01-01.
        updated_from (str | Unset): Filter transactions updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesBankingTransactionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        bank_account_ids=bank_account_ids,
        card_payment_ids=card_payment_ids,
        from_=from_,
        to=to,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    bank_account_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesBankingTransactionsResponse200]:
    """Reads all Transactions

     Reads all Transactions

    Args:
        ids (list[str] | Unset): An array of transaction IDs to filter by. Example: ['135'].
        bank_account_ids (list[str] | Unset): An array of Factorial Banking Bank Account IDs to
            filter by. Example: ['357'].
        card_payment_ids (list[str] | Unset): An array of Factorial Card Payment IDs to filter by.
            Example: ['135'].
        from_ (str | Unset): Date from which the transactions should be fetched. Example:
            2021-01-01.
        to (str | Unset): Date until which the transactions should be fetched. Example:
            2025-01-01.
        updated_from (str | Unset): Filter transactions updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesBankingTransactionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        bank_account_ids=bank_account_ids,
        card_payment_ids=card_payment_ids,
        from_=from_,
        to=to,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    bank_account_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesBankingTransactionsResponse200 | None:
    """Reads all Transactions

     Reads all Transactions

    Args:
        ids (list[str] | Unset): An array of transaction IDs to filter by. Example: ['135'].
        bank_account_ids (list[str] | Unset): An array of Factorial Banking Bank Account IDs to
            filter by. Example: ['357'].
        card_payment_ids (list[str] | Unset): An array of Factorial Card Payment IDs to filter by.
            Example: ['135'].
        from_ (str | Unset): Date from which the transactions should be fetched. Example:
            2021-01-01.
        to (str | Unset): Date until which the transactions should be fetched. Example:
            2025-01-01.
        updated_from (str | Unset): Filter transactions updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesBankingTransactionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            bank_account_ids=bank_account_ids,
            card_payment_ids=card_payment_ids,
            from_=from_,
            to=to,
            updated_from=updated_from,
        )
    ).parsed
