from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_trainings_training_memberships_response_200 import (
    GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    training_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    due_date: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["training_id"] = training_id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["search"] = search

    params["team_id"] = team_id

    params["status"] = status

    params["class_id"] = class_id

    params["employee_id"] = employee_id

    params["due_date"] = due_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/trainings/training_memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    training_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    due_date: str,
) -> Response[GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200]:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (str | Unset): This field is used to filter those trainings memberships that
            belongs to this training. Example: 1.
        ids (list[str] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: ['1'].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (str | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (str | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (str | Unset): Get the training memberships by passing the employee id
            Example: 20.
        due_date (str): This field is used to filter training memberships by due date. Values can
            be 'overdue', 'no_due_date', or a number of days (e.g., '7', '30', '90'). Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        training_id=training_id,
        ids=ids,
        search=search,
        team_id=team_id,
        status=status,
        class_id=class_id,
        employee_id=employee_id,
        due_date=due_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    training_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    due_date: str,
) -> GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200 | None:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (str | Unset): This field is used to filter those trainings memberships that
            belongs to this training. Example: 1.
        ids (list[str] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: ['1'].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (str | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (str | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (str | Unset): Get the training memberships by passing the employee id
            Example: 20.
        due_date (str): This field is used to filter training memberships by due date. Values can
            be 'overdue', 'no_due_date', or a number of days (e.g., '7', '30', '90'). Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200
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
        due_date=due_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    training_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    due_date: str,
) -> Response[GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200]:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (str | Unset): This field is used to filter those trainings memberships that
            belongs to this training. Example: 1.
        ids (list[str] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: ['1'].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (str | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (str | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (str | Unset): Get the training memberships by passing the employee id
            Example: 20.
        due_date (str): This field is used to filter training memberships by due date. Values can
            be 'overdue', 'no_due_date', or a number of days (e.g., '7', '30', '90'). Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200]
    """

    kwargs = _get_kwargs(
        training_id=training_id,
        ids=ids,
        search=search,
        team_id=team_id,
        status=status,
        class_id=class_id,
        employee_id=employee_id,
        due_date=due_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    training_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    team_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    class_id: str | Unset = UNSET,
    employee_id: str | Unset = UNSET,
    due_date: str,
) -> GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200 | None:
    """Reads all Training memberships

     Reads all Training memberships

    Args:
        training_id (str | Unset): This field is used to filter those trainings memberships that
            belongs to this training. Example: 1.
        ids (list[str] | Unset): This field is used to filter those trainings memberships whose id
            match with the given. Example: ['1'].
        search (str | Unset): This field is used to filter those trainings memberships whose
            employee name include some of the text written. Example: Jane.
        team_id (str | Unset): This field is used to filter those memberships whose employees
            belongs to this team. Example: 1.
        status (str | Unset): This field is used to filter those trainings memberships whose
            attendance status is the given. Example: notstarted.
        class_id (str | Unset): This field is used to filter those trainings memberships whose
            employees belongs to this group. Example: 1.
        employee_id (str | Unset): Get the training memberships by passing the employee id
            Example: 20.
        due_date (str): This field is used to filter training memberships by due date. Values can
            be 'overdue', 'no_due_date', or a number of days (e.g., '7', '30', '90'). Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesTrainingsTrainingMembershipsResponse200
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
            due_date=due_date,
        )
    ).parsed
