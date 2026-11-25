from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connected_app_list import ConnectedAppList
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/me/connected-apps",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConnectedAppList | Error | None:
    if response.status_code == 200:
        response_200 = ConnectedAppList.from_dict(response.json())

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
) -> Response[ConnectedAppList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectedAppList | Error]:
    """List connected apps

     The AI assistants and MCP clients signed in to this account that still hold a live token: name, the
    host they connected from, when they were authorised and last used, and how many tokens they hold.
    Needs a whole-account admin key that is not itself one of these apps’ tokens (an app cannot list its
    siblings): anything else is refused 403.

    Args:
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppList | Error]
    """

    kwargs = _get_kwargs(
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectedAppList | Error | None:
    """List connected apps

     The AI assistants and MCP clients signed in to this account that still hold a live token: name, the
    host they connected from, when they were authorised and last used, and how many tokens they hold.
    Needs a whole-account admin key that is not itself one of these apps’ tokens (an app cannot list its
    siblings): anything else is refused 403.

    Args:
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppList | Error
    """

    return sync_detailed(
        client=client,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectedAppList | Error]:
    """List connected apps

     The AI assistants and MCP clients signed in to this account that still hold a live token: name, the
    host they connected from, when they were authorised and last used, and how many tokens they hold.
    Needs a whole-account admin key that is not itself one of these apps’ tokens (an app cannot list its
    siblings): anything else is refused 403.

    Args:
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppList | Error]
    """

    kwargs = _get_kwargs(
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectedAppList | Error | None:
    """List connected apps

     The AI assistants and MCP clients signed in to this account that still hold a live token: name, the
    host they connected from, when they were authorised and last used, and how many tokens they hold.
    Needs a whole-account admin key that is not itself one of these apps’ tokens (an app cannot list its
    siblings): anything else is refused 403.

    Args:
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppList | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
