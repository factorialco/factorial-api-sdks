from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_companies_legal_entities_response_200 import (
    GetApi20260401ResourcesCompaniesLegalEntitiesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    companies_ids: list[int] | Unset = UNSET,
    country_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employees_ids: list[int] | Unset = UNSET
    if not isinstance(employees_ids, Unset):
        json_employees_ids = employees_ids

    params["employees_ids[]"] = json_employees_ids

    json_companies_ids: list[int] | Unset = UNSET
    if not isinstance(companies_ids, Unset):
        json_companies_ids = companies_ids

    params["companies_ids[]"] = json_companies_ids

    json_country_ids: list[str] | Unset = UNSET
    if not isinstance(country_ids, Unset):
        json_country_ids = country_ids

    params["country_ids[]"] = json_country_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/companies/legal_entities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesCompaniesLegalEntitiesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesCompaniesLegalEntitiesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesCompaniesLegalEntitiesResponse200]:
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
    employees_ids: list[int] | Unset = UNSET,
    companies_ids: list[int] | Unset = UNSET,
    country_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesCompaniesLegalEntitiesResponse200]:
    """Reads all Legal entities

     Reads all Legal entities

    Args:
        ids (list[int] | Unset): identifier of the legal entity Example: [754, 98].
        employees_ids (list[int] | Unset): identifier of the employees asigned to the legal entity
            Example: [1, 2, 3].
        companies_ids (list[int] | Unset): identifier of the companies to which the legal entity
            belongs Example: [1].
        country_ids (list[str] | Unset): country code of the legal entity Example: ['es'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesCompaniesLegalEntitiesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employees_ids=employees_ids,
        companies_ids=companies_ids,
        country_ids=country_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    companies_ids: list[int] | Unset = UNSET,
    country_ids: list[str] | Unset = UNSET,
) -> GetApi20260401ResourcesCompaniesLegalEntitiesResponse200 | None:
    """Reads all Legal entities

     Reads all Legal entities

    Args:
        ids (list[int] | Unset): identifier of the legal entity Example: [754, 98].
        employees_ids (list[int] | Unset): identifier of the employees asigned to the legal entity
            Example: [1, 2, 3].
        companies_ids (list[int] | Unset): identifier of the companies to which the legal entity
            belongs Example: [1].
        country_ids (list[str] | Unset): country code of the legal entity Example: ['es'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesCompaniesLegalEntitiesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employees_ids=employees_ids,
        companies_ids=companies_ids,
        country_ids=country_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    companies_ids: list[int] | Unset = UNSET,
    country_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesCompaniesLegalEntitiesResponse200]:
    """Reads all Legal entities

     Reads all Legal entities

    Args:
        ids (list[int] | Unset): identifier of the legal entity Example: [754, 98].
        employees_ids (list[int] | Unset): identifier of the employees asigned to the legal entity
            Example: [1, 2, 3].
        companies_ids (list[int] | Unset): identifier of the companies to which the legal entity
            belongs Example: [1].
        country_ids (list[str] | Unset): country code of the legal entity Example: ['es'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesCompaniesLegalEntitiesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employees_ids=employees_ids,
        companies_ids=companies_ids,
        country_ids=country_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    employees_ids: list[int] | Unset = UNSET,
    companies_ids: list[int] | Unset = UNSET,
    country_ids: list[str] | Unset = UNSET,
) -> GetApi20260401ResourcesCompaniesLegalEntitiesResponse200 | None:
    """Reads all Legal entities

     Reads all Legal entities

    Args:
        ids (list[int] | Unset): identifier of the legal entity Example: [754, 98].
        employees_ids (list[int] | Unset): identifier of the employees asigned to the legal entity
            Example: [1, 2, 3].
        companies_ids (list[int] | Unset): identifier of the companies to which the legal entity
            belongs Example: [1].
        country_ids (list[str] | Unset): country code of the legal entity Example: ['es'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesCompaniesLegalEntitiesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employees_ids=employees_ids,
            companies_ids=companies_ids,
            country_ids=country_ids,
        )
    ).parsed
