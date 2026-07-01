from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payroll_supplement import PayrollSupplement
from ...models.put_api_20260701_resources_payroll_supplements_id_body import (
    PutApi20260701ResourcesPayrollSupplementsIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20260701ResourcesPayrollSupplementsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2026-07-01/resources/payroll/supplements/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PayrollSupplement | None:
    if response.status_code == 200:
        response_200 = PayrollSupplement.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PayrollSupplement]:
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
    body: PutApi20260701ResourcesPayrollSupplementsIdBody | Unset = UNSET,
) -> Response[PayrollSupplement]:
    """Updates a Supplement

     Updates a Supplement unless it is an additional compensation supplement (In such case, you need to
    create a new one, then remove the old compensation supplement from the contract and add the newly
    created one to it).

    Args:
        id (str):
        body (PutApi20260701ResourcesPayrollSupplementsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayrollSupplement]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesPayrollSupplementsIdBody | Unset = UNSET,
) -> PayrollSupplement | None:
    """Updates a Supplement

     Updates a Supplement unless it is an additional compensation supplement (In such case, you need to
    create a new one, then remove the old compensation supplement from the contract and add the newly
    created one to it).

    Args:
        id (str):
        body (PutApi20260701ResourcesPayrollSupplementsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayrollSupplement
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesPayrollSupplementsIdBody | Unset = UNSET,
) -> Response[PayrollSupplement]:
    """Updates a Supplement

     Updates a Supplement unless it is an additional compensation supplement (In such case, you need to
    create a new one, then remove the old compensation supplement from the contract and add the newly
    created one to it).

    Args:
        id (str):
        body (PutApi20260701ResourcesPayrollSupplementsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayrollSupplement]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PutApi20260701ResourcesPayrollSupplementsIdBody | Unset = UNSET,
) -> PayrollSupplement | None:
    """Updates a Supplement

     Updates a Supplement unless it is an additional compensation supplement (In such case, you need to
    create a new one, then remove the old compensation supplement from the contract and add the newly
    created one to it).

    Args:
        id (str):
        body (PutApi20260701ResourcesPayrollSupplementsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayrollSupplement
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
