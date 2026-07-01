from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finance_tax_rate import FinanceTaxRate
from ...models.put_api_20260701_resources_finance_tax_rates_id_body import (
    PutApi20260701ResourcesFinanceTaxRatesIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-07-01/resources/finance/tax_rates/{id}".format(
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
) -> FinanceTaxRate | None:
    if response.status_code == 200:
        response_200 = FinanceTaxRate.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FinanceTaxRate]:
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
    body: PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset = UNSET,
) -> Response[FinanceTaxRate]:
    """Updates a Tax rate

     Updates a Tax rate

    Args:
        id (str):
        body (PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceTaxRate]
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
    body: PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset = UNSET,
) -> FinanceTaxRate | None:
    """Updates a Tax rate

     Updates a Tax rate

    Args:
        id (str):
        body (PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceTaxRate
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
    body: PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset = UNSET,
) -> Response[FinanceTaxRate]:
    """Updates a Tax rate

     Updates a Tax rate

    Args:
        id (str):
        body (PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceTaxRate]
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
    body: PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset = UNSET,
) -> FinanceTaxRate | None:
    """Updates a Tax rate

     Updates a Tax rate

    Args:
        id (str):
        body (PutApi20260701ResourcesFinanceTaxRatesIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceTaxRate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
