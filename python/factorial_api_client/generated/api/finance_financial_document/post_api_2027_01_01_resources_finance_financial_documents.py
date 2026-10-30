from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.finance_financial_document import FinanceFinancialDocument
from ...models.post_api_20270101_resources_finance_financial_documents_body import (
    PostApi20270101ResourcesFinanceFinancialDocumentsBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/finance/financial_documents",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FinanceFinancialDocument | None:
    if response.status_code == 201:
        response_201 = FinanceFinancialDocument.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | FinanceFinancialDocument]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> Response[ErrorResponse | FinanceFinancialDocument]:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FinanceFinancialDocument]
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
    body: PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> ErrorResponse | FinanceFinancialDocument | None:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FinanceFinancialDocument
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> Response[ErrorResponse | FinanceFinancialDocument]:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FinanceFinancialDocument]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset = UNSET,
) -> ErrorResponse | FinanceFinancialDocument | None:
    """Creates a Financial document

     Create a purchase financial document (invoice, credit note or receipt) together with its file. Sent
    as multipart/form-data. The document is created in draft (pending review) state; the strict
    required-field set is only enforced when it is validated in the app.

    Args:
        body (PostApi20270101ResourcesFinanceFinancialDocumentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FinanceFinancialDocument
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
