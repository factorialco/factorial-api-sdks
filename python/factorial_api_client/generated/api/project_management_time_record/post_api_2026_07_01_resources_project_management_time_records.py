from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260701_resources_project_management_time_records_body import (
    PostApi20260701ResourcesProjectManagementTimeRecordsBody,
)
from ...models.project_management_time_record import ProjectManagementTimeRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/project_management/time_records",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementTimeRecord | None:
    if response.status_code == 201:
        response_201 = ProjectManagementTimeRecord.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementTimeRecord]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset = UNSET,
) -> Response[ProjectManagementTimeRecord]:
    r"""Creates a Time record

     ###### **What does it do?**
    \"This endpoint is used to create time records. A time record is an entity that establishes a
    mandatory relationship between `project_worker` and `attendance_shift_id`, and optionally with
    `subproject`. For a successful creation of a `time_record`, the `project_worker` must be
    **assigned**, and the associated `project` must be **active**.\"
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    create `time_records`.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementTimeRecord]
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
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset = UNSET,
) -> ProjectManagementTimeRecord | None:
    r"""Creates a Time record

     ###### **What does it do?**
    \"This endpoint is used to create time records. A time record is an entity that establishes a
    mandatory relationship between `project_worker` and `attendance_shift_id`, and optionally with
    `subproject`. For a successful creation of a `time_record`, the `project_worker` must be
    **assigned**, and the associated `project` must be **active**.\"
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    create `time_records`.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementTimeRecord
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset = UNSET,
) -> Response[ProjectManagementTimeRecord]:
    r"""Creates a Time record

     ###### **What does it do?**
    \"This endpoint is used to create time records. A time record is an entity that establishes a
    mandatory relationship between `project_worker` and `attendance_shift_id`, and optionally with
    `subproject`. For a successful creation of a `time_record`, the `project_worker` must be
    **assigned**, and the associated `project` must be **active**.\"
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    create `time_records`.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementTimeRecord]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset = UNSET,
) -> ProjectManagementTimeRecord | None:
    r"""Creates a Time record

     ###### **What does it do?**
    \"This endpoint is used to create time records. A time record is an entity that establishes a
    mandatory relationship between `project_worker` and `attendance_shift_id`, and optionally with
    `subproject`. For a successful creation of a `time_record`, the `project_worker` must be
    **assigned**, and the associated `project` must be **active**.\"
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    create `time_records`.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementTimeRecord
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
