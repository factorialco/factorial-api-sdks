from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260701_resources_project_management_time_records_bulk_process_body import (
    PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody,
)
from ...models.project_management_time_record import ProjectManagementTimeRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/project_management/time_records/bulk_process",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ProjectManagementTimeRecord] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProjectManagementTimeRecord.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ProjectManagementTimeRecord]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset = UNSET,
) -> Response[list[ProjectManagementTimeRecord]]:
    r"""Bulk processes a Time record

     ###### **What does it do?**
    This versatile endpoint allows for the creation, update, or deletion of a time record associated
    with an `attendance_shift_id`. To achieve this, provide an array of items with the following
    structure:

      ```json
        [{
          \"time_record_id\": number | null,
          \"attendance_shift_id\": number | null,
          \"project_worker_id\": number | null,
          \"subproject_id\": number | null
        }]
      ```

      - If no `time_record_id` provided, a created will be performed with the other data that will be
    required (except for `subproject_id`, that is always optional).
      - If `time_record_id but no other data provided, then the action will be a **delete**.
      - If `time_record_id` and more data, then it's an **update**.

    Please note: The relationship between `time_record` and `attendance_shift` is unique. In the
    provided array of items, if two items have exactly the same `attendance_shift_id`, only the last
    action specified will be executed, **unless the first action is a delete and the second one an
    update**.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProjectManagementTimeRecord]]
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
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset = UNSET,
) -> list[ProjectManagementTimeRecord] | None:
    r"""Bulk processes a Time record

     ###### **What does it do?**
    This versatile endpoint allows for the creation, update, or deletion of a time record associated
    with an `attendance_shift_id`. To achieve this, provide an array of items with the following
    structure:

      ```json
        [{
          \"time_record_id\": number | null,
          \"attendance_shift_id\": number | null,
          \"project_worker_id\": number | null,
          \"subproject_id\": number | null
        }]
      ```

      - If no `time_record_id` provided, a created will be performed with the other data that will be
    required (except for `subproject_id`, that is always optional).
      - If `time_record_id but no other data provided, then the action will be a **delete**.
      - If `time_record_id` and more data, then it's an **update**.

    Please note: The relationship between `time_record` and `attendance_shift` is unique. In the
    provided array of items, if two items have exactly the same `attendance_shift_id`, only the last
    action specified will be executed, **unless the first action is a delete and the second one an
    update**.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProjectManagementTimeRecord]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset = UNSET,
) -> Response[list[ProjectManagementTimeRecord]]:
    r"""Bulk processes a Time record

     ###### **What does it do?**
    This versatile endpoint allows for the creation, update, or deletion of a time record associated
    with an `attendance_shift_id`. To achieve this, provide an array of items with the following
    structure:

      ```json
        [{
          \"time_record_id\": number | null,
          \"attendance_shift_id\": number | null,
          \"project_worker_id\": number | null,
          \"subproject_id\": number | null
        }]
      ```

      - If no `time_record_id` provided, a created will be performed with the other data that will be
    required (except for `subproject_id`, that is always optional).
      - If `time_record_id but no other data provided, then the action will be a **delete**.
      - If `time_record_id` and more data, then it's an **update**.

    Please note: The relationship between `time_record` and `attendance_shift` is unique. In the
    provided array of items, if two items have exactly the same `attendance_shift_id`, only the last
    action specified will be executed, **unless the first action is a delete and the second one an
    update**.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProjectManagementTimeRecord]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset = UNSET,
) -> list[ProjectManagementTimeRecord] | None:
    r"""Bulk processes a Time record

     ###### **What does it do?**
    This versatile endpoint allows for the creation, update, or deletion of a time record associated
    with an `attendance_shift_id`. To achieve this, provide an array of items with the following
    structure:

      ```json
        [{
          \"time_record_id\": number | null,
          \"attendance_shift_id\": number | null,
          \"project_worker_id\": number | null,
          \"subproject_id\": number | null
        }]
      ```

      - If no `time_record_id` provided, a created will be performed with the other data that will be
    required (except for `subproject_id`, that is always optional).
      - If `time_record_id but no other data provided, then the action will be a **delete**.
      - If `time_record_id` and more data, then it's an **update**.

    Please note: The relationship between `time_record` and `attendance_shift` is unique. In the
    provided array of items, if two items have exactly the same `attendance_shift_id`, only the last
    action specified will be executed, **unless the first action is a delete and the second one an
    update**.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature.

    Args:
        body (PostApi20260701ResourcesProjectManagementTimeRecordsBulkProcessBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProjectManagementTimeRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
