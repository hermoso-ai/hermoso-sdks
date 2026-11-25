from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.user_removal import UserRemoval
from ...types import Unset


def _get_kwargs(
    email: str,
    *,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/users/{email}".format(
            email=quote(str(email), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | UserRemoval | None:
    if response.status_code == 200:
        response_200 = UserRemoval.from_dict(response.json())

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
) -> Response[Error | UserRemoval]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | UserRemoval]:
    """Remove a person from this profile

     Their access ends at once, and every connection they made on this profile is disconnected with them;
    posts queued through their accounts will not go out (`connections_disconnected`,
    `scheduled_posts_not_going_out`). Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UserRemoval]
    """

    kwargs = _get_kwargs(
        email=email,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | UserRemoval | None:
    """Remove a person from this profile

     Their access ends at once, and every connection they made on this profile is disconnected with them;
    posts queued through their accounts will not go out (`connections_disconnected`,
    `scheduled_posts_not_going_out`). Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UserRemoval
    """

    return sync_detailed(
        email=email,
        client=client,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | UserRemoval]:
    """Remove a person from this profile

     Their access ends at once, and every connection they made on this profile is disconnected with them;
    posts queued through their accounts will not go out (`connections_disconnected`,
    `scheduled_posts_not_going_out`). Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UserRemoval]
    """

    kwargs = _get_kwargs(
        email=email,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | UserRemoval | None:
    """Remove a person from this profile

     Their access ends at once, and every connection they made on this profile is disconnected with them;
    posts queued through their accounts will not go out (`connections_disconnected`,
    `scheduled_posts_not_going_out`). Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UserRemoval
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
