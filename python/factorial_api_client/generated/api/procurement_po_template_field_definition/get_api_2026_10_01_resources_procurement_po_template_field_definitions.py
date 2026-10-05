from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_procurement_po_template_field_definitions_response_200 import (
    GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200,
)
from ...models.get_api_20261001_resources_procurement_po_template_field_definitions_section_type import (
    GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    po_template_version_ids: list[str] | Unset = UNSET,
    section_type: GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType
    | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_po_template_version_ids: list[str] | Unset = UNSET
    if not isinstance(po_template_version_ids, Unset):
        json_po_template_version_ids = po_template_version_ids

    params["po_template_version_ids[]"] = json_po_template_version_ids

    json_section_type: str | Unset = UNSET
    if not isinstance(section_type, Unset):
        json_section_type = section_type.value

    params["section_type[]"] = json_section_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/procurement/po_template_field_definitions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200.from_dict(
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
) -> Response[GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200]:
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
    po_template_version_ids: list[str] | Unset = UNSET,
    section_type: GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType
    | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200]:
    """Reads all Po template field definitions

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        ids (list[str] | Unset): An array of field definition IDs to filter by. Example: ['1'].
        po_template_version_ids (list[str] | Unset): An array of PO template version IDs to filter
            fields for. This is the primary way to introspect a version's schema: pass the id of the
            active version (or a historical one) to obtain all its fields.
             Example: ['1'].
        section_type (GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType |
            Unset): Filter by section type. "general_information", "vendor_contact" and
            "notes_and_delivery" are header-level (one value per PO); "line_item_columns" describes
            the per-line-item columns.
             Example: ['general_information'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        po_template_version_ids=po_template_version_ids,
        section_type=section_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    po_template_version_ids: list[str] | Unset = UNSET,
    section_type: GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType
    | Unset = UNSET,
) -> GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200 | None:
    """Reads all Po template field definitions

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        ids (list[str] | Unset): An array of field definition IDs to filter by. Example: ['1'].
        po_template_version_ids (list[str] | Unset): An array of PO template version IDs to filter
            fields for. This is the primary way to introspect a version's schema: pass the id of the
            active version (or a historical one) to obtain all its fields.
             Example: ['1'].
        section_type (GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType |
            Unset): Filter by section type. "general_information", "vendor_contact" and
            "notes_and_delivery" are header-level (one value per PO); "line_item_columns" describes
            the per-line-item columns.
             Example: ['general_information'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        po_template_version_ids=po_template_version_ids,
        section_type=section_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    po_template_version_ids: list[str] | Unset = UNSET,
    section_type: GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType
    | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200]:
    """Reads all Po template field definitions

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        ids (list[str] | Unset): An array of field definition IDs to filter by. Example: ['1'].
        po_template_version_ids (list[str] | Unset): An array of PO template version IDs to filter
            fields for. This is the primary way to introspect a version's schema: pass the id of the
            active version (or a historical one) to obtain all its fields.
             Example: ['1'].
        section_type (GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType |
            Unset): Filter by section type. "general_information", "vendor_contact" and
            "notes_and_delivery" are header-level (one value per PO); "line_item_columns" describes
            the per-line-item columns.
             Example: ['general_information'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        po_template_version_ids=po_template_version_ids,
        section_type=section_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    po_template_version_ids: list[str] | Unset = UNSET,
    section_type: GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType
    | Unset = UNSET,
) -> GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200 | None:
    """Reads all Po template field definitions

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        ids (list[str] | Unset): An array of field definition IDs to filter by. Example: ['1'].
        po_template_version_ids (list[str] | Unset): An array of PO template version IDs to filter
            fields for. This is the primary way to introspect a version's schema: pass the id of the
            active version (or a historical one) to obtain all its fields.
             Example: ['1'].
        section_type (GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType |
            Unset): Filter by section type. "general_information", "vendor_contact" and
            "notes_and_delivery" are header-level (one value per PO); "line_item_columns" describes
            the per-line-item columns.
             Example: ['general_information'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            po_template_version_ids=po_template_version_ids,
            section_type=section_type,
        )
    ).parsed
