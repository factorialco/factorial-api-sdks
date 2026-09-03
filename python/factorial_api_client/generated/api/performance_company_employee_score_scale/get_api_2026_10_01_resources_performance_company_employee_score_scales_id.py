from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_company_employee_score_scale import PerformanceCompanyEmployeeScoreScale
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/performance/company_employee_score_scales/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PerformanceCompanyEmployeeScoreScale | None:
    if response.status_code == 200:
        response_200 = PerformanceCompanyEmployeeScoreScale.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PerformanceCompanyEmployeeScoreScale]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PerformanceCompanyEmployeeScoreScale]:
    """Reads a single Company employee score scale

     Retrieves the predefined scale set for the company and used when scoring the employee inside a
    review.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceCompanyEmployeeScoreScale]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> PerformanceCompanyEmployeeScoreScale | None:
    """Reads a single Company employee score scale

     Retrieves the predefined scale set for the company and used when scoring the employee inside a
    review.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceCompanyEmployeeScoreScale
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PerformanceCompanyEmployeeScoreScale]:
    """Reads a single Company employee score scale

     Retrieves the predefined scale set for the company and used when scoring the employee inside a
    review.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceCompanyEmployeeScoreScale]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> PerformanceCompanyEmployeeScoreScale | None:
    """Reads a single Company employee score scale

     Retrieves the predefined scale set for the company and used when scoring the employee inside a
    review.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceCompanyEmployeeScoreScale
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
