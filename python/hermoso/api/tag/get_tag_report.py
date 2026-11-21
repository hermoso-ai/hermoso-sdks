from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.hermoso_tag_report import HermosoTagReport
from ...types import Unset


def _get_kwargs(
    *,
    group_by: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["group_by"] = group_by

    params["from"] = from_

    params["to"] = to

    params["days"] = days

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tag/report",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | HermosoTagReport | None:
    if response.status_code == 200:
        response_200 = HermosoTagReport.from_dict(response.json())

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
) -> Response[Error | HermosoTagReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_by: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | HermosoTagReport]:
    """Visits, leads and revenue by source

     Visits → leads → purchases → revenue (per currency) from the tag, grouped by `group_by`: channel
    (default), source, medium, campaign, post, ad or page. UTC days, at most 92; bots are left out and
    test events reported apart. Free.

    Args:
        group_by (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HermosoTagReport]
    """

    kwargs = _get_kwargs(
        group_by=group_by,
        from_=from_,
        to=to,
        days=days,
        limit=limit,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_by: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | HermosoTagReport | None:
    """Visits, leads and revenue by source

     Visits → leads → purchases → revenue (per currency) from the tag, grouped by `group_by`: channel
    (default), source, medium, campaign, post, ad or page. UTC days, at most 92; bots are left out and
    test events reported apart. Free.

    Args:
        group_by (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HermosoTagReport
    """

    return sync_detailed(
        client=client,
        group_by=group_by,
        from_=from_,
        to=to,
        days=days,
        limit=limit,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_by: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | HermosoTagReport]:
    """Visits, leads and revenue by source

     Visits → leads → purchases → revenue (per currency) from the tag, grouped by `group_by`: channel
    (default), source, medium, campaign, post, ad or page. UTC days, at most 92; bots are left out and
    test events reported apart. Free.

    Args:
        group_by (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HermosoTagReport]
    """

    kwargs = _get_kwargs(
        group_by=group_by,
        from_=from_,
        to=to,
        days=days,
        limit=limit,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_by: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | HermosoTagReport | None:
    """Visits, leads and revenue by source

     Visits → leads → purchases → revenue (per currency) from the tag, grouped by `group_by`: channel
    (default), source, medium, campaign, post, ad or page. UTC days, at most 92; bots are left out and
    test events reported apart. Free.

    Args:
        group_by (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HermosoTagReport
    """

    return (
        await asyncio_detailed(
            client=client,
            group_by=group_by,
            from_=from_,
            to=to,
            days=days,
            limit=limit,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
