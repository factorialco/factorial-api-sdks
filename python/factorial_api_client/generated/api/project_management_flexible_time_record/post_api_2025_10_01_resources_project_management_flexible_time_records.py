from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20251001_resources_project_management_flexible_time_records_body import (
    PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody,
)
from ...models.project_management_flexible_time_record import ProjectManagementFlexibleTimeRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/project_management/flexible_time_records",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementFlexibleTimeRecord | None:
    if response.status_code == 201:
        response_201 = ProjectManagementFlexibleTimeRecord.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementFlexibleTimeRecord]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset = UNSET,
) -> Response[ProjectManagementFlexibleTimeRecord]:
    """Creates a Flexible time record

     ###### **What does it do?**
    This endpoint allows the creation of a new `flexible time record` with the given params. A flexible
    time record is used to impute time to a project, without having an strict relation with an
    attendance's shift. For a successful creation; the given `project` must be `active` and the given
    `project worker` must be `assigned`.
    ###### **What params does it accept?**

      - `project_worker_id`: the `project worker` that will be related to the `flexible time record`.
      - `date`: the date that occured the `flexible time record`.
      - `imputed minutes`: the amount of time that has to be imputed, in minutes.
      - `subproject_id`: optionally, the id of the `subproject` worked on.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to create flexible time records.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecord]
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
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset = UNSET,
) -> ProjectManagementFlexibleTimeRecord | None:
    """Creates a Flexible time record

     ###### **What does it do?**
    This endpoint allows the creation of a new `flexible time record` with the given params. A flexible
    time record is used to impute time to a project, without having an strict relation with an
    attendance's shift. For a successful creation; the given `project` must be `active` and the given
    `project worker` must be `assigned`.
    ###### **What params does it accept?**

      - `project_worker_id`: the `project worker` that will be related to the `flexible time record`.
      - `date`: the date that occured the `flexible time record`.
      - `imputed minutes`: the amount of time that has to be imputed, in minutes.
      - `subproject_id`: optionally, the id of the `subproject` worked on.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to create flexible time records.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecord
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset = UNSET,
) -> Response[ProjectManagementFlexibleTimeRecord]:
    """Creates a Flexible time record

     ###### **What does it do?**
    This endpoint allows the creation of a new `flexible time record` with the given params. A flexible
    time record is used to impute time to a project, without having an strict relation with an
    attendance's shift. For a successful creation; the given `project` must be `active` and the given
    `project worker` must be `assigned`.
    ###### **What params does it accept?**

      - `project_worker_id`: the `project worker` that will be related to the `flexible time record`.
      - `date`: the date that occured the `flexible time record`.
      - `imputed minutes`: the amount of time that has to be imputed, in minutes.
      - `subproject_id`: optionally, the id of the `subproject` worked on.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to create flexible time records.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecord]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset = UNSET,
) -> ProjectManagementFlexibleTimeRecord | None:
    """Creates a Flexible time record

     ###### **What does it do?**
    This endpoint allows the creation of a new `flexible time record` with the given params. A flexible
    time record is used to impute time to a project, without having an strict relation with an
    attendance's shift. For a successful creation; the given `project` must be `active` and the given
    `project worker` must be `assigned`.
    ###### **What params does it accept?**

      - `project_worker_id`: the `project worker` that will be related to the `flexible time record`.
      - `date`: the date that occured the `flexible time record`.
      - `imputed minutes`: the amount of time that has to be imputed, in minutes.
      - `subproject_id`: optionally, the id of the `subproject` worked on.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to create flexible time records.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecord
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
