from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_custom_fields_values_response_200 import (
    GetApi20270101ResourcesCustomFieldsValuesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employee_ids: list[str] | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    value: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    field_id: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_identifiers: list[str] | Unset = UNSET
    if not isinstance(identifiers, Unset):
        json_identifiers = identifiers

    params["identifiers[]"] = json_identifiers

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["instance_id"] = instance_id

    params["value"] = value

    params["slug"] = slug

    params["field_id"] = field_id

    params["updated_at_gteq"] = updated_at_gteq

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/custom_fields/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesCustomFieldsValuesResponse200.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    value: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    field_id: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200]:
    """Reads all Values

     Reads all Values

    Args:
        employee_ids (list[str] | Unset): Employee identifiers to filter custom field values by
            Example: ['18'].
        identifiers (list[str] | Unset): Custom field to filter by identifier Example:
            ['01f931507aa27e1168025e27cd46b8588435b741'].
        ids (list[str] | Unset): Custom field value identifiers to filter by Example: ['73'].
        instance_id (str | Unset): Identifier of the instance that the custom field value is
            attached to Example: 18.
        value (str | Unset): Custom field value to filter by Example: 1235436.
        slug (str | Unset): Custom field slug to filter by Example: matricule.
        field_id (str | Unset): Custom field identifier to filter by Example: 75.
        updated_at_gteq (str | Unset): Filter values updated on or after this date (ISO 8601
            format). Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        identifiers=identifiers,
        ids=ids,
        instance_id=instance_id,
        value=value,
        slug=slug,
        field_id=field_id,
        updated_at_gteq=updated_at_gteq,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    value: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    field_id: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200 | None:
    """Reads all Values

     Reads all Values

    Args:
        employee_ids (list[str] | Unset): Employee identifiers to filter custom field values by
            Example: ['18'].
        identifiers (list[str] | Unset): Custom field to filter by identifier Example:
            ['01f931507aa27e1168025e27cd46b8588435b741'].
        ids (list[str] | Unset): Custom field value identifiers to filter by Example: ['73'].
        instance_id (str | Unset): Identifier of the instance that the custom field value is
            attached to Example: 18.
        value (str | Unset): Custom field value to filter by Example: 1235436.
        slug (str | Unset): Custom field slug to filter by Example: matricule.
        field_id (str | Unset): Custom field identifier to filter by Example: 75.
        updated_at_gteq (str | Unset): Filter values updated on or after this date (ISO 8601
            format). Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
        identifiers=identifiers,
        ids=ids,
        instance_id=instance_id,
        value=value,
        slug=slug,
        field_id=field_id,
        updated_at_gteq=updated_at_gteq,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    value: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    field_id: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200]:
    """Reads all Values

     Reads all Values

    Args:
        employee_ids (list[str] | Unset): Employee identifiers to filter custom field values by
            Example: ['18'].
        identifiers (list[str] | Unset): Custom field to filter by identifier Example:
            ['01f931507aa27e1168025e27cd46b8588435b741'].
        ids (list[str] | Unset): Custom field value identifiers to filter by Example: ['73'].
        instance_id (str | Unset): Identifier of the instance that the custom field value is
            attached to Example: 18.
        value (str | Unset): Custom field value to filter by Example: 1235436.
        slug (str | Unset): Custom field slug to filter by Example: matricule.
        field_id (str | Unset): Custom field identifier to filter by Example: 75.
        updated_at_gteq (str | Unset): Filter values updated on or after this date (ISO 8601
            format). Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        identifiers=identifiers,
        ids=ids,
        instance_id=instance_id,
        value=value,
        slug=slug,
        field_id=field_id,
        updated_at_gteq=updated_at_gteq,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str] | Unset = UNSET,
    identifiers: list[str] | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    value: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    field_id: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200 | None:
    """Reads all Values

     Reads all Values

    Args:
        employee_ids (list[str] | Unset): Employee identifiers to filter custom field values by
            Example: ['18'].
        identifiers (list[str] | Unset): Custom field to filter by identifier Example:
            ['01f931507aa27e1168025e27cd46b8588435b741'].
        ids (list[str] | Unset): Custom field value identifiers to filter by Example: ['73'].
        instance_id (str | Unset): Identifier of the instance that the custom field value is
            attached to Example: 18.
        value (str | Unset): Custom field value to filter by Example: 1235436.
        slug (str | Unset): Custom field slug to filter by Example: matricule.
        field_id (str | Unset): Custom field identifier to filter by Example: 75.
        updated_at_gteq (str | Unset): Filter values updated on or after this date (ISO 8601
            format). Example: 2024-10-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesCustomFieldsValuesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
            identifiers=identifiers,
            ids=ids,
            instance_id=instance_id,
            value=value,
            slug=slug,
            field_id=field_id,
            updated_at_gteq=updated_at_gteq,
        )
    ).parsed
