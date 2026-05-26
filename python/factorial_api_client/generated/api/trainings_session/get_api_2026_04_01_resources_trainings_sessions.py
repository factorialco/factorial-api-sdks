from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_trainings_sessions_response_200 import (
    GetApi20260401ResourcesTrainingsSessionsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    training_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    start_after: str | Unset = UNSET,
    start_before: str | Unset = UNSET,
    access_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    training_class_ids: list[str] | Unset = UNSET,
    next_: bool | Unset = UNSET,
    modality: str | Unset = UNSET,
    starts_at: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_training_ids: list[int] | Unset = UNSET
    if not isinstance(training_ids, Unset):
        json_training_ids = training_ids

    params["training_ids[]"] = json_training_ids

    params["search"] = search

    params["start_after"] = start_after

    params["start_before"] = start_before

    params["access_id"] = access_id

    params["employee_id"] = employee_id

    json_training_class_ids: list[str] | Unset = UNSET
    if not isinstance(training_class_ids, Unset):
        json_training_class_ids = training_class_ids

    params["training_class_ids[]"] = json_training_class_ids

    params["next"] = next_

    params["modality"] = modality

    json_starts_at: list[str] | Unset = UNSET
    if not isinstance(starts_at, Unset):
        json_starts_at = starts_at

    params["starts_at[]"] = json_starts_at

    params["active"] = active

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/trainings/sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesTrainingsSessionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesTrainingsSessionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesTrainingsSessionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    training_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    start_after: str | Unset = UNSET,
    start_before: str | Unset = UNSET,
    access_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    training_class_ids: list[str] | Unset = UNSET,
    next_: bool | Unset = UNSET,
    modality: str | Unset = UNSET,
    starts_at: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTrainingsSessionsResponse200]:
    """Reads all Sessions

     Reads all Sessions

    Args:
        ids (list[int] | Unset): This field is used to filter those sessions whose id match with
            the given. Example: [1].
        training_ids (list[int] | Unset): This field is used to filter those sessions whose belong
            to these trainings. Example: [1].
        search (str | Unset): This field is used to filter those sessions whose name include some
            of the text written. Example: Session 1.
        start_after (str | Unset): This field is used to filter those sessions whose starts date
            is after the given. Example: 2024-01-05T00:00:00.000Z.
        start_before (str | Unset): This field is used to filter those sessions whose starts date
            is before the given. Example: 2025-06-05T00:00:00.000Z.
        access_id (int | Unset): access_id associated to the employee, refers to
            employees/employees endpoint.
        employee_id (int | Unset): employee_id associated to the employee, refers to
            employees/employees endpoint. Example: 20.
        training_class_ids (list[str] | Unset): This field is used to filter those sessions whose
            belong to this training groups. Example: [1].
        next_ (bool | Unset): When this field is active, it filters and orders those sessions that
            are closest in time, with the first element being the closest.
        modality (str | Unset): The mode the session will be handled, online, in person or hybrid.
            Example: inperson.
        starts_at (list[str] | Unset): This field is used to filter the sessions that start at a
            given date. Example: ['2025-02-04T10:31:48.000Z'].
        active (bool | Unset): When this field is active, filter by only active sessions Example:
            True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTrainingsSessionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        training_ids=training_ids,
        search=search,
        start_after=start_after,
        start_before=start_before,
        access_id=access_id,
        employee_id=employee_id,
        training_class_ids=training_class_ids,
        next_=next_,
        modality=modality,
        starts_at=starts_at,
        active=active,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    training_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    start_after: str | Unset = UNSET,
    start_before: str | Unset = UNSET,
    access_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    training_class_ids: list[str] | Unset = UNSET,
    next_: bool | Unset = UNSET,
    modality: str | Unset = UNSET,
    starts_at: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> GetApi20260401ResourcesTrainingsSessionsResponse200 | None:
    """Reads all Sessions

     Reads all Sessions

    Args:
        ids (list[int] | Unset): This field is used to filter those sessions whose id match with
            the given. Example: [1].
        training_ids (list[int] | Unset): This field is used to filter those sessions whose belong
            to these trainings. Example: [1].
        search (str | Unset): This field is used to filter those sessions whose name include some
            of the text written. Example: Session 1.
        start_after (str | Unset): This field is used to filter those sessions whose starts date
            is after the given. Example: 2024-01-05T00:00:00.000Z.
        start_before (str | Unset): This field is used to filter those sessions whose starts date
            is before the given. Example: 2025-06-05T00:00:00.000Z.
        access_id (int | Unset): access_id associated to the employee, refers to
            employees/employees endpoint.
        employee_id (int | Unset): employee_id associated to the employee, refers to
            employees/employees endpoint. Example: 20.
        training_class_ids (list[str] | Unset): This field is used to filter those sessions whose
            belong to this training groups. Example: [1].
        next_ (bool | Unset): When this field is active, it filters and orders those sessions that
            are closest in time, with the first element being the closest.
        modality (str | Unset): The mode the session will be handled, online, in person or hybrid.
            Example: inperson.
        starts_at (list[str] | Unset): This field is used to filter the sessions that start at a
            given date. Example: ['2025-02-04T10:31:48.000Z'].
        active (bool | Unset): When this field is active, filter by only active sessions Example:
            True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTrainingsSessionsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        training_ids=training_ids,
        search=search,
        start_after=start_after,
        start_before=start_before,
        access_id=access_id,
        employee_id=employee_id,
        training_class_ids=training_class_ids,
        next_=next_,
        modality=modality,
        starts_at=starts_at,
        active=active,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    training_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    start_after: str | Unset = UNSET,
    start_before: str | Unset = UNSET,
    access_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    training_class_ids: list[str] | Unset = UNSET,
    next_: bool | Unset = UNSET,
    modality: str | Unset = UNSET,
    starts_at: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTrainingsSessionsResponse200]:
    """Reads all Sessions

     Reads all Sessions

    Args:
        ids (list[int] | Unset): This field is used to filter those sessions whose id match with
            the given. Example: [1].
        training_ids (list[int] | Unset): This field is used to filter those sessions whose belong
            to these trainings. Example: [1].
        search (str | Unset): This field is used to filter those sessions whose name include some
            of the text written. Example: Session 1.
        start_after (str | Unset): This field is used to filter those sessions whose starts date
            is after the given. Example: 2024-01-05T00:00:00.000Z.
        start_before (str | Unset): This field is used to filter those sessions whose starts date
            is before the given. Example: 2025-06-05T00:00:00.000Z.
        access_id (int | Unset): access_id associated to the employee, refers to
            employees/employees endpoint.
        employee_id (int | Unset): employee_id associated to the employee, refers to
            employees/employees endpoint. Example: 20.
        training_class_ids (list[str] | Unset): This field is used to filter those sessions whose
            belong to this training groups. Example: [1].
        next_ (bool | Unset): When this field is active, it filters and orders those sessions that
            are closest in time, with the first element being the closest.
        modality (str | Unset): The mode the session will be handled, online, in person or hybrid.
            Example: inperson.
        starts_at (list[str] | Unset): This field is used to filter the sessions that start at a
            given date. Example: ['2025-02-04T10:31:48.000Z'].
        active (bool | Unset): When this field is active, filter by only active sessions Example:
            True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTrainingsSessionsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        training_ids=training_ids,
        search=search,
        start_after=start_after,
        start_before=start_before,
        access_id=access_id,
        employee_id=employee_id,
        training_class_ids=training_class_ids,
        next_=next_,
        modality=modality,
        starts_at=starts_at,
        active=active,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    training_ids: list[int] | Unset = UNSET,
    search: str | Unset = UNSET,
    start_after: str | Unset = UNSET,
    start_before: str | Unset = UNSET,
    access_id: int | Unset = UNSET,
    employee_id: int | Unset = UNSET,
    training_class_ids: list[str] | Unset = UNSET,
    next_: bool | Unset = UNSET,
    modality: str | Unset = UNSET,
    starts_at: list[str] | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> GetApi20260401ResourcesTrainingsSessionsResponse200 | None:
    """Reads all Sessions

     Reads all Sessions

    Args:
        ids (list[int] | Unset): This field is used to filter those sessions whose id match with
            the given. Example: [1].
        training_ids (list[int] | Unset): This field is used to filter those sessions whose belong
            to these trainings. Example: [1].
        search (str | Unset): This field is used to filter those sessions whose name include some
            of the text written. Example: Session 1.
        start_after (str | Unset): This field is used to filter those sessions whose starts date
            is after the given. Example: 2024-01-05T00:00:00.000Z.
        start_before (str | Unset): This field is used to filter those sessions whose starts date
            is before the given. Example: 2025-06-05T00:00:00.000Z.
        access_id (int | Unset): access_id associated to the employee, refers to
            employees/employees endpoint.
        employee_id (int | Unset): employee_id associated to the employee, refers to
            employees/employees endpoint. Example: 20.
        training_class_ids (list[str] | Unset): This field is used to filter those sessions whose
            belong to this training groups. Example: [1].
        next_ (bool | Unset): When this field is active, it filters and orders those sessions that
            are closest in time, with the first element being the closest.
        modality (str | Unset): The mode the session will be handled, online, in person or hybrid.
            Example: inperson.
        starts_at (list[str] | Unset): This field is used to filter the sessions that start at a
            given date. Example: ['2025-02-04T10:31:48.000Z'].
        active (bool | Unset): When this field is active, filter by only active sessions Example:
            True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTrainingsSessionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            training_ids=training_ids,
            search=search,
            start_after=start_after,
            start_before=start_before,
            access_id=access_id,
            employee_id=employee_id,
            training_class_ids=training_class_ids,
            next_=next_,
            modality=modality,
            starts_at=starts_at,
            active=active,
        )
    ).parsed
