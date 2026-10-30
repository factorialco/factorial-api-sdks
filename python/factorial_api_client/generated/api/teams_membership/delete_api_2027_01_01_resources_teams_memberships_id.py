from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.teams_membership import TeamsMembership
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/2027-01-01/resources/teams/memberships/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TeamsMembership | None:
    if response.status_code == 200:
        response_200 = TeamsMembership.from_dict(response.json())

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
) -> Response[ErrorResponse | TeamsMembership]:
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
) -> Response[ErrorResponse | TeamsMembership]:
    """Deletes a Membership

     Delete the membership to remove the employee from the team. For companies with nested teams what
    actually gets deleted depends on the kind of row: deleting a direct membership removes it, and the
    inherited copies it produced in the ancestor teams are cleaned up asynchronously. Deleting an
    INHERITED membership instead removes the employee's direct membership in EVERY sub-team that row
    originates from — rows with other ids, in teams you did not name — and the request is rejected
    altogether if you cannot manage one of those sub-teams. The inherited row you named also disappears
    asynchronously rather than in the request, so an immediate re-read may still return it; repeating
    the DELETE is safe rather than an error. Read that employee's memberships with
    `with_source_attribution` before deleting to see what is at stake: `direct` indicates which kind of
    row it is, and `source_team_ids` where the deletion would land. Both are advisory — the read and the
    delete resolve their answers independently, so re-read after deleting rather than assuming which
    branch ran.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TeamsMembership]
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
) -> ErrorResponse | TeamsMembership | None:
    """Deletes a Membership

     Delete the membership to remove the employee from the team. For companies with nested teams what
    actually gets deleted depends on the kind of row: deleting a direct membership removes it, and the
    inherited copies it produced in the ancestor teams are cleaned up asynchronously. Deleting an
    INHERITED membership instead removes the employee's direct membership in EVERY sub-team that row
    originates from — rows with other ids, in teams you did not name — and the request is rejected
    altogether if you cannot manage one of those sub-teams. The inherited row you named also disappears
    asynchronously rather than in the request, so an immediate re-read may still return it; repeating
    the DELETE is safe rather than an error. Read that employee's memberships with
    `with_source_attribution` before deleting to see what is at stake: `direct` indicates which kind of
    row it is, and `source_team_ids` where the deletion would land. Both are advisory — the read and the
    delete resolve their answers independently, so re-read after deleting rather than assuming which
    branch ran.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TeamsMembership
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | TeamsMembership]:
    """Deletes a Membership

     Delete the membership to remove the employee from the team. For companies with nested teams what
    actually gets deleted depends on the kind of row: deleting a direct membership removes it, and the
    inherited copies it produced in the ancestor teams are cleaned up asynchronously. Deleting an
    INHERITED membership instead removes the employee's direct membership in EVERY sub-team that row
    originates from — rows with other ids, in teams you did not name — and the request is rejected
    altogether if you cannot manage one of those sub-teams. The inherited row you named also disappears
    asynchronously rather than in the request, so an immediate re-read may still return it; repeating
    the DELETE is safe rather than an error. Read that employee's memberships with
    `with_source_attribution` before deleting to see what is at stake: `direct` indicates which kind of
    row it is, and `source_team_ids` where the deletion would land. Both are advisory — the read and the
    delete resolve their answers independently, so re-read after deleting rather than assuming which
    branch ran.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TeamsMembership]
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
) -> ErrorResponse | TeamsMembership | None:
    """Deletes a Membership

     Delete the membership to remove the employee from the team. For companies with nested teams what
    actually gets deleted depends on the kind of row: deleting a direct membership removes it, and the
    inherited copies it produced in the ancestor teams are cleaned up asynchronously. Deleting an
    INHERITED membership instead removes the employee's direct membership in EVERY sub-team that row
    originates from — rows with other ids, in teams you did not name — and the request is rejected
    altogether if you cannot manage one of those sub-teams. The inherited row you named also disappears
    asynchronously rather than in the request, so an immediate re-read may still return it; repeating
    the DELETE is safe rather than an error. Read that employee's memberships with
    `with_source_attribution` before deleting to see what is at stake: `direct` indicates which kind of
    row it is, and `source_team_ids` where the deletion would land. Both are advisory — the read and the
    delete resolve their answers independently, so re-read after deleting rather than assuming which
    branch ran.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TeamsMembership
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
