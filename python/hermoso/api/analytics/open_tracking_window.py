from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tracking_window import TrackingWindow
from ...models.tracking_window_open import TrackingWindowOpen
from ...types import Unset


def _get_kwargs(
    *,
    body: TrackingWindowOpen,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/analytics/tracking",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | TrackingWindow | None:
    if response.status_code == 200:
        response_200 = TrackingWindow.from_dict(response.json())

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
) -> Response[Error | TrackingWindow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TrackingWindowOpen,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | TrackingWindow]:
    """Open a tracking window

     Watch a post once a day for `tracking_days` (1-90, default 30), then a final reading and the
    `post.tracking_completed` event. `post_id`: a post the brand published, read through its own
    connection, free. `url`: any public TikTok, Instagram, YouTube, Facebook, X or Threads post, one
    data lookup per reading: without `confirm: true` nothing is opened and the answer is the quote
    (`needs_confirm`). A post already tracked returns its open window (`existing: true`).

    Args:
        x_hermoso_user (str | Unset):
        body (TrackingWindowOpen):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TrackingWindow]
    """

    kwargs = _get_kwargs(
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TrackingWindowOpen,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | TrackingWindow | None:
    """Open a tracking window

     Watch a post once a day for `tracking_days` (1-90, default 30), then a final reading and the
    `post.tracking_completed` event. `post_id`: a post the brand published, read through its own
    connection, free. `url`: any public TikTok, Instagram, YouTube, Facebook, X or Threads post, one
    data lookup per reading: without `confirm: true` nothing is opened and the answer is the quote
    (`needs_confirm`). A post already tracked returns its open window (`existing: true`).

    Args:
        x_hermoso_user (str | Unset):
        body (TrackingWindowOpen):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TrackingWindow
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TrackingWindowOpen,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | TrackingWindow]:
    """Open a tracking window

     Watch a post once a day for `tracking_days` (1-90, default 30), then a final reading and the
    `post.tracking_completed` event. `post_id`: a post the brand published, read through its own
    connection, free. `url`: any public TikTok, Instagram, YouTube, Facebook, X or Threads post, one
    data lookup per reading: without `confirm: true` nothing is opened and the answer is the quote
    (`needs_confirm`). A post already tracked returns its open window (`existing: true`).

    Args:
        x_hermoso_user (str | Unset):
        body (TrackingWindowOpen):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TrackingWindow]
    """

    kwargs = _get_kwargs(
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TrackingWindowOpen,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | TrackingWindow | None:
    """Open a tracking window

     Watch a post once a day for `tracking_days` (1-90, default 30), then a final reading and the
    `post.tracking_completed` event. `post_id`: a post the brand published, read through its own
    connection, free. `url`: any public TikTok, Instagram, YouTube, Facebook, X or Threads post, one
    data lookup per reading: without `confirm: true` nothing is opened and the answer is the quote
    (`needs_confirm`). A post already tracked returns its open window (`existing: true`).

    Args:
        x_hermoso_user (str | Unset):
        body (TrackingWindowOpen):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TrackingWindow
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
