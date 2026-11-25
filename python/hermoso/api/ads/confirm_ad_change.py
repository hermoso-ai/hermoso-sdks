from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ad_change import AdChange
from ...models.ad_change_confirm import AdChangeConfirm
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    change_id: str,
    *,
    body: AdChangeConfirm,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/ads/changes/{change_id}/confirm".format(
            change_id=quote(str(change_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AdChange | Error | None:
    if response.status_code == 200:
        response_200 = AdChange.from_dict(response.json())

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
) -> Response[AdChange | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    change_id: str,
    *,
    client: AuthenticatedClient,
    body: AdChangeConfirm,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AdChange | Error]:
    """Confirm a staged ad change

     Runs the staged call through the same checks a direct call makes. It can start or raise ad spend, so
    `confirm: true` is required; without it the change is described and nothing runs. A change runs at
    most once; one the platform refuses is marked `failed` with the platform’s words.

    Args:
        change_id (str):
        x_hermoso_user (str | Unset):
        body (AdChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdChange | Error]
    """

    kwargs = _get_kwargs(
        change_id=change_id,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    change_id: str,
    *,
    client: AuthenticatedClient,
    body: AdChangeConfirm,
    x_hermoso_user: str | Unset = UNSET,
) -> AdChange | Error | None:
    """Confirm a staged ad change

     Runs the staged call through the same checks a direct call makes. It can start or raise ad spend, so
    `confirm: true` is required; without it the change is described and nothing runs. A change runs at
    most once; one the platform refuses is marked `failed` with the platform’s words.

    Args:
        change_id (str):
        x_hermoso_user (str | Unset):
        body (AdChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdChange | Error
    """

    return sync_detailed(
        change_id=change_id,
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    change_id: str,
    *,
    client: AuthenticatedClient,
    body: AdChangeConfirm,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AdChange | Error]:
    """Confirm a staged ad change

     Runs the staged call through the same checks a direct call makes. It can start or raise ad spend, so
    `confirm: true` is required; without it the change is described and nothing runs. A change runs at
    most once; one the platform refuses is marked `failed` with the platform’s words.

    Args:
        change_id (str):
        x_hermoso_user (str | Unset):
        body (AdChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdChange | Error]
    """

    kwargs = _get_kwargs(
        change_id=change_id,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    change_id: str,
    *,
    client: AuthenticatedClient,
    body: AdChangeConfirm,
    x_hermoso_user: str | Unset = UNSET,
) -> AdChange | Error | None:
    """Confirm a staged ad change

     Runs the staged call through the same checks a direct call makes. It can start or raise ad spend, so
    `confirm: true` is required; without it the change is described and nothing runs. A change runs at
    most once; one the platform refuses is marked `failed` with the platform’s words.

    Args:
        change_id (str):
        x_hermoso_user (str | Unset):
        body (AdChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdChange | Error
    """

    return (
        await asyncio_detailed(
            change_id=change_id,
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
