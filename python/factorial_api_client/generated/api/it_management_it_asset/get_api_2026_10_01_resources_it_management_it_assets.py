from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_it_management_it_assets_response_200 import (
    GetApi20261001ResourcesItManagementItAssetsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    serial_numbers: list[str] | Unset = UNSET,
    type_names: list[str] | Unset = UNSET,
    asset_category_ids: list[str] | Unset = UNSET,
    owner_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    workplace_ids: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_serial_numbers: list[str] | Unset = UNSET
    if not isinstance(serial_numbers, Unset):
        json_serial_numbers = serial_numbers

    params["serial_numbers[]"] = json_serial_numbers

    json_type_names: list[str] | Unset = UNSET
    if not isinstance(type_names, Unset):
        json_type_names = type_names

    params["type_names[]"] = json_type_names

    json_asset_category_ids: list[str] | Unset = UNSET
    if not isinstance(asset_category_ids, Unset):
        json_asset_category_ids = asset_category_ids

    params["asset_category_ids[]"] = json_asset_category_ids

    json_owner_ids: list[str] | Unset = UNSET
    if not isinstance(owner_ids, Unset):
        json_owner_ids = owner_ids

    params["owner_ids[]"] = json_owner_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["location_ids[]"] = json_location_ids

    json_workplace_ids: list[str] | Unset = UNSET
    if not isinstance(workplace_ids, Unset):
        json_workplace_ids = workplace_ids

    params["workplace_ids[]"] = json_workplace_ids

    json_team_ids: list[str] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids[]"] = json_team_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/it_management/it_assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesItManagementItAssetsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesItManagementItAssetsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesItManagementItAssetsResponse200]:
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
    serial_numbers: list[str] | Unset = UNSET,
    type_names: list[str] | Unset = UNSET,
    asset_category_ids: list[str] | Unset = UNSET,
    owner_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    workplace_ids: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesItManagementItAssetsResponse200]:
    """Reads all It assets

     Reads all It assets

    Args:
        ids (list[str] | Unset): IT Asset identifiers to retrieve Example:
            ['0199e6ea-20c0-73d3-9782-8267dc96773a'].
        serial_numbers (list[str] | Unset): Serial numbers of IT assets to retrieve Example:
            ['SN123456789'].
        type_names (list[str] | Unset): Type names of IT assets to filter Example: ['laptop'].
        asset_category_ids (list[str] | Unset): Asset category IDs to filter assets by group
            Example: ['d3debfa9-4e86-4b3f-af94-2bda28512370'].
        owner_ids (list[str] | Unset): Owner (employee) identifiers to filter assets Example:
            ['1'].
        location_ids (list[str] | Unset): Location identifiers to filter assets Example: ['1'].
        workplace_ids (list[str] | Unset): Workplace identifiers to filter assets Example: ['1'].
        team_ids (list[str] | Unset): Team identifiers to filter assets Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesItManagementItAssetsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        serial_numbers=serial_numbers,
        type_names=type_names,
        asset_category_ids=asset_category_ids,
        owner_ids=owner_ids,
        location_ids=location_ids,
        workplace_ids=workplace_ids,
        team_ids=team_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    serial_numbers: list[str] | Unset = UNSET,
    type_names: list[str] | Unset = UNSET,
    asset_category_ids: list[str] | Unset = UNSET,
    owner_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    workplace_ids: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesItManagementItAssetsResponse200 | None:
    """Reads all It assets

     Reads all It assets

    Args:
        ids (list[str] | Unset): IT Asset identifiers to retrieve Example:
            ['0199e6ea-20c0-73d3-9782-8267dc96773a'].
        serial_numbers (list[str] | Unset): Serial numbers of IT assets to retrieve Example:
            ['SN123456789'].
        type_names (list[str] | Unset): Type names of IT assets to filter Example: ['laptop'].
        asset_category_ids (list[str] | Unset): Asset category IDs to filter assets by group
            Example: ['d3debfa9-4e86-4b3f-af94-2bda28512370'].
        owner_ids (list[str] | Unset): Owner (employee) identifiers to filter assets Example:
            ['1'].
        location_ids (list[str] | Unset): Location identifiers to filter assets Example: ['1'].
        workplace_ids (list[str] | Unset): Workplace identifiers to filter assets Example: ['1'].
        team_ids (list[str] | Unset): Team identifiers to filter assets Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesItManagementItAssetsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        serial_numbers=serial_numbers,
        type_names=type_names,
        asset_category_ids=asset_category_ids,
        owner_ids=owner_ids,
        location_ids=location_ids,
        workplace_ids=workplace_ids,
        team_ids=team_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    serial_numbers: list[str] | Unset = UNSET,
    type_names: list[str] | Unset = UNSET,
    asset_category_ids: list[str] | Unset = UNSET,
    owner_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    workplace_ids: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesItManagementItAssetsResponse200]:
    """Reads all It assets

     Reads all It assets

    Args:
        ids (list[str] | Unset): IT Asset identifiers to retrieve Example:
            ['0199e6ea-20c0-73d3-9782-8267dc96773a'].
        serial_numbers (list[str] | Unset): Serial numbers of IT assets to retrieve Example:
            ['SN123456789'].
        type_names (list[str] | Unset): Type names of IT assets to filter Example: ['laptop'].
        asset_category_ids (list[str] | Unset): Asset category IDs to filter assets by group
            Example: ['d3debfa9-4e86-4b3f-af94-2bda28512370'].
        owner_ids (list[str] | Unset): Owner (employee) identifiers to filter assets Example:
            ['1'].
        location_ids (list[str] | Unset): Location identifiers to filter assets Example: ['1'].
        workplace_ids (list[str] | Unset): Workplace identifiers to filter assets Example: ['1'].
        team_ids (list[str] | Unset): Team identifiers to filter assets Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesItManagementItAssetsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        serial_numbers=serial_numbers,
        type_names=type_names,
        asset_category_ids=asset_category_ids,
        owner_ids=owner_ids,
        location_ids=location_ids,
        workplace_ids=workplace_ids,
        team_ids=team_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    serial_numbers: list[str] | Unset = UNSET,
    type_names: list[str] | Unset = UNSET,
    asset_category_ids: list[str] | Unset = UNSET,
    owner_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    workplace_ids: list[str] | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesItManagementItAssetsResponse200 | None:
    """Reads all It assets

     Reads all It assets

    Args:
        ids (list[str] | Unset): IT Asset identifiers to retrieve Example:
            ['0199e6ea-20c0-73d3-9782-8267dc96773a'].
        serial_numbers (list[str] | Unset): Serial numbers of IT assets to retrieve Example:
            ['SN123456789'].
        type_names (list[str] | Unset): Type names of IT assets to filter Example: ['laptop'].
        asset_category_ids (list[str] | Unset): Asset category IDs to filter assets by group
            Example: ['d3debfa9-4e86-4b3f-af94-2bda28512370'].
        owner_ids (list[str] | Unset): Owner (employee) identifiers to filter assets Example:
            ['1'].
        location_ids (list[str] | Unset): Location identifiers to filter assets Example: ['1'].
        workplace_ids (list[str] | Unset): Workplace identifiers to filter assets Example: ['1'].
        team_ids (list[str] | Unset): Team identifiers to filter assets Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesItManagementItAssetsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            serial_numbers=serial_numbers,
            type_names=type_names,
            asset_category_ids=asset_category_ids,
            owner_ids=owner_ids,
            location_ids=location_ids,
            workplace_ids=workplace_ids,
            team_ids=team_ids,
        )
    ).parsed
