from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_fields_resource_field import CustomFieldsResourceField
from ...models.post_api_20251001_resources_custom_fields_resource_fields_body import (
    PostApi20251001ResourcesCustomFieldsResourceFieldsBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/custom_fields/resource_fields",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldsResourceField | None:
    if response.status_code == 201:
        response_201 = CustomFieldsResourceField.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldsResourceField]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset = UNSET,
) -> Response[CustomFieldsResourceField]:
    """Creates a Resource field

     Creates an schema custom field

    Args:
        body (PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsResourceField]
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
    body: PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset = UNSET,
) -> CustomFieldsResourceField | None:
    """Creates a Resource field

     Creates an schema custom field

    Args:
        body (PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsResourceField
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset = UNSET,
) -> Response[CustomFieldsResourceField]:
    """Creates a Resource field

     Creates an schema custom field

    Args:
        body (PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsResourceField]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset = UNSET,
) -> CustomFieldsResourceField | None:
    """Creates a Resource field

     Creates an schema custom field

    Args:
        body (PostApi20251001ResourcesCustomFieldsResourceFieldsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsResourceField
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
