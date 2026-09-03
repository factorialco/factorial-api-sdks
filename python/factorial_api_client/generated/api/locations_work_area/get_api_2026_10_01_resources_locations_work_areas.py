from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_locations_work_areas_response_200 import (
    GetApi20261001ResourcesLocationsWorkAreasResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_non_archived: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["location_ids[]"] = json_location_ids

    params["only_non_archived"] = only_non_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/locations/work_areas",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesLocationsWorkAreasResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesLocationsWorkAreasResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesLocationsWorkAreasResponse200]:
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
    location_ids: list[str] | Unset = UNSET,
    only_non_archived: bool,
) -> Response[GetApi20261001ResourcesLocationsWorkAreasResponse200]:
    """Reads all Work areas

     Reads all Work areas

    Args:
        ids (list[str] | Unset):
        location_ids (list[str] | Unset):
        only_non_archived (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesLocationsWorkAreasResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        location_ids=location_ids,
        only_non_archived=only_non_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_non_archived: bool,
) -> GetApi20261001ResourcesLocationsWorkAreasResponse200 | None:
    """Reads all Work areas

     Reads all Work areas

    Args:
        ids (list[str] | Unset):
        location_ids (list[str] | Unset):
        only_non_archived (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesLocationsWorkAreasResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        location_ids=location_ids,
        only_non_archived=only_non_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_non_archived: bool,
) -> Response[GetApi20261001ResourcesLocationsWorkAreasResponse200]:
    """Reads all Work areas

     Reads all Work areas

    Args:
        ids (list[str] | Unset):
        location_ids (list[str] | Unset):
        only_non_archived (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesLocationsWorkAreasResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        location_ids=location_ids,
        only_non_archived=only_non_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    only_non_archived: bool,
) -> GetApi20261001ResourcesLocationsWorkAreasResponse200 | None:
    """Reads all Work areas

     Reads all Work areas

    Args:
        ids (list[str] | Unset):
        location_ids (list[str] | Unset):
        only_non_archived (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesLocationsWorkAreasResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            location_ids=location_ids,
            only_non_archived=only_non_archived,
        )
    ).parsed
