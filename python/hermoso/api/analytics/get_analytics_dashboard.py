from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analytics_dashboard import AnalyticsDashboard
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    period: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    top_posts: int | Unset = UNSET,
    recent_posts: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["period"] = period

    params["days"] = days

    params["from"] = from_

    params["to"] = to

    params["channel"] = channel

    params["account"] = account

    params["top_posts"] = top_posts

    params["recent_posts"] = recent_posts

    params["timezone"] = timezone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/dashboard",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AnalyticsDashboard | Error | None:
    if response.status_code == 200:
        response_200 = AnalyticsDashboard.from_dict(response.json())

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
) -> Response[AnalyticsDashboard | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    period: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    top_posts: int | Unset = UNSET,
    recent_posts: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AnalyticsDashboard | Error]:
    """Analytics dashboard with the previous period

     One read across the brand’s connected channels: per channel, posts, reach (each platform’s own
    unit), engagement, engagement rate and follower change, each as `current`, `previous`, `change` and
    `pct`, plus a day-by-day series, top posts and recent posts. The previous window is the same number
    of days immediately before (`this_week` compares week to date with last week to the same weekday).
    Reach is never added across platforms, a missing number is null with `why`, and YouTube carries no
    totals or changes (its API policy). Numbers belong to the day a post was published. Free.

    Args:
        period (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        top_posts (int | Unset):
        recent_posts (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsDashboard | Error]
    """

    kwargs = _get_kwargs(
        period=period,
        days=days,
        from_=from_,
        to=to,
        channel=channel,
        account=account,
        top_posts=top_posts,
        recent_posts=recent_posts,
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
    period: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    top_posts: int | Unset = UNSET,
    recent_posts: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> AnalyticsDashboard | Error | None:
    """Analytics dashboard with the previous period

     One read across the brand’s connected channels: per channel, posts, reach (each platform’s own
    unit), engagement, engagement rate and follower change, each as `current`, `previous`, `change` and
    `pct`, plus a day-by-day series, top posts and recent posts. The previous window is the same number
    of days immediately before (`this_week` compares week to date with last week to the same weekday).
    Reach is never added across platforms, a missing number is null with `why`, and YouTube carries no
    totals or changes (its API policy). Numbers belong to the day a post was published. Free.

    Args:
        period (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        top_posts (int | Unset):
        recent_posts (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsDashboard | Error
    """

    return sync_detailed(
        client=client,
        period=period,
        days=days,
        from_=from_,
        to=to,
        channel=channel,
        account=account,
        top_posts=top_posts,
        recent_posts=recent_posts,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    period: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    top_posts: int | Unset = UNSET,
    recent_posts: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AnalyticsDashboard | Error]:
    """Analytics dashboard with the previous period

     One read across the brand’s connected channels: per channel, posts, reach (each platform’s own
    unit), engagement, engagement rate and follower change, each as `current`, `previous`, `change` and
    `pct`, plus a day-by-day series, top posts and recent posts. The previous window is the same number
    of days immediately before (`this_week` compares week to date with last week to the same weekday).
    Reach is never added across platforms, a missing number is null with `why`, and YouTube carries no
    totals or changes (its API policy). Numbers belong to the day a post was published. Free.

    Args:
        period (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        top_posts (int | Unset):
        recent_posts (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsDashboard | Error]
    """

    kwargs = _get_kwargs(
        period=period,
        days=days,
        from_=from_,
        to=to,
        channel=channel,
        account=account,
        top_posts=top_posts,
        recent_posts=recent_posts,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    period: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    top_posts: int | Unset = UNSET,
    recent_posts: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> AnalyticsDashboard | Error | None:
    """Analytics dashboard with the previous period

     One read across the brand’s connected channels: per channel, posts, reach (each platform’s own
    unit), engagement, engagement rate and follower change, each as `current`, `previous`, `change` and
    `pct`, plus a day-by-day series, top posts and recent posts. The previous window is the same number
    of days immediately before (`this_week` compares week to date with last week to the same weekday).
    Reach is never added across platforms, a missing number is null with `why`, and YouTube carries no
    totals or changes (its API policy). Numbers belong to the day a post was published. Free.

    Args:
        period (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        top_posts (int | Unset):
        recent_posts (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsDashboard | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
            days=days,
            from_=from_,
            to=to,
            channel=channel,
            account=account,
            top_posts=top_posts,
            recent_posts=recent_posts,
            timezone=timezone,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
