from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_public_webhook_subscription import ApiPublicWebhookSubscription
from ...models.post_api_20260701_resources_api_public_webhook_subscriptions_body import (
    PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/api_public/webhook_subscriptions",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiPublicWebhookSubscription | None:
    if response.status_code == 201:
        response_201 = ApiPublicWebhookSubscription.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiPublicWebhookSubscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset = UNSET,
) -> Response[ApiPublicWebhookSubscription]:
    """Creates a Webhook subscription

     Creates a Webhook subscription

    Args:
        body (PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPublicWebhookSubscription]
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
    body: PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset = UNSET,
) -> ApiPublicWebhookSubscription | None:
    """Creates a Webhook subscription

     Creates a Webhook subscription

    Args:
        body (PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPublicWebhookSubscription
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset = UNSET,
) -> Response[ApiPublicWebhookSubscription]:
    """Creates a Webhook subscription

     Creates a Webhook subscription

    Args:
        body (PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPublicWebhookSubscription]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset = UNSET,
) -> ApiPublicWebhookSubscription | None:
    """Creates a Webhook subscription

     Creates a Webhook subscription

    Args:
        body (PostApi20260701ResourcesApiPublicWebhookSubscriptionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPublicWebhookSubscription
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
