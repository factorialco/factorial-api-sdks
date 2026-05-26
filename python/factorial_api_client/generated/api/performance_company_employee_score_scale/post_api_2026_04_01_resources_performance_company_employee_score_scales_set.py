from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_company_employee_score_scale import PerformanceCompanyEmployeeScoreScale
from ...models.post_api_20260401_resources_performance_company_employee_score_scales_set_body import (
    PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/performance/company_employee_score_scales/set",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset = UNSET,
) -> Response[PerformanceCompanyEmployeeScoreScale]:
    """Sets a Company employee score scale

     Set the predefined employee score scale for the company.

    Args:
        body (PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceCompanyEmployeeScoreScale]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset = UNSET,
) -> PerformanceCompanyEmployeeScoreScale | None:
    """Sets a Company employee score scale

     Set the predefined employee score scale for the company.

    Args:
        body (PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceCompanyEmployeeScoreScale
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset = UNSET,
) -> Response[PerformanceCompanyEmployeeScoreScale]:
    """Sets a Company employee score scale

     Set the predefined employee score scale for the company.

    Args:
        body (PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceCompanyEmployeeScoreScale]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset = UNSET,
) -> PerformanceCompanyEmployeeScoreScale | None:
    """Sets a Company employee score scale

     Set the predefined employee score scale for the company.

    Args:
        body (PostApi20260401ResourcesPerformanceCompanyEmployeeScoreScalesSetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceCompanyEmployeeScoreScale
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
