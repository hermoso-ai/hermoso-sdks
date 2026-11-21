from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.best_time import BestTime
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    days: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["channel"] = channel

    params["account"] = account

    params["source"] = source

    params["days"] = days

    params["timezone"] = timezone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/best-time",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> BestTime | Error | None:
    if response.status_code == 200:
        response_200 = BestTime.from_dict(response.json())

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
) -> Response[BestTime | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    days: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[BestTime | Error]:
    """Best time to post

     From this brand's own measured posts, per channel, on `timezone`: a day × hour grid (`slots`, one
    row per channel and slot with the post count, the average engagement and the lift against that
    channel's usual), the best weekday and 3-hour band where one beat the usual by 15% over at least 5
    posts, and Instagram's followers-online hours when Instagram is connected. Raw numbers are never
    pooled across channels; below 15 measured posts nothing is named and `why` says how many there are.
    `day_of_week` 0 = Monday.

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        days (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BestTime | Error]
    """

    kwargs = _get_kwargs(
        channel=channel,
        account=account,
        source=source,
        days=days,
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
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    days: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> BestTime | Error | None:
    """Best time to post

     From this brand's own measured posts, per channel, on `timezone`: a day × hour grid (`slots`, one
    row per channel and slot with the post count, the average engagement and the lift against that
    channel's usual), the best weekday and 3-hour band where one beat the usual by 15% over at least 5
    posts, and Instagram's followers-online hours when Instagram is connected. Raw numbers are never
    pooled across channels; below 15 measured posts nothing is named and `why` says how many there are.
    `day_of_week` 0 = Monday.

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        days (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BestTime | Error
    """

    return sync_detailed(
        client=client,
        channel=channel,
        account=account,
        source=source,
        days=days,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    days: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[BestTime | Error]:
    """Best time to post

     From this brand's own measured posts, per channel, on `timezone`: a day × hour grid (`slots`, one
    row per channel and slot with the post count, the average engagement and the lift against that
    channel's usual), the best weekday and 3-hour band where one beat the usual by 15% over at least 5
    posts, and Instagram's followers-online hours when Instagram is connected. Raw numbers are never
    pooled across channels; below 15 measured posts nothing is named and `why` says how many there are.
    `day_of_week` 0 = Monday.

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        days (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BestTime | Error]
    """

    kwargs = _get_kwargs(
        channel=channel,
        account=account,
        source=source,
        days=days,
        timezone=timezone,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    days: int | Unset = UNSET,
    timezone: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> BestTime | Error | None:
    """Best time to post

     From this brand's own measured posts, per channel, on `timezone`: a day × hour grid (`slots`, one
    row per channel and slot with the post count, the average engagement and the lift against that
    channel's usual), the best weekday and 3-hour band where one beat the usual by 15% over at least 5
    posts, and Instagram's followers-online hours when Instagram is connected. Raw numbers are never
    pooled across channels; below 15 measured posts nothing is named and `why` says how many there are.
    `day_of_week` 0 = Monday.

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        days (int | Unset):
        timezone (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BestTime | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            channel=channel,
            account=account,
            source=source,
            days=days,
            timezone=timezone,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
