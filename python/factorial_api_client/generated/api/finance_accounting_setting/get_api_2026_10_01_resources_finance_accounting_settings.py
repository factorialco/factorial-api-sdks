from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_finance_accounting_settings_response_200 import (
    GetApi20261001ResourcesFinanceAccountingSettingsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
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

    params["updated_from"] = updated_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/finance/accounting_settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesFinanceAccountingSettingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesFinanceAccountingSettingsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesFinanceAccountingSettingsResponse200]:
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
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesFinanceAccountingSettingsResponse200]:
    """Reads all Accounting settings

     Reads all Accounting settings

    Args:
        ids (list[str] | Unset): List of AccountingSetting IDs to filter. Example: ['1234'].
        legal_entity_ids (list[str] | Unset): Filter by an array of legal entity IDs. Example:
            ['101'].
        updated_from (str | Unset): Start date for filtering accounting settings records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesFinanceAccountingSettingsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        legal_entity_ids=legal_entity_ids,
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
    updated_from: str | Unset = UNSET,
) -> GetApi20261001ResourcesFinanceAccountingSettingsResponse200 | None:
    """Reads all Accounting settings

     Reads all Accounting settings

    Args:
        ids (list[str] | Unset): List of AccountingSetting IDs to filter. Example: ['1234'].
        legal_entity_ids (list[str] | Unset): Filter by an array of legal entity IDs. Example:
            ['101'].
        updated_from (str | Unset): Start date for filtering accounting settings records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesFinanceAccountingSettingsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesFinanceAccountingSettingsResponse200]:
    """Reads all Accounting settings

     Reads all Accounting settings

    Args:
        ids (list[str] | Unset): List of AccountingSetting IDs to filter. Example: ['1234'].
        legal_entity_ids (list[str] | Unset): Filter by an array of legal entity IDs. Example:
            ['101'].
        updated_from (str | Unset): Start date for filtering accounting settings records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesFinanceAccountingSettingsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
) -> GetApi20261001ResourcesFinanceAccountingSettingsResponse200 | None:
    """Reads all Accounting settings

     Reads all Accounting settings

    Args:
        ids (list[str] | Unset): List of AccountingSetting IDs to filter. Example: ['1234'].
        legal_entity_ids (list[str] | Unset): Filter by an array of legal entity IDs. Example:
            ['101'].
        updated_from (str | Unset): Start date for filtering accounting settings records based on
            their last update. Example: 2025-01-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesFinanceAccountingSettingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            legal_entity_ids=legal_entity_ids,
            updated_from=updated_from,
        )
    ).parsed
