from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_finance_journal_entries_response_200 import (
    GetApi20260701ResourcesFinanceJournalEntriesResponse200,
)
from ...models.get_api_20260701_resources_finance_journal_entries_source_type import (
    GetApi20260701ResourcesFinanceJournalEntriesSourceType,
)
from ...models.get_api_20260701_resources_finance_journal_entries_status import (
    GetApi20260701ResourcesFinanceJournalEntriesStatus,
)
from ...models.get_api_20260701_resources_finance_journal_entries_types import (
    GetApi20260701ResourcesFinanceJournalEntriesTypes,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    source_type: GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset = UNSET,
    types: GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset = UNSET,
    status: GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_legal_entity_ids: list[str] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    json_source_ids: list[str] | Unset = UNSET
    if not isinstance(source_ids, Unset):
        json_source_ids = source_ids

    params["source_ids[]"] = json_source_ids

    json_source_type: str | Unset = UNSET
    if not isinstance(source_type, Unset):
        json_source_type = source_type.value

    params["source_type"] = json_source_type

    json_types: str | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types.value

    params["types[]"] = json_types

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/finance/journal_entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesFinanceJournalEntriesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesFinanceJournalEntriesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesFinanceJournalEntriesResponse200]:
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
    legal_entity_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    source_type: GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset = UNSET,
    types: GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset = UNSET,
    status: GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceJournalEntriesResponse200]:
    """Reads all Journal entries

     Reads all Journal entries

    Args:
        ids (list[str] | Unset): Filter by JournalEntry IDs Example: ['4321'].
        legal_entity_ids (list[str] | Unset): Filter by Legal Entity IDs Example: ['1001'].
        source_ids (list[str] | Unset): Filter by Source IDs Example: ['15'].
        source_type (GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset): Filter by
            related source type Example: bank_transaction.
        types (GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset): Filter by entry type
            Example: ['bank', 'invoice', 'credit_note', 'receipt'].
        status (GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset): Filter by Journal
            Entry Status Example: published.
        updated_from (str | Unset): Start date for filtering journal entries records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceJournalEntriesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        legal_entity_ids=legal_entity_ids,
        source_ids=source_ids,
        source_type=source_type,
        types=types,
        status=status,
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
    legal_entity_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    source_type: GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset = UNSET,
    types: GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset = UNSET,
    status: GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceJournalEntriesResponse200 | None:
    """Reads all Journal entries

     Reads all Journal entries

    Args:
        ids (list[str] | Unset): Filter by JournalEntry IDs Example: ['4321'].
        legal_entity_ids (list[str] | Unset): Filter by Legal Entity IDs Example: ['1001'].
        source_ids (list[str] | Unset): Filter by Source IDs Example: ['15'].
        source_type (GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset): Filter by
            related source type Example: bank_transaction.
        types (GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset): Filter by entry type
            Example: ['bank', 'invoice', 'credit_note', 'receipt'].
        status (GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset): Filter by Journal
            Entry Status Example: published.
        updated_from (str | Unset): Start date for filtering journal entries records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceJournalEntriesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        legal_entity_ids=legal_entity_ids,
        source_ids=source_ids,
        source_type=source_type,
        types=types,
        status=status,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    source_type: GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset = UNSET,
    types: GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset = UNSET,
    status: GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceJournalEntriesResponse200]:
    """Reads all Journal entries

     Reads all Journal entries

    Args:
        ids (list[str] | Unset): Filter by JournalEntry IDs Example: ['4321'].
        legal_entity_ids (list[str] | Unset): Filter by Legal Entity IDs Example: ['1001'].
        source_ids (list[str] | Unset): Filter by Source IDs Example: ['15'].
        source_type (GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset): Filter by
            related source type Example: bank_transaction.
        types (GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset): Filter by entry type
            Example: ['bank', 'invoice', 'credit_note', 'receipt'].
        status (GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset): Filter by Journal
            Entry Status Example: published.
        updated_from (str | Unset): Start date for filtering journal entries records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceJournalEntriesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        legal_entity_ids=legal_entity_ids,
        source_ids=source_ids,
        source_type=source_type,
        types=types,
        status=status,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    source_type: GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset = UNSET,
    types: GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset = UNSET,
    status: GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceJournalEntriesResponse200 | None:
    """Reads all Journal entries

     Reads all Journal entries

    Args:
        ids (list[str] | Unset): Filter by JournalEntry IDs Example: ['4321'].
        legal_entity_ids (list[str] | Unset): Filter by Legal Entity IDs Example: ['1001'].
        source_ids (list[str] | Unset): Filter by Source IDs Example: ['15'].
        source_type (GetApi20260701ResourcesFinanceJournalEntriesSourceType | Unset): Filter by
            related source type Example: bank_transaction.
        types (GetApi20260701ResourcesFinanceJournalEntriesTypes | Unset): Filter by entry type
            Example: ['bank', 'invoice', 'credit_note', 'receipt'].
        status (GetApi20260701ResourcesFinanceJournalEntriesStatus | Unset): Filter by Journal
            Entry Status Example: published.
        updated_from (str | Unset): Start date for filtering journal entries records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceJournalEntriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            legal_entity_ids=legal_entity_ids,
            source_ids=source_ids,
            source_type=source_type,
            types=types,
            status=status,
            updated_from=updated_from,
        )
    ).parsed
