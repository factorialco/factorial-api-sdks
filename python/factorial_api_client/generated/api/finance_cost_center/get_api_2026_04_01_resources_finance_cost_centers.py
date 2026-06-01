from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_finance_cost_centers_response_200 import (
    GetApi20260401ResourcesFinanceCostCentersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    include_actives_on_date: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["company_id"] = company_id

    json_legal_entity_ids: list[int] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    params["include_actives_on_date"] = include_actives_on_date

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/finance/cost_centers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesFinanceCostCentersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesFinanceCostCentersResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesFinanceCostCentersResponse200]:
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
    legal_entity_ids: list[int] | Unset = UNSET,
    include_actives_on_date: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesFinanceCostCentersResponse200]:
    """Reads all Cost centers

     Reads all Cost centers

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        legal_entity_ids (list[int] | Unset):
        include_actives_on_date (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceCostCentersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        legal_entity_ids=legal_entity_ids,
        include_actives_on_date=include_actives_on_date,
        search=search,
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
    legal_entity_ids: list[int] | Unset = UNSET,
    include_actives_on_date: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> GetApi20260401ResourcesFinanceCostCentersResponse200 | None:
    """Reads all Cost centers

     Reads all Cost centers

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        legal_entity_ids (list[int] | Unset):
        include_actives_on_date (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceCostCentersResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_id=company_id,
        legal_entity_ids=legal_entity_ids,
        include_actives_on_date=include_actives_on_date,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    include_actives_on_date: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesFinanceCostCentersResponse200]:
    """Reads all Cost centers

     Reads all Cost centers

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        legal_entity_ids (list[int] | Unset):
        include_actives_on_date (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesFinanceCostCentersResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        legal_entity_ids=legal_entity_ids,
        include_actives_on_date=include_actives_on_date,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    legal_entity_ids: list[int] | Unset = UNSET,
    include_actives_on_date: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> GetApi20260401ResourcesFinanceCostCentersResponse200 | None:
    """Reads all Cost centers

     Reads all Cost centers

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        legal_entity_ids (list[int] | Unset):
        include_actives_on_date (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesFinanceCostCentersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_id=company_id,
            legal_entity_ids=legal_entity_ids,
            include_actives_on_date=include_actives_on_date,
            search=search,
        )
    ).parsed
