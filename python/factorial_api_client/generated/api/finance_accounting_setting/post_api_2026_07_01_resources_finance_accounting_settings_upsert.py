from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finance_accounting_setting import FinanceAccountingSetting
from ...models.post_api_20260701_resources_finance_accounting_settings_upsert_body import (
    PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/finance/accounting_settings/upsert",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinanceAccountingSetting | None:
    if response.status_code == 200:
        response_200 = FinanceAccountingSetting.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FinanceAccountingSetting]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset = UNSET,
) -> Response[FinanceAccountingSetting]:
    """Upserts an Accounting setting

     Upserts an Accounting setting

    Args:
        body (PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceAccountingSetting]
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
    body: PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset = UNSET,
) -> FinanceAccountingSetting | None:
    """Upserts an Accounting setting

     Upserts an Accounting setting

    Args:
        body (PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceAccountingSetting
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset = UNSET,
) -> Response[FinanceAccountingSetting]:
    """Upserts an Accounting setting

     Upserts an Accounting setting

    Args:
        body (PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceAccountingSetting]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset = UNSET,
) -> FinanceAccountingSetting | None:
    """Upserts an Accounting setting

     Upserts an Accounting setting

    Args:
        body (PostApi20260701ResourcesFinanceAccountingSettingsUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceAccountingSetting
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
