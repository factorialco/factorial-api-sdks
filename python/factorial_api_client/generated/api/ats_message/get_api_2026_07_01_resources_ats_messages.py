from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_ats_messages_response_200 import (
    GetApi20260701ResourcesAtsMessagesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    ats_conversation_id: str | Unset = UNSET,
    ats_conversation_ids: list[str] | Unset = UNSET,
    last_per_conversation: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["ats_conversation_id"] = ats_conversation_id

    json_ats_conversation_ids: list[str] | Unset = UNSET
    if not isinstance(ats_conversation_ids, Unset):
        json_ats_conversation_ids = ats_conversation_ids

    params["ats_conversation_ids[]"] = json_ats_conversation_ids

    params["last_per_conversation"] = last_per_conversation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/ats/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesAtsMessagesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesAtsMessagesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesAtsMessagesResponse200]:
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
    ids: list[str] | Unset = UNSET,
    ats_conversation_id: str | Unset = UNSET,
    ats_conversation_ids: list[str] | Unset = UNSET,
    last_per_conversation: bool,
) -> Response[GetApi20260701ResourcesAtsMessagesResponse200]:
    """Reads all Messages

     Reads all Messages

    Args:
        id (str | Unset):
        ids (list[str] | Unset):
        ats_conversation_id (str | Unset):
        ats_conversation_ids (list[str] | Unset):
        last_per_conversation (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAtsMessagesResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        ids=ids,
        ats_conversation_id=ats_conversation_id,
        ats_conversation_ids=ats_conversation_ids,
        last_per_conversation=last_per_conversation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    ats_conversation_id: str | Unset = UNSET,
    ats_conversation_ids: list[str] | Unset = UNSET,
    last_per_conversation: bool,
) -> GetApi20260701ResourcesAtsMessagesResponse200 | None:
    """Reads all Messages

     Reads all Messages

    Args:
        id (str | Unset):
        ids (list[str] | Unset):
        ats_conversation_id (str | Unset):
        ats_conversation_ids (list[str] | Unset):
        last_per_conversation (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAtsMessagesResponse200
    """

    return sync_detailed(
        client=client,
        id=id,
        ids=ids,
        ats_conversation_id=ats_conversation_id,
        ats_conversation_ids=ats_conversation_ids,
        last_per_conversation=last_per_conversation,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    ats_conversation_id: str | Unset = UNSET,
    ats_conversation_ids: list[str] | Unset = UNSET,
    last_per_conversation: bool,
) -> Response[GetApi20260701ResourcesAtsMessagesResponse200]:
    """Reads all Messages

     Reads all Messages

    Args:
        id (str | Unset):
        ids (list[str] | Unset):
        ats_conversation_id (str | Unset):
        ats_conversation_ids (list[str] | Unset):
        last_per_conversation (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesAtsMessagesResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        ids=ids,
        ats_conversation_id=ats_conversation_id,
        ats_conversation_ids=ats_conversation_ids,
        last_per_conversation=last_per_conversation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    ats_conversation_id: str | Unset = UNSET,
    ats_conversation_ids: list[str] | Unset = UNSET,
    last_per_conversation: bool,
) -> GetApi20260701ResourcesAtsMessagesResponse200 | None:
    """Reads all Messages

     Reads all Messages

    Args:
        id (str | Unset):
        ids (list[str] | Unset):
        ats_conversation_id (str | Unset):
        ats_conversation_ids (list[str] | Unset):
        last_per_conversation (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesAtsMessagesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            ids=ids,
            ats_conversation_id=ats_conversation_id,
            ats_conversation_ids=ats_conversation_ids,
            last_per_conversation=last_per_conversation,
        )
    ).parsed
