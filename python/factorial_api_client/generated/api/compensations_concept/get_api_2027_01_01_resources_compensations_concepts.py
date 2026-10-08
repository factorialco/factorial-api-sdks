from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_compensations_concepts_categories import (
    GetApi20270101ResourcesCompensationsConceptsCategories,
)
from ...models.get_api_20270101_resources_compensations_concepts_response_200 import (
    GetApi20270101ResourcesCompensationsConceptsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20270101ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_categories: str | Unset = UNSET
    if not isinstance(categories, Unset):
        json_categories = categories.value

    params["categories[]"] = json_categories

    params["with_active_status"] = with_active_status

    params["enabled"] = enabled

    params["default"] = default

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/compensations/concepts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesCompensationsConceptsResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200]:
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
    categories: GetApi20270101ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200]:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20270101ResourcesCompensationsConceptsCategories | Unset): Return only
            the concepts in these categories: `earnings_fixed_salary`, `earnings_variable`,
            `earnings_benefits_in_kind`, `earnings_others`, `deductions`, `company_contribution` or
            `summarized_values`. Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): Set to true to return only the concepts Factorial ships by
            default, leaving out the ones the company created itself. Passing false has no effect.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
        enabled=enabled,
        default=default,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20270101ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200 | None:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20270101ResourcesCompensationsConceptsCategories | Unset): Return only
            the concepts in these categories: `earnings_fixed_salary`, `earnings_variable`,
            `earnings_benefits_in_kind`, `earnings_others`, `deductions`, `company_contribution` or
            `summarized_values`. Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): Set to true to return only the concepts Factorial ships by
            default, leaving out the ones the company created itself. Passing false has no effect.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
        enabled=enabled,
        default=default,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20270101ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200]:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20270101ResourcesCompensationsConceptsCategories | Unset): Return only
            the concepts in these categories: `earnings_fixed_salary`, `earnings_variable`,
            `earnings_benefits_in_kind`, `earnings_others`, `deductions`, `company_contribution` or
            `summarized_values`. Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): Set to true to return only the concepts Factorial ships by
            default, leaving out the ones the company created itself. Passing false has no effect.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        categories=categories,
        with_active_status=with_active_status,
        enabled=enabled,
        default=default,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    categories: GetApi20270101ResourcesCompensationsConceptsCategories | Unset = UNSET,
    with_active_status: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    default: bool | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200 | None:
    """Reads all Concepts

     Retrieves compensation concepts (custom and default)

    Args:
        ids (list[str] | Unset): Filter by concept ids Example: ['1'].
        categories (GetApi20270101ResourcesCompensationsConceptsCategories | Unset): Return only
            the concepts in these categories: `earnings_fixed_salary`, `earnings_variable`,
            `earnings_benefits_in_kind`, `earnings_others`, `deductions`, `company_contribution` or
            `summarized_values`. Example: ['earnings_fixed_salary', 'deductions'].
        with_active_status (bool | Unset): When true, returns only active concepts Example: True.
        enabled (bool | Unset): When true, returns active concepts only; when false, only inactive
            Example: True.
        default (bool | Unset): Set to true to return only the concepts Factorial ships by
            default, leaving out the ones the company created itself. Passing false has no effect.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesCompensationsConceptsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            categories=categories,
            with_active_status=with_active_status,
            enabled=enabled,
            default=default,
        )
    ).parsed
