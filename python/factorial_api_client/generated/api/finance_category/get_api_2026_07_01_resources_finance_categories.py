from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_finance_categories_category_level import (
    GetApi20260701ResourcesFinanceCategoriesCategoryLevel,
)
from ...models.get_api_20260701_resources_finance_categories_response_200 import (
    GetApi20260701ResourcesFinanceCategoriesResponse200,
)
from ...models.get_api_20260701_resources_finance_categories_statuses import (
    GetApi20260701ResourcesFinanceCategoriesStatuses,
)
from ...models.get_api_20260701_resources_finance_categories_type import (
    GetApi20260701ResourcesFinanceCategoriesType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    parent_category_ids: list[str] | Unset = UNSET,
    category_level: GetApi20260701ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20260701ResourcesFinanceCategoriesType,
    statuses: GetApi20260701ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_company_ids: list[str] | Unset = UNSET
    if not isinstance(company_ids, Unset):
        json_company_ids = company_ids

    params["company_ids[]"] = json_company_ids

    json_parent_category_ids: list[str] | Unset = UNSET
    if not isinstance(parent_category_ids, Unset):
        json_parent_category_ids = parent_category_ids

    params["parent_category_ids[]"] = json_parent_category_ids

    json_category_level = category_level.value
    params["category_level"] = json_category_level

    json_type_ = type_.value
    params["type"] = json_type_

    json_statuses = statuses.value
    params["statuses[]"] = json_statuses

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/finance/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesFinanceCategoriesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesFinanceCategoriesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesFinanceCategoriesResponse200]:
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
    company_ids: list[str] | Unset = UNSET,
    parent_category_ids: list[str] | Unset = UNSET,
    category_level: GetApi20260701ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20260701ResourcesFinanceCategoriesType,
    statuses: GetApi20260701ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceCategoriesResponse200]:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20260701ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20260701ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20260701ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceCategoriesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_ids=company_ids,
        parent_category_ids=parent_category_ids,
        category_level=category_level,
        type_=type_,
        statuses=statuses,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    parent_category_ids: list[str] | Unset = UNSET,
    category_level: GetApi20260701ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20260701ResourcesFinanceCategoriesType,
    statuses: GetApi20260701ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceCategoriesResponse200 | None:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20260701ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20260701ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20260701ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceCategoriesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_ids=company_ids,
        parent_category_ids=parent_category_ids,
        category_level=category_level,
        type_=type_,
        statuses=statuses,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    parent_category_ids: list[str] | Unset = UNSET,
    category_level: GetApi20260701ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20260701ResourcesFinanceCategoriesType,
    statuses: GetApi20260701ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> Response[GetApi20260701ResourcesFinanceCategoriesResponse200]:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20260701ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20260701ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20260701ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesFinanceCategoriesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_ids=company_ids,
        parent_category_ids=parent_category_ids,
        category_level=category_level,
        type_=type_,
        statuses=statuses,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    parent_category_ids: list[str] | Unset = UNSET,
    category_level: GetApi20260701ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20260701ResourcesFinanceCategoriesType,
    statuses: GetApi20260701ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> GetApi20260701ResourcesFinanceCategoriesResponse200 | None:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20260701ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20260701ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20260701ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesFinanceCategoriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_ids=company_ids,
            parent_category_ids=parent_category_ids,
            category_level=category_level,
            type_=type_,
            statuses=statuses,
            search=search,
        )
    ).parsed
