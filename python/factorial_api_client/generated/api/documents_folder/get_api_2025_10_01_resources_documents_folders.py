from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_documents_folders_response_200 import (
    GetApi20251001ResourcesDocumentsFoldersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["employee_id"] = employee_id

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/documents/folders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesDocumentsFoldersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesDocumentsFoldersResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesDocumentsFoldersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesDocumentsFoldersResponse200]:
    """Reads all Folders

     Get all folders.

    Args:
        active (bool | Unset): Active folder. Example: True.
        employee_id (int | Unset): Employee id Example: 15.
        ids (list[int] | Unset): ids of the folders. Example: [10, 12, 13].
        name (str | Unset): Name of the folder. Example: Payslips.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesDocumentsFoldersResponse200]
    """

    kwargs = _get_kwargs(
        active=active,
        employee_id=employee_id,
        ids=ids,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
) -> GetApi20251001ResourcesDocumentsFoldersResponse200 | None:
    """Reads all Folders

     Get all folders.

    Args:
        active (bool | Unset): Active folder. Example: True.
        employee_id (int | Unset): Employee id Example: 15.
        ids (list[int] | Unset): ids of the folders. Example: [10, 12, 13].
        name (str | Unset): Name of the folder. Example: Payslips.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesDocumentsFoldersResponse200
    """

    return sync_detailed(
        client=client,
        active=active,
        employee_id=employee_id,
        ids=ids,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesDocumentsFoldersResponse200]:
    """Reads all Folders

     Get all folders.

    Args:
        active (bool | Unset): Active folder. Example: True.
        employee_id (int | Unset): Employee id Example: 15.
        ids (list[int] | Unset): ids of the folders. Example: [10, 12, 13].
        name (str | Unset): Name of the folder. Example: Payslips.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesDocumentsFoldersResponse200]
    """

    kwargs = _get_kwargs(
        active=active,
        employee_id=employee_id,
        ids=ids,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
) -> GetApi20251001ResourcesDocumentsFoldersResponse200 | None:
    """Reads all Folders

     Get all folders.

    Args:
        active (bool | Unset): Active folder. Example: True.
        employee_id (int | Unset): Employee id Example: 15.
        ids (list[int] | Unset): ids of the folders. Example: [10, 12, 13].
        name (str | Unset): Name of the folder. Example: Payslips.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesDocumentsFoldersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            employee_id=employee_id,
            ids=ids,
            name=name,
        )
    ).parsed
