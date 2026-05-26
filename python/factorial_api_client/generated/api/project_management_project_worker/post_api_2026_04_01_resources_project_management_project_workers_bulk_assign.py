from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_20260401_resources_project_management_project_workers_bulk_assign_body import (
    PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody,
)
from ...models.project_management_project_worker import ProjectManagementProjectWorker
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-04-01/resources/project_management/project_workers/bulk_assign",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ProjectManagementProjectWorker] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProjectManagementProjectWorker.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ProjectManagementProjectWorker]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset = UNSET,
) -> Response[list[ProjectManagementProjectWorker]]:
    """Bulk assigns a Project worker

     ###### **What does it do?**
    This method is used to specify a set of employees that should be assigned as a result of the
    execution. All the employees in the list will be assigned and all others will be unassigned.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProjectManagementProjectWorker]]
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
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset = UNSET,
) -> list[ProjectManagementProjectWorker] | None:
    """Bulk assigns a Project worker

     ###### **What does it do?**
    This method is used to specify a set of employees that should be assigned as a result of the
    execution. All the employees in the list will be assigned and all others will be unassigned.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProjectManagementProjectWorker]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset = UNSET,
) -> Response[list[ProjectManagementProjectWorker]]:
    """Bulk assigns a Project worker

     ###### **What does it do?**
    This method is used to specify a set of employees that should be assigned as a result of the
    execution. All the employees in the list will be assigned and all others will be unassigned.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProjectManagementProjectWorker]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset = UNSET,
) -> list[ProjectManagementProjectWorker] | None:
    """Bulk assigns a Project worker

     ###### **What does it do?**
    This method is used to specify a set of employees that should be assigned as a result of the
    execution. All the employees in the list will be assigned and all others will be unassigned.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with a role in the given
    project.

    Args:
        body (PostApi20260401ResourcesProjectManagementProjectWorkersBulkAssignBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProjectManagementProjectWorker]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
