from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_expenses_per_diems_response_200 import (
    GetApi20260401ResourcesExpensesPerDiemsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    exclude_drafts: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_expenses_expensable_ids: list[int] | Unset = UNSET
    if not isinstance(expenses_expensable_ids, Unset):
        json_expenses_expensable_ids = expenses_expensable_ids

    params["expenses_expensable_ids[]"] = json_expenses_expensable_ids

    params["exclude_drafts"] = exclude_drafts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/expenses/per_diems",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesExpensesPerDiemsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesExpensesPerDiemsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesExpensesPerDiemsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    exclude_drafts: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesExpensesPerDiemsResponse200]:
    """Reads all Per diems

     Reads all Per diems

    Args:
        ids (list[int] | Unset): The IDs of the per diem to read. Example: [1, 2].
        expenses_expensable_ids (list[int] | Unset): The IDs of the expensables to read per diems
            for. Example: [1, 2].
        exclude_drafts (bool | Unset): Whether to exclude drafts from the results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesExpensesPerDiemsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        expenses_expensable_ids=expenses_expensable_ids,
        exclude_drafts=exclude_drafts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    exclude_drafts: bool | Unset = UNSET,
) -> GetApi20260401ResourcesExpensesPerDiemsResponse200 | None:
    """Reads all Per diems

     Reads all Per diems

    Args:
        ids (list[int] | Unset): The IDs of the per diem to read. Example: [1, 2].
        expenses_expensable_ids (list[int] | Unset): The IDs of the expensables to read per diems
            for. Example: [1, 2].
        exclude_drafts (bool | Unset): Whether to exclude drafts from the results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesExpensesPerDiemsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        expenses_expensable_ids=expenses_expensable_ids,
        exclude_drafts=exclude_drafts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    exclude_drafts: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesExpensesPerDiemsResponse200]:
    """Reads all Per diems

     Reads all Per diems

    Args:
        ids (list[int] | Unset): The IDs of the per diem to read. Example: [1, 2].
        expenses_expensable_ids (list[int] | Unset): The IDs of the expensables to read per diems
            for. Example: [1, 2].
        exclude_drafts (bool | Unset): Whether to exclude drafts from the results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesExpensesPerDiemsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        expenses_expensable_ids=expenses_expensable_ids,
        exclude_drafts=exclude_drafts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    exclude_drafts: bool | Unset = UNSET,
) -> GetApi20260401ResourcesExpensesPerDiemsResponse200 | None:
    """Reads all Per diems

     Reads all Per diems

    Args:
        ids (list[int] | Unset): The IDs of the per diem to read. Example: [1, 2].
        expenses_expensable_ids (list[int] | Unset): The IDs of the expensables to read per diems
            for. Example: [1, 2].
        exclude_drafts (bool | Unset): Whether to exclude drafts from the results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesExpensesPerDiemsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            expenses_expensable_ids=expenses_expensable_ids,
            exclude_drafts=exclude_drafts,
        )
    ).parsed
