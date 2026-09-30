from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finance_financial_document import FinanceFinancialDocument
from ...models.put_api_20261001_resources_finance_financial_documents_id_body import (
    PutApi20261001ResourcesFinanceFinancialDocumentsIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-10-01/resources/finance/financial_documents/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinanceFinancialDocument | None:
    if response.status_code == 200:
        response_200 = FinanceFinancialDocument.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FinanceFinancialDocument]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset = UNSET,
) -> Response[FinanceFinancialDocument]:
    """Updates a Financial document

     Update a purchase financial document with PUT semantics: read the document, modify it, and send the
    complete resource back — the fields are replaced as sent. Status transitions are accepted and have
    their real side effects. Fields required on a validated document are only enforced when the document
    is validated (validated_at present in the payload), not before.

    Args:
        id (str):
        body (PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceFinancialDocument]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset = UNSET,
) -> FinanceFinancialDocument | None:
    """Updates a Financial document

     Update a purchase financial document with PUT semantics: read the document, modify it, and send the
    complete resource back — the fields are replaced as sent. Status transitions are accepted and have
    their real side effects. Fields required on a validated document are only enforced when the document
    is validated (validated_at present in the payload), not before.

    Args:
        id (str):
        body (PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceFinancialDocument
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset = UNSET,
) -> Response[FinanceFinancialDocument]:
    """Updates a Financial document

     Update a purchase financial document with PUT semantics: read the document, modify it, and send the
    complete resource back — the fields are replaced as sent. Status transitions are accepted and have
    their real side effects. Fields required on a validated document are only enforced when the document
    is validated (validated_at present in the payload), not before.

    Args:
        id (str):
        body (PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceFinancialDocument]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset = UNSET,
) -> FinanceFinancialDocument | None:
    """Updates a Financial document

     Update a purchase financial document with PUT semantics: read the document, modify it, and send the
    complete resource back — the fields are replaced as sent. Status transitions are accepted and have
    their real side effects. Fields required on a validated document are only enforced when the document
    is validated (validated_at present in the payload), not before.

    Args:
        id (str):
        body (PutApi20261001ResourcesFinanceFinancialDocumentsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceFinancialDocument
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
