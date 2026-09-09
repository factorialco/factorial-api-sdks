from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_timeoff_leave_types_response_200 import (
    GetApi20261001ResourcesTimeoffLeaveTypesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
    payable: bool | Unset = UNSET,
    identifier: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    reference_date: str | Unset = UNSET,
    leave_type_id: str | Unset = UNSET,
    allow_endless: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_company_ids: list[str] | Unset = UNSET
    if not isinstance(company_ids, Unset):
        json_company_ids = company_ids

    params["company_ids[]"] = json_company_ids

    params["active"] = active

    params["payable"] = payable

    params["identifier"] = identifier

    params["employee_id"] = employee_id

    params["reference_date"] = reference_date

    params["leave_type_id"] = leave_type_id

    params["allow_endless"] = allow_endless

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/timeoff/leave_types",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesTimeoffLeaveTypesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesTimeoffLeaveTypesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesTimeoffLeaveTypesResponse200]:
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
    company_ids: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
    payable: bool | Unset = UNSET,
    identifier: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    reference_date: str | Unset = UNSET,
    leave_type_id: str | Unset = UNSET,
    allow_endless: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTimeoffLeaveTypesResponse200]:
    """Reads all Leave types

     Reads all Leave types

    Args:
        ids (list[str] | Unset): Identifiers of the leave types Example: ['1', '2'].
        company_ids (list[str] | Unset): Identifiers of the companies Example: ['1', '2'].
        active (bool | Unset): Whether the leave type is active Example: True.
        payable (bool | Unset): Whether the leave type is payable
        identifier (str | Unset): A unique identifier for the leave type, or an array of
            identifiers Example: ['holiday'].
        employee_id (str | Unset): Identifier of the employee Example: 1.
        reference_date (str | Unset): A reference date for the leave type Example: 2024-08-22.
        leave_type_id (str | Unset): Identifier of a specific leave type Example: 1.
        allow_endless (bool | Unset): Whether the leave type allows for no end date Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTimeoffLeaveTypesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_ids=company_ids,
        active=active,
        payable=payable,
        identifier=identifier,
        employee_id=employee_id,
        reference_date=reference_date,
        leave_type_id=leave_type_id,
        allow_endless=allow_endless,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
    payable: bool | Unset = UNSET,
    identifier: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    reference_date: str | Unset = UNSET,
    leave_type_id: str | Unset = UNSET,
    allow_endless: bool | Unset = UNSET,
) -> GetApi20261001ResourcesTimeoffLeaveTypesResponse200 | None:
    """Reads all Leave types

     Reads all Leave types

    Args:
        ids (list[str] | Unset): Identifiers of the leave types Example: ['1', '2'].
        company_ids (list[str] | Unset): Identifiers of the companies Example: ['1', '2'].
        active (bool | Unset): Whether the leave type is active Example: True.
        payable (bool | Unset): Whether the leave type is payable
        identifier (str | Unset): A unique identifier for the leave type, or an array of
            identifiers Example: ['holiday'].
        employee_id (str | Unset): Identifier of the employee Example: 1.
        reference_date (str | Unset): A reference date for the leave type Example: 2024-08-22.
        leave_type_id (str | Unset): Identifier of a specific leave type Example: 1.
        allow_endless (bool | Unset): Whether the leave type allows for no end date Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTimeoffLeaveTypesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_ids=company_ids,
        active=active,
        payable=payable,
        identifier=identifier,
        employee_id=employee_id,
        reference_date=reference_date,
        leave_type_id=leave_type_id,
        allow_endless=allow_endless,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
    payable: bool | Unset = UNSET,
    identifier: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    reference_date: str | Unset = UNSET,
    leave_type_id: str | Unset = UNSET,
    allow_endless: bool | Unset = UNSET,
) -> Response[GetApi20261001ResourcesTimeoffLeaveTypesResponse200]:
    """Reads all Leave types

     Reads all Leave types

    Args:
        ids (list[str] | Unset): Identifiers of the leave types Example: ['1', '2'].
        company_ids (list[str] | Unset): Identifiers of the companies Example: ['1', '2'].
        active (bool | Unset): Whether the leave type is active Example: True.
        payable (bool | Unset): Whether the leave type is payable
        identifier (str | Unset): A unique identifier for the leave type, or an array of
            identifiers Example: ['holiday'].
        employee_id (str | Unset): Identifier of the employee Example: 1.
        reference_date (str | Unset): A reference date for the leave type Example: 2024-08-22.
        leave_type_id (str | Unset): Identifier of a specific leave type Example: 1.
        allow_endless (bool | Unset): Whether the leave type allows for no end date Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesTimeoffLeaveTypesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_ids=company_ids,
        active=active,
        payable=payable,
        identifier=identifier,
        employee_id=employee_id,
        reference_date=reference_date,
        leave_type_id=leave_type_id,
        allow_endless=allow_endless,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
    payable: bool | Unset = UNSET,
    identifier: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    reference_date: str | Unset = UNSET,
    leave_type_id: str | Unset = UNSET,
    allow_endless: bool | Unset = UNSET,
) -> GetApi20261001ResourcesTimeoffLeaveTypesResponse200 | None:
    """Reads all Leave types

     Reads all Leave types

    Args:
        ids (list[str] | Unset): Identifiers of the leave types Example: ['1', '2'].
        company_ids (list[str] | Unset): Identifiers of the companies Example: ['1', '2'].
        active (bool | Unset): Whether the leave type is active Example: True.
        payable (bool | Unset): Whether the leave type is payable
        identifier (str | Unset): A unique identifier for the leave type, or an array of
            identifiers Example: ['holiday'].
        employee_id (str | Unset): Identifier of the employee Example: 1.
        reference_date (str | Unset): A reference date for the leave type Example: 2024-08-22.
        leave_type_id (str | Unset): Identifier of a specific leave type Example: 1.
        allow_endless (bool | Unset): Whether the leave type allows for no end date Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesTimeoffLeaveTypesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_ids=company_ids,
            active=active,
            payable=payable,
            identifier=identifier,
            employee_id=employee_id,
            reference_date=reference_date,
            leave_type_id=leave_type_id,
            allow_endless=allow_endless,
        )
    ).parsed
