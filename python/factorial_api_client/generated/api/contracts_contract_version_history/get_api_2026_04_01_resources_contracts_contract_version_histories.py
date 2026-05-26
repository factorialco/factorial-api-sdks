from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_contracts_contract_version_histories_response_200 import (
    GetApi20260401ResourcesContractsContractVersionHistoriesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    contract_version_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    current_on: str | Unset = UNSET,
    changes_lteq: str | Unset = UNSET,
    changes_gteq: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_contract_version_ids: list[int] | Unset = UNSET
    if not isinstance(contract_version_ids, Unset):
        json_contract_version_ids = contract_version_ids

    params["contract_version_ids[]"] = json_contract_version_ids

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["current_on"] = current_on

    params["changes_lteq"] = changes_lteq

    params["changes_gteq"] = changes_gteq

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/contracts/contract_version_histories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesContractsContractVersionHistoriesResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20260401ResourcesContractsContractVersionHistoriesResponse200.from_dict(
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
) -> Response[GetApi20260401ResourcesContractsContractVersionHistoriesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    contract_version_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    current_on: str | Unset = UNSET,
    changes_lteq: str | Unset = UNSET,
    changes_gteq: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesContractsContractVersionHistoriesResponse200]:
    """Reads all Contract version histories

     Reads all Contract version histories

    Args:
        ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        contract_version_ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        employee_ids (list[int] | Unset): the ids of the employees. Example: 1.
        current_on (str | Unset): the date to filter the contract version histories. Example:
            2024-10-06.
        changes_lteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-07.
        changes_gteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-05.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesContractsContractVersionHistoriesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        contract_version_ids=contract_version_ids,
        employee_ids=employee_ids,
        current_on=current_on,
        changes_lteq=changes_lteq,
        changes_gteq=changes_gteq,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    contract_version_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    current_on: str | Unset = UNSET,
    changes_lteq: str | Unset = UNSET,
    changes_gteq: str | Unset = UNSET,
) -> GetApi20260401ResourcesContractsContractVersionHistoriesResponse200 | None:
    """Reads all Contract version histories

     Reads all Contract version histories

    Args:
        ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        contract_version_ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        employee_ids (list[int] | Unset): the ids of the employees. Example: 1.
        current_on (str | Unset): the date to filter the contract version histories. Example:
            2024-10-06.
        changes_lteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-07.
        changes_gteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-05.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesContractsContractVersionHistoriesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        contract_version_ids=contract_version_ids,
        employee_ids=employee_ids,
        current_on=current_on,
        changes_lteq=changes_lteq,
        changes_gteq=changes_gteq,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    contract_version_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    current_on: str | Unset = UNSET,
    changes_lteq: str | Unset = UNSET,
    changes_gteq: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesContractsContractVersionHistoriesResponse200]:
    """Reads all Contract version histories

     Reads all Contract version histories

    Args:
        ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        contract_version_ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        employee_ids (list[int] | Unset): the ids of the employees. Example: 1.
        current_on (str | Unset): the date to filter the contract version histories. Example:
            2024-10-06.
        changes_lteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-07.
        changes_gteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-05.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesContractsContractVersionHistoriesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        contract_version_ids=contract_version_ids,
        employee_ids=employee_ids,
        current_on=current_on,
        changes_lteq=changes_lteq,
        changes_gteq=changes_gteq,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    contract_version_ids: list[int] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    current_on: str | Unset = UNSET,
    changes_lteq: str | Unset = UNSET,
    changes_gteq: str | Unset = UNSET,
) -> GetApi20260401ResourcesContractsContractVersionHistoriesResponse200 | None:
    """Reads all Contract version histories

     Reads all Contract version histories

    Args:
        ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        contract_version_ids (list[int] | Unset): the ids of the contract versions. Example: 1.
        employee_ids (list[int] | Unset): the ids of the employees. Example: 1.
        current_on (str | Unset): the date to filter the contract version histories. Example:
            2024-10-06.
        changes_lteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-07.
        changes_gteq (str | Unset): the date to filter the contract version histories. Example:
            2024-10-05.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesContractsContractVersionHistoriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            contract_version_ids=contract_version_ids,
            employee_ids=employee_ids,
            current_on=current_on,
            changes_lteq=changes_lteq,
            changes_gteq=changes_gteq,
        )
    ).parsed
