from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_expenses_mileages_response_200 import (
    GetApi20260701ResourcesExpensesMileagesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[str] | Unset = UNSET,
    expenses_expensable_ids: list[str] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[str] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_expenses_expensable_ids: list[str] | Unset = UNSET
    if not isinstance(expenses_expensable_ids, Unset):
        json_expenses_expensable_ids = expenses_expensable_ids

    params["expenses_expensable_ids[]"] = json_expenses_expensable_ids

    params["include_manual_drafts"] = include_manual_drafts

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_external_authorization_ids: list[str] | Unset = UNSET
    if not isinstance(external_authorization_ids, Unset):
        json_external_authorization_ids = external_authorization_ids

    params["external_authorization_ids[]"] = json_external_authorization_ids

    json_card_ids: list[str] | Unset = UNSET
    if not isinstance(card_ids, Unset):
        json_card_ids = card_ids

    params["card_ids[]"] = json_card_ids

    json_card_payment_ids: list[str] | Unset = UNSET
    if not isinstance(card_payment_ids, Unset):
        json_card_payment_ids = card_payment_ids

    params["card_payment_ids[]"] = json_card_payment_ids

    params["include_attachments"] = include_attachments

    params["from"] = from_

    params["to"] = to

    json_dispute_ids: list[str] | Unset = UNSET
    if not isinstance(dispute_ids, Unset):
        json_dispute_ids = dispute_ids

    params["dispute_ids[]"] = json_dispute_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/expenses/mileages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesExpensesMileagesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesExpensesMileagesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesExpensesMileagesResponse200]:
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
    expenses_expensable_ids: list[str] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[str] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesExpensesMileagesResponse200]:
    """Reads all Mileages

     Reads all Mileages

    Args:
        ids (list[str] | Unset):
        expenses_expensable_ids (list[str] | Unset):
        include_manual_drafts (bool):
        employee_ids (list[str] | Unset):
        external_authorization_ids (list[str] | Unset):
        card_ids (list[str] | Unset):
        card_payment_ids (list[str] | Unset):
        include_attachments (bool):
        from_ (str | Unset):
        to (str | Unset):
        dispute_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesExpensesMileagesResponse200]
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
    ids: list[str] | Unset = UNSET,
    expenses_expensable_ids: list[str] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[str] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesExpensesMileagesResponse200 | None:
    """Reads all Mileages

     Reads all Mileages

    Args:
        ids (list[str] | Unset):
        expenses_expensable_ids (list[str] | Unset):
        include_manual_drafts (bool):
        employee_ids (list[str] | Unset):
        external_authorization_ids (list[str] | Unset):
        card_ids (list[str] | Unset):
        card_payment_ids (list[str] | Unset):
        include_attachments (bool):
        from_ (str | Unset):
        to (str | Unset):
        dispute_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesExpensesMileagesResponse200
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
    ids: list[str] | Unset = UNSET,
    expenses_expensable_ids: list[str] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[str] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesExpensesMileagesResponse200]:
    """Reads all Mileages

     Reads all Mileages

    Args:
        ids (list[str] | Unset):
        expenses_expensable_ids (list[str] | Unset):
        include_manual_drafts (bool):
        employee_ids (list[str] | Unset):
        external_authorization_ids (list[str] | Unset):
        card_ids (list[str] | Unset):
        card_payment_ids (list[str] | Unset):
        include_attachments (bool):
        from_ (str | Unset):
        to (str | Unset):
        dispute_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesExpensesMileagesResponse200]
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
    ids: list[str] | Unset = UNSET,
    expenses_expensable_ids: list[str] | Unset = UNSET,
    include_manual_drafts: bool,
    employee_ids: list[str] | Unset = UNSET,
    external_authorization_ids: list[str] | Unset = UNSET,
    card_ids: list[str] | Unset = UNSET,
    card_payment_ids: list[str] | Unset = UNSET,
    include_attachments: bool,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    dispute_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesExpensesMileagesResponse200 | None:
    """Reads all Mileages

     Reads all Mileages

    Args:
        ids (list[str] | Unset):
        expenses_expensable_ids (list[str] | Unset):
        include_manual_drafts (bool):
        employee_ids (list[str] | Unset):
        external_authorization_ids (list[str] | Unset):
        card_ids (list[str] | Unset):
        card_payment_ids (list[str] | Unset):
        include_attachments (bool):
        from_ (str | Unset):
        to (str | Unset):
        dispute_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesExpensesMileagesResponse200
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
