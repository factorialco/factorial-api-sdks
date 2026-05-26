from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_finance_ledger_account_resources_resource_type import (
    GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType,
)
from ...models.get_api_20260401_resources_finance_ledger_account_resources_response_200 import (
    GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    resource_ids: list[int] | Unset = UNSET,
    resource_type: GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
    finance_account_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_resource_ids: list[int] | Unset = UNSET
    if not isinstance(resource_ids, Unset):
        json_resource_ids = resource_ids

    params["resource_ids[]"] = json_resource_ids

    json_resource_type: str | Unset = UNSET
    if not isinstance(resource_type, Unset):
        json_resource_type = resource_type.value

    params["resource_type"] = json_resource_type

    json_legal_entity_ids: list[int] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    params["updated_from"] = updated_from

    json_finance_account_ids: list[int] | Unset = UNSET
    if not isinstance(finance_account_ids, Unset):
        json_finance_account_ids = finance_account_ids

    params["finance_account_ids[]"] = json_finance_account_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/finance/ledger_account_resources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200]:
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
    resource_ids: list[int] | Unset = UNSET,
    resource_type: GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
    finance_account_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200]:
    """Reads all Ledger account resources

     Fetch one or all ledger account resource for the company.

    Args:
        ids (list[int] | Unset): Search ledger account resources by ID Example: [135].
        resource_ids (list[int] | Unset): Filter ledger account resources by resource ID Example:
            [155].
        resource_type (GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset):
            Filter ledger account resources by resource type Example: taxtype.
        legal_entity_ids (list[int] | Unset): Filter ledger account resources by legal entity ID
            Example: [13].
        updated_from (str | Unset): Filter ledger account resources by updated at Example:
            2021-01-01.
        finance_account_ids (list[int] | Unset): Filter ledger account resources by finance
            account ID Example: [15].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        resource_ids=resource_ids,
        resource_type=resource_type,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
        finance_account_ids=finance_account_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    resource_ids: list[int] | Unset = UNSET,
    resource_type: GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
    finance_account_ids: list[int] | Unset = UNSET,
) -> GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200 | None:
    """Reads all Ledger account resources

     Fetch one or all ledger account resource for the company.

    Args:
        ids (list[int] | Unset): Search ledger account resources by ID Example: [135].
        resource_ids (list[int] | Unset): Filter ledger account resources by resource ID Example:
            [155].
        resource_type (GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset):
            Filter ledger account resources by resource type Example: taxtype.
        legal_entity_ids (list[int] | Unset): Filter ledger account resources by legal entity ID
            Example: [13].
        updated_from (str | Unset): Filter ledger account resources by updated at Example:
            2021-01-01.
        finance_account_ids (list[int] | Unset): Filter ledger account resources by finance
            account ID Example: [15].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        resource_ids=resource_ids,
        resource_type=resource_type,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
        finance_account_ids=finance_account_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    resource_ids: list[int] | Unset = UNSET,
    resource_type: GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
    finance_account_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200]:
    """Reads all Ledger account resources

     Fetch one or all ledger account resource for the company.

    Args:
        ids (list[int] | Unset): Search ledger account resources by ID Example: [135].
        resource_ids (list[int] | Unset): Filter ledger account resources by resource ID Example:
            [155].
        resource_type (GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset):
            Filter ledger account resources by resource type Example: taxtype.
        legal_entity_ids (list[int] | Unset): Filter ledger account resources by legal entity ID
            Example: [13].
        updated_from (str | Unset): Filter ledger account resources by updated at Example:
            2021-01-01.
        finance_account_ids (list[int] | Unset): Filter ledger account resources by finance
            account ID Example: [15].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        resource_ids=resource_ids,
        resource_type=resource_type,
        legal_entity_ids=legal_entity_ids,
        updated_from=updated_from,
        finance_account_ids=finance_account_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    resource_ids: list[int] | Unset = UNSET,
    resource_type: GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    updated_from: str | Unset = UNSET,
    finance_account_ids: list[int] | Unset = UNSET,
) -> GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200 | None:
    """Reads all Ledger account resources

     Fetch one or all ledger account resource for the company.

    Args:
        ids (list[int] | Unset): Search ledger account resources by ID Example: [135].
        resource_ids (list[int] | Unset): Filter ledger account resources by resource ID Example:
            [155].
        resource_type (GetApi20260401ResourcesFinanceLedgerAccountResourcesResourceType | Unset):
            Filter ledger account resources by resource type Example: taxtype.
        legal_entity_ids (list[int] | Unset): Filter ledger account resources by legal entity ID
            Example: [13].
        updated_from (str | Unset): Filter ledger account resources by updated at Example:
            2021-01-01.
        finance_account_ids (list[int] | Unset): Filter ledger account resources by finance
            account ID Example: [15].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceLedgerAccountResourcesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            resource_ids=resource_ids,
            resource_type=resource_type,
            legal_entity_ids=legal_entity_ids,
            updated_from=updated_from,
            finance_account_ids=finance_account_ids,
        )
    ).parsed
