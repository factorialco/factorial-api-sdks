from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20261001_resources_work_schedule_day_configurations_bulk_cud_body import (
    PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody,
)
from ...models.work_schedule_day_configuration import WorkScheduleDayConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-10-01/resources/work_schedule/day_configurations/bulk_cud",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[WorkScheduleDayConfiguration] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WorkScheduleDayConfiguration.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[WorkScheduleDayConfiguration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset = UNSET,
) -> Response[list[WorkScheduleDayConfiguration]]:
    """Bulk cuds a Day configuration

     Bulk cuds a Day configuration

    Args:
        body (PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WorkScheduleDayConfiguration]]
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
    body: PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset = UNSET,
) -> list[WorkScheduleDayConfiguration] | None:
    """Bulk cuds a Day configuration

     Bulk cuds a Day configuration

    Args:
        body (PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WorkScheduleDayConfiguration]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset = UNSET,
) -> Response[list[WorkScheduleDayConfiguration]]:
    """Bulk cuds a Day configuration

     Bulk cuds a Day configuration

    Args:
        body (PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WorkScheduleDayConfiguration]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset = UNSET,
) -> list[WorkScheduleDayConfiguration] | None:
    """Bulk cuds a Day configuration

     Bulk cuds a Day configuration

    Args:
        body (PostApi20261001ResourcesWorkScheduleDayConfigurationsBulkCudBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WorkScheduleDayConfiguration]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
