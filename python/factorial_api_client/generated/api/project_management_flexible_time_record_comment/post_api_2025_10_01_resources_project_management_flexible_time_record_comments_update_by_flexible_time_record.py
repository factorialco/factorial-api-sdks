from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20251001_resources_project_management_flexible_time_record_comments_update_by_flexible_time_record_body import (
    PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleTimeRecordBody,
)
from ...models.project_management_flexible_time_record_comment import (
    ProjectManagementFlexibleTimeRecordComment,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleTimeRecordBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/project_management/flexible_time_record_comments/update_by_flexible_time_record",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementFlexibleTimeRecordComment | None:
    if response.status_code == 200:
        response_200 = ProjectManagementFlexibleTimeRecordComment.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementFlexibleTimeRecordComment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleTimeRecordBody
    | Unset = UNSET,
) -> Response[ProjectManagementFlexibleTimeRecordComment]:
    """Update by flexible time records a Flexible time record comment

     ###### **What does it do?**
    This endpoint can be used to update the content for a `flexible time record comment`.
    ###### **What params does it accept?**

      - `content`: the new content for the comment.
      - `flexible_time_record_id`: the `flexible time record` to which the comment to be updated is
    associated.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleT
            imeRecordBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecordComment]
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
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleTimeRecordBody
    | Unset = UNSET,
) -> ProjectManagementFlexibleTimeRecordComment | None:
    """Update by flexible time records a Flexible time record comment

     ###### **What does it do?**
    This endpoint can be used to update the content for a `flexible time record comment`.
    ###### **What params does it accept?**

      - `content`: the new content for the comment.
      - `flexible_time_record_id`: the `flexible time record` to which the comment to be updated is
    associated.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleT
            imeRecordBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecordComment
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleTimeRecordBody
    | Unset = UNSET,
) -> Response[ProjectManagementFlexibleTimeRecordComment]:
    """Update by flexible time records a Flexible time record comment

     ###### **What does it do?**
    This endpoint can be used to update the content for a `flexible time record comment`.
    ###### **What params does it accept?**

      - `content`: the new content for the comment.
      - `flexible_time_record_id`: the `flexible time record` to which the comment to be updated is
    associated.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleT
            imeRecordBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementFlexibleTimeRecordComment]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleTimeRecordBody
    | Unset = UNSET,
) -> ProjectManagementFlexibleTimeRecordComment | None:
    """Update by flexible time records a Flexible time record comment

     ###### **What does it do?**
    This endpoint can be used to update the content for a `flexible time record comment`.
    ###### **What params does it accept?**

      - `content`: the new content for the comment.
      - `flexible_time_record_id`: the `flexible time record` to which the comment to be updated is
    associated.

    ###### **Who can use it?**
    Only companies who have enabled `projects_flexible_tracking` feature.

    Args:
        body (PostApi20251001ResourcesProjectManagementFlexibleTimeRecordCommentsUpdateByFlexibleT
            imeRecordBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementFlexibleTimeRecordComment
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
