from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.procurement_po_template_version import ProcurementPoTemplateVersion
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/procurement/po_template_versions/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProcurementPoTemplateVersion | None:
    if response.status_code == 200:
        response_200 = ProcurementPoTemplateVersion.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProcurementPoTemplateVersion]:
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
) -> Response[ProcurementPoTemplateVersion]:
    """Reads a single Po template version

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPoTemplateVersion]
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
) -> ProcurementPoTemplateVersion | None:
    """Reads a single Po template version

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPoTemplateVersion
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProcurementPoTemplateVersion]:
    """Reads a single Po template version

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcurementPoTemplateVersion]
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
) -> ProcurementPoTemplateVersion | None:
    """Reads a single Po template version

     Fetch PO template versions for the company. A version is the immutable snapshot of a template's
    schema: it owns the field definitions a purchase order created against it must comply with. To
    introspect the schema an integrator will write POs against, request the active version
    (status=active) and read its field definitions. To update a purchase order created with an older
    template, request the specific historical version by id (purchase_order.po_template_version_id) so
    the correct schema is used.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcurementPoTemplateVersion
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
