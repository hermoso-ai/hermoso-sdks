from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversion_insights import ConversionInsights
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/accuracy",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConversionInsights | Error | None:
    if response.status_code == 200:
        response_200 = ConversionInsights.from_dict(response.json())

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
) -> Response[ConversionInsights | Error]:
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
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConversionInsights | Error]:
    """Delivery accuracy per destination

     Per destination over the window: real sales, how many were sent, accepted, failed or never sent
    (with the reasons), and how many events carried an identifier the platform matches on.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversionInsights | Error]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
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
    x_hermoso_user: str | Unset = UNSET,
) -> ConversionInsights | Error | None:
    """Delivery accuracy per destination

     Per destination over the window: real sales, how many were sent, accepted, failed or never sent
    (with the reasons), and how many events carried an identifier the platform matches on.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversionInsights | Error
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConversionInsights | Error]:
    """Delivery accuracy per destination

     Per destination over the window: real sales, how many were sent, accepted, failed or never sent
    (with the reasons), and how many events carried an identifier the platform matches on.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversionInsights | Error]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConversionInsights | Error | None:
    """Delivery accuracy per destination

     Per destination over the window: real sales, how many were sent, accepted, failed or never sent
    (with the reasons), and how many events carried an identifier the platform matches on.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversionInsights | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
