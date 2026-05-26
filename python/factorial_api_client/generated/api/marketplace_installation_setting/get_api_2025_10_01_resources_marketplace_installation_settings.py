from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_marketplace_installation_settings_response_200 import (
    GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    company_id: int,
    integration_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["company_id"] = company_id

    params["integration_id"] = integration_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/marketplace/installation_settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    company_id: int,
    integration_id: str,
) -> Response[GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200]:
    """Reads all Installation settings

     Reads all Installation settings

    Args:
        company_id (int): Identifier of the company Example: 1.
        integration_id (str): ID of the integration Example: Y0h_Sh7pRxCWpl0DySn_uQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        integration_id=integration_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    company_id: int,
    integration_id: str,
) -> GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200 | None:
    """Reads all Installation settings

     Reads all Installation settings

    Args:
        company_id (int): Identifier of the company Example: 1.
        integration_id (str): ID of the integration Example: Y0h_Sh7pRxCWpl0DySn_uQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200
    """

    return sync_detailed(
        client=client,
        company_id=company_id,
        integration_id=integration_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    company_id: int,
    integration_id: str,
) -> Response[GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200]:
    """Reads all Installation settings

     Reads all Installation settings

    Args:
        company_id (int): Identifier of the company Example: 1.
        integration_id (str): ID of the integration Example: Y0h_Sh7pRxCWpl0DySn_uQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        integration_id=integration_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    company_id: int,
    integration_id: str,
) -> GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200 | None:
    """Reads all Installation settings

     Reads all Installation settings

    Args:
        company_id (int): Identifier of the company Example: 1.
        integration_id (str): ID of the integration Example: Y0h_Sh7pRxCWpl0DySn_uQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesMarketplaceInstallationSettingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            company_id=company_id,
            integration_id=integration_id,
        )
    ).parsed
