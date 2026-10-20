from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_ats_messages_response_200 import (
    GetApi20270101ResourcesAtsMessagesResponse200,
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
        "url": "/api/2027-01-01/resources/ats/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesAtsMessagesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200]:
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
) -> Response[ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200]:
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
        Response[ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200]
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
) -> ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200 | None:
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
        ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200
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
) -> Response[ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200]:
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
        Response[ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200]
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
) -> ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200 | None:
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
        ErrorResponse | GetApi20270101ResourcesAtsMessagesResponse200
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
