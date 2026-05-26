from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.posts_post import PostsPost
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/posts/posts/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostsPost | None:
    if response.status_code == 200:
        response_200 = PostsPost.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostsPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PostsPost]:
    """Reads a single Post

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostsPost]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> PostsPost | None:
    """Reads a single Post

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostsPost
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PostsPost]:
    """Reads a single Post

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostsPost]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> PostsPost | None:
    """Reads a single Post

     ###### **What does it do?**
    These endpoints allow you to retrieve posts of a community
    ###### **What can you do with groups?**
    Increase visibility and communication within the company by creating interaction and community
    within your company.
    ###### **Who can use it?**
    For having this funcionality available, you need to have Communities V2 feature available

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostsPost
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
