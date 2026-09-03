from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_procurement_po_template_versions_response_200 import (
    GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200,
)
from ...models.get_api_20261001_resources_procurement_po_template_versions_status import (
    GetApi20261001ResourcesProcurementPoTemplateVersionsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    po_template_ids: list[str] | Unset = UNSET,
    status: GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_po_template_ids: list[str] | Unset = UNSET
    if not isinstance(po_template_ids, Unset):
        json_po_template_ids = po_template_ids

    params["po_template_ids[]"] = json_po_template_ids

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status[]"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/procurement/po_template_versions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200]:
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
    po_template_ids: list[str] | Unset = UNSET,
    status: GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200]:
    """Reads all Po template versions

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        ids (list[str] | Unset): An array of PO template version IDs to filter by. Use the
            po_template_version_id pinned on a purchase order to retrieve the exact (possibly
            historical, non-active) schema it was created with.
             Example: ['1'].
        po_template_ids (list[str] | Unset): An array of PO template IDs to filter versions for.
            Example: ['1'].
        status (GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset): Filter by
            version status. Use "active" to retrieve the single currently-active version of each
            template (the schema new POs are created against). Other values: "draft", "archived".
             Example: ['active'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        po_template_ids=po_template_ids,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    po_template_ids: list[str] | Unset = UNSET,
    status: GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset = UNSET,
) -> GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200 | None:
    """Reads all Po template versions

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        ids (list[str] | Unset): An array of PO template version IDs to filter by. Use the
            po_template_version_id pinned on a purchase order to retrieve the exact (possibly
            historical, non-active) schema it was created with.
             Example: ['1'].
        po_template_ids (list[str] | Unset): An array of PO template IDs to filter versions for.
            Example: ['1'].
        status (GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset): Filter by
            version status. Use "active" to retrieve the single currently-active version of each
            template (the schema new POs are created against). Other values: "draft", "archived".
             Example: ['active'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        po_template_ids=po_template_ids,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    po_template_ids: list[str] | Unset = UNSET,
    status: GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset = UNSET,
) -> Response[GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200]:
    """Reads all Po template versions

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        ids (list[str] | Unset): An array of PO template version IDs to filter by. Use the
            po_template_version_id pinned on a purchase order to retrieve the exact (possibly
            historical, non-active) schema it was created with.
             Example: ['1'].
        po_template_ids (list[str] | Unset): An array of PO template IDs to filter versions for.
            Example: ['1'].
        status (GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset): Filter by
            version status. Use "active" to retrieve the single currently-active version of each
            template (the schema new POs are created against). Other values: "draft", "archived".
             Example: ['active'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        po_template_ids=po_template_ids,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    po_template_ids: list[str] | Unset = UNSET,
    status: GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset = UNSET,
) -> GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200 | None:
    """Reads all Po template versions

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        ids (list[str] | Unset): An array of PO template version IDs to filter by. Use the
            po_template_version_id pinned on a purchase order to retrieve the exact (possibly
            historical, non-active) schema it was created with.
             Example: ['1'].
        po_template_ids (list[str] | Unset): An array of PO template IDs to filter versions for.
            Example: ['1'].
        status (GetApi20261001ResourcesProcurementPoTemplateVersionsStatus | Unset): Filter by
            version status. Use "active" to retrieve the single currently-active version of each
            template (the schema new POs are created against). Other values: "draft", "archived".
             Example: ['active'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesProcurementPoTemplateVersionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            po_template_ids=po_template_ids,
            status=status,
        )
    ).parsed
