from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finance_financial_document import FinanceFinancialDocument
from ...models.post_api_20261001_resources_finance_financial_documents_body import (
    PostApi20261001ResourcesFinanceFinancialDocumentsBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-10-01/resources/finance/financial_documents",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinanceFinancialDocument | None:
    if response.status_code == 201:
        response_201 = FinanceFinancialDocument.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> Response[FinanceFinancialDocument]:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceFinancialDocument]
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
    body: PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> FinanceFinancialDocument | None:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceFinancialDocument
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> Response[FinanceFinancialDocument]:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceFinancialDocument]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> FinanceFinancialDocument | None:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20261001ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceFinancialDocument
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
