from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payroll_integrations_base_code import PayrollIntegrationsBaseCode
from ...models.post_api_20251001_resources_payroll_integrations_base_codes_body import (
    PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/payroll_integrations_base/codes",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PayrollIntegrationsBaseCode | None:
    if response.status_code == 201:
        response_201 = PayrollIntegrationsBaseCode.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PayrollIntegrationsBaseCode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset = UNSET,
) -> Response[PayrollIntegrationsBaseCode]:
    """Creates a Code

     Creates a Code

    Args:
        body (PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayrollIntegrationsBaseCode]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset = UNSET,
) -> PayrollIntegrationsBaseCode | None:
    """Creates a Code

     Creates a Code

    Args:
        body (PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayrollIntegrationsBaseCode
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset = UNSET,
) -> Response[PayrollIntegrationsBaseCode]:
    """Creates a Code

     Creates a Code

    Args:
        body (PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayrollIntegrationsBaseCode]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset = UNSET,
) -> PayrollIntegrationsBaseCode | None:
    """Creates a Code

     Creates a Code

    Args:
        body (PostApi20251001ResourcesPayrollIntegrationsBaseCodesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayrollIntegrationsBaseCode
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
