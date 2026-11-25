from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_link import ConnectLink
from ...models.connect_link_create import ConnectLinkCreate
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    body: ConnectLinkCreate,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect-links",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConnectLink | Error | None:
    if response.status_code == 200:
        response_200 = ConnectLink.from_dict(response.json())

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
) -> Response[ConnectLink | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConnectLinkCreate,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectLink | Error]:
    """Create a connect link for your customer

     A short-lived hosted link that lets someone with NO Hermoso login connect their own account
    (Facebook and Instagram, Instagram, TikTok, YouTube, LinkedIn, X, Pinterest, Threads, Google
    Business Profile and the ad platforms) to the brand named by `X-Hermoso-User`. Hand `url` to your
    customer. They see a short page from Hermoso, accept Hermoso’s Terms and Privacy Policy, sign in on
    the platform’s own consent screen, and land on your `redirect_url` with `connect_status` (success |
    cancelled | error), `provider`, `brand`, `link_id`, `account`, `error_code` and your `state` added
    to its query string (a same-named parameter of yours is overwritten).

    THE PLATFORM’S CONSENT SCREEN SHOWS HERMOSO’S NAME, because the connection is made with Hermoso’s
    app on that platform, unless you saved your own app for it (manage_oauth_apps): then it shows yours.
    WHITE LABEL: the page your customer sees carries your saved welcome screen (name, logo, colours;
    connect_welcome_screen) when it is on by default or `welcome` is true, and the link opens on your
    own connect domain once one is active (manage_connect_domains). `external_id` maps your own customer
    id to this brand, found again with manage_external_ids.

    A link connects ONE provider to ONE brand. It can be retried after a cancel until it expires, and is
    spent once an account connects. Know when it connects from the `account.connected` webhook event
    (connect a webhook on the brand and include the `connections` group) or by polling GET /v1/connect-
    links/{id}. Facebook and LinkedIn then need the Pages chosen: call list_connector_accounts and
    set_connector_accounts through /v1/tools (the link’s creator owns that choice). Accounts that
    connect with a pasted key (Bluesky, Telegram) are connected with POST /v1/tools/connect_connector
    instead.

    Args:
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ConnectLinkCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectLink | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ConnectLinkCreate,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectLink | Error | None:
    """Create a connect link for your customer

     A short-lived hosted link that lets someone with NO Hermoso login connect their own account
    (Facebook and Instagram, Instagram, TikTok, YouTube, LinkedIn, X, Pinterest, Threads, Google
    Business Profile and the ad platforms) to the brand named by `X-Hermoso-User`. Hand `url` to your
    customer. They see a short page from Hermoso, accept Hermoso’s Terms and Privacy Policy, sign in on
    the platform’s own consent screen, and land on your `redirect_url` with `connect_status` (success |
    cancelled | error), `provider`, `brand`, `link_id`, `account`, `error_code` and your `state` added
    to its query string (a same-named parameter of yours is overwritten).

    THE PLATFORM’S CONSENT SCREEN SHOWS HERMOSO’S NAME, because the connection is made with Hermoso’s
    app on that platform, unless you saved your own app for it (manage_oauth_apps): then it shows yours.
    WHITE LABEL: the page your customer sees carries your saved welcome screen (name, logo, colours;
    connect_welcome_screen) when it is on by default or `welcome` is true, and the link opens on your
    own connect domain once one is active (manage_connect_domains). `external_id` maps your own customer
    id to this brand, found again with manage_external_ids.

    A link connects ONE provider to ONE brand. It can be retried after a cancel until it expires, and is
    spent once an account connects. Know when it connects from the `account.connected` webhook event
    (connect a webhook on the brand and include the `connections` group) or by polling GET /v1/connect-
    links/{id}. Facebook and LinkedIn then need the Pages chosen: call list_connector_accounts and
    set_connector_accounts through /v1/tools (the link’s creator owns that choice). Accounts that
    connect with a pasted key (Bluesky, Telegram) are connected with POST /v1/tools/connect_connector
    instead.

    Args:
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ConnectLinkCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectLink | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConnectLinkCreate,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectLink | Error]:
    """Create a connect link for your customer

     A short-lived hosted link that lets someone with NO Hermoso login connect their own account
    (Facebook and Instagram, Instagram, TikTok, YouTube, LinkedIn, X, Pinterest, Threads, Google
    Business Profile and the ad platforms) to the brand named by `X-Hermoso-User`. Hand `url` to your
    customer. They see a short page from Hermoso, accept Hermoso’s Terms and Privacy Policy, sign in on
    the platform’s own consent screen, and land on your `redirect_url` with `connect_status` (success |
    cancelled | error), `provider`, `brand`, `link_id`, `account`, `error_code` and your `state` added
    to its query string (a same-named parameter of yours is overwritten).

    THE PLATFORM’S CONSENT SCREEN SHOWS HERMOSO’S NAME, because the connection is made with Hermoso’s
    app on that platform, unless you saved your own app for it (manage_oauth_apps): then it shows yours.
    WHITE LABEL: the page your customer sees carries your saved welcome screen (name, logo, colours;
    connect_welcome_screen) when it is on by default or `welcome` is true, and the link opens on your
    own connect domain once one is active (manage_connect_domains). `external_id` maps your own customer
    id to this brand, found again with manage_external_ids.

    A link connects ONE provider to ONE brand. It can be retried after a cancel until it expires, and is
    spent once an account connects. Know when it connects from the `account.connected` webhook event
    (connect a webhook on the brand and include the `connections` group) or by polling GET /v1/connect-
    links/{id}. Facebook and LinkedIn then need the Pages chosen: call list_connector_accounts and
    set_connector_accounts through /v1/tools (the link’s creator owns that choice). Accounts that
    connect with a pasted key (Bluesky, Telegram) are connected with POST /v1/tools/connect_connector
    instead.

    Args:
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ConnectLinkCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectLink | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConnectLinkCreate,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectLink | Error | None:
    """Create a connect link for your customer

     A short-lived hosted link that lets someone with NO Hermoso login connect their own account
    (Facebook and Instagram, Instagram, TikTok, YouTube, LinkedIn, X, Pinterest, Threads, Google
    Business Profile and the ad platforms) to the brand named by `X-Hermoso-User`. Hand `url` to your
    customer. They see a short page from Hermoso, accept Hermoso’s Terms and Privacy Policy, sign in on
    the platform’s own consent screen, and land on your `redirect_url` with `connect_status` (success |
    cancelled | error), `provider`, `brand`, `link_id`, `account`, `error_code` and your `state` added
    to its query string (a same-named parameter of yours is overwritten).

    THE PLATFORM’S CONSENT SCREEN SHOWS HERMOSO’S NAME, because the connection is made with Hermoso’s
    app on that platform, unless you saved your own app for it (manage_oauth_apps): then it shows yours.
    WHITE LABEL: the page your customer sees carries your saved welcome screen (name, logo, colours;
    connect_welcome_screen) when it is on by default or `welcome` is true, and the link opens on your
    own connect domain once one is active (manage_connect_domains). `external_id` maps your own customer
    id to this brand, found again with manage_external_ids.

    A link connects ONE provider to ONE brand. It can be retried after a cancel until it expires, and is
    spent once an account connects. Know when it connects from the `account.connected` webhook event
    (connect a webhook on the brand and include the `connections` group) or by polling GET /v1/connect-
    links/{id}. Facebook and LinkedIn then need the Pages chosen: call list_connector_accounts and
    set_connector_accounts through /v1/tools (the link’s creator owns that choice). Accounts that
    connect with a pasted key (Bluesky, Telegram) are connected with POST /v1/tools/connect_connector
    instead.

    Args:
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ConnectLinkCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectLink | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
