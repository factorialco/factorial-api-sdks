from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_time_record import ProjectManagementTimeRecord
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/project_management/time_records/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementTimeRecord | None:
    if response.status_code == 200:
        response_200 = ProjectManagementTimeRecord.from_dict(response.json())

        return response_200

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
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectManagementTimeRecord]:
    """Reads a single Time record

     ###### **What does it do?**
    This endpoint reads and retrieves a list of time records. You can utilize URL parameters to filter
    the results.
    ###### **What params does it accept?**

      - `ids`: retrieve only the time records that matches the `ids` passed in the request.
      - `project_workers_ids`: Retrieve only the time records assigned to any `project_workers_ids`
    passed in the request.
      - `subproject_ids`: retrieve only the time records related with any `subproject_ids` passed in the
    request.
      - `attendance_shift_ids`: retrieve only the time records related with any `attendance_shift_ids`
    passed in the request.
      - `employee_ids`: ⚠️ This param, will be deprecated soon. **Please use `project_worker_ids` param
    instead.**
      - `month`: Filter time records created in a specific month of the year.
      - `year`: To be used with the `month` parameter to filter time records created in a particular
    period.
      - `updated_after`: this parameter is needed to filter time records created or updated after a
    date.

    ###### **Is it related to other entities?**
    A `time_record` is mandatory related to a `project_worker_id` and an `attendance_shift_id`.
    Optionally, it can be related to a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read time_records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementTimeRecord]
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
) -> ProjectManagementTimeRecord | None:
    """Reads a single Time record

     ###### **What does it do?**
    This endpoint reads and retrieves a list of time records. You can utilize URL parameters to filter
    the results.
    ###### **What params does it accept?**

      - `ids`: retrieve only the time records that matches the `ids` passed in the request.
      - `project_workers_ids`: Retrieve only the time records assigned to any `project_workers_ids`
    passed in the request.
      - `subproject_ids`: retrieve only the time records related with any `subproject_ids` passed in the
    request.
      - `attendance_shift_ids`: retrieve only the time records related with any `attendance_shift_ids`
    passed in the request.
      - `employee_ids`: ⚠️ This param, will be deprecated soon. **Please use `project_worker_ids` param
    instead.**
      - `month`: Filter time records created in a specific month of the year.
      - `year`: To be used with the `month` parameter to filter time records created in a particular
    period.
      - `updated_after`: this parameter is needed to filter time records created or updated after a
    date.

    ###### **Is it related to other entities?**
    A `time_record` is mandatory related to a `project_worker_id` and an `attendance_shift_id`.
    Optionally, it can be related to a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read time_records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementTimeRecord
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectManagementTimeRecord]:
    """Reads a single Time record

     ###### **What does it do?**
    This endpoint reads and retrieves a list of time records. You can utilize URL parameters to filter
    the results.
    ###### **What params does it accept?**

      - `ids`: retrieve only the time records that matches the `ids` passed in the request.
      - `project_workers_ids`: Retrieve only the time records assigned to any `project_workers_ids`
    passed in the request.
      - `subproject_ids`: retrieve only the time records related with any `subproject_ids` passed in the
    request.
      - `attendance_shift_ids`: retrieve only the time records related with any `attendance_shift_ids`
    passed in the request.
      - `employee_ids`: ⚠️ This param, will be deprecated soon. **Please use `project_worker_ids` param
    instead.**
      - `month`: Filter time records created in a specific month of the year.
      - `year`: To be used with the `month` parameter to filter time records created in a particular
    period.
      - `updated_after`: this parameter is needed to filter time records created or updated after a
    date.

    ###### **Is it related to other entities?**
    A `time_record` is mandatory related to a `project_worker_id` and an `attendance_shift_id`.
    Optionally, it can be related to a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read time_records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementTimeRecord]
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
) -> ProjectManagementTimeRecord | None:
    """Reads a single Time record

     ###### **What does it do?**
    This endpoint reads and retrieves a list of time records. You can utilize URL parameters to filter
    the results.
    ###### **What params does it accept?**

      - `ids`: retrieve only the time records that matches the `ids` passed in the request.
      - `project_workers_ids`: Retrieve only the time records assigned to any `project_workers_ids`
    passed in the request.
      - `subproject_ids`: retrieve only the time records related with any `subproject_ids` passed in the
    request.
      - `attendance_shift_ids`: retrieve only the time records related with any `attendance_shift_ids`
    passed in the request.
      - `employee_ids`: ⚠️ This param, will be deprecated soon. **Please use `project_worker_ids` param
    instead.**
      - `month`: Filter time records created in a specific month of the year.
      - `year`: To be used with the `month` parameter to filter time records created in a particular
    period.
      - `updated_after`: this parameter is needed to filter time records created or updated after a
    date.

    ###### **Is it related to other entities?**
    A `time_record` is mandatory related to a `project_worker_id` and an `attendance_shift_id`.
    Optionally, it can be related to a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read time_records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementTimeRecord
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
