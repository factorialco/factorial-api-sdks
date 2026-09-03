from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_documents_documents_response_200 import (
    GetApi20261001ResourcesDocumentsDocumentsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    by_bookkeeper_documents: bool | Unset = UNSET,
    by_pending_assignment: bool,
    by_trash_bin: bool,
    by_without_folder: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    folder_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    leave_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["by_bookkeeper_documents"] = by_bookkeeper_documents

    params["by_pending_assignment"] = by_pending_assignment

    params["by_trash_bin"] = by_trash_bin

    params["by_without_folder"] = by_without_folder

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["folder_id"] = folder_id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["leave_id"] = leave_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/documents/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesDocumentsDocumentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesDocumentsDocumentsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesDocumentsDocumentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    by_bookkeeper_documents: bool | Unset = UNSET,
    by_pending_assignment: bool,
    by_trash_bin: bool,
    by_without_folder: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    folder_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    leave_id: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesDocumentsDocumentsResponse200]:
    """Reads all Documents

     Reads all Documents

    Args:
        by_bookkeeper_documents (bool | Unset): flag to indicate if the document belongs to a
            bookkeeper. Example: True.
        by_pending_assignment (bool): flag to indicate if the document is pending assignment.
            Example: True.
        by_trash_bin (bool): flag to indicate if the document is in the trash bin. Example: True.
        by_without_folder (bool | Unset): flag to indicate if the document doesn't have a folder.
            Example: True.
        employee_ids (list[str] | Unset): list of employee identifiers. Example: ['1', '2', '3'].
        folder_id (str | Unset): folder identifier. Example: 1.
        ids (list[str] | Unset): list of document identifiers. Example: ['1', '2', '3'].
        leave_id (str | Unset): leave identifier associated to the document, refers to
            /timeoff/leaves endpoint. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesDocumentsDocumentsResponse200]
    """

    kwargs = _get_kwargs(
        by_bookkeeper_documents=by_bookkeeper_documents,
        by_pending_assignment=by_pending_assignment,
        by_trash_bin=by_trash_bin,
        by_without_folder=by_without_folder,
        employee_ids=employee_ids,
        folder_id=folder_id,
        ids=ids,
        leave_id=leave_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    by_bookkeeper_documents: bool | Unset = UNSET,
    by_pending_assignment: bool,
    by_trash_bin: bool,
    by_without_folder: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    folder_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    leave_id: str | Unset = UNSET,
) -> GetApi20261001ResourcesDocumentsDocumentsResponse200 | None:
    """Reads all Documents

     Reads all Documents

    Args:
        by_bookkeeper_documents (bool | Unset): flag to indicate if the document belongs to a
            bookkeeper. Example: True.
        by_pending_assignment (bool): flag to indicate if the document is pending assignment.
            Example: True.
        by_trash_bin (bool): flag to indicate if the document is in the trash bin. Example: True.
        by_without_folder (bool | Unset): flag to indicate if the document doesn't have a folder.
            Example: True.
        employee_ids (list[str] | Unset): list of employee identifiers. Example: ['1', '2', '3'].
        folder_id (str | Unset): folder identifier. Example: 1.
        ids (list[str] | Unset): list of document identifiers. Example: ['1', '2', '3'].
        leave_id (str | Unset): leave identifier associated to the document, refers to
            /timeoff/leaves endpoint. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesDocumentsDocumentsResponse200
    """

    return sync_detailed(
        client=client,
        by_bookkeeper_documents=by_bookkeeper_documents,
        by_pending_assignment=by_pending_assignment,
        by_trash_bin=by_trash_bin,
        by_without_folder=by_without_folder,
        employee_ids=employee_ids,
        folder_id=folder_id,
        ids=ids,
        leave_id=leave_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    by_bookkeeper_documents: bool | Unset = UNSET,
    by_pending_assignment: bool,
    by_trash_bin: bool,
    by_without_folder: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    folder_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    leave_id: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesDocumentsDocumentsResponse200]:
    """Reads all Documents

     Reads all Documents

    Args:
        by_bookkeeper_documents (bool | Unset): flag to indicate if the document belongs to a
            bookkeeper. Example: True.
        by_pending_assignment (bool): flag to indicate if the document is pending assignment.
            Example: True.
        by_trash_bin (bool): flag to indicate if the document is in the trash bin. Example: True.
        by_without_folder (bool | Unset): flag to indicate if the document doesn't have a folder.
            Example: True.
        employee_ids (list[str] | Unset): list of employee identifiers. Example: ['1', '2', '3'].
        folder_id (str | Unset): folder identifier. Example: 1.
        ids (list[str] | Unset): list of document identifiers. Example: ['1', '2', '3'].
        leave_id (str | Unset): leave identifier associated to the document, refers to
            /timeoff/leaves endpoint. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesDocumentsDocumentsResponse200]
    """

    kwargs = _get_kwargs(
        by_bookkeeper_documents=by_bookkeeper_documents,
        by_pending_assignment=by_pending_assignment,
        by_trash_bin=by_trash_bin,
        by_without_folder=by_without_folder,
        employee_ids=employee_ids,
        folder_id=folder_id,
        ids=ids,
        leave_id=leave_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    by_bookkeeper_documents: bool | Unset = UNSET,
    by_pending_assignment: bool,
    by_trash_bin: bool,
    by_without_folder: bool | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    folder_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    leave_id: str | Unset = UNSET,
) -> GetApi20261001ResourcesDocumentsDocumentsResponse200 | None:
    """Reads all Documents

     Reads all Documents

    Args:
        by_bookkeeper_documents (bool | Unset): flag to indicate if the document belongs to a
            bookkeeper. Example: True.
        by_pending_assignment (bool): flag to indicate if the document is pending assignment.
            Example: True.
        by_trash_bin (bool): flag to indicate if the document is in the trash bin. Example: True.
        by_without_folder (bool | Unset): flag to indicate if the document doesn't have a folder.
            Example: True.
        employee_ids (list[str] | Unset): list of employee identifiers. Example: ['1', '2', '3'].
        folder_id (str | Unset): folder identifier. Example: 1.
        ids (list[str] | Unset): list of document identifiers. Example: ['1', '2', '3'].
        leave_id (str | Unset): leave identifier associated to the document, refers to
            /timeoff/leaves endpoint. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesDocumentsDocumentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            by_bookkeeper_documents=by_bookkeeper_documents,
            by_pending_assignment=by_pending_assignment,
            by_trash_bin=by_trash_bin,
            by_without_folder=by_without_folder,
            employee_ids=employee_ids,
            folder_id=folder_id,
            ids=ids,
            leave_id=leave_id,
        )
    ).parsed
