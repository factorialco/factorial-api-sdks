from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_contracts_contract_templates_response_200 import (
    GetApi20251001ResourcesContractsContractTemplatesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    contract_version_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["company_id"] = company_id

    params["contract_version_type"] = contract_version_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/contracts/contract_templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesContractsContractTemplatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesContractsContractTemplatesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesContractsContractTemplatesResponse200]:
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
    company_id: int | Unset = UNSET,
    contract_version_type: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesContractsContractTemplatesResponse200]:
    """Reads all Contract templates

     Read Contract Template

    Args:
        ids (list[int] | Unset): Filter by contract template IDs Example: [1].
        company_id (int | Unset): Filter by company ID Example: 1.
        contract_version_type (str | Unset): Filter by contract version type (e.g., es for Spain,
            fr for France) Example: es.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesContractsContractTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        contract_version_type=contract_version_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    contract_version_type: str | Unset = UNSET,
) -> GetApi20251001ResourcesContractsContractTemplatesResponse200 | None:
    """Reads all Contract templates

     Read Contract Template

    Args:
        ids (list[int] | Unset): Filter by contract template IDs Example: [1].
        company_id (int | Unset): Filter by company ID Example: 1.
        contract_version_type (str | Unset): Filter by contract version type (e.g., es for Spain,
            fr for France) Example: es.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesContractsContractTemplatesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_id=company_id,
        contract_version_type=contract_version_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    contract_version_type: str | Unset = UNSET,
) -> Response[GetApi20251001ResourcesContractsContractTemplatesResponse200]:
    """Reads all Contract templates

     Read Contract Template

    Args:
        ids (list[int] | Unset): Filter by contract template IDs Example: [1].
        company_id (int | Unset): Filter by company ID Example: 1.
        contract_version_type (str | Unset): Filter by contract version type (e.g., es for Spain,
            fr for France) Example: es.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesContractsContractTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        contract_version_type=contract_version_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    contract_version_type: str | Unset = UNSET,
) -> GetApi20251001ResourcesContractsContractTemplatesResponse200 | None:
    """Reads all Contract templates

     Read Contract Template

    Args:
        ids (list[int] | Unset): Filter by contract template IDs Example: [1].
        company_id (int | Unset): Filter by company ID Example: 1.
        contract_version_type (str | Unset): Filter by contract version type (e.g., es for Spain,
            fr for France) Example: es.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesContractsContractTemplatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_id=company_id,
            contract_version_type=contract_version_type,
        )
    ).parsed
