from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.follower_history import FollowerHistory
from ...types import Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["granularity"] = granularity

    params["channel"] = channel

    params["account"] = account

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/follower-history",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | FollowerHistory | None:
    if response.status_code == 200:
        response_200 = FollowerHistory.from_dict(response.json())

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
) -> Response[Error | FollowerHistory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | FollowerHistory]:
    """Follower history

     Follower count over time for every connected account (read once a day): one point per day, week or
    month with the change since the period before, up to a year (a longer range is cut and `warning`
    says so). A day whose read failed is a gap with its reason in `gaps`, never a 0. YouTube keeps its
    counts without a change (its API policy forbids derived numbers).

    Args:
        from_ (str | Unset):
        to (str | Unset):
        granularity (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FollowerHistory]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        granularity=granularity,
        channel=channel,
        account=account,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | FollowerHistory | None:
    """Follower history

     Follower count over time for every connected account (read once a day): one point per day, week or
    month with the change since the period before, up to a year (a longer range is cut and `warning`
    says so). A day whose read failed is a gap with its reason in `gaps`, never a 0. YouTube keeps its
    counts without a change (its API policy forbids derived numbers).

    Args:
        from_ (str | Unset):
        to (str | Unset):
        granularity (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FollowerHistory
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        granularity=granularity,
        channel=channel,
        account=account,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | FollowerHistory]:
    """Follower history

     Follower count over time for every connected account (read once a day): one point per day, week or
    month with the change since the period before, up to a year (a longer range is cut and `warning`
    says so). A day whose read failed is a gap with its reason in `gaps`, never a 0. YouTube keeps its
    counts without a change (its API policy forbids derived numbers).

    Args:
        from_ (str | Unset):
        to (str | Unset):
        granularity (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FollowerHistory]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        granularity=granularity,
        channel=channel,
        account=account,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    granularity: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | FollowerHistory | None:
    """Follower history

     Follower count over time for every connected account (read once a day): one point per day, week or
    month with the change since the period before, up to a year (a longer range is cut and `warning`
    says so). A day whose read failed is a gap with its reason in `gaps`, never a 0. YouTube keeps its
    counts without a change (its API policy forbids derived numbers).

    Args:
        from_ (str | Unset):
        to (str | Unset):
        granularity (str | Unset):
        channel (str | Unset):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FollowerHistory
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            granularity=granularity,
            channel=channel,
            account=account,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
