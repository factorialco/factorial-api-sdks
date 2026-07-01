from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260701_resources_payroll_supplements_response_200 import (
    GetApi20260701ResourcesPayrollSupplementsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    policy_period_ids: list[str],
    compensation_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_employee_ids: list[str] | Unset = UNSET
    if not isinstance(employee_ids, Unset):
        json_employee_ids = employee_ids

    params["employee_ids[]"] = json_employee_ids

    json_policy_period_ids = policy_period_ids

    params["policy_period_ids[]"] = json_policy_period_ids

    params["compensation_id"] = compensation_id

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_legal_entity_ids: list[str] | Unset = UNSET
    if not isinstance(legal_entity_ids, Unset):
        json_legal_entity_ids = legal_entity_ids

    params["legal_entity_ids[]"] = json_legal_entity_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-07-01/resources/payroll/supplements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260701ResourcesPayrollSupplementsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260701ResourcesPayrollSupplementsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260701ResourcesPayrollSupplementsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    policy_period_ids: list[str],
    compensation_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesPayrollSupplementsResponse200]:
    """Reads all Supplements

     Reads all Supplements

    Args:
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        policy_period_ids (list[str]): The policy period ids to retrieve Example: ['1'].
        compensation_id (str | Unset): The compensation id to retrieve Example: 1.
        ids (list[str] | Unset): ids Example: ['1'].
        legal_entity_ids (list[str] | Unset): The legal entities id to retrieve Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesPayrollSupplementsResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        employee_ids=employee_ids,
        policy_period_ids=policy_period_ids,
        compensation_id=compensation_id,
        ids=ids,
        legal_entity_ids=legal_entity_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    policy_period_ids: list[str],
    compensation_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesPayrollSupplementsResponse200 | None:
    """Reads all Supplements

     Reads all Supplements

    Args:
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        policy_period_ids (list[str]): The policy period ids to retrieve Example: ['1'].
        compensation_id (str | Unset): The compensation id to retrieve Example: 1.
        ids (list[str] | Unset): ids Example: ['1'].
        legal_entity_ids (list[str] | Unset): The legal entities id to retrieve Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesPayrollSupplementsResponse200
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        employee_ids=employee_ids,
        policy_period_ids=policy_period_ids,
        compensation_id=compensation_id,
        ids=ids,
        legal_entity_ids=legal_entity_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    policy_period_ids: list[str],
    compensation_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
) -> Response[GetApi20260701ResourcesPayrollSupplementsResponse200]:
    """Reads all Supplements

     Reads all Supplements

    Args:
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        policy_period_ids (list[str]): The policy period ids to retrieve Example: ['1'].
        compensation_id (str | Unset): The compensation id to retrieve Example: 1.
        ids (list[str] | Unset): ids Example: ['1'].
        legal_entity_ids (list[str] | Unset): The legal entities id to retrieve Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260701ResourcesPayrollSupplementsResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        employee_ids=employee_ids,
        policy_period_ids=policy_period_ids,
        compensation_id=compensation_id,
        ids=ids,
        legal_entity_ids=legal_entity_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    employee_ids: list[str] | Unset = UNSET,
    policy_period_ids: list[str],
    compensation_id: str | Unset = UNSET,
    ids: list[str] | Unset = UNSET,
    legal_entity_ids: list[str] | Unset = UNSET,
) -> GetApi20260701ResourcesPayrollSupplementsResponse200 | None:
    """Reads all Supplements

     Reads all Supplements

    Args:
        from_ (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        to (str | Unset): Valid date following the format YYYY-MM-DD Example: 2024-01-01.
        employee_ids (list[str] | Unset): The employee ids to retrieve Example: ['1'].
        policy_period_ids (list[str]): The policy period ids to retrieve Example: ['1'].
        compensation_id (str | Unset): The compensation id to retrieve Example: 1.
        ids (list[str] | Unset): ids Example: ['1'].
        legal_entity_ids (list[str] | Unset): The legal entities id to retrieve Example: ['1'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260701ResourcesPayrollSupplementsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            employee_ids=employee_ids,
            policy_period_ids=policy_period_ids,
            compensation_id=compensation_id,
            ids=ids,
            legal_entity_ids=legal_entity_ids,
        )
    ).parsed
