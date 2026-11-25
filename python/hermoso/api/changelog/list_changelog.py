from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.changelog_page import ChangelogPage
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    impact: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type"] = type_

    params["impact"] = impact

    params["platform"] = platform

    params["before"] = before

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/changelog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ChangelogPage | Error | None:
    if response.status_code == 200:
        response_200 = ChangelogPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ChangelogPage | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    impact: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ChangelogPage | Error]:
    """List API changelog entries

     The API changelog, newest first. No key needed. Each entry carries `changes`, the deterministic diff
    of the public surface (the /v1 operations added, removed or changed, and the agent tools added or
    removed), and `impact` computed from it: `action_required` when something an integration may call is
    gone or moved, `additive` when only new things appeared. A deploy that changes the API adds an entry
    by itself. Page with `before` set to the previous page’s `next_cursor`.

    Args:
        type_ (str | Unset):
        impact (str | Unset):
        platform (str | Unset):
        before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangelogPage | Error]
    """

    kwargs = _get_kwargs(
        type_=type_,
        impact=impact,
        platform=platform,
        before=before,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    impact: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ChangelogPage | Error | None:
    """List API changelog entries

     The API changelog, newest first. No key needed. Each entry carries `changes`, the deterministic diff
    of the public surface (the /v1 operations added, removed or changed, and the agent tools added or
    removed), and `impact` computed from it: `action_required` when something an integration may call is
    gone or moved, `additive` when only new things appeared. A deploy that changes the API adds an entry
    by itself. Page with `before` set to the previous page’s `next_cursor`.

    Args:
        type_ (str | Unset):
        impact (str | Unset):
        platform (str | Unset):
        before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangelogPage | Error
    """

    return sync_detailed(
        client=client,
        type_=type_,
        impact=impact,
        platform=platform,
        before=before,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    impact: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ChangelogPage | Error]:
    """List API changelog entries

     The API changelog, newest first. No key needed. Each entry carries `changes`, the deterministic diff
    of the public surface (the /v1 operations added, removed or changed, and the agent tools added or
    removed), and `impact` computed from it: `action_required` when something an integration may call is
    gone or moved, `additive` when only new things appeared. A deploy that changes the API adds an entry
    by itself. Page with `before` set to the previous page’s `next_cursor`.

    Args:
        type_ (str | Unset):
        impact (str | Unset):
        platform (str | Unset):
        before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangelogPage | Error]
    """

    kwargs = _get_kwargs(
        type_=type_,
        impact=impact,
        platform=platform,
        before=before,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    impact: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ChangelogPage | Error | None:
    """List API changelog entries

     The API changelog, newest first. No key needed. Each entry carries `changes`, the deterministic diff
    of the public surface (the /v1 operations added, removed or changed, and the agent tools added or
    removed), and `impact` computed from it: `action_required` when something an integration may call is
    gone or moved, `additive` when only new things appeared. A deploy that changes the API adds an entry
    by itself. Page with `before` set to the previous page’s `next_cursor`.

    Args:
        type_ (str | Unset):
        impact (str | Unset):
        platform (str | Unset):
        before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangelogPage | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            impact=impact,
            platform=platform,
            before=before,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
