from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_project_management_projects_response_200 import (
    GetApi20260401ResourcesProjectManagementProjectsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    include_inputed_minutes: bool,
    include_costs: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    legal_entity_id: int | Unset = UNSET,
    client_ids: list[int] | Unset = UNSET,
    no_clients: bool | Unset = UNSET,
    total_currency: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["name"] = name

    params["name_or_code"] = name_or_code

    params["include_inputed_minutes"] = include_inputed_minutes

    params["include_costs"] = include_costs

    params["updated_after"] = updated_after

    params["legal_entity_id"] = legal_entity_id

    json_client_ids: list[int] | Unset = UNSET
    if not isinstance(client_ids, Unset):
        json_client_ids = client_ids

    params["client_ids[]"] = json_client_ids

    params["no_clients"] = no_clients

    params["total_currency"] = total_currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/project_management/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesProjectManagementProjectsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20260401ResourcesProjectManagementProjectsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesProjectManagementProjectsResponse200]:
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
    name: str | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    include_inputed_minutes: bool,
    include_costs: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    legal_entity_id: int | Unset = UNSET,
    client_ids: list[int] | Unset = UNSET,
    no_clients: bool | Unset = UNSET,
    total_currency: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesProjectManagementProjectsResponse200]:
    """Reads all Projects

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        ids (list[int] | Unset): Retrieve only the projects that matches the ids provided in the
            request. Example: [314159, 271828].
        name (str | Unset): Retrieve only the projects that match the name passed in the request.
            (deprecated) Example: Project Name.
        name_or_code (str | Unset): Retrieve only the projects that match the name or code passed
            in the request. Example: Project Name.
        include_inputed_minutes (bool): If true we will perform the minutes calculations and will
            be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_costs (bool | Unset): If true we will perform the costs calculations and will be
            return the total cost. If false, 0 will be returned and no costs calculations will be
            performed. Example: True.
        updated_after (str | Unset): Retrieve only the projects that were created or updated after
            the date provided in the request. Example: 1993-08-23.
        legal_entity_id (int | Unset): Retrieve only the projects that are related to the legal
            entity passed in the request. Example: 123.
        client_ids (list[int] | Unset): Retrieve only the projects that are related to the clients
            passed in the request, refers to finance/contacts. Example: [314159, 271828].
        no_clients (bool | Unset): Retrieve only the projects that are not related to any client,
            refers to finance/contacts.
        total_currency (str | Unset): Retrieve only the projects that have the total cost in the
            currency passed in the request. Example: USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesProjectManagementProjectsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        name=name,
        name_or_code=name_or_code,
        include_inputed_minutes=include_inputed_minutes,
        include_costs=include_costs,
        updated_after=updated_after,
        legal_entity_id=legal_entity_id,
        client_ids=client_ids,
        no_clients=no_clients,
        total_currency=total_currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    include_inputed_minutes: bool,
    include_costs: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    legal_entity_id: int | Unset = UNSET,
    client_ids: list[int] | Unset = UNSET,
    no_clients: bool | Unset = UNSET,
    total_currency: str | Unset = UNSET,
) -> GetApi20260401ResourcesProjectManagementProjectsResponse200 | None:
    """Reads all Projects

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        ids (list[int] | Unset): Retrieve only the projects that matches the ids provided in the
            request. Example: [314159, 271828].
        name (str | Unset): Retrieve only the projects that match the name passed in the request.
            (deprecated) Example: Project Name.
        name_or_code (str | Unset): Retrieve only the projects that match the name or code passed
            in the request. Example: Project Name.
        include_inputed_minutes (bool): If true we will perform the minutes calculations and will
            be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_costs (bool | Unset): If true we will perform the costs calculations and will be
            return the total cost. If false, 0 will be returned and no costs calculations will be
            performed. Example: True.
        updated_after (str | Unset): Retrieve only the projects that were created or updated after
            the date provided in the request. Example: 1993-08-23.
        legal_entity_id (int | Unset): Retrieve only the projects that are related to the legal
            entity passed in the request. Example: 123.
        client_ids (list[int] | Unset): Retrieve only the projects that are related to the clients
            passed in the request, refers to finance/contacts. Example: [314159, 271828].
        no_clients (bool | Unset): Retrieve only the projects that are not related to any client,
            refers to finance/contacts.
        total_currency (str | Unset): Retrieve only the projects that have the total cost in the
            currency passed in the request. Example: USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesProjectManagementProjectsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        name=name,
        name_or_code=name_or_code,
        include_inputed_minutes=include_inputed_minutes,
        include_costs=include_costs,
        updated_after=updated_after,
        legal_entity_id=legal_entity_id,
        client_ids=client_ids,
        no_clients=no_clients,
        total_currency=total_currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    include_inputed_minutes: bool,
    include_costs: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    legal_entity_id: int | Unset = UNSET,
    client_ids: list[int] | Unset = UNSET,
    no_clients: bool | Unset = UNSET,
    total_currency: str | Unset = UNSET,
) -> Response[GetApi20260401ResourcesProjectManagementProjectsResponse200]:
    """Reads all Projects

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        ids (list[int] | Unset): Retrieve only the projects that matches the ids provided in the
            request. Example: [314159, 271828].
        name (str | Unset): Retrieve only the projects that match the name passed in the request.
            (deprecated) Example: Project Name.
        name_or_code (str | Unset): Retrieve only the projects that match the name or code passed
            in the request. Example: Project Name.
        include_inputed_minutes (bool): If true we will perform the minutes calculations and will
            be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_costs (bool | Unset): If true we will perform the costs calculations and will be
            return the total cost. If false, 0 will be returned and no costs calculations will be
            performed. Example: True.
        updated_after (str | Unset): Retrieve only the projects that were created or updated after
            the date provided in the request. Example: 1993-08-23.
        legal_entity_id (int | Unset): Retrieve only the projects that are related to the legal
            entity passed in the request. Example: 123.
        client_ids (list[int] | Unset): Retrieve only the projects that are related to the clients
            passed in the request, refers to finance/contacts. Example: [314159, 271828].
        no_clients (bool | Unset): Retrieve only the projects that are not related to any client,
            refers to finance/contacts.
        total_currency (str | Unset): Retrieve only the projects that have the total cost in the
            currency passed in the request. Example: USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesProjectManagementProjectsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        name=name,
        name_or_code=name_or_code,
        include_inputed_minutes=include_inputed_minutes,
        include_costs=include_costs,
        updated_after=updated_after,
        legal_entity_id=legal_entity_id,
        client_ids=client_ids,
        no_clients=no_clients,
        total_currency=total_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_or_code: str | Unset = UNSET,
    include_inputed_minutes: bool,
    include_costs: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    legal_entity_id: int | Unset = UNSET,
    client_ids: list[int] | Unset = UNSET,
    no_clients: bool | Unset = UNSET,
    total_currency: str | Unset = UNSET,
) -> GetApi20260401ResourcesProjectManagementProjectsResponse200 | None:
    """Reads all Projects

     ###### **What does it do?** This reads the data of projects, and retrieves the information based on
    the permissions:

      - If the user has the `team_leader` permission, he will only be able to read the projects that he
    is the team leader.
      - If the user has the `reportees` permission, he will only be able to read the projects that he is
    the team leader or the projects that he is a team member.
      - If the user has `everyone` permission, he will be able to read all projects.
      - If the user has the `owned` permission, he will only be able to read the projects that he is the
    assigned.

    ###### **Is it related to other entities?** A project is always related to a company, so you can use
    the query params to list only the projects that are related to a specific company. ###### **Who can
    use it?** Only companies who have enabled the `projects_management` feature and users with the
    permission of read projects.

    Args:
        ids (list[int] | Unset): Retrieve only the projects that matches the ids provided in the
            request. Example: [314159, 271828].
        name (str | Unset): Retrieve only the projects that match the name passed in the request.
            (deprecated) Example: Project Name.
        name_or_code (str | Unset): Retrieve only the projects that match the name or code passed
            in the request. Example: Project Name.
        include_inputed_minutes (bool): If true we will perform the minutes calculations and will
            be return the total inputed_minutes. If false, 0 will be returned and no minutes
            calculations will be performed. Example: True.
        include_costs (bool | Unset): If true we will perform the costs calculations and will be
            return the total cost. If false, 0 will be returned and no costs calculations will be
            performed. Example: True.
        updated_after (str | Unset): Retrieve only the projects that were created or updated after
            the date provided in the request. Example: 1993-08-23.
        legal_entity_id (int | Unset): Retrieve only the projects that are related to the legal
            entity passed in the request. Example: 123.
        client_ids (list[int] | Unset): Retrieve only the projects that are related to the clients
            passed in the request, refers to finance/contacts. Example: [314159, 271828].
        no_clients (bool | Unset): Retrieve only the projects that are not related to any client,
            refers to finance/contacts.
        total_currency (str | Unset): Retrieve only the projects that have the total cost in the
            currency passed in the request. Example: USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesProjectManagementProjectsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            name=name,
            name_or_code=name_or_code,
            include_inputed_minutes=include_inputed_minutes,
            include_costs=include_costs,
            updated_after=updated_after,
            legal_entity_id=legal_entity_id,
            client_ids=client_ids,
            no_clients=no_clients,
            total_currency=total_currency,
        )
    ).parsed
