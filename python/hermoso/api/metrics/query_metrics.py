from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.metrics_result import MetricsResult
from ...types import Unset


def _get_kwargs(
    *,
    entity: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    group_by: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["entity"] = entity

    params["metrics"] = metrics

    params["group_by"] = group_by

    params["granularity"] = granularity

    params["days"] = days

    params["from_date"] = from_date

    params["to_date"] = to_date

    params["channel"] = channel

    params["account"] = account

    params["sort"] = sort

    params["limit"] = limit

    params["timezone"] = timezone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/metrics",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | MetricsResult | None:
    if response.status_code == 200:
        response_200 = MetricsResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Error | MetricsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    entity: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    group_by: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | MetricsResult]:
    """Query metrics

     `entity` posts (posts, measured, reach, engagement, engagement_rate of posts published in the
    window; `group_by` channel, account, media, hour, dayOfWeek, post), accounts (followers and follower
    change per account; `group_by` account, channel or none) or inbox (received, sent, response times;
    `group_by` none or channel), at `granularity` total, day, week or month. Reach and engagement are
    never added across platforms: a grouping that would pool them is split by channel and `notes` says
    so. Free.

    Args:
        entity (str | Unset):
        metrics (str | Unset):
        group_by (str | Unset):
        granularity (str | Unset):
        days (int | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MetricsResult]
    """

    kwargs = _get_kwargs(
        entity=entity,
        metrics=metrics,
        group_by=group_by,
        granularity=granularity,
        days=days,
        from_date=from_date,
        to_date=to_date,
        channel=channel,
        account=account,
        sort=sort,
        limit=limit,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    entity: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    group_by: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | MetricsResult | None:
    """Query metrics

     `entity` posts (posts, measured, reach, engagement, engagement_rate of posts published in the
    window; `group_by` channel, account, media, hour, dayOfWeek, post), accounts (followers and follower
    change per account; `group_by` account, channel or none) or inbox (received, sent, response times;
    `group_by` none or channel), at `granularity` total, day, week or month. Reach and engagement are
    never added across platforms: a grouping that would pool them is split by channel and `notes` says
    so. Free.

    Args:
        entity (str | Unset):
        metrics (str | Unset):
        group_by (str | Unset):
        granularity (str | Unset):
        days (int | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MetricsResult
    """

    return sync_detailed(
        client=client,
        entity=entity,
        metrics=metrics,
        group_by=group_by,
        granularity=granularity,
        days=days,
        from_date=from_date,
        to_date=to_date,
        channel=channel,
        account=account,
        sort=sort,
        limit=limit,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    entity: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    group_by: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | MetricsResult]:
    """Query metrics

     `entity` posts (posts, measured, reach, engagement, engagement_rate of posts published in the
    window; `group_by` channel, account, media, hour, dayOfWeek, post), accounts (followers and follower
    change per account; `group_by` account, channel or none) or inbox (received, sent, response times;
    `group_by` none or channel), at `granularity` total, day, week or month. Reach and engagement are
    never added across platforms: a grouping that would pool them is split by channel and `notes` says
    so. Free.

    Args:
        entity (str | Unset):
        metrics (str | Unset):
        group_by (str | Unset):
        granularity (str | Unset):
        days (int | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MetricsResult]
    """

    kwargs = _get_kwargs(
        entity=entity,
        metrics=metrics,
        group_by=group_by,
        granularity=granularity,
        days=days,
        from_date=from_date,
        to_date=to_date,
        channel=channel,
        account=account,
        sort=sort,
        limit=limit,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    entity: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    group_by: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | MetricsResult | None:
    """Query metrics

     `entity` posts (posts, measured, reach, engagement, engagement_rate of posts published in the
    window; `group_by` channel, account, media, hour, dayOfWeek, post), accounts (followers and follower
    change per account; `group_by` account, channel or none) or inbox (received, sent, response times;
    `group_by` none or channel), at `granularity` total, day, week or month. Reach and engagement are
    never added across platforms: a grouping that would pool them is split by channel and `notes` says
    so. Free.

    Args:
        entity (str | Unset):
        metrics (str | Unset):
        group_by (str | Unset):
        granularity (str | Unset):
        days (int | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MetricsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            entity=entity,
            metrics=metrics,
            group_by=group_by,
            granularity=granularity,
            days=days,
            from_date=from_date,
            to_date=to_date,
            channel=channel,
            account=account,
            sort=sort,
            limit=limit,
            timezone=timezone,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
