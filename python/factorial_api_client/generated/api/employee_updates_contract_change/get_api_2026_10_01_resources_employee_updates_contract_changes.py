from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_employee_updates_contract_changes_response_200 import (
    GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/employee_updates/contract_changes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200]:
    """Reads all Contract changes

     This endpoint can be used to retrieve a list of contract changes `employee updates` details.

    Args:
        ids (list[str] | Unset): filter by contract change incidence ids. Example: ['1', '2',
            '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200 | None:
    """Reads all Contract changes

     This endpoint can be used to retrieve a list of contract changes `employee updates` details.

    Args:
        ids (list[str] | Unset): filter by contract change incidence ids. Example: ['1', '2',
            '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200]:
    """Reads all Contract changes

     This endpoint can be used to retrieve a list of contract changes `employee updates` details.

    Args:
        ids (list[str] | Unset): filter by contract change incidence ids. Example: ['1', '2',
            '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200 | None:
    """Reads all Contract changes

     This endpoint can be used to retrieve a list of contract changes `employee updates` details.

    Args:
        ids (list[str] | Unset): filter by contract change incidence ids. Example: ['1', '2',
            '3'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesEmployeeUpdatesContractChangesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
        )
    ).parsed
