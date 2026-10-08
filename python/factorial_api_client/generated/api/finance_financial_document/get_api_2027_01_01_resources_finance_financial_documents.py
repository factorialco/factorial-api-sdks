from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_finance_financial_documents_document_types import (
    GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes,
)
from ...models.get_api_20270101_resources_finance_financial_documents_response_200 import (
    GetApi20270101ResourcesFinanceFinancialDocumentsResponse200,
)
from ...models.get_api_20270101_resources_finance_financial_documents_statuses import (
    GetApi20270101ResourcesFinanceFinancialDocumentsStatuses,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    company_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    vendor_id: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    document_types: GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["company_id"] = company_id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["vendor_id"] = vendor_id

    params["currency"] = currency

    json_statuses: str | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses.value

    params["statuses[]"] = json_statuses

    json_legal_entity_ids: list[str] | Unset = UNSET
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
        "url": "/api/2027-01-01/resources/finance/financial_documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesFinanceFinancialDocumentsResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    company_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    vendor_id: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    document_types: GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200]:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (str | Unset): Return only the documents of this company. It must be a company
            the reader has access to: an id outside that set makes the read fail rather than come back
            empty. Example: 1.
        ids (list[str] | Unset): Return only the financial documents with these ids. Example:
            ['135'].
        vendor_id (str | Unset): Return only the documents issued by this vendor contact. Example:
            33.
        currency (str | Unset): Return only the documents in this currency, as an uppercase ISO
            4217 code. It takes one code, not a list. Example: USD.
        statuses (GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset): Return only
            the documents in these states: `processing`, `review` (awaiting approval), `sent_to_pay`
            or `paid`. Example: ['review'].
        legal_entity_ids (list[str] | Unset): Return only the documents booked against these legal
            entities. Example: ['13'].
        document_types (GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Return only the documents of these kinds: `invoice`, `receipt` or `credit_note`. Example:
            ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200]
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
    company_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    vendor_id: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    document_types: GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200 | None:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (str | Unset): Return only the documents of this company. It must be a company
            the reader has access to: an id outside that set makes the read fail rather than come back
            empty. Example: 1.
        ids (list[str] | Unset): Return only the financial documents with these ids. Example:
            ['135'].
        vendor_id (str | Unset): Return only the documents issued by this vendor contact. Example:
            33.
        currency (str | Unset): Return only the documents in this currency, as an uppercase ISO
            4217 code. It takes one code, not a list. Example: USD.
        statuses (GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset): Return only
            the documents in these states: `processing`, `review` (awaiting approval), `sent_to_pay`
            or `paid`. Example: ['review'].
        legal_entity_ids (list[str] | Unset): Return only the documents booked against these legal
            entities. Example: ['13'].
        document_types (GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Return only the documents of these kinds: `invoice`, `receipt` or `credit_note`. Example:
            ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200
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
    company_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    vendor_id: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    document_types: GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200]:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (str | Unset): Return only the documents of this company. It must be a company
            the reader has access to: an id outside that set makes the read fail rather than come back
            empty. Example: 1.
        ids (list[str] | Unset): Return only the financial documents with these ids. Example:
            ['135'].
        vendor_id (str | Unset): Return only the documents issued by this vendor contact. Example:
            33.
        currency (str | Unset): Return only the documents in this currency, as an uppercase ISO
            4217 code. It takes one code, not a list. Example: USD.
        statuses (GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset): Return only
            the documents in these states: `processing`, `review` (awaiting approval), `sent_to_pay`
            or `paid`. Example: ['review'].
        legal_entity_ids (list[str] | Unset): Return only the documents booked against these legal
            entities. Example: ['13'].
        document_types (GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Return only the documents of these kinds: `invoice`, `receipt` or `credit_note`. Example:
            ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200]
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
    company_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    vendor_id: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    statuses: GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    document_types: GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200 | None:
    """Reads all Financial documents

     Fetch one or all financial documents for the company.

    Args:
        company_id (str | Unset): Return only the documents of this company. It must be a company
            the reader has access to: an id outside that set makes the read fail rather than come back
            empty. Example: 1.
        ids (list[str] | Unset): Return only the financial documents with these ids. Example:
            ['135'].
        vendor_id (str | Unset): Return only the documents issued by this vendor contact. Example:
            33.
        currency (str | Unset): Return only the documents in this currency, as an uppercase ISO
            4217 code. It takes one code, not a list. Example: USD.
        statuses (GetApi20270101ResourcesFinanceFinancialDocumentsStatuses | Unset): Return only
            the documents in these states: `processing`, `review` (awaiting approval), `sent_to_pay`
            or `paid`. Example: ['review'].
        legal_entity_ids (list[str] | Unset): Return only the documents booked against these legal
            entities. Example: ['13'].
        document_types (GetApi20270101ResourcesFinanceFinancialDocumentsDocumentTypes | Unset):
            Return only the documents of these kinds: `invoice`, `receipt` or `credit_note`. Example:
            ['invoice'].
        updated_from (str | Unset): Filter financial documents updated from a specific date
            Example: 2020-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesFinanceFinancialDocumentsResponse200
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
