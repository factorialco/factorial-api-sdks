from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_holidays_company_holidays_response_200 import (
    GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    team_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_location_ids: list[int] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["location_ids[]"] = json_location_ids

    json_team_ids: list[int] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids[]"] = json_team_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["start_at"] = start_at

    params["end_at"] = end_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/holidays/company_holidays",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200]:
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
    location_ids: list[int] | Unset = UNSET,
    team_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200]:
    """Reads all Company holidays

     Retrieves company holidays

    Args:
        ids (list[int] | Unset): Company holiday ids Example: [56].
        location_ids (list[int] | Unset): Location ids Example: [1].
        team_ids (list[int] | Unset): Team ids Example: [3].
        employee_ids (list[int] | Unset): Filter by the default location of these employees
            Example: [1].
        start_at (str | Unset): Start date Example: 2024-12-01.
        end_at (str | Unset): End date Example: 2024-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        location_ids=location_ids,
        team_ids=team_ids,
        employee_ids=employee_ids,
        start_at=start_at,
        end_at=end_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    team_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
) -> GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200 | None:
    """Reads all Company holidays

     Retrieves company holidays

    Args:
        ids (list[int] | Unset): Company holiday ids Example: [56].
        location_ids (list[int] | Unset): Location ids Example: [1].
        team_ids (list[int] | Unset): Team ids Example: [3].
        employee_ids (list[int] | Unset): Filter by the default location of these employees
            Example: [1].
        start_at (str | Unset): Start date Example: 2024-12-01.
        end_at (str | Unset): End date Example: 2024-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        location_ids=location_ids,
        team_ids=team_ids,
        employee_ids=employee_ids,
        start_at=start_at,
        end_at=end_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    team_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200]:
    """Reads all Company holidays

     Retrieves company holidays

    Args:
        ids (list[int] | Unset): Company holiday ids Example: [56].
        location_ids (list[int] | Unset): Location ids Example: [1].
        team_ids (list[int] | Unset): Team ids Example: [3].
        employee_ids (list[int] | Unset): Filter by the default location of these employees
            Example: [1].
        start_at (str | Unset): Start date Example: 2024-12-01.
        end_at (str | Unset): End date Example: 2024-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        location_ids=location_ids,
        team_ids=team_ids,
        employee_ids=employee_ids,
        start_at=start_at,
        end_at=end_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    location_ids: list[int] | Unset = UNSET,
    team_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    start_at: str | Unset = UNSET,
    end_at: str | Unset = UNSET,
) -> GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200 | None:
    """Reads all Company holidays

     Retrieves company holidays

    Args:
        ids (list[int] | Unset): Company holiday ids Example: [56].
        location_ids (list[int] | Unset): Location ids Example: [1].
        team_ids (list[int] | Unset): Team ids Example: [3].
        employee_ids (list[int] | Unset): Filter by the default location of these employees
            Example: [1].
        start_at (str | Unset): Start date Example: 2024-12-01.
        end_at (str | Unset): End date Example: 2024-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesHolidaysCompanyHolidaysResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            location_ids=location_ids,
            team_ids=team_ids,
            employee_ids=employee_ids,
            start_at=start_at,
            end_at=end_at,
        )
    ).parsed
