from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contracts_contract_flow import ContractsContractFlow
from ...models.post_api_20261001_resources_contracts_legal_entity_changes_body import (
    PostApi20261001ResourcesContractsLegalEntityChangesBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2026-10-01/resources/contracts/legal_entity_changes",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContractsContractFlow | None:
    if response.status_code == 201:
        response_201 = ContractsContractFlow.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContractsContractFlow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset = UNSET,
) -> Response[ContractsContractFlow]:
    """Move an employee to another legal entity.

     Creates a new contract under the target legal entity, plus its first contract version, effective on
    the given date. The employee's own legal entity follows on that date, when the new version becomes
    their reference contract version — so the employee still belongs to the previous legal entity until
    then. The country data of the new version is resolved against the target legal entity's template, so
    fields that only existed under the previous one are dropped. Requires the legal entity change
    feature to be enabled for the company.

    Args:
        body (PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractsContractFlow]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset = UNSET,
) -> ContractsContractFlow | None:
    """Move an employee to another legal entity.

     Creates a new contract under the target legal entity, plus its first contract version, effective on
    the given date. The employee's own legal entity follows on that date, when the new version becomes
    their reference contract version — so the employee still belongs to the previous legal entity until
    then. The country data of the new version is resolved against the target legal entity's template, so
    fields that only existed under the previous one are dropped. Requires the legal entity change
    feature to be enabled for the company.

    Args:
        body (PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractsContractFlow
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset = UNSET,
) -> Response[ContractsContractFlow]:
    """Move an employee to another legal entity.

     Creates a new contract under the target legal entity, plus its first contract version, effective on
    the given date. The employee's own legal entity follows on that date, when the new version becomes
    their reference contract version — so the employee still belongs to the previous legal entity until
    then. The country data of the new version is resolved against the target legal entity's template, so
    fields that only existed under the previous one are dropped. Requires the legal entity change
    feature to be enabled for the company.

    Args:
        body (PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractsContractFlow]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset = UNSET,
) -> ContractsContractFlow | None:
    """Move an employee to another legal entity.

     Creates a new contract under the target legal entity, plus its first contract version, effective on
    the given date. The employee's own legal entity follows on that date, when the new version becomes
    their reference contract version — so the employee still belongs to the previous legal entity until
    then. The country data of the new version is resolved against the target legal entity's template, so
    fields that only existed under the previous one are dropped. Requires the legal entity change
    feature to be enabled for the company.

    Args:
        body (PostApi20261001ResourcesContractsLegalEntityChangesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractsContractFlow
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
