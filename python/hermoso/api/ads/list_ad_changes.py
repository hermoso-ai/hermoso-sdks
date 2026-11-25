from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ad_change_list import AdChangeList
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["status"] = status

    params["platform"] = platform

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ads/changes",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AdChangeList | Error | None:
    if response.status_code == 200:
        response_200 = AdChangeList.from_dict(response.json())

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
) -> Response[AdChangeList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AdChangeList | Error]:
    """List staged ad changes

     The ad changes waiting for confirmation (status `staged`, the default), or confirmed / failed /
    discarded / all, newest first, without their arguments. A confirmed or failed change stays listed
    for 7 days.

    Args:
        status (str | Unset):
        platform (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdChangeList | Error]
    """

    kwargs = _get_kwargs(
        status=status,
        platform=platform,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> AdChangeList | Error | None:
    """List staged ad changes

     The ad changes waiting for confirmation (status `staged`, the default), or confirmed / failed /
    discarded / all, newest first, without their arguments. A confirmed or failed change stays listed
    for 7 days.

    Args:
        status (str | Unset):
        platform (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdChangeList | Error
    """

    return sync_detailed(
        client=client,
        status=status,
        platform=platform,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AdChangeList | Error]:
    """List staged ad changes

     The ad changes waiting for confirmation (status `staged`, the default), or confirmed / failed /
    discarded / all, newest first, without their arguments. A confirmed or failed change stays listed
    for 7 days.

    Args:
        status (str | Unset):
        platform (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdChangeList | Error]
    """

    kwargs = _get_kwargs(
        status=status,
        platform=platform,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> AdChangeList | Error | None:
    """List staged ad changes

     The ad changes waiting for confirmation (status `staged`, the default), or confirmed / failed /
    discarded / all, newest first, without their arguments. A confirmed or failed change stays listed
    for 7 days.

    Args:
        status (str | Unset):
        platform (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdChangeList | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            platform=platform,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
