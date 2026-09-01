from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_review_evaluation import PerformanceReviewEvaluation
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/2026-10-01/resources/performance/review_evaluations/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PerformanceReviewEvaluation | None:
    if response.status_code == 200:
        response_200 = PerformanceReviewEvaluation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PerformanceReviewEvaluation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PerformanceReviewEvaluation]:
    r"""Reads a single Review evaluation

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewEvaluation]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> PerformanceReviewEvaluation | None:
    r"""Reads a single Review evaluation

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewEvaluation
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PerformanceReviewEvaluation]:
    r"""Reads a single Review evaluation

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewEvaluation]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> PerformanceReviewEvaluation | None:
    r"""Reads a single Review evaluation

     Retrieves the pending and published review evaluations. The evaluations are created based on the
    participants and the review types when the review process is started.

    For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations
    will be created for each participant when the review process starts. One will be for the self-
    review, where the participant is both the target and the reviewer. The other will be for the manager
    review, where the participant is the target, and the manager is the reviewer.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewEvaluation
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
