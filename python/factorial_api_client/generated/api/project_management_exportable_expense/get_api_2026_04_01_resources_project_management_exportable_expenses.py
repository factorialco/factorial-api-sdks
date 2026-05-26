from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20260401_resources_project_management_exportable_expenses_response_200 import (
    GetApi20260401ResourcesProjectManagementExportableExpensesResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start_date: str,
    end_date: str,
    project_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start_date"] = start_date

    params["end_date"] = end_date

    json_project_ids = project_ids

    params["project_ids[]"] = json_project_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-04-01/resources/project_management/exportable_expenses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20260401ResourcesProjectManagementExportableExpensesResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetApi20260401ResourcesProjectManagementExportableExpensesResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20260401ResourcesProjectManagementExportableExpensesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    project_ids: list[int],
) -> Response[GetApi20260401ResourcesProjectManagementExportableExpensesResponse200]:
    r"""Reads all Exportable expenses

     ###### **What does it do?**

      This will generate an export of the type **\"Project's expenses\"**. You will have to pass the
    start and end date to determine the range for which htis information will be exported; as well as
    the projects ids to get the information of specifically given projects.

    ###### **What params does it accept?**
      - `start_date`: It's mandatory to pass this data, being start date to delimit the range of
    information exported.
      - `end_date`: It's mandatory to pass this data, corresponding to an end date for the date range of
    data to be exported.
      - `project_ids`: Mandatory data to pass to the export, specifying the projects to be exported
    from.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        start_date (str):
        end_date (str):
        project_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesProjectManagementExportableExpensesResponse200]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        project_ids=project_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    project_ids: list[int],
) -> GetApi20260401ResourcesProjectManagementExportableExpensesResponse200 | None:
    r"""Reads all Exportable expenses

     ###### **What does it do?**

      This will generate an export of the type **\"Project's expenses\"**. You will have to pass the
    start and end date to determine the range for which htis information will be exported; as well as
    the projects ids to get the information of specifically given projects.

    ###### **What params does it accept?**
      - `start_date`: It's mandatory to pass this data, being start date to delimit the range of
    information exported.
      - `end_date`: It's mandatory to pass this data, corresponding to an end date for the date range of
    data to be exported.
      - `project_ids`: Mandatory data to pass to the export, specifying the projects to be exported
    from.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        start_date (str):
        end_date (str):
        project_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesProjectManagementExportableExpensesResponse200
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        project_ids=project_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    project_ids: list[int],
) -> Response[GetApi20260401ResourcesProjectManagementExportableExpensesResponse200]:
    r"""Reads all Exportable expenses

     ###### **What does it do?**

      This will generate an export of the type **\"Project's expenses\"**. You will have to pass the
    start and end date to determine the range for which htis information will be exported; as well as
    the projects ids to get the information of specifically given projects.

    ###### **What params does it accept?**
      - `start_date`: It's mandatory to pass this data, being start date to delimit the range of
    information exported.
      - `end_date`: It's mandatory to pass this data, corresponding to an end date for the date range of
    data to be exported.
      - `project_ids`: Mandatory data to pass to the export, specifying the projects to be exported
    from.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        start_date (str):
        end_date (str):
        project_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20260401ResourcesProjectManagementExportableExpensesResponse200]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        project_ids=project_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    project_ids: list[int],
) -> GetApi20260401ResourcesProjectManagementExportableExpensesResponse200 | None:
    r"""Reads all Exportable expenses

     ###### **What does it do?**

      This will generate an export of the type **\"Project's expenses\"**. You will have to pass the
    start and end date to determine the range for which htis information will be exported; as well as
    the projects ids to get the information of specifically given projects.

    ###### **What params does it accept?**
      - `start_date`: It's mandatory to pass this data, being start date to delimit the range of
    information exported.
      - `end_date`: It's mandatory to pass this data, corresponding to an end date for the date range of
    data to be exported.
      - `project_ids`: Mandatory data to pass to the export, specifying the projects to be exported
    from.

    ###### **Who can use it?**
    Only companies who have enabled the `projects_management` feature and users with the permission of
    read projects.

    Args:
        start_date (str):
        end_date (str):
        project_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20260401ResourcesProjectManagementExportableExpensesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            project_ids=project_ids,
        )
    ).parsed
