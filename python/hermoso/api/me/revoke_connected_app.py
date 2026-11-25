from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connected_app_revocation import ConnectedAppRevocation
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    app_id: str,
    *,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/me/connected-apps/{app_id}".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConnectedAppRevocation | Error | None:
    if response.status_code == 200:
        response_200 = ConnectedAppRevocation.from_dict(response.json())

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
) -> Response[ConnectedAppRevocation | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectedAppRevocation | Error]:
    """Revoke a connected app

     Ends every token the app holds, so it stops working at once and has to be authorised again. Read
    back from the key store. Same credential rule as the list.

    Args:
        app_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppRevocation | Error]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectedAppRevocation | Error | None:
    """Revoke a connected app

     Ends every token the app holds, so it stops working at once and has to be authorised again. Read
    back from the key store. Same credential rule as the list.

    Args:
        app_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppRevocation | Error
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectedAppRevocation | Error]:
    """Revoke a connected app

     Ends every token the app holds, so it stops working at once and has to be authorised again. Read
    back from the key store. Same credential rule as the list.

    Args:
        app_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppRevocation | Error]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectedAppRevocation | Error | None:
    """Revoke a connected app

     Ends every token the app holds, so it stops working at once and has to be authorised again. Read
    back from the key store. Same credential rule as the list.

    Args:
        app_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppRevocation | Error
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
