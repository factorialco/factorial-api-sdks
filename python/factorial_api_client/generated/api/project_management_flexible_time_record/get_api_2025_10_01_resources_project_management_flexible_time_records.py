from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_project_management_flexible_time_records_response_200 import (
    GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int],
    project_worker_ids: list[int],
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids[]"] = json_ids

    json_project_worker_ids = project_worker_ids

    params["project_worker_ids[]"] = json_project_worker_ids

    params["starts_on"] = starts_on

    params["ends_on"] = ends_on

    params["updated_after"] = updated_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/project_management/flexible_time_records",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    project_worker_ids: list[int],
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200]:
    """Reads all Flexible time records

     ###### **What does it do?**
    This endpoint can be used to retrieve a list of `flexible time records`. To fetch *flexible time
    record comments*, you have to use this
    [endpoint](https://apidoc.factorialhr.com/v2.0/reference/get_api-v2-resources-project-management-
    flexible-time-record-comments) and pass the `flexible_time_record_id` as a param.
    ###### **What params does it accept?**

      - `ids`: retrieve only the `flexible time records` that matches the `ids` passed in the request.
      - `project_worker_ids`: retrieve only the `flexible time records` assigned to any `project_worker`
    specified in the request.
      - `starts_on`: filter `flexible time records` that started **later** the given param.
      - `ends_on`: filter `flexible time records` that started **before** the given param.
      - `updated_after`: this parameter is needed to filter flexible time records created or updated
    after a date.

    ###### **Is it related to other entities?**
    A `flexible time record` is always related to a `project worker` and can optionally be related to a
    `subproject`.
    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to read flexible time records.

    Args:
        ids (list[int]):
        project_worker_ids (list[int]):
        starts_on (str | Unset):
        ends_on (str | Unset):
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_worker_ids=project_worker_ids,
        starts_on=starts_on,
        ends_on=ends_on,
        updated_after=updated_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    project_worker_ids: list[int],
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200 | None:
    """Reads all Flexible time records

     ###### **What does it do?**
    This endpoint can be used to retrieve a list of `flexible time records`. To fetch *flexible time
    record comments*, you have to use this
    [endpoint](https://apidoc.factorialhr.com/v2.0/reference/get_api-v2-resources-project-management-
    flexible-time-record-comments) and pass the `flexible_time_record_id` as a param.
    ###### **What params does it accept?**

      - `ids`: retrieve only the `flexible time records` that matches the `ids` passed in the request.
      - `project_worker_ids`: retrieve only the `flexible time records` assigned to any `project_worker`
    specified in the request.
      - `starts_on`: filter `flexible time records` that started **later** the given param.
      - `ends_on`: filter `flexible time records` that started **before** the given param.
      - `updated_after`: this parameter is needed to filter flexible time records created or updated
    after a date.

    ###### **Is it related to other entities?**
    A `flexible time record` is always related to a `project worker` and can optionally be related to a
    `subproject`.
    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to read flexible time records.

    Args:
        ids (list[int]):
        project_worker_ids (list[int]):
        starts_on (str | Unset):
        ends_on (str | Unset):
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        project_worker_ids=project_worker_ids,
        starts_on=starts_on,
        ends_on=ends_on,
        updated_after=updated_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    project_worker_ids: list[int],
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200]:
    """Reads all Flexible time records

     ###### **What does it do?**
    This endpoint can be used to retrieve a list of `flexible time records`. To fetch *flexible time
    record comments*, you have to use this
    [endpoint](https://apidoc.factorialhr.com/v2.0/reference/get_api-v2-resources-project-management-
    flexible-time-record-comments) and pass the `flexible_time_record_id` as a param.
    ###### **What params does it accept?**

      - `ids`: retrieve only the `flexible time records` that matches the `ids` passed in the request.
      - `project_worker_ids`: retrieve only the `flexible time records` assigned to any `project_worker`
    specified in the request.
      - `starts_on`: filter `flexible time records` that started **later** the given param.
      - `ends_on`: filter `flexible time records` that started **before** the given param.
      - `updated_after`: this parameter is needed to filter flexible time records created or updated
    after a date.

    ###### **Is it related to other entities?**
    A `flexible time record` is always related to a `project worker` and can optionally be related to a
    `subproject`.
    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to read flexible time records.

    Args:
        ids (list[int]):
        project_worker_ids (list[int]):
        starts_on (str | Unset):
        ends_on (str | Unset):
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        project_worker_ids=project_worker_ids,
        starts_on=starts_on,
        ends_on=ends_on,
        updated_after=updated_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    project_worker_ids: list[int],
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
    updated_after: str | Unset = UNSET,
) -> GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200 | None:
    """Reads all Flexible time records

     ###### **What does it do?**
    This endpoint can be used to retrieve a list of `flexible time records`. To fetch *flexible time
    record comments*, you have to use this
    [endpoint](https://apidoc.factorialhr.com/v2.0/reference/get_api-v2-resources-project-management-
    flexible-time-record-comments) and pass the `flexible_time_record_id` as a param.
    ###### **What params does it accept?**

      - `ids`: retrieve only the `flexible time records` that matches the `ids` passed in the request.
      - `project_worker_ids`: retrieve only the `flexible time records` assigned to any `project_worker`
    specified in the request.
      - `starts_on`: filter `flexible time records` that started **later** the given param.
      - `ends_on`: filter `flexible time records` that started **before** the given param.
      - `updated_after`: this parameter is needed to filter flexible time records created or updated
    after a date.

    ###### **Is it related to other entities?**
    A `flexible time record` is always related to a `project worker` and can optionally be related to a
    `subproject`.
    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to read flexible time records.

    Args:
        ids (list[int]):
        project_worker_ids (list[int]):
        starts_on (str | Unset):
        ends_on (str | Unset):
        updated_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesProjectManagementFlexibleTimeRecordsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            project_worker_ids=project_worker_ids,
            starts_on=starts_on,
            ends_on=ends_on,
            updated_after=updated_after,
        )
    ).parsed
