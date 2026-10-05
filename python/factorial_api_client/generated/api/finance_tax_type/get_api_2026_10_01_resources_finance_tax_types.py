from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_finance_tax_types_response_200 import (
    GetApi20261001ResourcesFinanceTaxTypesResponse200,
)
from ...models.get_api_20261001_resources_finance_tax_types_type import (
    GetApi20261001ResourcesFinanceTaxTypesType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    country_code: str | Unset = UNSET,
    type_: GetApi20261001ResourcesFinanceTaxTypesType | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["country_code"] = country_code

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/finance/tax_types",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesFinanceTaxTypesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesFinanceTaxTypesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesFinanceTaxTypesResponse200]:
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
    country_code: str | Unset = UNSET,
    type_: GetApi20261001ResourcesFinanceTaxTypesType | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesFinanceTaxTypesResponse200]:
    """Reads all Tax types

     Reads all Tax types

    Args:
        ids (list[str] | Unset): List of TaxType IDs to filter. Example: ['1234'].
        country_code (str | Unset): Filters TaxTypes by a specified country code or includes those
            without any country code if set to nil. Example: ES.
        type_ (GetApi20261001ResourcesFinanceTaxTypesType | Unset): Filters TaxTypes by a type
            (vat, personal_income). Example: vat.
        updated_from (str | Unset): Start date for filtering TaxType records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesFinanceTaxTypesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        country_code=country_code,
        type_=type_,
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
    country_code: str | Unset = UNSET,
    type_: GetApi20261001ResourcesFinanceTaxTypesType | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20261001ResourcesFinanceTaxTypesResponse200 | None:
    """Reads all Tax types

     Reads all Tax types

    Args:
        ids (list[str] | Unset): List of TaxType IDs to filter. Example: ['1234'].
        country_code (str | Unset): Filters TaxTypes by a specified country code or includes those
            without any country code if set to nil. Example: ES.
        type_ (GetApi20261001ResourcesFinanceTaxTypesType | Unset): Filters TaxTypes by a type
            (vat, personal_income). Example: vat.
        updated_from (str | Unset): Start date for filtering TaxType records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesFinanceTaxTypesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        country_code=country_code,
        type_=type_,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    country_code: str | Unset = UNSET,
    type_: GetApi20261001ResourcesFinanceTaxTypesType | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesFinanceTaxTypesResponse200]:
    """Reads all Tax types

     Reads all Tax types

    Args:
        ids (list[str] | Unset): List of TaxType IDs to filter. Example: ['1234'].
        country_code (str | Unset): Filters TaxTypes by a specified country code or includes those
            without any country code if set to nil. Example: ES.
        type_ (GetApi20261001ResourcesFinanceTaxTypesType | Unset): Filters TaxTypes by a type
            (vat, personal_income). Example: vat.
        updated_from (str | Unset): Start date for filtering TaxType records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesFinanceTaxTypesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        country_code=country_code,
        type_=type_,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    country_code: str | Unset = UNSET,
    type_: GetApi20261001ResourcesFinanceTaxTypesType | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20261001ResourcesFinanceTaxTypesResponse200 | None:
    """Reads all Tax types

     Reads all Tax types

    Args:
        ids (list[str] | Unset): List of TaxType IDs to filter. Example: ['1234'].
        country_code (str | Unset): Filters TaxTypes by a specified country code or includes those
            without any country code if set to nil. Example: ES.
        type_ (GetApi20261001ResourcesFinanceTaxTypesType | Unset): Filters TaxTypes by a type
            (vat, personal_income). Example: vat.
        updated_from (str | Unset): Start date for filtering TaxType records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesFinanceTaxTypesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            country_code=country_code,
            type_=type_,
            updated_from=updated_from,
        )
    ).parsed
