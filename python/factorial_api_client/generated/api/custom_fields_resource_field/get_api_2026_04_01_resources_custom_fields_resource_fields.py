from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_custom_fields_resource_fields_response_200 import (
    GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    field_ids: list[int] | Unset = UNSET,
    schema_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_field_ids: list[int] | Unset = UNSET
    if not isinstance(field_ids, Unset):
        json_field_ids = field_ids

    params["field_ids[]"] = json_field_ids

    json_schema_ids: list[int] | Unset = UNSET
    if not isinstance(schema_ids, Unset):
        json_schema_ids = schema_ids

    params["schema_ids[]"] = json_schema_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/custom_fields/resource_fields",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200]:
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
    field_ids: list[int] | Unset = UNSET,
    schema_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200]:
    """Reads all Resource fields

     Reads schema custom fields

    Args:
        ids (list[int] | Unset): Resource field identifiers Example: [1].
        field_ids (list[int] | Unset): Custom Field identifiers Example: [2].
        schema_ids (list[int] | Unset): Custom Resources Schema identifiers Example: [1, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        field_ids=field_ids,
        schema_ids=schema_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    field_ids: list[int] | Unset = UNSET,
    schema_ids: list[int] | Unset = UNSET,
) -> GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200 | None:
    """Reads all Resource fields

     Reads schema custom fields

    Args:
        ids (list[int] | Unset): Resource field identifiers Example: [1].
        field_ids (list[int] | Unset): Custom Field identifiers Example: [2].
        schema_ids (list[int] | Unset): Custom Resources Schema identifiers Example: [1, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        field_ids=field_ids,
        schema_ids=schema_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    field_ids: list[int] | Unset = UNSET,
    schema_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200]:
    """Reads all Resource fields

     Reads schema custom fields

    Args:
        ids (list[int] | Unset): Resource field identifiers Example: [1].
        field_ids (list[int] | Unset): Custom Field identifiers Example: [2].
        schema_ids (list[int] | Unset): Custom Resources Schema identifiers Example: [1, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        field_ids=field_ids,
        schema_ids=schema_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    field_ids: list[int] | Unset = UNSET,
    schema_ids: list[int] | Unset = UNSET,
) -> GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200 | None:
    """Reads all Resource fields

     Reads schema custom fields

    Args:
        ids (list[int] | Unset): Resource field identifiers Example: [1].
        field_ids (list[int] | Unset): Custom Field identifiers Example: [2].
        schema_ids (list[int] | Unset): Custom Resources Schema identifiers Example: [1, 3].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesCustomFieldsResourceFieldsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            field_ids=field_ids,
            schema_ids=schema_ids,
        )
    ).parsed
