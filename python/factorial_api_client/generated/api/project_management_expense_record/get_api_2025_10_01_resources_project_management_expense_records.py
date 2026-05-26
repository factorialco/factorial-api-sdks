from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_20251001_resources_project_management_expense_records_response_200 import (
    GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    expense_ids: list[int] | Unset = UNSET,
    project_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    employee_user_name_like: str | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["start_date"] = start_date

    params["end_date"] = end_date

    json_expense_ids: list[int] | Unset = UNSET
    if not isinstance(expense_ids, Unset):
        json_expense_ids = expense_ids

    params["expense_ids[]"] = json_expense_ids

    json_project_ids: list[int] | Unset = UNSET
    if not isinstance(project_ids, Unset):
        json_project_ids = project_ids

    params["project_ids[]"] = json_project_ids

    json_subproject_ids: list[int] | Unset = UNSET
    if not isinstance(subproject_ids, Unset):
        json_subproject_ids = subproject_ids

    params["subproject_ids[]"] = json_subproject_ids

    params["updated_after"] = updated_after

    params["employee_user_name_like"] = employee_user_name_like

    json_project_worker_ids: list[int] | Unset = UNSET
    if not isinstance(project_worker_ids, Unset):
        json_project_worker_ids = project_worker_ids

    params["project_worker_ids[]"] = json_project_worker_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2025-10-01/resources/project_management/expense_records",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200]:
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
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    expense_ids: list[int] | Unset = UNSET,
    project_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    employee_user_name_like: str | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200]:
    """Reads all Expense records

     Reads all Expense records

    Args:
        ids (list[int] | Unset): Retrieve only the expense records that matches the project ids
            provided in the request. Example: [123, 456].
        start_date (str | Unset): Retrieve only the expense records with end date greater than or
            equal to the start date provided in the request. Example: 2025-01-01.
        end_date (str | Unset): Retrieve only the expense records with start date less than or
            equal to the end date provided in the request. Example: 2025-01-01.
        expense_ids (list[int] | Unset): Retrieve only the expense records that matches the
            expense ids provided in the request. Example: [123, 456].
        project_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project ids provided in the request. Example: [123, 456].
        subproject_ids (list[int] | Unset): Retrieve only the expense records that matches the
            subproject ids provided in the request. Example: [123, 456].
        updated_after (str | Unset): Retrieve only the expense records that matches the updated
            after date provided in the request. Example: 2025-01-01.
        employee_user_name_like (str | Unset): Retrieve only the expense records that matches the
            employee user name like provided in the request. Example: John Doe.
        project_worker_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project worker ids provided in the request. Example: [123, 456].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        start_date=start_date,
        end_date=end_date,
        expense_ids=expense_ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        updated_after=updated_after,
        employee_user_name_like=employee_user_name_like,
        project_worker_ids=project_worker_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    expense_ids: list[int] | Unset = UNSET,
    project_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    employee_user_name_like: str | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200 | None:
    """Reads all Expense records

     Reads all Expense records

    Args:
        ids (list[int] | Unset): Retrieve only the expense records that matches the project ids
            provided in the request. Example: [123, 456].
        start_date (str | Unset): Retrieve only the expense records with end date greater than or
            equal to the start date provided in the request. Example: 2025-01-01.
        end_date (str | Unset): Retrieve only the expense records with start date less than or
            equal to the end date provided in the request. Example: 2025-01-01.
        expense_ids (list[int] | Unset): Retrieve only the expense records that matches the
            expense ids provided in the request. Example: [123, 456].
        project_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project ids provided in the request. Example: [123, 456].
        subproject_ids (list[int] | Unset): Retrieve only the expense records that matches the
            subproject ids provided in the request. Example: [123, 456].
        updated_after (str | Unset): Retrieve only the expense records that matches the updated
            after date provided in the request. Example: 2025-01-01.
        employee_user_name_like (str | Unset): Retrieve only the expense records that matches the
            employee user name like provided in the request. Example: John Doe.
        project_worker_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project worker ids provided in the request. Example: [123, 456].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        start_date=start_date,
        end_date=end_date,
        expense_ids=expense_ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        updated_after=updated_after,
        employee_user_name_like=employee_user_name_like,
        project_worker_ids=project_worker_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    expense_ids: list[int] | Unset = UNSET,
    project_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    employee_user_name_like: str | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
) -> Response[GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200]:
    """Reads all Expense records

     Reads all Expense records

    Args:
        ids (list[int] | Unset): Retrieve only the expense records that matches the project ids
            provided in the request. Example: [123, 456].
        start_date (str | Unset): Retrieve only the expense records with end date greater than or
            equal to the start date provided in the request. Example: 2025-01-01.
        end_date (str | Unset): Retrieve only the expense records with start date less than or
            equal to the end date provided in the request. Example: 2025-01-01.
        expense_ids (list[int] | Unset): Retrieve only the expense records that matches the
            expense ids provided in the request. Example: [123, 456].
        project_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project ids provided in the request. Example: [123, 456].
        subproject_ids (list[int] | Unset): Retrieve only the expense records that matches the
            subproject ids provided in the request. Example: [123, 456].
        updated_after (str | Unset): Retrieve only the expense records that matches the updated
            after date provided in the request. Example: 2025-01-01.
        employee_user_name_like (str | Unset): Retrieve only the expense records that matches the
            employee user name like provided in the request. Example: John Doe.
        project_worker_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project worker ids provided in the request. Example: [123, 456].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        start_date=start_date,
        end_date=end_date,
        expense_ids=expense_ids,
        project_ids=project_ids,
        subproject_ids=subproject_ids,
        updated_after=updated_after,
        employee_user_name_like=employee_user_name_like,
        project_worker_ids=project_worker_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    expense_ids: list[int] | Unset = UNSET,
    project_ids: list[int] | Unset = UNSET,
    subproject_ids: list[int] | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    employee_user_name_like: str | Unset = UNSET,
    project_worker_ids: list[int] | Unset = UNSET,
) -> GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200 | None:
    """Reads all Expense records

     Reads all Expense records

    Args:
        ids (list[int] | Unset): Retrieve only the expense records that matches the project ids
            provided in the request. Example: [123, 456].
        start_date (str | Unset): Retrieve only the expense records with end date greater than or
            equal to the start date provided in the request. Example: 2025-01-01.
        end_date (str | Unset): Retrieve only the expense records with start date less than or
            equal to the end date provided in the request. Example: 2025-01-01.
        expense_ids (list[int] | Unset): Retrieve only the expense records that matches the
            expense ids provided in the request. Example: [123, 456].
        project_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project ids provided in the request. Example: [123, 456].
        subproject_ids (list[int] | Unset): Retrieve only the expense records that matches the
            subproject ids provided in the request. Example: [123, 456].
        updated_after (str | Unset): Retrieve only the expense records that matches the updated
            after date provided in the request. Example: 2025-01-01.
        employee_user_name_like (str | Unset): Retrieve only the expense records that matches the
            employee user name like provided in the request. Example: John Doe.
        project_worker_ids (list[int] | Unset): Retrieve only the expense records that matches the
            project worker ids provided in the request. Example: [123, 456].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApi20251001ResourcesProjectManagementExpenseRecordsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            start_date=start_date,
            end_date=end_date,
            expense_ids=expense_ids,
            project_ids=project_ids,
            subproject_ids=subproject_ids,
            updated_after=updated_after,
            employee_user_name_like=employee_user_name_like,
            project_worker_ids=project_worker_ids,
        )
    ).parsed
