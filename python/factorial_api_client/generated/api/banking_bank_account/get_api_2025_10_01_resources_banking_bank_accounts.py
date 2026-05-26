from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_banking_bank_accounts_response_200 import (
    GetApi20251001ResourcesBankingBankAccountsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    currency: str | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["currency"] = currency

    json_legal_entity_ids: list[int] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/banking/bank_accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesBankingBankAccountsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesBankingBankAccountsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesBankingBankAccountsResponse200]:
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
    currency: str | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesBankingBankAccountsResponse200]:
    """Reads all Bank accounts

     Fetch one or all bank accounts for the company.

    Args:
        ids (list[int] | Unset): An array of bank account IDs to filter by. Example: [1].
        currency (str | Unset): A currency to filter by. Example: EUR.
        legal_entity_ids (list[int] | Unset): An array of legal entity IDs to filter by. Example:
            [11].
        updated_from (str | Unset): Filter by accounts updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesBankingBankAccountsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        currency=currency,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    currency: str | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20251001ResourcesBankingBankAccountsResponse200 | None:
    """Reads all Bank accounts

     Fetch one or all bank accounts for the company.

    Args:
        ids (list[int] | Unset): An array of bank account IDs to filter by. Example: [1].
        currency (str | Unset): A currency to filter by. Example: EUR.
        legal_entity_ids (list[int] | Unset): An array of legal entity IDs to filter by. Example:
            [11].
        updated_from (str | Unset): Filter by accounts updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesBankingBankAccountsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        currency=currency,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    currency: str | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesBankingBankAccountsResponse200]:
    """Reads all Bank accounts

     Fetch one or all bank accounts for the company.

    Args:
        ids (list[int] | Unset): An array of bank account IDs to filter by. Example: [1].
        currency (str | Unset): A currency to filter by. Example: EUR.
        legal_entity_ids (list[int] | Unset): An array of legal entity IDs to filter by. Example:
            [11].
        updated_from (str | Unset): Filter by accounts updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesBankingBankAccountsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        currency=currency,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    currency: str | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20251001ResourcesBankingBankAccountsResponse200 | None:
    """Reads all Bank accounts

     Fetch one or all bank accounts for the company.

    Args:
        ids (list[int] | Unset): An array of bank account IDs to filter by. Example: [1].
        currency (str | Unset): A currency to filter by. Example: EUR.
        legal_entity_ids (list[int] | Unset): An array of legal entity IDs to filter by. Example:
            [11].
        updated_from (str | Unset): Filter by accounts updated from a specific date. Example:
            2021-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesBankingBankAccountsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            currency=currency,
            legal_entity_ids=legal_entity_ids,
            updated_from=updated_from,
        )
    ).parsed
