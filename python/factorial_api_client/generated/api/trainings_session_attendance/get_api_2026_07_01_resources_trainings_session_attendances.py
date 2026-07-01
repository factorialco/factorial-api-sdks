from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_trainings_session_attendances_response_200 import (
    GetApi20260701ResourcesTrainingsSessionAttendancesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    session_id: str | Unset = UNSET,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    session_access_membership_ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["session_id"] = session_id

    params["id"] = id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_session_access_membership_ids: list[str] | Unset = UNSET
    if not isinstance(session_access_membership_ids, Unset):
        json_session_access_membership_ids = session_access_membership_ids

    params["session_access_membership_ids[]"] = json_session_access_membership_ids

    json_access_ids: list[str] | Unset = UNSET
    if not isinstance(access_ids, Unset):
        json_access_ids = access_ids

    params["access_ids[]"] = json_access_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/trainings/session_attendances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesTrainingsSessionAttendancesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesTrainingsSessionAttendancesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesTrainingsSessionAttendancesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str | Unset = UNSET,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    session_access_membership_ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesTrainingsSessionAttendancesResponse200]:
    """Reads all Session attendances

     Reads all Session attendances

    Args:
        session_id (str | Unset):
        id (str | Unset):
        ids (list[str] | Unset):
        session_access_membership_ids (list[str] | Unset):
        access_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTrainingsSessionAttendancesResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        id=id,
        ids=ids,
        session_access_membership_ids=session_access_membership_ids,
        access_ids=access_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    session_id: str | Unset = UNSET,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    session_access_membership_ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesTrainingsSessionAttendancesResponse200 | None:
    """Reads all Session attendances

     Reads all Session attendances

    Args:
        session_id (str | Unset):
        id (str | Unset):
        ids (list[str] | Unset):
        session_access_membership_ids (list[str] | Unset):
        access_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTrainingsSessionAttendancesResponse200
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        id=id,
        ids=ids,
        session_access_membership_ids=session_access_membership_ids,
        access_ids=access_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str | Unset = UNSET,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    session_access_membership_ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesTrainingsSessionAttendancesResponse200]:
    """Reads all Session attendances

     Reads all Session attendances

    Args:
        session_id (str | Unset):
        id (str | Unset):
        ids (list[str] | Unset):
        session_access_membership_ids (list[str] | Unset):
        access_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTrainingsSessionAttendancesResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        id=id,
        ids=ids,
        session_access_membership_ids=session_access_membership_ids,
        access_ids=access_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    session_id: str | Unset = UNSET,
    id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    session_access_membership_ids: list[str] | Unset = UNSET,
    access_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesTrainingsSessionAttendancesResponse200 | None:
    """Reads all Session attendances

     Reads all Session attendances

    Args:
        session_id (str | Unset):
        id (str | Unset):
        ids (list[str] | Unset):
        session_access_membership_ids (list[str] | Unset):
        access_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTrainingsSessionAttendancesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            id=id,
            ids=ids,
            session_access_membership_ids=session_access_membership_ids,
            access_ids=access_ids,
        )
    ).parsed
