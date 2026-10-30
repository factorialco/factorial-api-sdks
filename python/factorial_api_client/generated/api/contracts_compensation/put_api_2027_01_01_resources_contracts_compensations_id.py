from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contracts_compensation import ContractsCompensation
from ...models.error_response import ErrorResponse
from ...models.put_api_20270101_resources_contracts_compensations_id_body import (
    PutApi20270101ResourcesContractsCompensationsIdBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutApi20270101ResourcesContractsCompensationsIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/2027-01-01/resources/contracts/compensations/{id}".format(
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
) -> ContractsCompensation | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ContractsCompensation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = ErrorResponse.from_dict(response.json())

        return response_428

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContractsCompensation | ErrorResponse]:
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
    body: PutApi20270101ResourcesContractsCompensationsIdBody | Unset = UNSET,
) -> Response[ContractsCompensation | ErrorResponse]:
    """Updates a Compensation

     Updates a Compensation

    Args:
        id (str):
        body (PutApi20270101ResourcesContractsCompensationsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractsCompensation | ErrorResponse]
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
    body: PutApi20270101ResourcesContractsCompensationsIdBody | Unset = UNSET,
) -> ContractsCompensation | ErrorResponse | None:
    """Updates a Compensation

     Updates a Compensation

    Args:
        id (str):
        body (PutApi20270101ResourcesContractsCompensationsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractsCompensation | ErrorResponse
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
    body: PutApi20270101ResourcesContractsCompensationsIdBody | Unset = UNSET,
) -> Response[ContractsCompensation | ErrorResponse]:
    """Updates a Compensation

     Updates a Compensation

    Args:
        id (str):
        body (PutApi20270101ResourcesContractsCompensationsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractsCompensation | ErrorResponse]
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
    body: PutApi20270101ResourcesContractsCompensationsIdBody | Unset = UNSET,
) -> ContractsCompensation | ErrorResponse | None:
    """Updates a Compensation

     Updates a Compensation

    Args:
        id (str):
        body (PutApi20270101ResourcesContractsCompensationsIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractsCompensation | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
