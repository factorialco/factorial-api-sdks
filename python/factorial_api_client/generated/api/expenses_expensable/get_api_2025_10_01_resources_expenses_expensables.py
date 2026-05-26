from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_expenses_expensables_response_200 import (
    GetApi20251001ResourcesExpensesExpensablesResponse200,
)
from ...models.get_api_20251001_resources_expenses_expensables_status import (
    GetApi20251001ResourcesExpensesExpensablesStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    by_resources: list[Any] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    reporter_ids: list[int] | Unset = UNSET,
    status: GetApi20251001ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["company_id"] = company_id

    json_group_ids: list[int] | Unset = UNSET
    if not isinstance(group_ids, Unset):
        json_group_ids = group_ids

    params["group_ids[]"] = json_group_ids

    json_by_resources: list[Any] | Unset = UNSET
    if not isinstance(by_resources, Unset):
        json_by_resources = by_resources

    params["by_resources[]"] = json_by_resources

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_reporter_ids: list[int] | Unset = UNSET
    if not isinstance(reporter_ids, Unset):
        json_reporter_ids = reporter_ids

    params["reporter_ids[]"] = json_reporter_ids

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status[]"] = json_status

    json_creation_type: list[str] | Unset = UNSET
    if not isinstance(creation_type, Unset):
        json_creation_type = creation_type

    params["creation_type[]"] = json_creation_type

    params["from"] = from_

    params["to"] = to

    params["search"] = search

    params["include_grouped"] = include_grouped

    params["include_attachments"] = include_attachments

    params["include_manual_drafts"] = include_manual_drafts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/expenses/expensables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesExpensesExpensablesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesExpensesExpensablesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesExpensesExpensablesResponse200]:
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
    company_id: int | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    by_resources: list[Any] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    reporter_ids: list[int] | Unset = UNSET,
    status: GetApi20251001ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> Response[GetApi20251001ResourcesExpensesExpensablesResponse200]:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        group_ids (list[int] | Unset):
        by_resources (list[Any] | Unset):
        employee_ids (list[int] | Unset):
        reporter_ids (list[int] | Unset):
        status (GetApi20251001ResourcesExpensesExpensablesStatus | Unset):
        creation_type (list[str] | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesExpensesExpensablesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        group_ids=group_ids,
        by_resources=by_resources,
        employee_ids=employee_ids,
        reporter_ids=reporter_ids,
        status=status,
        creation_type=creation_type,
        from_=from_,
        to=to,
        search=search,
        include_grouped=include_grouped,
        include_attachments=include_attachments,
        include_manual_drafts=include_manual_drafts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    by_resources: list[Any] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    reporter_ids: list[int] | Unset = UNSET,
    status: GetApi20251001ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> GetApi20251001ResourcesExpensesExpensablesResponse200 | None:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        group_ids (list[int] | Unset):
        by_resources (list[Any] | Unset):
        employee_ids (list[int] | Unset):
        reporter_ids (list[int] | Unset):
        status (GetApi20251001ResourcesExpensesExpensablesStatus | Unset):
        creation_type (list[str] | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesExpensesExpensablesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        company_id=company_id,
        group_ids=group_ids,
        by_resources=by_resources,
        employee_ids=employee_ids,
        reporter_ids=reporter_ids,
        status=status,
        creation_type=creation_type,
        from_=from_,
        to=to,
        search=search,
        include_grouped=include_grouped,
        include_attachments=include_attachments,
        include_manual_drafts=include_manual_drafts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    by_resources: list[Any] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    reporter_ids: list[int] | Unset = UNSET,
    status: GetApi20251001ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> Response[GetApi20251001ResourcesExpensesExpensablesResponse200]:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        group_ids (list[int] | Unset):
        by_resources (list[Any] | Unset):
        employee_ids (list[int] | Unset):
        reporter_ids (list[int] | Unset):
        status (GetApi20251001ResourcesExpensesExpensablesStatus | Unset):
        creation_type (list[str] | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesExpensesExpensablesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        company_id=company_id,
        group_ids=group_ids,
        by_resources=by_resources,
        employee_ids=employee_ids,
        reporter_ids=reporter_ids,
        status=status,
        creation_type=creation_type,
        from_=from_,
        to=to,
        search=search,
        include_grouped=include_grouped,
        include_attachments=include_attachments,
        include_manual_drafts=include_manual_drafts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    company_id: int | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    by_resources: list[Any] | Unset = UNSET,
    employee_ids: list[int] | Unset = UNSET,
    reporter_ids: list[int] | Unset = UNSET,
    status: GetApi20251001ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> GetApi20251001ResourcesExpensesExpensablesResponse200 | None:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[int] | Unset):
        company_id (int | Unset):
        group_ids (list[int] | Unset):
        by_resources (list[Any] | Unset):
        employee_ids (list[int] | Unset):
        reporter_ids (list[int] | Unset):
        status (GetApi20251001ResourcesExpensesExpensablesStatus | Unset):
        creation_type (list[str] | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesExpensesExpensablesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            company_id=company_id,
            group_ids=group_ids,
            by_resources=by_resources,
            employee_ids=employee_ids,
            reporter_ids=reporter_ids,
            status=status,
            creation_type=creation_type,
            from_=from_,
            to=to,
            search=search,
            include_grouped=include_grouped,
            include_attachments=include_attachments,
            include_manual_drafts=include_manual_drafts,
        )
    ).parsed
