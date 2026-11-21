from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection_deleted import ConnectionDeleted
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    provider: str,
    *,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["account"] = account

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/connections/{provider}".format(
            provider=quote(str(provider), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConnectionDeleted | Error | None:
    if response.status_code == 200:
        response_200 = ConnectionDeleted.from_dict(response.json())

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
) -> Response[ConnectionDeleted | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectionDeleted | Error]:
    """Disconnect an account from the brand

     Removes the connection from THIS brand only. It never revokes Hermoso’s access at the platform, so
    the same account keeps working on any other brand it is connected to; the account holder removes
    that access in the platform’s own settings. Pass `account` to remove one account from a channel that
    holds several. Posts already published are not affected.

    Args:
        provider (str):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionDeleted | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        account=account,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: str,
    *,
    client: AuthenticatedClient,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectionDeleted | Error | None:
    """Disconnect an account from the brand

     Removes the connection from THIS brand only. It never revokes Hermoso’s access at the platform, so
    the same account keeps working on any other brand it is connected to; the account holder removes
    that access in the platform’s own settings. Pass `account` to remove one account from a channel that
    holds several. Posts already published are not affected.

    Args:
        provider (str):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionDeleted | Error
    """

    return sync_detailed(
        provider=provider,
        client=client,
        account=account,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConnectionDeleted | Error]:
    """Disconnect an account from the brand

     Removes the connection from THIS brand only. It never revokes Hermoso’s access at the platform, so
    the same account keeps working on any other brand it is connected to; the account holder removes
    that access in the platform’s own settings. Pass `account` to remove one account from a channel that
    holds several. Posts already published are not affected.

    Args:
        provider (str):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionDeleted | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        account=account,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient,
    account: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConnectionDeleted | Error | None:
    """Disconnect an account from the brand

     Removes the connection from THIS brand only. It never revokes Hermoso’s access at the platform, so
    the same account keeps working on any other brand it is connected to; the account holder removes
    that access in the platform’s own settings. Pass `account` to remove one account from a channel that
    holds several. Posts already published are not affected.

    Args:
        provider (str):
        account (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionDeleted | Error
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            account=account,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
