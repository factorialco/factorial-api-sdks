from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_posts_posts_response_200 import (
    GetApi20260701ResourcesPostsPostsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    groups: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_groups: list[str] | Unset = UNSET
    if not isinstance(groups, Unset):
        json_groups = groups

    params["groups[]"] = json_groups

    params["from"] = from_

    params["until"] = until

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/posts/posts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesPostsPostsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesPostsPostsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesPostsPostsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    groups: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesPostsPostsResponse200]:
    """Reads all Posts

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        groups (list[str] | Unset): group identifiers of the posts Example: ['1', '2', '3'].
        from_ (str | Unset): date from which posts will be retrieved Example: 2024-05-02.
        until (str | Unset): date until which the posts will be retrieved Example: 2024-08-01.
        ids (list[str] | Unset): identifiers of the post Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesPostsPostsResponse200]
    """

    kwargs = _get_kwargs(
        groups=groups,
        from_=from_,
        until=until,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    groups: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesPostsPostsResponse200 | None:
    """Reads all Posts

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        groups (list[str] | Unset): group identifiers of the posts Example: ['1', '2', '3'].
        from_ (str | Unset): date from which posts will be retrieved Example: 2024-05-02.
        until (str | Unset): date until which the posts will be retrieved Example: 2024-08-01.
        ids (list[str] | Unset): identifiers of the post Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesPostsPostsResponse200
    """

    return sync_detailed(
        client=client,
        groups=groups,
        from_=from_,
        until=until,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    groups: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesPostsPostsResponse200]:
    """Reads all Posts

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        groups (list[str] | Unset): group identifiers of the posts Example: ['1', '2', '3'].
        from_ (str | Unset): date from which posts will be retrieved Example: 2024-05-02.
        until (str | Unset): date until which the posts will be retrieved Example: 2024-08-01.
        ids (list[str] | Unset): identifiers of the post Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesPostsPostsResponse200]
    """

    kwargs = _get_kwargs(
        groups=groups,
        from_=from_,
        until=until,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    groups: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesPostsPostsResponse200 | None:
    """Reads all Posts

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        groups (list[str] | Unset): group identifiers of the posts Example: ['1', '2', '3'].
        from_ (str | Unset): date from which posts will be retrieved Example: 2024-05-02.
        until (str | Unset): date until which the posts will be retrieved Example: 2024-08-01.
        ids (list[str] | Unset): identifiers of the post Example: ['1', '2', '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesPostsPostsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            groups=groups,
            from_=from_,
            until=until,
            ids=ids,
        )
    ).parsed
