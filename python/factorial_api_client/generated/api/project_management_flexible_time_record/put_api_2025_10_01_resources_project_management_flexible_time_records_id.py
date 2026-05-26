from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_flexible_time_record import ProjectManagementFlexibleTimeRecord
from ...models.put_api_20251001_resources_project_management_flexible_time_records_id_body import (
    PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2025-10-01/resources/project_management/flexible_time_records/{id}".format(
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
) -> ProjectManagementFlexibleTimeRecord | None:
    if response.status_code == 200:
        response_200 = ProjectManagementFlexibleTimeRecord.from_dict(response.json())

        return response_200

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset = UNSET,
) -> Response[ProjectManagementFlexibleTimeRecord]:
    """Updates a Flexible time record

     ###### **What does it do?**
    This endpoint is used to update the amount of time that has been imputed for the `flexible time
    record`.
    ###### **What params does it accept?**

      - `imputed minutes`: the new amount of time that has to be imputed, in minutes.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to update flexible time records.

    Args:
        id (str):
        body (PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecord]
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
    body: PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset = UNSET,
) -> ProjectManagementFlexibleTimeRecord | None:
    """Updates a Flexible time record

     ###### **What does it do?**
    This endpoint is used to update the amount of time that has been imputed for the `flexible time
    record`.
    ###### **What params does it accept?**

      - `imputed minutes`: the new amount of time that has to be imputed, in minutes.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to update flexible time records.

    Args:
        id (str):
        body (PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecord
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
    body: PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset = UNSET,
) -> Response[ProjectManagementFlexibleTimeRecord]:
    """Updates a Flexible time record

     ###### **What does it do?**
    This endpoint is used to update the amount of time that has been imputed for the `flexible time
    record`.
    ###### **What params does it accept?**

      - `imputed minutes`: the new amount of time that has to be imputed, in minutes.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to update flexible time records.

    Args:
        id (str):
        body (PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecord]
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
    body: PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset = UNSET,
) -> ProjectManagementFlexibleTimeRecord | None:
    """Updates a Flexible time record

     ###### **What does it do?**
    This endpoint is used to update the amount of time that has been imputed for the `flexible time
    record`.
    ###### **What params does it accept?**

      - `imputed minutes`: the new amount of time that has to be imputed, in minutes.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to update flexible time records.

    Args:
        id (str):
        body (PutApi20251001ResourcesProjectManagementFlexibleTimeRecordsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecord
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
