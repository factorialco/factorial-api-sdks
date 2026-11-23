from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_finance_categories_category_level import (
    GetApi20270101ResourcesFinanceCategoriesCategoryLevel,
)
from ...models.get_api_20270101_resources_finance_categories_response_200 import (
    GetApi20270101ResourcesFinanceCategoriesResponse200,
)
from ...models.get_api_20270101_resources_finance_categories_statuses import (
    GetApi20270101ResourcesFinanceCategoriesStatuses,
)
from ...models.get_api_20270101_resources_finance_categories_type import (
    GetApi20270101ResourcesFinanceCategoriesType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    company_ids: list[str] | Unset = UNSET,
    parent_category_ids: list[str] | Unset = UNSET,
    category_level: GetApi20270101ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20270101ResourcesFinanceCategoriesType,
    statuses: GetApi20270101ResourcesFinanceCategoriesStatuses,
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
        "url": "/api/2027-01-01/resources/finance/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesFinanceCategoriesResponse200.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200]:
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
    category_level: GetApi20270101ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20270101ResourcesFinanceCategoriesType,
    statuses: GetApi20270101ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200]:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20270101ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20270101ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20270101ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200]
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
    category_level: GetApi20270101ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20270101ResourcesFinanceCategoriesType,
    statuses: GetApi20270101ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200 | None:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20270101ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20270101ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20270101ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200
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
    category_level: GetApi20270101ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20270101ResourcesFinanceCategoriesType,
    statuses: GetApi20270101ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200]:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20270101ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20270101ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20270101ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200]
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
    category_level: GetApi20270101ResourcesFinanceCategoriesCategoryLevel,
    type_: GetApi20270101ResourcesFinanceCategoriesType,
    statuses: GetApi20270101ResourcesFinanceCategoriesStatuses,
    search: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200 | None:
    """Reads all Categories

     Fetch expense categories and subcategories for the company

    Args:
        ids (list[str] | Unset): Search categories by ID Example: ['1'].
        company_ids (list[str] | Unset): Search categories by company IDs Example: ['1'].
        parent_category_ids (list[str] | Unset): Search subcategories by parent category ID
            Example: ['2'].
        category_level (GetApi20270101ResourcesFinanceCategoriesCategoryLevel): Filter by category
            level Example: all.
        type_ (GetApi20270101ResourcesFinanceCategoriesType): Filter by category type Example:
            expense.
        statuses (GetApi20270101ResourcesFinanceCategoriesStatuses): Filter by category status
            Example: ['enabled'].
        search (str | Unset): Search by category label or identifier Example: accommodation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesFinanceCategoriesResponse200
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
