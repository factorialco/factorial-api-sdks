from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20261001_resources_finance_cost_center_memberships_response_200 import (
    GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cost_center_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    active_on: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    applying_on: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cost_center_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cost_center_id"] = cost_center_id

    params["employee_id"] = employee_id

    params["active_on"] = active_on

    params["only_active"] = only_active

    params["applying_on"] = applying_on

    params["company_id"] = company_id

    json_cost_center_ids: list[str] | Unset = UNSET
    if not isinstance(cost_center_ids, Unset):
        json_cost_center_ids = cost_center_ids

    params["cost_center_ids[]"] = json_cost_center_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/finance/cost_center_memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cost_center_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    active_on: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    applying_on: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cost_center_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200]:
    """Reads all Cost center memberships

     Reads all Cost center memberships

    Args:
        cost_center_id (str | Unset): To retreive active cost center memberships for a specific
            cost center Example: 1.
        employee_id (str | Unset): To retreive active cost center memberships for a specific
            employee Example: 1.
        active_on (str | Unset): To retreive active cost center memberships for a specific date
            Example: 2020-01-01.
        only_active (bool | Unset): To retreive only active cost center memberships, this is the
            default behavior
        applying_on (str | Unset): To retreive cost center memberships applying on a specific date
            Example: 2020-01-01.
        company_id (str | Unset): retrieve the cost center memberships for a specific company
            Example: 1.
        cost_center_ids (list[str] | Unset): retrieve the cost center memberships for a list of
            cost centers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        cost_center_id=cost_center_id,
        employee_id=employee_id,
        active_on=active_on,
        only_active=only_active,
        applying_on=applying_on,
        company_id=company_id,
        cost_center_ids=cost_center_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cost_center_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    active_on: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    applying_on: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cost_center_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200 | None:
    """Reads all Cost center memberships

     Reads all Cost center memberships

    Args:
        cost_center_id (str | Unset): To retreive active cost center memberships for a specific
            cost center Example: 1.
        employee_id (str | Unset): To retreive active cost center memberships for a specific
            employee Example: 1.
        active_on (str | Unset): To retreive active cost center memberships for a specific date
            Example: 2020-01-01.
        only_active (bool | Unset): To retreive only active cost center memberships, this is the
            default behavior
        applying_on (str | Unset): To retreive cost center memberships applying on a specific date
            Example: 2020-01-01.
        company_id (str | Unset): retrieve the cost center memberships for a specific company
            Example: 1.
        cost_center_ids (list[str] | Unset): retrieve the cost center memberships for a list of
            cost centers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200
    """

    return sync_detailed(
        client=client,
        cost_center_id=cost_center_id,
        employee_id=employee_id,
        active_on=active_on,
        only_active=only_active,
        applying_on=applying_on,
        company_id=company_id,
        cost_center_ids=cost_center_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cost_center_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    active_on: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    applying_on: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cost_center_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200]:
    """Reads all Cost center memberships

     Reads all Cost center memberships

    Args:
        cost_center_id (str | Unset): To retreive active cost center memberships for a specific
            cost center Example: 1.
        employee_id (str | Unset): To retreive active cost center memberships for a specific
            employee Example: 1.
        active_on (str | Unset): To retreive active cost center memberships for a specific date
            Example: 2020-01-01.
        only_active (bool | Unset): To retreive only active cost center memberships, this is the
            default behavior
        applying_on (str | Unset): To retreive cost center memberships applying on a specific date
            Example: 2020-01-01.
        company_id (str | Unset): retrieve the cost center memberships for a specific company
            Example: 1.
        cost_center_ids (list[str] | Unset): retrieve the cost center memberships for a list of
            cost centers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        cost_center_id=cost_center_id,
        employee_id=employee_id,
        active_on=active_on,
        only_active=only_active,
        applying_on=applying_on,
        company_id=company_id,
        cost_center_ids=cost_center_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cost_center_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    active_on: str | Unset = UNSET,
    only_active: bool | Unset = UNSET,
    applying_on: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    cost_center_ids: list[str] | Unset = UNSET,
) -> GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200 | None:
    """Reads all Cost center memberships

     Reads all Cost center memberships

    Args:
        cost_center_id (str | Unset): To retreive active cost center memberships for a specific
            cost center Example: 1.
        employee_id (str | Unset): To retreive active cost center memberships for a specific
            employee Example: 1.
        active_on (str | Unset): To retreive active cost center memberships for a specific date
            Example: 2020-01-01.
        only_active (bool | Unset): To retreive only active cost center memberships, this is the
            default behavior
        applying_on (str | Unset): To retreive cost center memberships applying on a specific date
            Example: 2020-01-01.
        company_id (str | Unset): retrieve the cost center memberships for a specific company
            Example: 1.
        cost_center_ids (list[str] | Unset): retrieve the cost center memberships for a list of
            cost centers Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20261001ResourcesFinanceCostCenterMembershipsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            cost_center_id=cost_center_id,
            employee_id=employee_id,
            active_on=active_on,
            only_active=only_active,
            applying_on=applying_on,
            company_id=company_id,
            cost_center_ids=cost_center_ids,
        )
    ).parsed
