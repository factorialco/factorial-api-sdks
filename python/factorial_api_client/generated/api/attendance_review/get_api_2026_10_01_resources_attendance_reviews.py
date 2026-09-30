from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_attendance_reviews_response_200 import (
    GetApi20261001ResourcesAttendanceReviewsResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    employee_ids: list[str],
    start_on: str,
    end_on: str,
    reviewed_at: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["start_on"] = start_on

    params["end_on"] = end_on

    params["reviewed_at"] = reviewed_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/attendance/reviews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesAttendanceReviewsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesAttendanceReviewsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesAttendanceReviewsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str],
    start_on: str,
    end_on: str,
    reviewed_at: str,
) -> Response[GetApi20261001ResourcesAttendanceReviewsResponse200]:
    """Reads all Reviews

     Reads all Reviews

    Args:
        employee_ids (list[str]): Employee identifiers Example: ['1', '2', '3'].
        start_on (str): Start date of the reviews Example: 2025-01-01.
        end_on (str): End date of the reviews Example: 2025-01-02.
        reviewed_at (str): Reviewed at date(ISO 8601 format string) Example:
            2025-01-02T00:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceReviewsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        reviewed_at=reviewed_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str],
    start_on: str,
    end_on: str,
    reviewed_at: str,
) -> GetApi20261001ResourcesAttendanceReviewsResponse200 | None:
    """Reads all Reviews

     Reads all Reviews

    Args:
        employee_ids (list[str]): Employee identifiers Example: ['1', '2', '3'].
        start_on (str): Start date of the reviews Example: 2025-01-01.
        end_on (str): End date of the reviews Example: 2025-01-02.
        reviewed_at (str): Reviewed at date(ISO 8601 format string) Example:
            2025-01-02T00:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceReviewsResponse200
    """

    return sync_detailed(
        client=client,
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        reviewed_at=reviewed_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str],
    start_on: str,
    end_on: str,
    reviewed_at: str,
) -> Response[GetApi20261001ResourcesAttendanceReviewsResponse200]:
    """Reads all Reviews

     Reads all Reviews

    Args:
        employee_ids (list[str]): Employee identifiers Example: ['1', '2', '3'].
        start_on (str): Start date of the reviews Example: 2025-01-01.
        end_on (str): End date of the reviews Example: 2025-01-02.
        reviewed_at (str): Reviewed at date(ISO 8601 format string) Example:
            2025-01-02T00:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesAttendanceReviewsResponse200]
    """

    kwargs = _get_kwargs(
        employee_ids=employee_ids,
        start_on=start_on,
        end_on=end_on,
        reviewed_at=reviewed_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_ids: list[str],
    start_on: str,
    end_on: str,
    reviewed_at: str,
) -> GetApi20261001ResourcesAttendanceReviewsResponse200 | None:
    """Reads all Reviews

     Reads all Reviews

    Args:
        employee_ids (list[str]): Employee identifiers Example: ['1', '2', '3'].
        start_on (str): Start date of the reviews Example: 2025-01-01.
        end_on (str): End date of the reviews Example: 2025-01-02.
        reviewed_at (str): Reviewed at date(ISO 8601 format string) Example:
            2025-01-02T00:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesAttendanceReviewsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_ids=employee_ids,
            start_on=start_on,
            end_on=end_on,
            reviewed_at=reviewed_at,
        )
    ).parsed
