from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_trainings_training_classes_response_200 import (
    GetApi20260401ResourcesTrainingsTrainingClassesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    training_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    start_date: list[str] | Unset = UNSET,
    end_date: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["id"] = id

    params["training_id"] = training_id

    params["search"] = search

    json_start_date: list[str] | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date

    params["start_date[]"] = json_start_date

    json_end_date: list[str] | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date

    params["end_date[]"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/trainings/training_classes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesTrainingsTrainingClassesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesTrainingsTrainingClassesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesTrainingsTrainingClassesResponse200]:
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
    id: int | Unset = UNSET,
    training_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    start_date: list[str] | Unset = UNSET,
    end_date: list[str] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTrainingsTrainingClassesResponse200]:
    """Reads all Training classes

     Reads all Training classes

    Args:
        ids (list[int] | Unset): Filter those training classes whose id match with the given.
        id (int | Unset): Get a specific training class.
        training_id (int | Unset): Get training classes for the specified training.
        search (str | Unset): This field is used to search in the training class name.
        start_date (list[str] | Unset): Field those classes that start on the given date.
        end_date (list[str] | Unset): Filter those classes that end on the given date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTrainingsTrainingClassesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        id=id,
        training_id=training_id,
        search=search,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    training_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    start_date: list[str] | Unset = UNSET,
    end_date: list[str] | Unset = UNSET,
) -> GetApi20260401ResourcesTrainingsTrainingClassesResponse200 | None:
    """Reads all Training classes

     Reads all Training classes

    Args:
        ids (list[int] | Unset): Filter those training classes whose id match with the given.
        id (int | Unset): Get a specific training class.
        training_id (int | Unset): Get training classes for the specified training.
        search (str | Unset): This field is used to search in the training class name.
        start_date (list[str] | Unset): Field those classes that start on the given date.
        end_date (list[str] | Unset): Filter those classes that end on the given date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTrainingsTrainingClassesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        id=id,
        training_id=training_id,
        search=search,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    training_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    start_date: list[str] | Unset = UNSET,
    end_date: list[str] | Unset = UNSET,
) -> Response[GetApi20260401ResourcesTrainingsTrainingClassesResponse200]:
    """Reads all Training classes

     Reads all Training classes

    Args:
        ids (list[int] | Unset): Filter those training classes whose id match with the given.
        id (int | Unset): Get a specific training class.
        training_id (int | Unset): Get training classes for the specified training.
        search (str | Unset): This field is used to search in the training class name.
        start_date (list[str] | Unset): Field those classes that start on the given date.
        end_date (list[str] | Unset): Filter those classes that end on the given date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesTrainingsTrainingClassesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        id=id,
        training_id=training_id,
        search=search,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    training_id: int | Unset = UNSET,
    search: str | Unset = UNSET,
    start_date: list[str] | Unset = UNSET,
    end_date: list[str] | Unset = UNSET,
) -> GetApi20260401ResourcesTrainingsTrainingClassesResponse200 | None:
    """Reads all Training classes

     Reads all Training classes

    Args:
        ids (list[int] | Unset): Filter those training classes whose id match with the given.
        id (int | Unset): Get a specific training class.
        training_id (int | Unset): Get training classes for the specified training.
        search (str | Unset): This field is used to search in the training class name.
        start_date (list[str] | Unset): Field those classes that start on the given date.
        end_date (list[str] | Unset): Filter those classes that end on the given date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesTrainingsTrainingClassesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            id=id,
            training_id=training_id,
            search=search,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
