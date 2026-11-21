from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.content_decay import ContentDecay
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["channel"] = channel

    params["account"] = account

    params["source"] = source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/content-decay",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ContentDecay | Error | None:
    if response.status_code == 200:
        response_200 = ContentDecay.from_dict(response.json())

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
) -> Response[ContentDecay | Error]:
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
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ContentDecay | Error]:
    """Content decay

     How fast posts stop earning: for each age bucket (0-6h … 30d+), the average share of a post's final
    engagement (and, separately, of its final reach) reached by then, from posts with two or more
    readings and a settled reading 6+ days after posting. Per channel, plus `buckets` pooled across
    channels (a share is unitless, so pooling it is legitimate where pooling raw numbers is not).

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentDecay | Error]
    """

    kwargs = _get_kwargs(
        channel=channel,
        account=account,
        source=source,
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
    x_hermoso_user: str | Unset = UNSET,
) -> ContentDecay | Error | None:
    """Content decay

     How fast posts stop earning: for each age bucket (0-6h … 30d+), the average share of a post's final
    engagement (and, separately, of its final reach) reached by then, from posts with two or more
    readings and a settled reading 6+ days after posting. Per channel, plus `buckets` pooled across
    channels (a share is unitless, so pooling it is legitimate where pooling raw numbers is not).

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentDecay | Error
    """

    return sync_detailed(
        client=client,
        channel=channel,
        account=account,
        source=source,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    account: str | Unset = UNSET,
    source: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ContentDecay | Error]:
    """Content decay

     How fast posts stop earning: for each age bucket (0-6h … 30d+), the average share of a post's final
    engagement (and, separately, of its final reach) reached by then, from posts with two or more
    readings and a settled reading 6+ days after posting. Per channel, plus `buckets` pooled across
    channels (a share is unitless, so pooling it is legitimate where pooling raw numbers is not).

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentDecay | Error]
    """

    kwargs = _get_kwargs(
        channel=channel,
        account=account,
        source=source,
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
    x_hermoso_user: str | Unset = UNSET,
) -> ContentDecay | Error | None:
    """Content decay

     How fast posts stop earning: for each age bucket (0-6h … 30d+), the average share of a post's final
    engagement (and, separately, of its final reach) reached by then, from posts with two or more
    readings and a settled reading 6+ days after posting. Per channel, plus `buckets` pooled across
    channels (a share is unitless, so pooling it is legitimate where pooling raw numbers is not).

    Args:
        channel (str | Unset):
        account (str | Unset):
        source (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentDecay | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            channel=channel,
            account=account,
            source=source,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
