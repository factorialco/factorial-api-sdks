from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_finance_financial_documents_document_types import (
    GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes,
)
from ...models.get_api_20260401_resources_finance_financial_documents_response_200 import (
    GetApi20260401ResourcesFinanceFinancialDocumentsResponse200,
)
from ...models.get_api_20260401_resources_finance_financial_documents_statuses import (
    GetApi20260401ResourcesFinanceFinancialDocumentsStatuses,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    company_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    vendor_id: int | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    document_types: GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["company_id"] = company_id

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["vendor_id"] = vendor_id

    params["currency"] = currency

    json_statuses: str | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses.value

    params["statuses[]"] = json_statuses

    json_legal_entity_ids: list[int] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    json_document_types: str | Unset = UNSET
    if not isinstance(document_types, Unset):
        json_document_types = document_types.value

    params["document_types[]"] = json_document_types

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/finance/financial_documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesFinanceFinancialDocumentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesFinanceFinancialDocumentsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesFinanceFinancialDocumentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    company_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    vendor_id: int | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    document_types: GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesFinanceFinancialDocumentsResponse200]:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (int | Unset): Search financial documents by company_id Example: 1.
        ids (list[int] | Unset): Search financial documents by ID Example: [135].
        vendor_id (int | Unset): Search financial documents by vendor_id Example: 33.
        currency (str | Unset): Search financial documents by currency Example: USD.
        statuses (GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset): Search
            financial documents by status Example: ['review'].
        legal_entity_ids (list[int] | Unset): Search financial documents by legal_entity_id
            Example: [13].
        document_types (GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Search financial documents by document_type Example: ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceFinancialDocumentsResponse200]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        ids=ids,
        vendor_id=vendor_id,
        currency=currency,
        statuses=statuses,
        legal_entity_ids=legal_entity_ids,
        document_types=document_types,
        updated_from=updated_from,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    company_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    vendor_id: int | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    document_types: GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260401ResourcesFinanceFinancialDocumentsResponse200 | None:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (int | Unset): Search financial documents by company_id Example: 1.
        ids (list[int] | Unset): Search financial documents by ID Example: [135].
        vendor_id (int | Unset): Search financial documents by vendor_id Example: 33.
        currency (str | Unset): Search financial documents by currency Example: USD.
        statuses (GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset): Search
            financial documents by status Example: ['review'].
        legal_entity_ids (list[int] | Unset): Search financial documents by legal_entity_id
            Example: [13].
        document_types (GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Search financial documents by document_type Example: ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceFinancialDocumentsResponse200
    """

    return sync_detailed(
        client=client,
        company_id=company_id,
        ids=ids,
        vendor_id=vendor_id,
        currency=currency,
        statuses=statuses,
        legal_entity_ids=legal_entity_ids,
        document_types=document_types,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    company_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    vendor_id: int | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    document_types: GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesFinanceFinancialDocumentsResponse200]:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (int | Unset): Search financial documents by company_id Example: 1.
        ids (list[int] | Unset): Search financial documents by ID Example: [135].
        vendor_id (int | Unset): Search financial documents by vendor_id Example: 33.
        currency (str | Unset): Search financial documents by currency Example: USD.
        statuses (GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset): Search
            financial documents by status Example: ['review'].
        legal_entity_ids (list[int] | Unset): Search financial documents by legal_entity_id
            Example: [13].
        document_types (GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Search financial documents by document_type Example: ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceFinancialDocumentsResponse200]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        ids=ids,
        vendor_id=vendor_id,
        currency=currency,
        statuses=statuses,
        legal_entity_ids=legal_entity_ids,
        document_types=document_types,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    company_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    vendor_id: int | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    document_types: GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260401ResourcesFinanceFinancialDocumentsResponse200 | None:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (int | Unset): Search financial documents by company_id Example: 1.
        ids (list[int] | Unset): Search financial documents by ID Example: [135].
        vendor_id (int | Unset): Search financial documents by vendor_id Example: 33.
        currency (str | Unset): Search financial documents by currency Example: USD.
        statuses (GetApi20260401ResourcesFinanceFinancialDocumentsStatuses | Unset): Search
            financial documents by status Example: ['review'].
        legal_entity_ids (list[int] | Unset): Search financial documents by legal_entity_id
            Example: [13].
        document_types (GetApi20260401ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Search financial documents by document_type Example: ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceFinancialDocumentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            company_id=company_id,
            ids=ids,
            vendor_id=vendor_id,
            currency=currency,
            statuses=statuses,
            legal_entity_ids=legal_entity_ids,
            document_types=document_types,
            updated_from=updated_from,
        )
    ).parsed
