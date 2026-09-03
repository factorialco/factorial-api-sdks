from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_bookkeepers_management_incidences_response_200 import (
    GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    search: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    contains_message: bool | Unset = UNSET,
    message_from: str | Unset = UNSET,
    custom_leave_name: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_legal_entities_ids: list[str] | Unset = UNSET
    if not isinstance(legal_entities_ids, Unset):
        json_legal_entities_ids = legal_entities_ids

    params["legal_entities_ids[]"] = json_legal_entities_ids

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status[]"] = json_status

    params["starts_on"] = starts_on

    params["ends_on"] = ends_on

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type[]"] = json_type_

    params["sort_by"] = sort_by

    params["direction"] = direction

    params["search"] = search

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["contains_message"] = contains_message

    params["message_from"] = message_from

    json_custom_leave_name: list[str] | Unset = UNSET
    if not isinstance(custom_leave_name, Unset):
        json_custom_leave_name = custom_leave_name

    params["custom_leave_name[]"] = json_custom_leave_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/bookkeepers_management/incidences",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200]:
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
    legal_entities_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    search: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    contains_message: bool | Unset = UNSET,
    message_from: str | Unset = UNSET,
    custom_leave_name: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200]:
    """Reads all Incidences

     Reads all Incidences

    Args:
        ids (list[str] | Unset): A list of incidence identifiers. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): A list of legal entities identifiers. Example:
            ['1', '2', '3'].
        status (list[str] | Unset): A list of statuses. Example: ['in-preparation', 'to-do',
            'doing', 'done', 'discarded'].
        starts_on (str | Unset): Get the incidence (aka employee update) that start safter this
            date (included). Example: 2020-01-01.
        ends_on (str | Unset): Get the incidence (aka employee update) that ends before this date
            (included). Example: 2020-01-01.
        type_ (list[str] | Unset): A list of types. It can be any of the following address, bank,
            cost_center, contract, gender, health_insurance, hiring, id, irpf, legal_entity,
            manual_incidence, name, nationality, parental, permits_and_certificates, phone_number,
            sick, tax_id, taxes_and_deductions, termination, work_activity, workplace Example:
            ['hiring', 'workplace'].
        sort_by (str | Unset): Field to sort by. It can be any of the following
            employee_first_name, employee_last_name, type, legal_entity_name, effective_date, status,
            created_at. Example: effective_date.
        direction (str | Unset): Sort direction. It can be 'asc' or 'desc'. Example: desc.
        search (str | Unset): Filter the result by the name of the employee. Example: Hellen.
        employee_ids (list[str] | Unset): A list of employee identifiers. Example: ['1', '2',
            '3'].
        contains_message (bool | Unset): Boolean that filters incidences that does or does not
            contains messages. Example: True.
        message_from (str | Unset): Filter by message sender. Example: bookkeeper.
        custom_leave_name (list[str] | Unset): A list of custom leave names. Example: ['Medical
            Leave', 'Paternity Leave'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        legal_entities_ids=legal_entities_ids,
        status=status,
        starts_on=starts_on,
        ends_on=ends_on,
        type_=type_,
        sort_by=sort_by,
        direction=direction,
        search=search,
        employee_ids=employee_ids,
        contains_message=contains_message,
        message_from=message_from,
        custom_leave_name=custom_leave_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    search: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    contains_message: bool | Unset = UNSET,
    message_from: str | Unset = UNSET,
    custom_leave_name: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200 | None:
    """Reads all Incidences

     Reads all Incidences

    Args:
        ids (list[str] | Unset): A list of incidence identifiers. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): A list of legal entities identifiers. Example:
            ['1', '2', '3'].
        status (list[str] | Unset): A list of statuses. Example: ['in-preparation', 'to-do',
            'doing', 'done', 'discarded'].
        starts_on (str | Unset): Get the incidence (aka employee update) that start safter this
            date (included). Example: 2020-01-01.
        ends_on (str | Unset): Get the incidence (aka employee update) that ends before this date
            (included). Example: 2020-01-01.
        type_ (list[str] | Unset): A list of types. It can be any of the following address, bank,
            cost_center, contract, gender, health_insurance, hiring, id, irpf, legal_entity,
            manual_incidence, name, nationality, parental, permits_and_certificates, phone_number,
            sick, tax_id, taxes_and_deductions, termination, work_activity, workplace Example:
            ['hiring', 'workplace'].
        sort_by (str | Unset): Field to sort by. It can be any of the following
            employee_first_name, employee_last_name, type, legal_entity_name, effective_date, status,
            created_at. Example: effective_date.
        direction (str | Unset): Sort direction. It can be 'asc' or 'desc'. Example: desc.
        search (str | Unset): Filter the result by the name of the employee. Example: Hellen.
        employee_ids (list[str] | Unset): A list of employee identifiers. Example: ['1', '2',
            '3'].
        contains_message (bool | Unset): Boolean that filters incidences that does or does not
            contains messages. Example: True.
        message_from (str | Unset): Filter by message sender. Example: bookkeeper.
        custom_leave_name (list[str] | Unset): A list of custom leave names. Example: ['Medical
            Leave', 'Paternity Leave'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        legal_entities_ids=legal_entities_ids,
        status=status,
        starts_on=starts_on,
        ends_on=ends_on,
        type_=type_,
        sort_by=sort_by,
        direction=direction,
        search=search,
        employee_ids=employee_ids,
        contains_message=contains_message,
        message_from=message_from,
        custom_leave_name=custom_leave_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    search: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    contains_message: bool | Unset = UNSET,
    message_from: str | Unset = UNSET,
    custom_leave_name: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200]:
    """Reads all Incidences

     Reads all Incidences

    Args:
        ids (list[str] | Unset): A list of incidence identifiers. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): A list of legal entities identifiers. Example:
            ['1', '2', '3'].
        status (list[str] | Unset): A list of statuses. Example: ['in-preparation', 'to-do',
            'doing', 'done', 'discarded'].
        starts_on (str | Unset): Get the incidence (aka employee update) that start safter this
            date (included). Example: 2020-01-01.
        ends_on (str | Unset): Get the incidence (aka employee update) that ends before this date
            (included). Example: 2020-01-01.
        type_ (list[str] | Unset): A list of types. It can be any of the following address, bank,
            cost_center, contract, gender, health_insurance, hiring, id, irpf, legal_entity,
            manual_incidence, name, nationality, parental, permits_and_certificates, phone_number,
            sick, tax_id, taxes_and_deductions, termination, work_activity, workplace Example:
            ['hiring', 'workplace'].
        sort_by (str | Unset): Field to sort by. It can be any of the following
            employee_first_name, employee_last_name, type, legal_entity_name, effective_date, status,
            created_at. Example: effective_date.
        direction (str | Unset): Sort direction. It can be 'asc' or 'desc'. Example: desc.
        search (str | Unset): Filter the result by the name of the employee. Example: Hellen.
        employee_ids (list[str] | Unset): A list of employee identifiers. Example: ['1', '2',
            '3'].
        contains_message (bool | Unset): Boolean that filters incidences that does or does not
            contains messages. Example: True.
        message_from (str | Unset): Filter by message sender. Example: bookkeeper.
        custom_leave_name (list[str] | Unset): A list of custom leave names. Example: ['Medical
            Leave', 'Paternity Leave'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        legal_entities_ids=legal_entities_ids,
        status=status,
        starts_on=starts_on,
        ends_on=ends_on,
        type_=type_,
        sort_by=sort_by,
        direction=direction,
        search=search,
        employee_ids=employee_ids,
        contains_message=contains_message,
        message_from=message_from,
        custom_leave_name=custom_leave_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    search: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    contains_message: bool | Unset = UNSET,
    message_from: str | Unset = UNSET,
    custom_leave_name: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200 | None:
    """Reads all Incidences

     Reads all Incidences

    Args:
        ids (list[str] | Unset): A list of incidence identifiers. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): A list of legal entities identifiers. Example:
            ['1', '2', '3'].
        status (list[str] | Unset): A list of statuses. Example: ['in-preparation', 'to-do',
            'doing', 'done', 'discarded'].
        starts_on (str | Unset): Get the incidence (aka employee update) that start safter this
            date (included). Example: 2020-01-01.
        ends_on (str | Unset): Get the incidence (aka employee update) that ends before this date
            (included). Example: 2020-01-01.
        type_ (list[str] | Unset): A list of types. It can be any of the following address, bank,
            cost_center, contract, gender, health_insurance, hiring, id, irpf, legal_entity,
            manual_incidence, name, nationality, parental, permits_and_certificates, phone_number,
            sick, tax_id, taxes_and_deductions, termination, work_activity, workplace Example:
            ['hiring', 'workplace'].
        sort_by (str | Unset): Field to sort by. It can be any of the following
            employee_first_name, employee_last_name, type, legal_entity_name, effective_date, status,
            created_at. Example: effective_date.
        direction (str | Unset): Sort direction. It can be 'asc' or 'desc'. Example: desc.
        search (str | Unset): Filter the result by the name of the employee. Example: Hellen.
        employee_ids (list[str] | Unset): A list of employee identifiers. Example: ['1', '2',
            '3'].
        contains_message (bool | Unset): Boolean that filters incidences that does or does not
            contains messages. Example: True.
        message_from (str | Unset): Filter by message sender. Example: bookkeeper.
        custom_leave_name (list[str] | Unset): A list of custom leave names. Example: ['Medical
            Leave', 'Paternity Leave'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesBookkeepersManagementIncidencesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            legal_entities_ids=legal_entities_ids,
            status=status,
            starts_on=starts_on,
            ends_on=ends_on,
            type_=type_,
            sort_by=sort_by,
            direction=direction,
            search=search,
            employee_ids=employee_ids,
            contains_message=contains_message,
            message_from=message_from,
            custom_leave_name=custom_leave_name,
        )
    ).parsed
