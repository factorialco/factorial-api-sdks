from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_employees_employees_response_200 import (
    GetApi20260701ResourcesEmployeesEmployeesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    full_text_name: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    company_identifier: str | Unset = UNSET,
    only_active: bool,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_managers: bool,
    name_starts_with: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_access_ids: list[str] | Unset = UNSET
    if not isinstance(access_ids, Unset):
        json_access_ids = access_ids

    params["access_ids[]"] = json_access_ids

    json_emails: list[str] | Unset = UNSET
    if not isinstance(emails, Unset):
        json_emails = emails

    params["emails[]"] = json_emails

    params["full_text_name"] = full_text_name

    params["updated_at_gteq"] = updated_at_gteq

    json_legal_entity_ids: list[str] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    params["company_identifier"] = company_identifier

    params["only_active"] = only_active

    json_team_ids: list[str] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids[]"] = json_team_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["location_ids[]"] = json_location_ids

    params["only_managers"] = only_managers

    params["name_starts_with"] = name_starts_with

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/employees/employees",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesEmployeesEmployeesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesEmployeesEmployeesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesEmployeesEmployeesResponse200]:
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
    access_ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    full_text_name: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    company_identifier: str | Unset = UNSET,
    only_active: bool,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_managers: bool,
    name_starts_with: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesEmployeesEmployeesResponse200]:
    """Reads all Employees

     Only admins can see all the employees' information, regular users will get a restricted version of
    the payload as a response based on the permission set by the admin

    Args:
        ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        access_ids (list[str] | Unset): filter by employee access ids. Example: ['1', '2', '3'].
        emails (list[str] | Unset): filter by employee emails. Example: ['ana@factorial.com',
            'john@factorial.com'].
        full_text_name (str | Unset): filter by employee name. Example: Ana Lopez Perez.
        updated_at_gteq (str | Unset): Filter employees by their latest update timestamp
            (`updated_at`), on or after this date. Only the date is considered; any time component is
            ignored (matching starts at 00:00:00 of the given date). Note: `updated_at` only stores
            the most recent update, so an employee updated multiple times is matched solely by its
            latest update, not by earlier ones. Example: 2024-01-01.
        legal_entity_ids (list[str] | Unset): filter by legal entity id (refereces to
            companies/legal_entities). Example: ['1', '2'].
        company_identifier (str | Unset): filter by employee company identifier. Example:
            bb9d281e.
        only_active (bool): get only active employees Example: True.
        team_ids (list[str] | Unset): filter employees by team id (references to core/teams).
            Example: ['1', '2'].
        location_ids (list[str] | Unset): filter employees by location id (references to
            locations/location). Example: ['1', '2'].
        only_managers (bool): get only manager employees. Example: True.
        name_starts_with (str | Unset): filter by employee names that start with the given text.
            Example: Ana.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesEmployeesEmployeesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        access_ids=access_ids,
        emails=emails,
        full_text_name=full_text_name,
        updated_at_gteq=updated_at_gteq,
        legal_entity_ids=legal_entity_ids,
        company_identifier=company_identifier,
        only_active=only_active,
        team_ids=team_ids,
        location_ids=location_ids,
        only_managers=only_managers,
        name_starts_with=name_starts_with,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    full_text_name: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    company_identifier: str | Unset = UNSET,
    only_active: bool,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_managers: bool,
    name_starts_with: str | Unset = UNSET,
) -> GetApi20260701ResourcesEmployeesEmployeesResponse200 | None:
    """Reads all Employees

     Only admins can see all the employees' information, regular users will get a restricted version of
    the payload as a response based on the permission set by the admin

    Args:
        ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        access_ids (list[str] | Unset): filter by employee access ids. Example: ['1', '2', '3'].
        emails (list[str] | Unset): filter by employee emails. Example: ['ana@factorial.com',
            'john@factorial.com'].
        full_text_name (str | Unset): filter by employee name. Example: Ana Lopez Perez.
        updated_at_gteq (str | Unset): Filter employees by their latest update timestamp
            (`updated_at`), on or after this date. Only the date is considered; any time component is
            ignored (matching starts at 00:00:00 of the given date). Note: `updated_at` only stores
            the most recent update, so an employee updated multiple times is matched solely by its
            latest update, not by earlier ones. Example: 2024-01-01.
        legal_entity_ids (list[str] | Unset): filter by legal entity id (refereces to
            companies/legal_entities). Example: ['1', '2'].
        company_identifier (str | Unset): filter by employee company identifier. Example:
            bb9d281e.
        only_active (bool): get only active employees Example: True.
        team_ids (list[str] | Unset): filter employees by team id (references to core/teams).
            Example: ['1', '2'].
        location_ids (list[str] | Unset): filter employees by location id (references to
            locations/location). Example: ['1', '2'].
        only_managers (bool): get only manager employees. Example: True.
        name_starts_with (str | Unset): filter by employee names that start with the given text.
            Example: Ana.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesEmployeesEmployeesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        access_ids=access_ids,
        emails=emails,
        full_text_name=full_text_name,
        updated_at_gteq=updated_at_gteq,
        legal_entity_ids=legal_entity_ids,
        company_identifier=company_identifier,
        only_active=only_active,
        team_ids=team_ids,
        location_ids=location_ids,
        only_managers=only_managers,
        name_starts_with=name_starts_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    full_text_name: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    company_identifier: str | Unset = UNSET,
    only_active: bool,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_managers: bool,
    name_starts_with: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesEmployeesEmployeesResponse200]:
    """Reads all Employees

     Only admins can see all the employees' information, regular users will get a restricted version of
    the payload as a response based on the permission set by the admin

    Args:
        ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        access_ids (list[str] | Unset): filter by employee access ids. Example: ['1', '2', '3'].
        emails (list[str] | Unset): filter by employee emails. Example: ['ana@factorial.com',
            'john@factorial.com'].
        full_text_name (str | Unset): filter by employee name. Example: Ana Lopez Perez.
        updated_at_gteq (str | Unset): Filter employees by their latest update timestamp
            (`updated_at`), on or after this date. Only the date is considered; any time component is
            ignored (matching starts at 00:00:00 of the given date). Note: `updated_at` only stores
            the most recent update, so an employee updated multiple times is matched solely by its
            latest update, not by earlier ones. Example: 2024-01-01.
        legal_entity_ids (list[str] | Unset): filter by legal entity id (refereces to
            companies/legal_entities). Example: ['1', '2'].
        company_identifier (str | Unset): filter by employee company identifier. Example:
            bb9d281e.
        only_active (bool): get only active employees Example: True.
        team_ids (list[str] | Unset): filter employees by team id (references to core/teams).
            Example: ['1', '2'].
        location_ids (list[str] | Unset): filter employees by location id (references to
            locations/location). Example: ['1', '2'].
        only_managers (bool): get only manager employees. Example: True.
        name_starts_with (str | Unset): filter by employee names that start with the given text.
            Example: Ana.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesEmployeesEmployeesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        access_ids=access_ids,
        emails=emails,
        full_text_name=full_text_name,
        updated_at_gteq=updated_at_gteq,
        legal_entity_ids=legal_entity_ids,
        company_identifier=company_identifier,
        only_active=only_active,
        team_ids=team_ids,
        location_ids=location_ids,
        only_managers=only_managers,
        name_starts_with=name_starts_with,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    full_text_name: str | Unset = UNSET,
    updated_at_gteq: str | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
    company_identifier: str | Unset = UNSET,
    only_active: bool,
    team_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_managers: bool,
    name_starts_with: str | Unset = UNSET,
) -> GetApi20260701ResourcesEmployeesEmployeesResponse200 | None:
    """Reads all Employees

     Only admins can see all the employees' information, regular users will get a restricted version of
    the payload as a response based on the permission set by the admin

    Args:
        ids (list[str] | Unset): filter by employee ids. Example: ['1', '2', '3'].
        access_ids (list[str] | Unset): filter by employee access ids. Example: ['1', '2', '3'].
        emails (list[str] | Unset): filter by employee emails. Example: ['ana@factorial.com',
            'john@factorial.com'].
        full_text_name (str | Unset): filter by employee name. Example: Ana Lopez Perez.
        updated_at_gteq (str | Unset): Filter employees by their latest update timestamp
            (`updated_at`), on or after this date. Only the date is considered; any time component is
            ignored (matching starts at 00:00:00 of the given date). Note: `updated_at` only stores
            the most recent update, so an employee updated multiple times is matched solely by its
            latest update, not by earlier ones. Example: 2024-01-01.
        legal_entity_ids (list[str] | Unset): filter by legal entity id (refereces to
            companies/legal_entities). Example: ['1', '2'].
        company_identifier (str | Unset): filter by employee company identifier. Example:
            bb9d281e.
        only_active (bool): get only active employees Example: True.
        team_ids (list[str] | Unset): filter employees by team id (references to core/teams).
            Example: ['1', '2'].
        location_ids (list[str] | Unset): filter employees by location id (references to
            locations/location). Example: ['1', '2'].
        only_managers (bool): get only manager employees. Example: True.
        name_starts_with (str | Unset): filter by employee names that start with the given text.
            Example: Ana.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesEmployeesEmployeesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            access_ids=access_ids,
            emails=emails,
            full_text_name=full_text_name,
            updated_at_gteq=updated_at_gteq,
            legal_entity_ids=legal_entity_ids,
            company_identifier=company_identifier,
            only_active=only_active,
            team_ids=team_ids,
            location_ids=location_ids,
            only_managers=only_managers,
            name_starts_with=name_starts_with,
        )
    ).parsed
