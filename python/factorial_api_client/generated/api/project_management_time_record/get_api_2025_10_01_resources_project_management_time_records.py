from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_project_management_time_records_response_200 import (
    GetApi20251001ResourcesProjectManagementTimeRecordsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    attendance_shift_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    year: int | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_project_worker_ids: list[int] | Unset = UNSET
    if not isinstance(project_worker_ids, Unset):
        json_project_worker_ids = project_worker_ids

    params["project_worker_ids[]"] = json_project_worker_ids

    json_subproject_ids: list[int] | Unset = UNSET
    if not isinstance(subproject_ids, Unset):
        json_subproject_ids = subproject_ids

    params["subproject_ids[]"] = json_subproject_ids

    json_attendance_shift_ids: list[int] | Unset = UNSET
    if not isinstance(attendance_shift_ids, Unset):
        json_attendance_shift_ids = attendance_shift_ids

    params["attendance_shift_ids[]"] = json_attendance_shift_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["month"] = month

    params["year"] = year

    params["updated_after"] = updated_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/project_management/time_records",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesProjectManagementTimeRecordsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesProjectManagementTimeRecordsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesProjectManagementTimeRecordsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    attendance_shift_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    year: int | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesProjectManagementTimeRecordsResponse200]:
    """Reads all Time records

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
        ids (list[int] | Unset): Time record ids to retrieve Example: [1, 2].
        project_worker_ids (list[int] | Unset): Project worker ids to retrieve Example: [1, 2].
        subproject_ids (list[int] | Unset): Subproject ids to retrieve Example: [1, 2].
        attendance_shift_ids (list[int] | Unset): Attendance shift ids to retrieve Example: [1,
            2].
        employee_ids (list[int] | Unset): Employee ids to retrieve Example: [1, 2].
        month (int | Unset): Month to filter Example: 1.
        year (int | Unset): Year to filter Example: 2021.
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesProjectManagementTimeRecordsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_worker_ids=project_worker_ids,
        subproject_ids=subproject_ids,
        attendance_shift_ids=attendance_shift_ids,
        employee_ids=employee_ids,
        month=month,
        year=year,
        updated_after=updated_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    attendance_shift_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    year: int | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> GetApi20251001ResourcesProjectManagementTimeRecordsResponse200 | None:
    """Reads all Time records

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
        ids (list[int] | Unset): Time record ids to retrieve Example: [1, 2].
        project_worker_ids (list[int] | Unset): Project worker ids to retrieve Example: [1, 2].
        subproject_ids (list[int] | Unset): Subproject ids to retrieve Example: [1, 2].
        attendance_shift_ids (list[int] | Unset): Attendance shift ids to retrieve Example: [1,
            2].
        employee_ids (list[int] | Unset): Employee ids to retrieve Example: [1, 2].
        month (int | Unset): Month to filter Example: 1.
        year (int | Unset): Year to filter Example: 2021.
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesProjectManagementTimeRecordsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        project_worker_ids=project_worker_ids,
        subproject_ids=subproject_ids,
        attendance_shift_ids=attendance_shift_ids,
        employee_ids=employee_ids,
        month=month,
        year=year,
        updated_after=updated_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    attendance_shift_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    year: int | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesProjectManagementTimeRecordsResponse200]:
    """Reads all Time records

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
        ids (list[int] | Unset): Time record ids to retrieve Example: [1, 2].
        project_worker_ids (list[int] | Unset): Project worker ids to retrieve Example: [1, 2].
        subproject_ids (list[int] | Unset): Subproject ids to retrieve Example: [1, 2].
        attendance_shift_ids (list[int] | Unset): Attendance shift ids to retrieve Example: [1,
            2].
        employee_ids (list[int] | Unset): Employee ids to retrieve Example: [1, 2].
        month (int | Unset): Month to filter Example: 1.
        year (int | Unset): Year to filter Example: 2021.
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesProjectManagementTimeRecordsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_worker_ids=project_worker_ids,
        subproject_ids=subproject_ids,
        attendance_shift_ids=attendance_shift_ids,
        employee_ids=employee_ids,
        month=month,
        year=year,
        updated_after=updated_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    attendance_shift_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    year: int | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> GetApi20251001ResourcesProjectManagementTimeRecordsResponse200 | None:
    """Reads all Time records

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
        ids (list[int] | Unset): Time record ids to retrieve Example: [1, 2].
        project_worker_ids (list[int] | Unset): Project worker ids to retrieve Example: [1, 2].
        subproject_ids (list[int] | Unset): Subproject ids to retrieve Example: [1, 2].
        attendance_shift_ids (list[int] | Unset): Attendance shift ids to retrieve Example: [1,
            2].
        employee_ids (list[int] | Unset): Employee ids to retrieve Example: [1, 2].
        month (int | Unset): Month to filter Example: 1.
        year (int | Unset): Year to filter Example: 2021.
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesProjectManagementTimeRecordsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            project_worker_ids=project_worker_ids,
            subproject_ids=subproject_ids,
            attendance_shift_ids=attendance_shift_ids,
            employee_ids=employee_ids,
            month=month,
            year=year,
            updated_after=updated_after,
        )
    ).parsed
