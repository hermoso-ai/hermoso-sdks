from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_redirects import ConnectRedirects
from ...models.connect_redirects_set import ConnectRedirectsSet
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    body: ConnectRedirectsSet,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/connect-redirects",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConnectRedirects | Error | None:
    if response.status_code == 200:
        response_200 = ConnectRedirects.from_dict(response.json())

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
) -> Response[ConnectRedirects | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConnectRedirectsSet,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectRedirects | Error]:
    """Replace the registered redirect addresses

     Replaces the whole list (an empty list removes them all). https only; `http://localhost` is accepted
    for local testing. No query string, fragment, credentials or wildcard — register an exact origin,
    optionally with a path prefix. Up to 20.

    Args:
        x_hermoso_user (str | Unset):
        body (ConnectRedirectsSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectRedirects | Error]
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
    body: ConnectRedirectsSet,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectRedirects | Error | None:
    """Replace the registered redirect addresses

     Replaces the whole list (an empty list removes them all). https only; `http://localhost` is accepted
    for local testing. No query string, fragment, credentials or wildcard — register an exact origin,
    optionally with a path prefix. Up to 20.

    Args:
        x_hermoso_user (str | Unset):
        body (ConnectRedirectsSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectRedirects | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConnectRedirectsSet,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectRedirects | Error]:
    """Replace the registered redirect addresses

     Replaces the whole list (an empty list removes them all). https only; `http://localhost` is accepted
    for local testing. No query string, fragment, credentials or wildcard — register an exact origin,
    optionally with a path prefix. Up to 20.

    Args:
        x_hermoso_user (str | Unset):
        body (ConnectRedirectsSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectRedirects | Error]
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
    body: ConnectRedirectsSet,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectRedirects | Error | None:
    """Replace the registered redirect addresses

     Replaces the whole list (an empty list removes them all). https only; `http://localhost` is accepted
    for local testing. No query string, fragment, credentials or wildcard — register an exact origin,
    optionally with a path prefix. Up to 20.

    Args:
        x_hermoso_user (str | Unset):
        body (ConnectRedirectsSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectRedirects | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
