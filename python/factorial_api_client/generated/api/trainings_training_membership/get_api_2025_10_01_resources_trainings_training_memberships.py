from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_trainings_training_memberships_response_200 import (
    GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    training_id: int,
    ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["training_id"] = training_id

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["search"] = search

    params["team_id"] = team_id

    params["status"] = status

    params["class_id"] = class_id

    params["employee_id"] = employee_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/trainings/training_memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    training_id: int,
    ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
) -> Response[GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200]:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (int): This field is used to filter those trainings memberships that belongs
            to this training. Example: 1.
        ids (list[int] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: [1].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (int | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (int | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (int | Unset): Get the training memberships by passing the employee id
            Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        training_id=training_id,
        ids=ids,
        search=search,
        team_id=team_id,
        status=status,
        class_id=class_id,
        employee_id=employee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    training_id: int,
    ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
) -> GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200 | None:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (int): This field is used to filter those trainings memberships that belongs
            to this training. Example: 1.
        ids (list[int] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: [1].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (int | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (int | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (int | Unset): Get the training memberships by passing the employee id
            Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200
    """

    return sync_detailed(
        client=client,
        training_id=training_id,
        ids=ids,
        search=search,
        team_id=team_id,
        status=status,
        class_id=class_id,
        employee_id=employee_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    training_id: int,
    ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
) -> Response[GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200]:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (int): This field is used to filter those trainings memberships that belongs
            to this training. Example: 1.
        ids (list[int] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: [1].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (int | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (int | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (int | Unset): Get the training memberships by passing the employee id
            Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        training_id=training_id,
        ids=ids,
        search=search,
        team_id=team_id,
        status=status,
        class_id=class_id,
        employee_id=employee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    training_id: int,
    ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
) -> GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200 | None:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (int): This field is used to filter those trainings memberships that belongs
            to this training. Example: 1.
        ids (list[int] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: [1].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (int | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (int | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (int | Unset): Get the training memberships by passing the employee id
            Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesTrainingsTrainingMembershipsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            training_id=training_id,
            ids=ids,
            search=search,
            team_id=team_id,
            status=status,
            class_id=class_id,
            employee_id=employee_id,
        )
    ).parsed
