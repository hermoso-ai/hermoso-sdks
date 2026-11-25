from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.activity_log_page import ActivityLogPage
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    status_code: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    api_key_id: str | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["type"] = type_

    params["status"] = status

    params["status_code"] = status_code

    params["request_id"] = request_id

    params["api_key_id"] = api_key_id

    params["profile_id"] = profile_id

    params["search"] = search

    params["days"] = days

    params["from"] = from_

    params["to"] = to

    params["limit"] = limit

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/logs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActivityLogPage | Error | None:
    if response.status_code == 200:
        response_200 = ActivityLogPage.from_dict(response.json())

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
) -> Response[ActivityLogPage | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    status_code: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    api_key_id: str | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ActivityLogPage | Error]:
    """List activity logs

     One 90-day log: `api_request` (every request this account’s keys made: method, path, status,
    latency, key, profile, request id; never a body or a query string), `publishing` (posts published,
    failed, scheduled, cancelled), `webhooks` (alert deliveries) and `connections` (connected accounts
    and the ones that need reconnecting). `all` merges them, newest first. A source that could not be
    read is named in `unreadable`, never returned as empty.

    Args:
        type_ (str | Unset):
        status (str | Unset):
        status_code (int | Unset):
        request_id (str | Unset):
        api_key_id (str | Unset):
        profile_id (str | Unset):
        search (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        skip (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityLogPage | Error]
    """

    kwargs = _get_kwargs(
        type_=type_,
        status=status,
        status_code=status_code,
        request_id=request_id,
        api_key_id=api_key_id,
        profile_id=profile_id,
        search=search,
        days=days,
        from_=from_,
        to=to,
        limit=limit,
        skip=skip,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    status_code: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    api_key_id: str | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ActivityLogPage | Error | None:
    """List activity logs

     One 90-day log: `api_request` (every request this account’s keys made: method, path, status,
    latency, key, profile, request id; never a body or a query string), `publishing` (posts published,
    failed, scheduled, cancelled), `webhooks` (alert deliveries) and `connections` (connected accounts
    and the ones that need reconnecting). `all` merges them, newest first. A source that could not be
    read is named in `unreadable`, never returned as empty.

    Args:
        type_ (str | Unset):
        status (str | Unset):
        status_code (int | Unset):
        request_id (str | Unset):
        api_key_id (str | Unset):
        profile_id (str | Unset):
        search (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        skip (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityLogPage | Error
    """

    return sync_detailed(
        client=client,
        type_=type_,
        status=status,
        status_code=status_code,
        request_id=request_id,
        api_key_id=api_key_id,
        profile_id=profile_id,
        search=search,
        days=days,
        from_=from_,
        to=to,
        limit=limit,
        skip=skip,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    status_code: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    api_key_id: str | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ActivityLogPage | Error]:
    """List activity logs

     One 90-day log: `api_request` (every request this account’s keys made: method, path, status,
    latency, key, profile, request id; never a body or a query string), `publishing` (posts published,
    failed, scheduled, cancelled), `webhooks` (alert deliveries) and `connections` (connected accounts
    and the ones that need reconnecting). `all` merges them, newest first. A source that could not be
    read is named in `unreadable`, never returned as empty.

    Args:
        type_ (str | Unset):
        status (str | Unset):
        status_code (int | Unset):
        request_id (str | Unset):
        api_key_id (str | Unset):
        profile_id (str | Unset):
        search (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        skip (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityLogPage | Error]
    """

    kwargs = _get_kwargs(
        type_=type_,
        status=status,
        status_code=status_code,
        request_id=request_id,
        api_key_id=api_key_id,
        profile_id=profile_id,
        search=search,
        days=days,
        from_=from_,
        to=to,
        limit=limit,
        skip=skip,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    status_code: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    api_key_id: str | Unset = UNSET,
    profile_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    skip: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ActivityLogPage | Error | None:
    """List activity logs

     One 90-day log: `api_request` (every request this account’s keys made: method, path, status,
    latency, key, profile, request id; never a body or a query string), `publishing` (posts published,
    failed, scheduled, cancelled), `webhooks` (alert deliveries) and `connections` (connected accounts
    and the ones that need reconnecting). `all` merges them, newest first. A source that could not be
    read is named in `unreadable`, never returned as empty.

    Args:
        type_ (str | Unset):
        status (str | Unset):
        status_code (int | Unset):
        request_id (str | Unset):
        api_key_id (str | Unset):
        profile_id (str | Unset):
        search (str | Unset):
        days (int | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        skip (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityLogPage | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            status=status,
            status_code=status_code,
            request_id=request_id,
            api_key_id=api_key_id,
            profile_id=profile_id,
            search=search,
            days=days,
            from_=from_,
            to=to,
            limit=limit,
            skip=skip,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
