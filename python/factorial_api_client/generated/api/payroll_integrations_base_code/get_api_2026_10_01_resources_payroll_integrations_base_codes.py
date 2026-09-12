from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_payroll_integrations_base_codes_integrations import (
    GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations,
)
from ...models.get_api_20261001_resources_payroll_integrations_base_codes_response_200 import (
    GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    code: str | Unset = UNSET,
    integrations: GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations,
    codeable_id: str | Unset = UNSET,
    codeable_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["code"] = code

    json_integrations = integrations.value
    params["integrations[]"] = json_integrations

    params["codeable_id"] = codeable_id

    params["codeable_type"] = codeable_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/payroll_integrations_base/codes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    integrations: GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations,
    codeable_id: str | Unset = UNSET,
    codeable_type: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200]:
    """Reads all Codes

     Reads all Codes

    Args:
        code (str | Unset): Code Value Example: COD-51.
        integrations (GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations): Payroll
            Integration names Example: a3innuva.
        codeable_id (str | Unset): Related object ID. Used together with codeable_type Example: 1.
        codeable_type (str | Unset): Related object type. Used together with codeable_id Example:
            Employee | Company | LegalEntity | Location.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200]
    """

    kwargs = _get_kwargs(
        code=code,
        integrations=integrations,
        codeable_id=codeable_id,
        codeable_type=codeable_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    integrations: GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations,
    codeable_id: str | Unset = UNSET,
    codeable_type: str | Unset = UNSET,
) -> GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200 | None:
    """Reads all Codes

     Reads all Codes

    Args:
        code (str | Unset): Code Value Example: COD-51.
        integrations (GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations): Payroll
            Integration names Example: a3innuva.
        codeable_id (str | Unset): Related object ID. Used together with codeable_type Example: 1.
        codeable_type (str | Unset): Related object type. Used together with codeable_id Example:
            Employee | Company | LegalEntity | Location.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200
    """

    return sync_detailed(
        client=client,
        code=code,
        integrations=integrations,
        codeable_id=codeable_id,
        codeable_type=codeable_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    integrations: GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations,
    codeable_id: str | Unset = UNSET,
    codeable_type: str | Unset = UNSET,
) -> Response[GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200]:
    """Reads all Codes

     Reads all Codes

    Args:
        code (str | Unset): Code Value Example: COD-51.
        integrations (GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations): Payroll
            Integration names Example: a3innuva.
        codeable_id (str | Unset): Related object ID. Used together with codeable_type Example: 1.
        codeable_type (str | Unset): Related object type. Used together with codeable_id Example:
            Employee | Company | LegalEntity | Location.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200]
    """

    kwargs = _get_kwargs(
        code=code,
        integrations=integrations,
        codeable_id=codeable_id,
        codeable_type=codeable_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    integrations: GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations,
    codeable_id: str | Unset = UNSET,
    codeable_type: str | Unset = UNSET,
) -> GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200 | None:
    """Reads all Codes

     Reads all Codes

    Args:
        code (str | Unset): Code Value Example: COD-51.
        integrations (GetApi20261001ResourcesPayrollIntegrationsBaseCodesIntegrations): Payroll
            Integration names Example: a3innuva.
        codeable_id (str | Unset): Related object ID. Used together with codeable_type Example: 1.
        codeable_type (str | Unset): Related object type. Used together with codeable_id Example:
            Employee | Company | LegalEntity | Location.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesPayrollIntegrationsBaseCodesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            integrations=integrations,
            codeable_id=codeable_id,
            codeable_type=codeable_type,
        )
    ).parsed
