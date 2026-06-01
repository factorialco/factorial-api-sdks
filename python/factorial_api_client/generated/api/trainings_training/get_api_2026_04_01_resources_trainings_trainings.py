from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_trainings_trainings_response_200 import (
    GetApi20260401ResourcesTrainingsTrainingsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    access_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    catalog: bool | Unset = UNSET,
    only_assigned: bool | Unset = UNSET,
    with_expired_memberships: bool | Unset = UNSET,
    return_expired_memberships: bool | Unset = UNSET,
    is_mandatory: bool | Unset = UNSET,
    with_current_training_classes: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["access_id"] = access_id

    params["search"] = search

    params["status"] = status

    params["catalog"] = catalog

    params["only_assigned"] = only_assigned

    params["with_expired_memberships"] = with_expired_memberships

    params["return_expired_memberships"] = return_expired_memberships

    params["is_mandatory"] = is_mandatory

    params["with_current_training_classes"] = with_current_training_classes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/trainings/trainings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesTrainingsTrainingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesTrainingsTrainingsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesTrainingsTrainingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    access_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    catalog: bool | Unset = UNSET,
    only_assigned: bool | Unset = UNSET,
    with_expired_memberships: bool | Unset = UNSET,
    return_expired_memberships: bool | Unset = UNSET,
    is_mandatory: bool | Unset = UNSET,
    with_current_training_classes: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTrainingsTrainingsResponse200]:
    """Reads all Trainings

     Reads all Trainings

    Args:
        id (int | Unset): This field is used to get a specific training.
        ids (list[int] | Unset): This field is used to filter those trainings whose id match with
            the given.
        access_id (int | Unset): @deprecated
        search (str | Unset): This field is used to search in the training name, training
            description or training category.
        status (str | Unset): This field is used to filter those trainings whose status is the
            same as the one we pass.
        catalog (bool | Unset): This field is used to filter those trainings whose are visible in
            the catalog.
        only_assigned (bool | Unset): This field is used to filter those trainings whose
            attendance status is different from not assigned.
        with_expired_memberships (bool | Unset): This field is used to filter those trainings
            whose members have the course expired (if 'true') or not (if 'false').
        return_expired_memberships (bool | Unset): Fills the information of the field
            'number_of_expired_participants' if 'true'
        is_mandatory (bool | Unset): This field is used to filter by mandatory or non-mandatory
            trainings if provided
        with_current_training_classes (bool | Unset): This field is used to filter those trainings
            whose have current training classes if 'true'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTrainingsTrainingsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        ids=ids,
        access_id=access_id,
        search=search,
        status=status,
        catalog=catalog,
        only_assigned=only_assigned,
        with_expired_memberships=with_expired_memberships,
        return_expired_memberships=return_expired_memberships,
        is_mandatory=is_mandatory,
        with_current_training_classes=with_current_training_classes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    access_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    catalog: bool | Unset = UNSET,
    only_assigned: bool | Unset = UNSET,
    with_expired_memberships: bool | Unset = UNSET,
    return_expired_memberships: bool | Unset = UNSET,
    is_mandatory: bool | Unset = UNSET,
    with_current_training_classes: bool | Unset = UNSET,
) -> GetApi20260401ResourcesTrainingsTrainingsResponse200 | None:
    """Reads all Trainings

     Reads all Trainings

    Args:
        id (int | Unset): This field is used to get a specific training.
        ids (list[int] | Unset): This field is used to filter those trainings whose id match with
            the given.
        access_id (int | Unset): @deprecated
        search (str | Unset): This field is used to search in the training name, training
            description or training category.
        status (str | Unset): This field is used to filter those trainings whose status is the
            same as the one we pass.
        catalog (bool | Unset): This field is used to filter those trainings whose are visible in
            the catalog.
        only_assigned (bool | Unset): This field is used to filter those trainings whose
            attendance status is different from not assigned.
        with_expired_memberships (bool | Unset): This field is used to filter those trainings
            whose members have the course expired (if 'true') or not (if 'false').
        return_expired_memberships (bool | Unset): Fills the information of the field
            'number_of_expired_participants' if 'true'
        is_mandatory (bool | Unset): This field is used to filter by mandatory or non-mandatory
            trainings if provided
        with_current_training_classes (bool | Unset): This field is used to filter those trainings
            whose have current training classes if 'true'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTrainingsTrainingsResponse200
    """

    return sync_detailed(
        client=client,
        id=id,
        ids=ids,
        access_id=access_id,
        search=search,
        status=status,
        catalog=catalog,
        only_assigned=only_assigned,
        with_expired_memberships=with_expired_memberships,
        return_expired_memberships=return_expired_memberships,
        is_mandatory=is_mandatory,
        with_current_training_classes=with_current_training_classes,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    access_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    catalog: bool | Unset = UNSET,
    only_assigned: bool | Unset = UNSET,
    with_expired_memberships: bool | Unset = UNSET,
    return_expired_memberships: bool | Unset = UNSET,
    is_mandatory: bool | Unset = UNSET,
    with_current_training_classes: bool | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTrainingsTrainingsResponse200]:
    """Reads all Trainings

     Reads all Trainings

    Args:
        id (int | Unset): This field is used to get a specific training.
        ids (list[int] | Unset): This field is used to filter those trainings whose id match with
            the given.
        access_id (int | Unset): @deprecated
        search (str | Unset): This field is used to search in the training name, training
            description or training category.
        status (str | Unset): This field is used to filter those trainings whose status is the
            same as the one we pass.
        catalog (bool | Unset): This field is used to filter those trainings whose are visible in
            the catalog.
        only_assigned (bool | Unset): This field is used to filter those trainings whose
            attendance status is different from not assigned.
        with_expired_memberships (bool | Unset): This field is used to filter those trainings
            whose members have the course expired (if 'true') or not (if 'false').
        return_expired_memberships (bool | Unset): Fills the information of the field
            'number_of_expired_participants' if 'true'
        is_mandatory (bool | Unset): This field is used to filter by mandatory or non-mandatory
            trainings if provided
        with_current_training_classes (bool | Unset): This field is used to filter those trainings
            whose have current training classes if 'true'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTrainingsTrainingsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        ids=ids,
        access_id=access_id,
        search=search,
        status=status,
        catalog=catalog,
        only_assigned=only_assigned,
        with_expired_memberships=with_expired_memberships,
        return_expired_memberships=return_expired_memberships,
        is_mandatory=is_mandatory,
        with_current_training_classes=with_current_training_classes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    access_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    catalog: bool | Unset = UNSET,
    only_assigned: bool | Unset = UNSET,
    with_expired_memberships: bool | Unset = UNSET,
    return_expired_memberships: bool | Unset = UNSET,
    is_mandatory: bool | Unset = UNSET,
    with_current_training_classes: bool | Unset = UNSET,
) -> GetApi20260401ResourcesTrainingsTrainingsResponse200 | None:
    """Reads all Trainings

     Reads all Trainings

    Args:
        id (int | Unset): This field is used to get a specific training.
        ids (list[int] | Unset): This field is used to filter those trainings whose id match with
            the given.
        access_id (int | Unset): @deprecated
        search (str | Unset): This field is used to search in the training name, training
            description or training category.
        status (str | Unset): This field is used to filter those trainings whose status is the
            same as the one we pass.
        catalog (bool | Unset): This field is used to filter those trainings whose are visible in
            the catalog.
        only_assigned (bool | Unset): This field is used to filter those trainings whose
            attendance status is different from not assigned.
        with_expired_memberships (bool | Unset): This field is used to filter those trainings
            whose members have the course expired (if 'true') or not (if 'false').
        return_expired_memberships (bool | Unset): Fills the information of the field
            'number_of_expired_participants' if 'true'
        is_mandatory (bool | Unset): This field is used to filter by mandatory or non-mandatory
            trainings if provided
        with_current_training_classes (bool | Unset): This field is used to filter those trainings
            whose have current training classes if 'true'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTrainingsTrainingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            ids=ids,
            access_id=access_id,
            search=search,
            status=status,
            catalog=catalog,
            only_assigned=only_assigned,
            with_expired_memberships=with_expired_memberships,
            return_expired_memberships=return_expired_memberships,
            is_mandatory=is_mandatory,
            with_current_training_classes=with_current_training_classes,
        )
    ).parsed
