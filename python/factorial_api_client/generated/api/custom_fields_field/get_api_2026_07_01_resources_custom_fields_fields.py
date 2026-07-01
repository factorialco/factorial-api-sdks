from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_custom_fields_fields_field_type import (
    GetApi20260701ResourcesCustomFieldsFieldsFieldType,
)
from ...models.get_api_20260701_resources_custom_fields_fields_response_200 import (
    GetApi20260701ResourcesCustomFieldsFieldsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    field_type: GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset = UNSET,
    label: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_field_type: str | Unset = UNSET
    if not isinstance(field_type, Unset):
        json_field_type = field_type.value

    params["field_type"] = json_field_type

    params["label"] = label

    params["slug"] = slug

    params["company_id"] = company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/custom_fields/fields",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesCustomFieldsFieldsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesCustomFieldsFieldsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesCustomFieldsFieldsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    field_type: GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset = UNSET,
    label: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesCustomFieldsFieldsResponse200]:
    """Reads all Fields

     Reads all Fields

    Args:
        ids (list[str] | Unset): Field identifiers Example: ['1', '2'].
        field_type (GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset): Filter fields by
            type Example: text.
        label (str | Unset): Field label Example: T-Shirt Size.
        slug (str | Unset): Custom field slug Example: tshirt_size.
        company_id (str | Unset): Company identifier where this field belongs Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesCustomFieldsFieldsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        field_type=field_type,
        label=label,
        slug=slug,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    field_type: GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset = UNSET,
    label: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> GetApi20260701ResourcesCustomFieldsFieldsResponse200 | None:
    """Reads all Fields

     Reads all Fields

    Args:
        ids (list[str] | Unset): Field identifiers Example: ['1', '2'].
        field_type (GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset): Filter fields by
            type Example: text.
        label (str | Unset): Field label Example: T-Shirt Size.
        slug (str | Unset): Custom field slug Example: tshirt_size.
        company_id (str | Unset): Company identifier where this field belongs Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesCustomFieldsFieldsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        field_type=field_type,
        label=label,
        slug=slug,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    field_type: GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset = UNSET,
    label: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesCustomFieldsFieldsResponse200]:
    """Reads all Fields

     Reads all Fields

    Args:
        ids (list[str] | Unset): Field identifiers Example: ['1', '2'].
        field_type (GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset): Filter fields by
            type Example: text.
        label (str | Unset): Field label Example: T-Shirt Size.
        slug (str | Unset): Custom field slug Example: tshirt_size.
        company_id (str | Unset): Company identifier where this field belongs Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesCustomFieldsFieldsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        field_type=field_type,
        label=label,
        slug=slug,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    field_type: GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset = UNSET,
    label: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> GetApi20260701ResourcesCustomFieldsFieldsResponse200 | None:
    """Reads all Fields

     Reads all Fields

    Args:
        ids (list[str] | Unset): Field identifiers Example: ['1', '2'].
        field_type (GetApi20260701ResourcesCustomFieldsFieldsFieldType | Unset): Filter fields by
            type Example: text.
        label (str | Unset): Field label Example: T-Shirt Size.
        slug (str | Unset): Custom field slug Example: tshirt_size.
        company_id (str | Unset): Company identifier where this field belongs Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesCustomFieldsFieldsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            field_type=field_type,
            label=label,
            slug=slug,
            company_id=company_id,
        )
    ).parsed
