from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_review_visibility_setting import PerformanceReviewVisibilitySetting
from ...models.put_api_20260701_resources_performance_review_visibility_settings_id_body import (
    PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-07-01/resources/performance/review_visibility_settings/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PerformanceReviewVisibilitySetting | None:
    if response.status_code == 200:
        response_200 = PerformanceReviewVisibilitySetting.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PerformanceReviewVisibilitySetting]:
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
    body: PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset = UNSET,
) -> Response[PerformanceReviewVisibilitySetting]:
    """Updates a Review visibility setting

     Modifiy the visibility settings of the review process.

    Args:
        id (str):
        body (PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewVisibilitySetting]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset = UNSET,
) -> PerformanceReviewVisibilitySetting | None:
    """Updates a Review visibility setting

     Modifiy the visibility settings of the review process.

    Args:
        id (str):
        body (PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewVisibilitySetting
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset = UNSET,
) -> Response[PerformanceReviewVisibilitySetting]:
    """Updates a Review visibility setting

     Modifiy the visibility settings of the review process.

    Args:
        id (str):
        body (PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewVisibilitySetting]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset = UNSET,
) -> PerformanceReviewVisibilitySetting | None:
    """Updates a Review visibility setting

     Modifiy the visibility settings of the review process.

    Args:
        id (str):
        body (PutApi20260701ResourcesPerformanceReviewVisibilitySettingsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewVisibilitySetting
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
