from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_20270101_resources_expenses_expensables_by_resources_item import (
    GetApi20270101ResourcesExpensesExpensablesByResourcesItem,
)
from ...models.get_api_20270101_resources_expenses_expensables_response_200 import (
    GetApi20270101ResourcesExpensesExpensablesResponse200,
)
from ...models.get_api_20270101_resources_expenses_expensables_status import (
    GetApi20270101ResourcesExpensesExpensablesStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    group_ids: list[str] | Unset = UNSET,
    by_resources: list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    reporter_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["company_id"] = company_id

    json_group_ids: list[str] | Unset = UNSET
    if not isinstance(group_ids, Unset):
        json_group_ids = group_ids

    params["group_ids[]"] = json_group_ids

    json_by_resources: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(by_resources, Unset):
        json_by_resources = []
        for by_resources_item_data in by_resources:
            by_resources_item = by_resources_item_data.to_dict()
            json_by_resources.append(by_resources_item)

    params["by_resources[]"] = json_by_resources

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_reporter_ids: list[str] | Unset = UNSET
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
        "url": "/api/2027-01-01/resources/expenses/expensables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20270101ResourcesExpensesExpensablesResponse200.from_dict(
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
) -> Response[ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200]:
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
    company_id: str | Unset = UNSET,
    group_ids: list[str] | Unset = UNSET,
    by_resources: list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    reporter_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200]:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[str] | Unset): Return only the expensables with these ids.
        company_id (str | Unset):
        group_ids (list[str] | Unset): Return only the expensables filed inside these expense
            groups, the report or trip bundles an employee submits several expensables in.
        by_resources (list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset):
        employee_ids (list[str] | Unset): Return only the expensables whose spending employee is
            one of these. When `reporter_ids` is given too the two are OR'ed, not intersected: the
            result holds the expensables owned by these employees plus the ones submitted by those
            reporters.
        reporter_ids (list[str] | Unset): Return only the expensables submitted by these employees
            on somebody else's behalf, such as an assistant or an office manager. OR'ed with
            `employee_ids` when both are given.
        status (GetApi20270101ResourcesExpensesExpensablesStatus | Unset): Return only the
            expensables in these states: `draft`, `pending`, `changes_requested`, `approved`,
            `rejected`, `reversed`, `in_payroll`, `sent_to_pay` or `paid`.
        creation_type (list[str] | Unset): Return only the expensables created this way: `manual`
            (entered by a person) or `automatic` (raised from a card transaction). Those are the only
            two values the filter understands, and any other string makes the read return nothing at
            all rather than ignoring the filter.
        from_ (str | Unset): Start of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `to`: given on its own it is ignored and no
            date narrowing happens.
        to (str | Unset): End of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `from`.
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200]
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
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    group_ids: list[str] | Unset = UNSET,
    by_resources: list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    reporter_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200 | None:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[str] | Unset): Return only the expensables with these ids.
        company_id (str | Unset):
        group_ids (list[str] | Unset): Return only the expensables filed inside these expense
            groups, the report or trip bundles an employee submits several expensables in.
        by_resources (list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset):
        employee_ids (list[str] | Unset): Return only the expensables whose spending employee is
            one of these. When `reporter_ids` is given too the two are OR'ed, not intersected: the
            result holds the expensables owned by these employees plus the ones submitted by those
            reporters.
        reporter_ids (list[str] | Unset): Return only the expensables submitted by these employees
            on somebody else's behalf, such as an assistant or an office manager. OR'ed with
            `employee_ids` when both are given.
        status (GetApi20270101ResourcesExpensesExpensablesStatus | Unset): Return only the
            expensables in these states: `draft`, `pending`, `changes_requested`, `approved`,
            `rejected`, `reversed`, `in_payroll`, `sent_to_pay` or `paid`.
        creation_type (list[str] | Unset): Return only the expensables created this way: `manual`
            (entered by a person) or `automatic` (raised from a card transaction). Those are the only
            two values the filter understands, and any other string makes the read return nothing at
            all rather than ignoring the filter.
        from_ (str | Unset): Start of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `to`: given on its own it is ignored and no
            date narrowing happens.
        to (str | Unset): End of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `from`.
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200
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
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    group_ids: list[str] | Unset = UNSET,
    by_resources: list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    reporter_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> Response[ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200]:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[str] | Unset): Return only the expensables with these ids.
        company_id (str | Unset):
        group_ids (list[str] | Unset): Return only the expensables filed inside these expense
            groups, the report or trip bundles an employee submits several expensables in.
        by_resources (list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset):
        employee_ids (list[str] | Unset): Return only the expensables whose spending employee is
            one of these. When `reporter_ids` is given too the two are OR'ed, not intersected: the
            result holds the expensables owned by these employees plus the ones submitted by those
            reporters.
        reporter_ids (list[str] | Unset): Return only the expensables submitted by these employees
            on somebody else's behalf, such as an assistant or an office manager. OR'ed with
            `employee_ids` when both are given.
        status (GetApi20270101ResourcesExpensesExpensablesStatus | Unset): Return only the
            expensables in these states: `draft`, `pending`, `changes_requested`, `approved`,
            `rejected`, `reversed`, `in_payroll`, `sent_to_pay` or `paid`.
        creation_type (list[str] | Unset): Return only the expensables created this way: `manual`
            (entered by a person) or `automatic` (raised from a card transaction). Those are the only
            two values the filter understands, and any other string makes the read return nothing at
            all rather than ignoring the filter.
        from_ (str | Unset): Start of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `to`: given on its own it is ignored and no
            date narrowing happens.
        to (str | Unset): End of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `from`.
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200]
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
    ids: list[str] | Unset = UNSET,
    company_id: str | Unset = UNSET,
    group_ids: list[str] | Unset = UNSET,
    by_resources: list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    reporter_ids: list[str] | Unset = UNSET,
    status: GetApi20270101ResourcesExpensesExpensablesStatus | Unset = UNSET,
    creation_type: list[str] | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_grouped: bool,
    include_attachments: bool,
    include_manual_drafts: bool,
) -> ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200 | None:
    """Reads all Expensables

     Reads all Expensables

    Args:
        ids (list[str] | Unset): Return only the expensables with these ids.
        company_id (str | Unset):
        group_ids (list[str] | Unset): Return only the expensables filed inside these expense
            groups, the report or trip bundles an employee submits several expensables in.
        by_resources (list[GetApi20270101ResourcesExpensesExpensablesByResourcesItem] | Unset):
        employee_ids (list[str] | Unset): Return only the expensables whose spending employee is
            one of these. When `reporter_ids` is given too the two are OR'ed, not intersected: the
            result holds the expensables owned by these employees plus the ones submitted by those
            reporters.
        reporter_ids (list[str] | Unset): Return only the expensables submitted by these employees
            on somebody else's behalf, such as an assistant or an office manager. OR'ed with
            `employee_ids` when both are given.
        status (GetApi20270101ResourcesExpensesExpensablesStatus | Unset): Return only the
            expensables in these states: `draft`, `pending`, `changes_requested`, `approved`,
            `rejected`, `reversed`, `in_payroll`, `sent_to_pay` or `paid`.
        creation_type (list[str] | Unset): Return only the expensables created this way: `manual`
            (entered by a person) or `automatic` (raised from a card transaction). Those are the only
            two values the filter understands, and any other string makes the read return nothing at
            all rather than ignoring the filter.
        from_ (str | Unset): Start of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `to`: given on its own it is ignored and no
            date narrowing happens.
        to (str | Unset): End of the window of expense dates (`effective_on`) to return,
            inclusive. It only takes effect together with `from`.
        search (str | Unset):
        include_grouped (bool):
        include_attachments (bool):
        include_manual_drafts (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetApi20270101ResourcesExpensesExpensablesResponse200
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
