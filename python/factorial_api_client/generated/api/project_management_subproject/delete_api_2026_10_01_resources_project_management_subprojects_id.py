from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_management_subproject import ProjectManagementSubproject
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/2026-10-01/resources/project_management/subprojects/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectManagementSubproject | None:
    if response.status_code == 200:
        response_200 = ProjectManagementSubproject.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectManagementSubproject]:
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
) -> Response[ProjectManagementSubproject]:
    """Deletes a Subproject

     ###### **What does it do?**
    This deletes a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementSubproject]
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
) -> ProjectManagementSubproject | None:
    """Deletes a Subproject

     ###### **What does it do?**
    This deletes a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementSubproject
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectManagementSubproject]:
    """Deletes a Subproject

     ###### **What does it do?**
    This deletes a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectManagementSubproject]
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
) -> ProjectManagementSubproject | None:
    """Deletes a Subproject

     ###### **What does it do?**
    This deletes a subproject.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the
    project owning the subproject.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectManagementSubproject
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
