from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_api_public_webhook_subscriptions_response_200 import (
    GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["company_id"] = company_id

    params["type"] = type_

    params["enabled"] = enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/api_public/webhook_subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200]:
    """Reads all Webhook subscriptions

     Reads all Webhook subscriptions

    Args:
        id (str | Unset): Identifier of the webhook subscription Example: 1.
        company_id (str | Unset): Company identifier of the webhook subscription Example: 1.
        type_ (str | Unset): Type of the webhook subscription Example: ats/job_posting/create.
        enabled (bool | Unset): List only enabled webhook subscriptions Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        company_id=company_id,
        type_=type_,
        enabled=enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200 | None:
    """Reads all Webhook subscriptions

     Reads all Webhook subscriptions

    Args:
        id (str | Unset): Identifier of the webhook subscription Example: 1.
        company_id (str | Unset): Company identifier of the webhook subscription Example: 1.
        type_ (str | Unset): Type of the webhook subscription Example: ats/job_posting/create.
        enabled (bool | Unset): List only enabled webhook subscriptions Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200
    """

    return sync_detailed(
        client=client,
        id=id,
        company_id=company_id,
        type_=type_,
        enabled=enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200]:
    """Reads all Webhook subscriptions

     Reads all Webhook subscriptions

    Args:
        id (str | Unset): Identifier of the webhook subscription Example: 1.
        company_id (str | Unset): Company identifier of the webhook subscription Example: 1.
        type_ (str | Unset): Type of the webhook subscription Example: ats/job_posting/create.
        enabled (bool | Unset): List only enabled webhook subscriptions Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        company_id=company_id,
        type_=type_,
        enabled=enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200 | None:
    """Reads all Webhook subscriptions

     Reads all Webhook subscriptions

    Args:
        id (str | Unset): Identifier of the webhook subscription Example: 1.
        company_id (str | Unset): Company identifier of the webhook subscription Example: 1.
        type_ (str | Unset): Type of the webhook subscription Example: ats/job_posting/create.
        enabled (bool | Unset): List only enabled webhook subscriptions Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesApiPublicWebhookSubscriptionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            company_id=company_id,
            type_=type_,
            enabled=enabled,
        )
    ).parsed
