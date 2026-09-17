from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.procurement_po_template_field_definition import ProcurementPoTemplateFieldDefinition
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/procurement/po_template_field_definitions/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProcurementPoTemplateFieldDefinition | None:
    if response.status_code == 200:
        response_200 = ProcurementPoTemplateFieldDefinition.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProcurementPoTemplateFieldDefinition]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProcurementPoTemplateFieldDefinition]:
    """Reads a single Po template field definition

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPoTemplateFieldDefinition]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ProcurementPoTemplateFieldDefinition | None:
    """Reads a single Po template field definition

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPoTemplateFieldDefinition
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProcurementPoTemplateFieldDefinition]:
    """Reads a single Po template field definition

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPoTemplateFieldDefinition]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ProcurementPoTemplateFieldDefinition | None:
    """Reads a single Po template field definition

     Fetch the field definitions of a PO template version. Together these describe the schema a purchase
    order created against that version must comply with: which fields exist, their keys, types, whether
    they are required, and the allowed values for select fields. Filter by po_template_version_ids to
    introspect the schema of a specific version (active or historical).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPoTemplateFieldDefinition
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
