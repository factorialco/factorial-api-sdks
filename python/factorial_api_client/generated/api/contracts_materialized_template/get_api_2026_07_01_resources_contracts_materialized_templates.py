from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_contracts_materialized_templates_response_200 import (
    GetApi20260701ResourcesContractsMaterializedTemplatesResponse200,
)
from ...models.get_api_20260701_resources_contracts_materialized_templates_template_type import (
    GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    company_id: str,
    legal_entity_ids: list[str] | Unset = UNSET,
    countries: list[str] | Unset = UNSET,
    template_type: GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType,
    field_ids: list[str] | Unset = UNSET,
    include_archived: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["company_id"] = company_id

    json_legal_entity_ids: list[str] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    json_countries: list[str] | Unset = UNSET
    if not isinstance(countries, Unset):
        json_countries = countries

    params["countries[]"] = json_countries

    json_template_type = template_type.value
    params["template_type"] = json_template_type

    json_field_ids: list[str] | Unset = UNSET
    if not isinstance(field_ids, Unset):
        json_field_ids = field_ids

    params["field_ids[]"] = json_field_ids

    params["include_archived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/contracts/materialized_templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesContractsMaterializedTemplatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesContractsMaterializedTemplatesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesContractsMaterializedTemplatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    company_id: str,
    legal_entity_ids: list[str] | Unset = UNSET,
    countries: list[str] | Unset = UNSET,
    template_type: GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType,
    field_ids: list[str] | Unset = UNSET,
    include_archived: bool,
) -> Response[GetApi20260701ResourcesContractsMaterializedTemplatesResponse200]:
    """Reads all Materialized templates

     Reads all Materialized templates

    Args:
        company_id (str): The identifier of the company whose templates you want to retrieve. All
            results are scoped to this company.
             Example: 1.
        legal_entity_ids (list[str] | Unset): Optional list of legal entity identifiers to filter
            results. When provided alongside template_type: legal_entity, returns only the
            materialized templates for those legal entities. Ignored for company and country template
            types.
             Example: ['1'].
        countries (list[str] | Unset): Optional list of ISO 3166-1 alpha-2 country codes to filter
            results. When provided alongside template_type: country, returns only templates for those
            countries. When used with template_type: legal_entity, narrows results to legal entities
            operating in those countries.
             Example: ['es'].
        template_type (GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType): The
            template level to retrieve. Use company to get the organization-wide base field
            definitions. Use country to get country-specific overrides merged with company defaults.
            Use legal_entity to get the final effective template for a specific legal entity, which is
            the most common use case when building contract creation or editing flows.
             Example: legal_entity.
        field_ids (list[str] | Unset): Optional list of field identifiers to filter the template
            fields returned. When provided, each materialized template will only include fields whose
            field_id matches one of the values in this list. Use this to retrieve a specific subset of
            fields (e.g. ["contract_type"]) without fetching the full template structure.
             Example: ['contract_type'].
        include_archived (bool): When true, archived options are included in the response
            alongside active ones. Defaults to false, which returns only active options. Set to true
            when you need to display contracts that reference options that have since been archived.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesContractsMaterializedTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        legal_entity_ids=legal_entity_ids,
        countries=countries,
        template_type=template_type,
        field_ids=field_ids,
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    company_id: str,
    legal_entity_ids: list[str] | Unset = UNSET,
    countries: list[str] | Unset = UNSET,
    template_type: GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType,
    field_ids: list[str] | Unset = UNSET,
    include_archived: bool,
) -> GetApi20260701ResourcesContractsMaterializedTemplatesResponse200 | None:
    """Reads all Materialized templates

     Reads all Materialized templates

    Args:
        company_id (str): The identifier of the company whose templates you want to retrieve. All
            results are scoped to this company.
             Example: 1.
        legal_entity_ids (list[str] | Unset): Optional list of legal entity identifiers to filter
            results. When provided alongside template_type: legal_entity, returns only the
            materialized templates for those legal entities. Ignored for company and country template
            types.
             Example: ['1'].
        countries (list[str] | Unset): Optional list of ISO 3166-1 alpha-2 country codes to filter
            results. When provided alongside template_type: country, returns only templates for those
            countries. When used with template_type: legal_entity, narrows results to legal entities
            operating in those countries.
             Example: ['es'].
        template_type (GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType): The
            template level to retrieve. Use company to get the organization-wide base field
            definitions. Use country to get country-specific overrides merged with company defaults.
            Use legal_entity to get the final effective template for a specific legal entity, which is
            the most common use case when building contract creation or editing flows.
             Example: legal_entity.
        field_ids (list[str] | Unset): Optional list of field identifiers to filter the template
            fields returned. When provided, each materialized template will only include fields whose
            field_id matches one of the values in this list. Use this to retrieve a specific subset of
            fields (e.g. ["contract_type"]) without fetching the full template structure.
             Example: ['contract_type'].
        include_archived (bool): When true, archived options are included in the response
            alongside active ones. Defaults to false, which returns only active options. Set to true
            when you need to display contracts that reference options that have since been archived.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesContractsMaterializedTemplatesResponse200
    """

    return sync_detailed(
        client=client,
        company_id=company_id,
        legal_entity_ids=legal_entity_ids,
        countries=countries,
        template_type=template_type,
        field_ids=field_ids,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    company_id: str,
    legal_entity_ids: list[str] | Unset = UNSET,
    countries: list[str] | Unset = UNSET,
    template_type: GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType,
    field_ids: list[str] | Unset = UNSET,
    include_archived: bool,
) -> Response[GetApi20260701ResourcesContractsMaterializedTemplatesResponse200]:
    """Reads all Materialized templates

     Reads all Materialized templates

    Args:
        company_id (str): The identifier of the company whose templates you want to retrieve. All
            results are scoped to this company.
             Example: 1.
        legal_entity_ids (list[str] | Unset): Optional list of legal entity identifiers to filter
            results. When provided alongside template_type: legal_entity, returns only the
            materialized templates for those legal entities. Ignored for company and country template
            types.
             Example: ['1'].
        countries (list[str] | Unset): Optional list of ISO 3166-1 alpha-2 country codes to filter
            results. When provided alongside template_type: country, returns only templates for those
            countries. When used with template_type: legal_entity, narrows results to legal entities
            operating in those countries.
             Example: ['es'].
        template_type (GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType): The
            template level to retrieve. Use company to get the organization-wide base field
            definitions. Use country to get country-specific overrides merged with company defaults.
            Use legal_entity to get the final effective template for a specific legal entity, which is
            the most common use case when building contract creation or editing flows.
             Example: legal_entity.
        field_ids (list[str] | Unset): Optional list of field identifiers to filter the template
            fields returned. When provided, each materialized template will only include fields whose
            field_id matches one of the values in this list. Use this to retrieve a specific subset of
            fields (e.g. ["contract_type"]) without fetching the full template structure.
             Example: ['contract_type'].
        include_archived (bool): When true, archived options are included in the response
            alongside active ones. Defaults to false, which returns only active options. Set to true
            when you need to display contracts that reference options that have since been archived.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesContractsMaterializedTemplatesResponse200]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        legal_entity_ids=legal_entity_ids,
        countries=countries,
        template_type=template_type,
        field_ids=field_ids,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    company_id: str,
    legal_entity_ids: list[str] | Unset = UNSET,
    countries: list[str] | Unset = UNSET,
    template_type: GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType,
    field_ids: list[str] | Unset = UNSET,
    include_archived: bool,
) -> GetApi20260701ResourcesContractsMaterializedTemplatesResponse200 | None:
    """Reads all Materialized templates

     Reads all Materialized templates

    Args:
        company_id (str): The identifier of the company whose templates you want to retrieve. All
            results are scoped to this company.
             Example: 1.
        legal_entity_ids (list[str] | Unset): Optional list of legal entity identifiers to filter
            results. When provided alongside template_type: legal_entity, returns only the
            materialized templates for those legal entities. Ignored for company and country template
            types.
             Example: ['1'].
        countries (list[str] | Unset): Optional list of ISO 3166-1 alpha-2 country codes to filter
            results. When provided alongside template_type: country, returns only templates for those
            countries. When used with template_type: legal_entity, narrows results to legal entities
            operating in those countries.
             Example: ['es'].
        template_type (GetApi20260701ResourcesContractsMaterializedTemplatesTemplateType): The
            template level to retrieve. Use company to get the organization-wide base field
            definitions. Use country to get country-specific overrides merged with company defaults.
            Use legal_entity to get the final effective template for a specific legal entity, which is
            the most common use case when building contract creation or editing flows.
             Example: legal_entity.
        field_ids (list[str] | Unset): Optional list of field identifiers to filter the template
            fields returned. When provided, each materialized template will only include fields whose
            field_id matches one of the values in this list. Use this to retrieve a specific subset of
            fields (e.g. ["contract_type"]) without fetching the full template structure.
             Example: ['contract_type'].
        include_archived (bool): When true, archived options are included in the response
            alongside active ones. Defaults to false, which returns only active options. Set to true
            when you need to display contracts that reference options that have since been archived.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesContractsMaterializedTemplatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            company_id=company_id,
            legal_entity_ids=legal_entity_ids,
            countries=countries,
            template_type=template_type,
            field_ids=field_ids,
            include_archived=include_archived,
        )
    ).parsed
