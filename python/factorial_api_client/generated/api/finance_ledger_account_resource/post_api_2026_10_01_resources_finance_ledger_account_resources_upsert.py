from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finance_ledger_account_resource import FinanceLedgerAccountResource
from ...models.post_api_20261001_resources_finance_ledger_account_resources_upsert_body import (
    PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-10-01/resources/finance/ledger_account_resources/upsert",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinanceLedgerAccountResource | None:
    if response.status_code == 200:
        response_200 = FinanceLedgerAccountResource.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FinanceLedgerAccountResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset = UNSET,
) -> Response[FinanceLedgerAccountResource]:
    """Upserts a Ledger account resource

     Create or update a ledger account resource.

    Args:
        body (PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceLedgerAccountResource]
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
    body: PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset = UNSET,
) -> FinanceLedgerAccountResource | None:
    """Upserts a Ledger account resource

     Create or update a ledger account resource.

    Args:
        body (PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceLedgerAccountResource
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset = UNSET,
) -> Response[FinanceLedgerAccountResource]:
    """Upserts a Ledger account resource

     Create or update a ledger account resource.

    Args:
        body (PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceLedgerAccountResource]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset = UNSET,
) -> FinanceLedgerAccountResource | None:
    """Upserts a Ledger account resource

     Create or update a ledger account resource.

    Args:
        body (PostApi20261001ResourcesFinanceLedgerAccountResourcesUpsertBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceLedgerAccountResource
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
