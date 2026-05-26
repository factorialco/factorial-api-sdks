from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_flexible_time_record import ProjectManagementFlexibleTimeRecord
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/2025-10-01/resources/project_management/flexible_time_records/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

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
) -> Response[ProjectManagementFlexibleTimeRecord]:
    """Deletes a Flexible time record

     ###### **What does it do?**
    This endpoint is used to delete a `flexible time record`.
    ###### **What params does it accept?**

      - `id`: the id of the `flexible time record` willing to be deleted.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to delete flexible time records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecord]
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
) -> ProjectManagementFlexibleTimeRecord | None:
    """Deletes a Flexible time record

     ###### **What does it do?**
    This endpoint is used to delete a `flexible time record`.
    ###### **What params does it accept?**

      - `id`: the id of the `flexible time record` willing to be deleted.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to delete flexible time records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecord
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectManagementFlexibleTimeRecord]:
    """Deletes a Flexible time record

     ###### **What does it do?**
    This endpoint is used to delete a `flexible time record`.
    ###### **What params does it accept?**

      - `id`: the id of the `flexible time record` willing to be deleted.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to delete flexible time records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecord]
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
) -> ProjectManagementFlexibleTimeRecord | None:
    """Deletes a Flexible time record

     ###### **What does it do?**
    This endpoint is used to delete a `flexible time record`.
    ###### **What params does it accept?**

      - `id`: the id of the `flexible time record` willing to be deleted.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature and users with the permission
    to delete flexible time records.

    Args:
        id (str):

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
        )
    ).parsed
