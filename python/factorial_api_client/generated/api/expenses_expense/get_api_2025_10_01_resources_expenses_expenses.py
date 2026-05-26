from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_expenses_expenses_response_200 import (
    GetApi20251001ResourcesExpensesExpensesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[int] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[int] | Unset = UNSET,
    card_payment_ids: list[int] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_expenses_expensable_ids: list[int] | Unset = UNSET
    if not isinstance(expenses_expensable_ids, Unset):
        json_expenses_expensable_ids = expenses_expensable_ids

    params["expenses_expensable_ids[]"] = json_expenses_expensable_ids

    params["include_manual_drafts"] = include_manual_drafts

    json_employee_ids: list[int] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_external_authorization_ids: list[str] | Unset = UNSET
    if not isinstance(external_authorization_ids, Unset):
        json_external_authorization_ids = external_authorization_ids

    params["external_authorization_ids[]"] = json_external_authorization_ids

    json_card_ids: list[int] | Unset = UNSET
    if not isinstance(card_ids, Unset):
        json_card_ids = card_ids

    params["card_ids[]"] = json_card_ids

    json_card_payment_ids: list[int] | Unset = UNSET
    if not isinstance(card_payment_ids, Unset):
        json_card_payment_ids = card_payment_ids

    params["card_payment_ids[]"] = json_card_payment_ids

    params["include_attachments"] = include_attachments

    params["from"] = from_

    params["to"] = to

    json_dispute_ids: list[int] | Unset = UNSET
    if not isinstance(dispute_ids, Unset):
        json_dispute_ids = dispute_ids

    params["dispute_ids[]"] = json_dispute_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/expenses/expenses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesExpensesExpensesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesExpensesExpensesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesExpensesExpensesResponse200]:
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
    expenses_expensable_ids: list[int] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[int] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[int] | Unset = UNSET,
    card_payment_ids: list[int] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesExpensesExpensesResponse200]:
    """Reads all Expenses

     Reads all Expenses

    Args:
        ids (list[int] | Unset): The ids of the expenses to filter by
        expenses_expensable_ids (list[int] | Unset): The ids of the expensables to filter by
        include_manual_drafts (bool): Whether to include manual drafts Example: True.
        employee_ids (list[int] | Unset): The ids of the employees to filter by
        external_authorization_ids (list[str] | Unset): The ids of the external authorizations to
            filter by
        card_ids (list[int] | Unset): The ids of the cards to filter by
        card_payment_ids (list[int] | Unset): The ids of the card payments to filter by
        include_attachments (bool): Wether to include the attachments
        from_ (str | Unset): The time from which to filter expenses
        to (str | Unset): The time to which to filter expenses
        dispute_ids (list[int] | Unset): The ids of the disputes to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesExpensesExpensesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        expenses_expensable_ids=expenses_expensable_ids,
        include_manual_drafts=include_manual_drafts,
        employee_ids=employee_ids,
        external_authorization_ids=external_authorization_ids,
        card_ids=card_ids,
        card_payment_ids=card_payment_ids,
        include_attachments=include_attachments,
        from_=from_,
        to=to,
        dispute_ids=dispute_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[int] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[int] | Unset = UNSET,
    card_payment_ids: list[int] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesExpensesExpensesResponse200 | None:
    """Reads all Expenses

     Reads all Expenses

    Args:
        ids (list[int] | Unset): The ids of the expenses to filter by
        expenses_expensable_ids (list[int] | Unset): The ids of the expensables to filter by
        include_manual_drafts (bool): Whether to include manual drafts Example: True.
        employee_ids (list[int] | Unset): The ids of the employees to filter by
        external_authorization_ids (list[str] | Unset): The ids of the external authorizations to
            filter by
        card_ids (list[int] | Unset): The ids of the cards to filter by
        card_payment_ids (list[int] | Unset): The ids of the card payments to filter by
        include_attachments (bool): Wether to include the attachments
        from_ (str | Unset): The time from which to filter expenses
        to (str | Unset): The time to which to filter expenses
        dispute_ids (list[int] | Unset): The ids of the disputes to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesExpensesExpensesResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        expenses_expensable_ids=expenses_expensable_ids,
        include_manual_drafts=include_manual_drafts,
        employee_ids=employee_ids,
        external_authorization_ids=external_authorization_ids,
        card_ids=card_ids,
        card_payment_ids=card_payment_ids,
        include_attachments=include_attachments,
        from_=from_,
        to=to,
        dispute_ids=dispute_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[int] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[int] | Unset = UNSET,
    card_payment_ids: list[int] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesExpensesExpensesResponse200]:
    """Reads all Expenses

     Reads all Expenses

    Args:
        ids (list[int] | Unset): The ids of the expenses to filter by
        expenses_expensable_ids (list[int] | Unset): The ids of the expensables to filter by
        include_manual_drafts (bool): Whether to include manual drafts Example: True.
        employee_ids (list[int] | Unset): The ids of the employees to filter by
        external_authorization_ids (list[str] | Unset): The ids of the external authorizations to
            filter by
        card_ids (list[int] | Unset): The ids of the cards to filter by
        card_payment_ids (list[int] | Unset): The ids of the card payments to filter by
        include_attachments (bool): Wether to include the attachments
        from_ (str | Unset): The time from which to filter expenses
        to (str | Unset): The time to which to filter expenses
        dispute_ids (list[int] | Unset): The ids of the disputes to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesExpensesExpensesResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        expenses_expensable_ids=expenses_expensable_ids,
        include_manual_drafts=include_manual_drafts,
        employee_ids=employee_ids,
        external_authorization_ids=external_authorization_ids,
        card_ids=card_ids,
        card_payment_ids=card_payment_ids,
        include_attachments=include_attachments,
        from_=from_,
        to=to,
        dispute_ids=dispute_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    expenses_expensable_ids: list[int] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[int] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[int] | Unset = UNSET,
    card_payment_ids: list[int] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesExpensesExpensesResponse200 | None:
    """Reads all Expenses

     Reads all Expenses

    Args:
        ids (list[int] | Unset): The ids of the expenses to filter by
        expenses_expensable_ids (list[int] | Unset): The ids of the expensables to filter by
        include_manual_drafts (bool): Whether to include manual drafts Example: True.
        employee_ids (list[int] | Unset): The ids of the employees to filter by
        external_authorization_ids (list[str] | Unset): The ids of the external authorizations to
            filter by
        card_ids (list[int] | Unset): The ids of the cards to filter by
        card_payment_ids (list[int] | Unset): The ids of the card payments to filter by
        include_attachments (bool): Wether to include the attachments
        from_ (str | Unset): The time from which to filter expenses
        to (str | Unset): The time to which to filter expenses
        dispute_ids (list[int] | Unset): The ids of the disputes to filter by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesExpensesExpensesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            expenses_expensable_ids=expenses_expensable_ids,
            include_manual_drafts=include_manual_drafts,
            employee_ids=employee_ids,
            external_authorization_ids=external_authorization_ids,
            card_ids=card_ids,
            card_payment_ids=card_payment_ids,
            include_attachments=include_attachments,
            from_=from_,
            to=to,
            dispute_ids=dispute_ids,
        )
    ).parsed
