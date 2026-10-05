from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compensations_additional_compensation import CompensationsAdditionalCompensation
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/2026-10-01/resources/compensations/additional_compensations/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompensationsAdditionalCompensation | None:
    if response.status_code == 200:
        response_200 = CompensationsAdditionalCompensation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompensationsAdditionalCompensation]:
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
) -> Response[CompensationsAdditionalCompensation]:
    """Deletes an Additional compensation

     Deletes an additional compensation. Cascades to the linked amount strategy and (when applicable)
    per-worked-day definition, and re-points any compensation policies that referenced the destroyed
    strategy.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompensationsAdditionalCompensation]
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
) -> CompensationsAdditionalCompensation | None:
    """Deletes an Additional compensation

     Deletes an additional compensation. Cascades to the linked amount strategy and (when applicable)
    per-worked-day definition, and re-points any compensation policies that referenced the destroyed
    strategy.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompensationsAdditionalCompensation
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CompensationsAdditionalCompensation]:
    """Deletes an Additional compensation

     Deletes an additional compensation. Cascades to the linked amount strategy and (when applicable)
    per-worked-day definition, and re-points any compensation policies that referenced the destroyed
    strategy.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompensationsAdditionalCompensation]
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
) -> CompensationsAdditionalCompensation | None:
    """Deletes an Additional compensation

     Deletes an additional compensation. Cascades to the linked amount strategy and (when applicable)
    per-worked-day definition, and re-points any compensation policies that referenced the destroyed
    strategy.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompensationsAdditionalCompensation
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
