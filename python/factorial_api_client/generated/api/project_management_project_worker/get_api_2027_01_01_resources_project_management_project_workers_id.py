from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.project_management_project_worker import ProjectManagementProjectWorker
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/project_management/project_workers/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ProjectManagementProjectWorker | None:
    if response.status_code == 200:
        response_200 = ProjectManagementProjectWorker.from_dict(response.json())

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
) -> Response[ErrorResponse | ProjectManagementProjectWorker]:
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
) -> Response[ErrorResponse | ProjectManagementProjectWorker]:
    """Reads a single Project worker

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectManagementProjectWorker]
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
) -> ErrorResponse | ProjectManagementProjectWorker | None:
    """Reads a single Project worker

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectManagementProjectWorker
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ProjectManagementProjectWorker]:
    """Reads a single Project worker

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectManagementProjectWorker]
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
) -> ErrorResponse | ProjectManagementProjectWorker | None:
    """Reads a single Project worker

     ###### **What does it do?**
    This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to
    filter the results.
    ###### **Is it related to other entities?**
    A project_worker is always related to a project and a employee. Only a `project worker` is able to
    add time to a project using the `time_record` entity.
    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission to
    read project workers.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectManagementProjectWorker
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
