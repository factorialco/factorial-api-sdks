from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_timeoff_french_leave_day_counts_response_200 import (
    GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    include_deleted: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_leave_ids: list[str] | Unset = UNSET
    if not isinstance(leave_ids, Unset):
        json_leave_ids = leave_ids

    params["leave_ids[]"] = json_leave_ids

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    params["from"] = from_

    params["to"] = to

    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2027-01-01/resources/timeoff/french_leave_day_counts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    include_deleted: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200]:
    """Reads all French leave day counts

     Returns the French day count for each requested leave. Leaves whose details the requester cannot see
    are omitted rather than rejected, so a partial result is normal. A leave with no computable count is
    also omitted. The request must be bounded — send either `leave_ids` or both `from` and `to`.

    Args:
        leave_ids (list[str] | Unset): Only return day counts for these leaves. Required unless
            `from` and `to` are sent Example: ['1', '2'].
        employee_ids (list[str] | Unset): Only return day counts for leaves belonging to these
            employees Example: ['42'].
        from_ (str | Unset): Start of the period the count is computed over (YYYY-MM-DD). Leaves
            are filtered to those overlapping the period, and a leave extending beyond it is counted
            only for the days inside. Must be sent together with `to`. Required unless `leave_ids` is
            sent. Example: 2026-01-01.
        to (str | Unset): End of the period the count is computed over (YYYY-MM-DD). Must be sent
            together with `from`. Required unless `leave_ids` is sent. Example: 2026-01-31.
        include_deleted (bool): Include leaves that have been deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200]
    """

    kwargs = _get_kwargs(
        leave_ids=leave_ids,
        employee_ids=employee_ids,
        from_=from_,
        to=to,
        include_deleted=include_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    include_deleted: bool,
) -> ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200 | None:
    """Reads all French leave day counts

     Returns the French day count for each requested leave. Leaves whose details the requester cannot see
    are omitted rather than rejected, so a partial result is normal. A leave with no computable count is
    also omitted. The request must be bounded — send either `leave_ids` or both `from` and `to`.

    Args:
        leave_ids (list[str] | Unset): Only return day counts for these leaves. Required unless
            `from` and `to` are sent Example: ['1', '2'].
        employee_ids (list[str] | Unset): Only return day counts for leaves belonging to these
            employees Example: ['42'].
        from_ (str | Unset): Start of the period the count is computed over (YYYY-MM-DD). Leaves
            are filtered to those overlapping the period, and a leave extending beyond it is counted
            only for the days inside. Must be sent together with `to`. Required unless `leave_ids` is
            sent. Example: 2026-01-01.
        to (str | Unset): End of the period the count is computed over (YYYY-MM-DD). Must be sent
            together with `from`. Required unless `leave_ids` is sent. Example: 2026-01-31.
        include_deleted (bool): Include leaves that have been deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200
    """

    return sync_detailed(
        client=client,
        leave_ids=leave_ids,
        employee_ids=employee_ids,
        from_=from_,
        to=to,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    include_deleted: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200]:
    """Reads all French leave day counts

     Returns the French day count for each requested leave. Leaves whose details the requester cannot see
    are omitted rather than rejected, so a partial result is normal. A leave with no computable count is
    also omitted. The request must be bounded — send either `leave_ids` or both `from` and `to`.

    Args:
        leave_ids (list[str] | Unset): Only return day counts for these leaves. Required unless
            `from` and `to` are sent Example: ['1', '2'].
        employee_ids (list[str] | Unset): Only return day counts for leaves belonging to these
            employees Example: ['42'].
        from_ (str | Unset): Start of the period the count is computed over (YYYY-MM-DD). Leaves
            are filtered to those overlapping the period, and a leave extending beyond it is counted
            only for the days inside. Must be sent together with `to`. Required unless `leave_ids` is
            sent. Example: 2026-01-01.
        to (str | Unset): End of the period the count is computed over (YYYY-MM-DD). Must be sent
            together with `from`. Required unless `leave_ids` is sent. Example: 2026-01-31.
        include_deleted (bool): Include leaves that have been deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200]
    """

    kwargs = _get_kwargs(
        leave_ids=leave_ids,
        employee_ids=employee_ids,
        from_=from_,
        to=to,
        include_deleted=include_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    leave_ids: list[str] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    include_deleted: bool,
) -> ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200 | None:
    """Reads all French leave day counts

     Returns the French day count for each requested leave. Leaves whose details the requester cannot see
    are omitted rather than rejected, so a partial result is normal. A leave with no computable count is
    also omitted. The request must be bounded — send either `leave_ids` or both `from` and `to`.

    Args:
        leave_ids (list[str] | Unset): Only return day counts for these leaves. Required unless
            `from` and `to` are sent Example: ['1', '2'].
        employee_ids (list[str] | Unset): Only return day counts for leaves belonging to these
            employees Example: ['42'].
        from_ (str | Unset): Start of the period the count is computed over (YYYY-MM-DD). Leaves
            are filtered to those overlapping the period, and a leave extending beyond it is counted
            only for the days inside. Must be sent together with `to`. Required unless `leave_ids` is
            sent. Example: 2026-01-01.
        to (str | Unset): End of the period the count is computed over (YYYY-MM-DD). Must be sent
            together with `from`. Required unless `leave_ids` is sent. Example: 2026-01-31.
        include_deleted (bool): Include leaves that have been deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesTimeoffFrenchLeaveDayCountsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            leave_ids=leave_ids,
            employee_ids=employee_ids,
            from_=from_,
            to=to,
            include_deleted=include_deleted,
        )
    ).parsed
