from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.inbox_stats import InboxStats
from ...types import Unset


def _get_kwargs(
    *,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    include_x: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["days"] = days

    params["from"] = from_

    params["to"] = to

    params["channel"] = channel

    params["account"] = account

    params["include_x"] = include_x

    params["timezone"] = timezone

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/inbox",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | InboxStats | None:
    if response.status_code == 200:
        response_200 = InboxStats.from_dict(response.json())

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
) -> Response[Error | InboxStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    include_x: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | InboxStats]:
    """Inbox stats

     Across every connected messaging channel (WhatsApp, Messenger, Instagram, Telegram, SMS, LINE,
    Slack, Discord, email; X only with `include_x=true`, which X bills per message read): messages
    received and sent per day (`timeseries`) and per channel (`byPlatform`), a day × hour `heatmap` on
    `timezone` with the busiest hours (`dow` 1 = Monday), `responseTime` (median, p90, p99, mean,
    fastest, slowest and a histogram, measured from the other person's message to the brand's next reply
    in the same conversation), reply rate, the receiving accounts by load (`topAccounts`), per-
    conversation rows (`conversations`) and who is `waiting` now. Hermoso keeps each message's time and
    direction, never its text, from when the inbox was first read; `coverage` says since when and which
    channels could not be read.

    Args:
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        include_x (bool | Unset):
        timezone (str | Unset):
        limit (int | Unset):
        page (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InboxStats]
    """

    kwargs = _get_kwargs(
        days=days,
        from_=from_,
        to=to,
        channel=channel,
        account=account,
        include_x=include_x,
        timezone=timezone,
        limit=limit,
        page=page,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    include_x: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | InboxStats | None:
    """Inbox stats

     Across every connected messaging channel (WhatsApp, Messenger, Instagram, Telegram, SMS, LINE,
    Slack, Discord, email; X only with `include_x=true`, which X bills per message read): messages
    received and sent per day (`timeseries`) and per channel (`byPlatform`), a day × hour `heatmap` on
    `timezone` with the busiest hours (`dow` 1 = Monday), `responseTime` (median, p90, p99, mean,
    fastest, slowest and a histogram, measured from the other person's message to the brand's next reply
    in the same conversation), reply rate, the receiving accounts by load (`topAccounts`), per-
    conversation rows (`conversations`) and who is `waiting` now. Hermoso keeps each message's time and
    direction, never its text, from when the inbox was first read; `coverage` says since when and which
    channels could not be read.

    Args:
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        include_x (bool | Unset):
        timezone (str | Unset):
        limit (int | Unset):
        page (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InboxStats
    """

    return sync_detailed(
        client=client,
        days=days,
        from_=from_,
        to=to,
        channel=channel,
        account=account,
        include_x=include_x,
        timezone=timezone,
        limit=limit,
        page=page,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    include_x: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | InboxStats]:
    """Inbox stats

     Across every connected messaging channel (WhatsApp, Messenger, Instagram, Telegram, SMS, LINE,
    Slack, Discord, email; X only with `include_x=true`, which X bills per message read): messages
    received and sent per day (`timeseries`) and per channel (`byPlatform`), a day × hour `heatmap` on
    `timezone` with the busiest hours (`dow` 1 = Monday), `responseTime` (median, p90, p99, mean,
    fastest, slowest and a histogram, measured from the other person's message to the brand's next reply
    in the same conversation), reply rate, the receiving accounts by load (`topAccounts`), per-
    conversation rows (`conversations`) and who is `waiting` now. Hermoso keeps each message's time and
    direction, never its text, from when the inbox was first read; `coverage` says since when and which
    channels could not be read.

    Args:
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        include_x (bool | Unset):
        timezone (str | Unset):
        limit (int | Unset):
        page (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InboxStats]
    """

    kwargs = _get_kwargs(
        days=days,
        from_=from_,
        to=to,
        channel=channel,
        account=account,
        include_x=include_x,
        timezone=timezone,
        limit=limit,
        page=page,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    include_x: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | InboxStats | None:
    """Inbox stats

     Across every connected messaging channel (WhatsApp, Messenger, Instagram, Telegram, SMS, LINE,
    Slack, Discord, email; X only with `include_x=true`, which X bills per message read): messages
    received and sent per day (`timeseries`) and per channel (`byPlatform`), a day × hour `heatmap` on
    `timezone` with the busiest hours (`dow` 1 = Monday), `responseTime` (median, p90, p99, mean,
    fastest, slowest and a histogram, measured from the other person's message to the brand's next reply
    in the same conversation), reply rate, the receiving accounts by load (`topAccounts`), per-
    conversation rows (`conversations`) and who is `waiting` now. Hermoso keeps each message's time and
    direction, never its text, from when the inbox was first read; `coverage` says since when and which
    channels could not be read.

    Args:
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        include_x (bool | Unset):
        timezone (str | Unset):
        limit (int | Unset):
        page (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InboxStats
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            from_=from_,
            to=to,
            channel=channel,
            account=account,
            include_x=include_x,
            timezone=timezone,
            limit=limit,
            page=page,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
