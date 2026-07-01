from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ats_application import AtsApplication
from ...models.post_api_20260701_resources_ats_applications_move_to_phase_body import (
    PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-07-01/resources/ats/applications/move_to_phase",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AtsApplication | None:
    if response.status_code == 200:
        response_200 = AtsApplication.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AtsApplication]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset = UNSET,
) -> Response[AtsApplication]:
    """Move to phases an Application

     Move an application to a different phase within the same job posting. Triggers the same side effects
    as moving a candidate in the product: configured phase-change automations and emails (smart actions)
    are executed.

    Args:
        body (PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AtsApplication]
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
    body: PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset = UNSET,
) -> AtsApplication | None:
    """Move to phases an Application

     Move an application to a different phase within the same job posting. Triggers the same side effects
    as moving a candidate in the product: configured phase-change automations and emails (smart actions)
    are executed.

    Args:
        body (PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AtsApplication
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset = UNSET,
) -> Response[AtsApplication]:
    """Move to phases an Application

     Move an application to a different phase within the same job posting. Triggers the same side effects
    as moving a candidate in the product: configured phase-change automations and emails (smart actions)
    are executed.

    Args:
        body (PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AtsApplication]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset = UNSET,
) -> AtsApplication | None:
    """Move to phases an Application

     Move an application to a different phase within the same job posting. Triggers the same side effects
    as moving a candidate in the product: configured phase-change automations and emails (smart actions)
    are executed.

    Args:
        body (PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AtsApplication
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
