from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.project_management_time_record import ProjectManagementTimeRecord
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/project_management/time_records/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

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
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ProjectManagementTimeRecord]:
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
        Response[ErrorResponse | ProjectManagementTimeRecord]
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
) -> ErrorResponse | ProjectManagementTimeRecord | None:
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
        ErrorResponse | ProjectManagementTimeRecord
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ProjectManagementTimeRecord]:
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
        Response[ErrorResponse | ProjectManagementTimeRecord]
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
) -> ErrorResponse | ProjectManagementTimeRecord | None:
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
        ErrorResponse | ProjectManagementTimeRecord
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
