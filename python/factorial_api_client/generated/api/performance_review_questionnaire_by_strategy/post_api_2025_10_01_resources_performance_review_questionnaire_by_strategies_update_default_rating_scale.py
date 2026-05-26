from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.performance_review_questionnaires_by_strategy import (
    PerformanceReviewQuestionnairesByStrategy,
)
from ...models.post_api_20251001_resources_performance_review_questionnaire_by_strategies_update_default_rating_scale_body import (
    PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/2025-10-01/resources/performance/review_questionnaire_by_strategies/update_default_rating_scale",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PerformanceReviewQuestionnairesByStrategy | None:
    if response.status_code == 200:
        response_200 = PerformanceReviewQuestionnairesByStrategy.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PerformanceReviewQuestionnairesByStrategy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody
    | Unset = UNSET,
) -> Response[PerformanceReviewQuestionnairesByStrategy]:
    """Update default rating scales a Review questionnaire by strategy

     Update the scoring range used in rating questions for all reviewer strategies.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatin
            gScaleBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewQuestionnairesByStrategy]
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
    body: PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody
    | Unset = UNSET,
) -> PerformanceReviewQuestionnairesByStrategy | None:
    """Update default rating scales a Review questionnaire by strategy

     Update the scoring range used in rating questions for all reviewer strategies.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatin
            gScaleBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewQuestionnairesByStrategy
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody
    | Unset = UNSET,
) -> Response[PerformanceReviewQuestionnairesByStrategy]:
    """Update default rating scales a Review questionnaire by strategy

     Update the scoring range used in rating questions for all reviewer strategies.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatin
            gScaleBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PerformanceReviewQuestionnairesByStrategy]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody
    | Unset = UNSET,
) -> PerformanceReviewQuestionnairesByStrategy | None:
    """Update default rating scales a Review questionnaire by strategy

     Update the scoring range used in rating questions for all reviewer strategies.

    Args:
        body (PostApi20251001ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatin
            gScaleBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PerformanceReviewQuestionnairesByStrategy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
