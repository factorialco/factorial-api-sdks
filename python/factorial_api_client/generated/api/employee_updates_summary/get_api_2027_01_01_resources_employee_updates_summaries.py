from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_employee_updates_summaries_response_200 import (
    GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_legal_entities_ids: list[str] | Unset = UNSET
    if not isinstance(legal_entities_ids, Unset):
        json_legal_entities_ids = legal_entities_ids

    params["legal_entities_ids[]"] = json_legal_entities_ids

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type[]"] = json_type_

    params["starts_on"] = starts_on

    params["ends_on"] = ends_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/employee_updates/summaries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200]:
    """Reads all Summaries

     This endpoint can be used to retrieve a list of `employee updates`.

    Args:
        ids (list[str] | Unset): retrieve only the `employee updates` that matches the `ids`
            passed in the request. Example: ['1', '2', '3'].
        employee_ids (list[str] | Unset): retrieve only the `employee updates` assigned to any
            `employee` specified in the request. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): retrieve only the `employee updates` assigned to
            any `legal entity` specified in the request. Example: ['1', '2', '3'].
        type_ (list[str] | Unset): filter `employee updates` that have the given type. The
            supported types are: sick, parental, name, id, address, irpf, bank, residence,
            nationality, gender, hiring, custom-leave, termination, contract, workplace,
            manual_incidence, legal_entity Example: sick.
        starts_on (str | Unset): filter `employee updates` that started **later** the given param.
            Example: 2024-06-06.
        ends_on (str | Unset): filter `employee updates` that started **before** the given param.
            Example: 2024-06-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        legal_entities_ids=legal_entities_ids,
        type_=type_,
        starts_on=starts_on,
        ends_on=ends_on,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200 | None:
    """Reads all Summaries

     This endpoint can be used to retrieve a list of `employee updates`.

    Args:
        ids (list[str] | Unset): retrieve only the `employee updates` that matches the `ids`
            passed in the request. Example: ['1', '2', '3'].
        employee_ids (list[str] | Unset): retrieve only the `employee updates` assigned to any
            `employee` specified in the request. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): retrieve only the `employee updates` assigned to
            any `legal entity` specified in the request. Example: ['1', '2', '3'].
        type_ (list[str] | Unset): filter `employee updates` that have the given type. The
            supported types are: sick, parental, name, id, address, irpf, bank, residence,
            nationality, gender, hiring, custom-leave, termination, contract, workplace,
            manual_incidence, legal_entity Example: sick.
        starts_on (str | Unset): filter `employee updates` that started **later** the given param.
            Example: 2024-06-06.
        ends_on (str | Unset): filter `employee updates` that started **before** the given param.
            Example: 2024-06-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        employee_ids=employee_ids,
        legal_entities_ids=legal_entities_ids,
        type_=type_,
        starts_on=starts_on,
        ends_on=ends_on,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
) -> Response[ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200]:
    """Reads all Summaries

     This endpoint can be used to retrieve a list of `employee updates`.

    Args:
        ids (list[str] | Unset): retrieve only the `employee updates` that matches the `ids`
            passed in the request. Example: ['1', '2', '3'].
        employee_ids (list[str] | Unset): retrieve only the `employee updates` assigned to any
            `employee` specified in the request. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): retrieve only the `employee updates` assigned to
            any `legal entity` specified in the request. Example: ['1', '2', '3'].
        type_ (list[str] | Unset): filter `employee updates` that have the given type. The
            supported types are: sick, parental, name, id, address, irpf, bank, residence,
            nationality, gender, hiring, custom-leave, termination, contract, workplace,
            manual_incidence, legal_entity Example: sick.
        starts_on (str | Unset): filter `employee updates` that started **later** the given param.
            Example: 2024-06-06.
        ends_on (str | Unset): filter `employee updates` that started **before** the given param.
            Example: 2024-06-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        employee_ids=employee_ids,
        legal_entities_ids=legal_entities_ids,
        type_=type_,
        starts_on=starts_on,
        ends_on=ends_on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    legal_entities_ids: list[str] | Unset = UNSET,
    type_: list[str] | Unset = UNSET,
    starts_on: str | Unset = UNSET,
    ends_on: str | Unset = UNSET,
) -> ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200 | None:
    """Reads all Summaries

     This endpoint can be used to retrieve a list of `employee updates`.

    Args:
        ids (list[str] | Unset): retrieve only the `employee updates` that matches the `ids`
            passed in the request. Example: ['1', '2', '3'].
        employee_ids (list[str] | Unset): retrieve only the `employee updates` assigned to any
            `employee` specified in the request. Example: ['1', '2', '3'].
        legal_entities_ids (list[str] | Unset): retrieve only the `employee updates` assigned to
            any `legal entity` specified in the request. Example: ['1', '2', '3'].
        type_ (list[str] | Unset): filter `employee updates` that have the given type. The
            supported types are: sick, parental, name, id, address, irpf, bank, residence,
            nationality, gender, hiring, custom-leave, termination, contract, workplace,
            manual_incidence, legal_entity Example: sick.
        starts_on (str | Unset): filter `employee updates` that started **later** the given param.
            Example: 2024-06-06.
        ends_on (str | Unset): filter `employee updates` that started **before** the given param.
            Example: 2024-06-06.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesEmployeeUpdatesSummariesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            employee_ids=employee_ids,
            legal_entities_ids=legal_entities_ids,
            type_=type_,
            starts_on=starts_on,
            ends_on=ends_on,
        )
    ).parsed
