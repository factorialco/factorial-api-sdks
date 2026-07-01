from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_finance_contacts_contact_type import (
    GetApi20260701ResourcesFinanceContactsContactType,
)
from ...models.get_api_20260701_resources_finance_contacts_response_200 import (
    GetApi20260701ResourcesFinanceContactsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    tax_ids: list[str] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name: str | Unset = UNSET,
    contact_type: GetApi20260701ResourcesFinanceContactsContactType | Unset = UNSET,
    website: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_tax_ids: list[str] | Unset = UNSET
    if not isinstance(tax_ids, Unset):
        json_tax_ids = tax_ids

    params["tax_ids[]"] = json_tax_ids

    params["legal_name"] = legal_name

    params["name"] = name

    json_contact_type: str | Unset = UNSET
    if not isinstance(contact_type, Unset):
        json_contact_type = contact_type.value

    params["contact_type"] = json_contact_type

    params["website"] = website

    params["email"] = email

    params["phone_number"] = phone_number

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/finance/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesFinanceContactsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesFinanceContactsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesFinanceContactsResponse200]:
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
    tax_ids: list[str] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name: str | Unset = UNSET,
    contact_type: GetApi20260701ResourcesFinanceContactsContactType | Unset = UNSET,
    website: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceContactsResponse200]:
    """Reads all Contacts

     Reads all Contacts

    Args:
        ids (list[str] | Unset): List of Contact IDs to filter by. Example: ['123', '456'].
        tax_ids (list[str] | Unset): List of Tax IDs to filter by. Example: ['X1234567',
            'B7654321'].
        legal_name (str | Unset): Filter by partial match of a contact's legal name. Example:
            Google.
        name (str | Unset): The commercial name of the Contact. Example: Google.
        contact_type (GetApi20260701ResourcesFinanceContactsContactType | Unset): Type of the
            contact (defaults to Vendor). Example: vendor.
        website (str | Unset): The website of the Contact. Example: https://www.example.com.
        email (str | Unset): The email of the Contact. Example: contact@example.com.
        phone_number (str | Unset): The phone number of the Contact. Example: +1234567890.
        updated_from (str | Unset): Start date for filtering Contacts records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceContactsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        tax_ids=tax_ids,
        legal_name=legal_name,
        name=name,
        contact_type=contact_type,
        website=website,
        email=email,
        phone_number=phone_number,
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
    tax_ids: list[str] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name: str | Unset = UNSET,
    contact_type: GetApi20260701ResourcesFinanceContactsContactType | Unset = UNSET,
    website: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceContactsResponse200 | None:
    """Reads all Contacts

     Reads all Contacts

    Args:
        ids (list[str] | Unset): List of Contact IDs to filter by. Example: ['123', '456'].
        tax_ids (list[str] | Unset): List of Tax IDs to filter by. Example: ['X1234567',
            'B7654321'].
        legal_name (str | Unset): Filter by partial match of a contact's legal name. Example:
            Google.
        name (str | Unset): The commercial name of the Contact. Example: Google.
        contact_type (GetApi20260701ResourcesFinanceContactsContactType | Unset): Type of the
            contact (defaults to Vendor). Example: vendor.
        website (str | Unset): The website of the Contact. Example: https://www.example.com.
        email (str | Unset): The email of the Contact. Example: contact@example.com.
        phone_number (str | Unset): The phone number of the Contact. Example: +1234567890.
        updated_from (str | Unset): Start date for filtering Contacts records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceContactsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        tax_ids=tax_ids,
        legal_name=legal_name,
        name=name,
        contact_type=contact_type,
        website=website,
        email=email,
        phone_number=phone_number,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    tax_ids: list[str] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name: str | Unset = UNSET,
    contact_type: GetApi20260701ResourcesFinanceContactsContactType | Unset = UNSET,
    website: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceContactsResponse200]:
    """Reads all Contacts

     Reads all Contacts

    Args:
        ids (list[str] | Unset): List of Contact IDs to filter by. Example: ['123', '456'].
        tax_ids (list[str] | Unset): List of Tax IDs to filter by. Example: ['X1234567',
            'B7654321'].
        legal_name (str | Unset): Filter by partial match of a contact's legal name. Example:
            Google.
        name (str | Unset): The commercial name of the Contact. Example: Google.
        contact_type (GetApi20260701ResourcesFinanceContactsContactType | Unset): Type of the
            contact (defaults to Vendor). Example: vendor.
        website (str | Unset): The website of the Contact. Example: https://www.example.com.
        email (str | Unset): The email of the Contact. Example: contact@example.com.
        phone_number (str | Unset): The phone number of the Contact. Example: +1234567890.
        updated_from (str | Unset): Start date for filtering Contacts records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceContactsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        tax_ids=tax_ids,
        legal_name=legal_name,
        name=name,
        contact_type=contact_type,
        website=website,
        email=email,
        phone_number=phone_number,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    tax_ids: list[str] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name: str | Unset = UNSET,
    contact_type: GetApi20260701ResourcesFinanceContactsContactType | Unset = UNSET,
    website: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceContactsResponse200 | None:
    """Reads all Contacts

     Reads all Contacts

    Args:
        ids (list[str] | Unset): List of Contact IDs to filter by. Example: ['123', '456'].
        tax_ids (list[str] | Unset): List of Tax IDs to filter by. Example: ['X1234567',
            'B7654321'].
        legal_name (str | Unset): Filter by partial match of a contact's legal name. Example:
            Google.
        name (str | Unset): The commercial name of the Contact. Example: Google.
        contact_type (GetApi20260701ResourcesFinanceContactsContactType | Unset): Type of the
            contact (defaults to Vendor). Example: vendor.
        website (str | Unset): The website of the Contact. Example: https://www.example.com.
        email (str | Unset): The email of the Contact. Example: contact@example.com.
        phone_number (str | Unset): The phone number of the Contact. Example: +1234567890.
        updated_from (str | Unset): Start date for filtering Contacts records based on their last
            update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceContactsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            tax_ids=tax_ids,
            legal_name=legal_name,
            name=name,
            contact_type=contact_type,
            website=website,
            email=email,
            phone_number=phone_number,
            updated_from=updated_from,
        )
    ).parsed
