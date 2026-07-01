from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_finance_journal_lines_journal_entry_types import (
    GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes,
)
from ...models.get_api_20260701_resources_finance_journal_lines_reconciliation_status import (
    GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus,
)
from ...models.get_api_20260701_resources_finance_journal_lines_response_200 import (
    GetApi20260701ResourcesFinanceJournalLinesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    journal_entry_ids: list[str] | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    journal_entry_types: GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes
    | Unset = UNSET,
    reconciliation_status: GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus
    | Unset = UNSET,
    description: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_journal_entry_ids: list[str] | Unset = UNSET
    if not isinstance(journal_entry_ids, Unset):
        json_journal_entry_ids = journal_entry_ids

    params["journal_entry_ids[]"] = json_journal_entry_ids

    json_account_ids: list[str] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids[]"] = json_account_ids

    json_journal_entry_types: str | Unset = UNSET
    if not isinstance(journal_entry_types, Unset):
        json_journal_entry_types = journal_entry_types.value

    params["journal_entry_types[]"] = json_journal_entry_types

    json_reconciliation_status: str | Unset = UNSET
    if not isinstance(reconciliation_status, Unset):
        json_reconciliation_status = reconciliation_status.value

    params["reconciliation_status"] = json_reconciliation_status

    params["description"] = description

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/finance/journal_lines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesFinanceJournalLinesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesFinanceJournalLinesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesFinanceJournalLinesResponse200]:
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
    journal_entry_ids: list[str] | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    journal_entry_types: GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes
    | Unset = UNSET,
    reconciliation_status: GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus
    | Unset = UNSET,
    description: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceJournalLinesResponse200]:
    """Reads all Journal lines

     Reads all Journal lines

    Args:
        ids (list[str] | Unset): Filter by specific JournalLine IDs Example: ['1234'].
        journal_entry_ids (list[str] | Unset): Filter by specific JournalEntry IDs Example:
            ['4321'].
        account_ids (list[str] | Unset): Filter by specific Account IDs Example: ['9876'].
        journal_entry_types (GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes | Unset):
            Filter by JournalEntry types, accepted values: bank, bill, invoice, credit_note,
            merged_ledger_account, reconciliation, tax, receipt, payroll_result, external Example:
            ['bank', 'bill', 'invoice', 'credit_note', 'merged_ledger_account', 'reconciliation',
            'tax', 'receipt', 'payroll_result', 'external'].
        reconciliation_status (GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus |
            Unset): The reconciliation status of the journal line Example: pending.
        description (str | Unset):
        updated_from (str | Unset): Start date for filtering journal line records based on their
            last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceJournalLinesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        journal_entry_ids=journal_entry_ids,
        account_ids=account_ids,
        journal_entry_types=journal_entry_types,
        reconciliation_status=reconciliation_status,
        description=description,
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
    journal_entry_ids: list[str] | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    journal_entry_types: GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes
    | Unset = UNSET,
    reconciliation_status: GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus
    | Unset = UNSET,
    description: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceJournalLinesResponse200 | None:
    """Reads all Journal lines

     Reads all Journal lines

    Args:
        ids (list[str] | Unset): Filter by specific JournalLine IDs Example: ['1234'].
        journal_entry_ids (list[str] | Unset): Filter by specific JournalEntry IDs Example:
            ['4321'].
        account_ids (list[str] | Unset): Filter by specific Account IDs Example: ['9876'].
        journal_entry_types (GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes | Unset):
            Filter by JournalEntry types, accepted values: bank, bill, invoice, credit_note,
            merged_ledger_account, reconciliation, tax, receipt, payroll_result, external Example:
            ['bank', 'bill', 'invoice', 'credit_note', 'merged_ledger_account', 'reconciliation',
            'tax', 'receipt', 'payroll_result', 'external'].
        reconciliation_status (GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus |
            Unset): The reconciliation status of the journal line Example: pending.
        description (str | Unset):
        updated_from (str | Unset): Start date for filtering journal line records based on their
            last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceJournalLinesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        journal_entry_ids=journal_entry_ids,
        account_ids=account_ids,
        journal_entry_types=journal_entry_types,
        reconciliation_status=reconciliation_status,
        description=description,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    journal_entry_ids: list[str] | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    journal_entry_types: GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes
    | Unset = UNSET,
    reconciliation_status: GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus
    | Unset = UNSET,
    description: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceJournalLinesResponse200]:
    """Reads all Journal lines

     Reads all Journal lines

    Args:
        ids (list[str] | Unset): Filter by specific JournalLine IDs Example: ['1234'].
        journal_entry_ids (list[str] | Unset): Filter by specific JournalEntry IDs Example:
            ['4321'].
        account_ids (list[str] | Unset): Filter by specific Account IDs Example: ['9876'].
        journal_entry_types (GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes | Unset):
            Filter by JournalEntry types, accepted values: bank, bill, invoice, credit_note,
            merged_ledger_account, reconciliation, tax, receipt, payroll_result, external Example:
            ['bank', 'bill', 'invoice', 'credit_note', 'merged_ledger_account', 'reconciliation',
            'tax', 'receipt', 'payroll_result', 'external'].
        reconciliation_status (GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus |
            Unset): The reconciliation status of the journal line Example: pending.
        description (str | Unset):
        updated_from (str | Unset): Start date for filtering journal line records based on their
            last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceJournalLinesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        journal_entry_ids=journal_entry_ids,
        account_ids=account_ids,
        journal_entry_types=journal_entry_types,
        reconciliation_status=reconciliation_status,
        description=description,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    journal_entry_ids: list[str] | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    journal_entry_types: GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes
    | Unset = UNSET,
    reconciliation_status: GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus
    | Unset = UNSET,
    description: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceJournalLinesResponse200 | None:
    """Reads all Journal lines

     Reads all Journal lines

    Args:
        ids (list[str] | Unset): Filter by specific JournalLine IDs Example: ['1234'].
        journal_entry_ids (list[str] | Unset): Filter by specific JournalEntry IDs Example:
            ['4321'].
        account_ids (list[str] | Unset): Filter by specific Account IDs Example: ['9876'].
        journal_entry_types (GetApi20260701ResourcesFinanceJournalLinesJournalEntryTypes | Unset):
            Filter by JournalEntry types, accepted values: bank, bill, invoice, credit_note,
            merged_ledger_account, reconciliation, tax, receipt, payroll_result, external Example:
            ['bank', 'bill', 'invoice', 'credit_note', 'merged_ledger_account', 'reconciliation',
            'tax', 'receipt', 'payroll_result', 'external'].
        reconciliation_status (GetApi20260701ResourcesFinanceJournalLinesReconciliationStatus |
            Unset): The reconciliation status of the journal line Example: pending.
        description (str | Unset):
        updated_from (str | Unset): Start date for filtering journal line records based on their
            last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceJournalLinesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            journal_entry_ids=journal_entry_ids,
            account_ids=account_ids,
            journal_entry_types=journal_entry_types,
            reconciliation_status=reconciliation_status,
            description=description,
            updated_from=updated_from,
        )
    ).parsed
