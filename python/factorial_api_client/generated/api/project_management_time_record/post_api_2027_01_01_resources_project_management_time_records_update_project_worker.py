from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_api_20270101_resources_project_management_time_records_update_project_worker_body import (
    PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody,
)
from ...models.project_management_time_record import ProjectManagementTimeRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2027-01-01/resources/project_management/time_records/update_project_worker",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ProjectManagementTimeRecord | None:
    if response.status_code == 200:
        response_200 = ProjectManagementTimeRecord.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ProjectManagementTimeRecord]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody
    | Unset = UNSET,
) -> Response[ErrorResponse | ProjectManagementTimeRecord]:
    """Update project workers a Time record

     ###### **What does it do?**
    This endpoint is used to change the project that an employee (`project_worker`) has assigned to an
    `attendance_shift`.

    Args:
        body (PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectManagementTimeRecord]
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
    body: PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody
    | Unset = UNSET,
) -> ErrorResponse | ProjectManagementTimeRecord | None:
    """Update project workers a Time record

     ###### **What does it do?**
    This endpoint is used to change the project that an employee (`project_worker`) has assigned to an
    `attendance_shift`.

    Args:
        body (PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectManagementTimeRecord
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody
    | Unset = UNSET,
) -> Response[ErrorResponse | ProjectManagementTimeRecord]:
    """Update project workers a Time record

     ###### **What does it do?**
    This endpoint is used to change the project that an employee (`project_worker`) has assigned to an
    `attendance_shift`.

    Args:
        body (PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectManagementTimeRecord]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody
    | Unset = UNSET,
) -> ErrorResponse | ProjectManagementTimeRecord | None:
    """Update project workers a Time record

     ###### **What does it do?**
    This endpoint is used to change the project that an employee (`project_worker`) has assigned to an
    `attendance_shift`.

    Args:
        body (PostApi20270101ResourcesProjectManagementTimeRecordsUpdateProjectWorkerBody |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectManagementTimeRecord
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
