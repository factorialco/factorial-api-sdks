from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finance_journal_entry import FinanceJournalEntry
from ...models.post_api_20260401_resources_finance_journal_entries_body import (
    PostApi20260401ResourcesFinanceJournalEntriesBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesFinanceJournalEntriesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/finance/journal_entries",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinanceJournalEntry | None:
    if response.status_code == 201:
        response_201 = FinanceJournalEntry.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FinanceJournalEntry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesFinanceJournalEntriesBody | Unset = UNSET,
) -> Response[FinanceJournalEntry]:
    """Creates a Journal entry

     Creates a Journal entry

    Args:
        body (PostApi20260401ResourcesFinanceJournalEntriesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceJournalEntry]
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
    body: PostApi20260401ResourcesFinanceJournalEntriesBody | Unset = UNSET,
) -> FinanceJournalEntry | None:
    """Creates a Journal entry

     Creates a Journal entry

    Args:
        body (PostApi20260401ResourcesFinanceJournalEntriesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceJournalEntry
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesFinanceJournalEntriesBody | Unset = UNSET,
) -> Response[FinanceJournalEntry]:
    """Creates a Journal entry

     Creates a Journal entry

    Args:
        body (PostApi20260401ResourcesFinanceJournalEntriesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinanceJournalEntry]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesFinanceJournalEntriesBody | Unset = UNSET,
) -> FinanceJournalEntry | None:
    """Creates a Journal entry

     Creates a Journal entry

    Args:
        body (PostApi20260401ResourcesFinanceJournalEntriesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinanceJournalEntry
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
