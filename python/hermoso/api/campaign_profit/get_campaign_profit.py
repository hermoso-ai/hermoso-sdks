from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.campaign_profit import CampaignProfit
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    platforms: str | Unset = UNSET,
    model: str | Unset = UNSET,
    revenue_from: str | Unset = UNSET,
    include_idle: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["days"] = days

    params["platforms"] = platforms

    params["model"] = model

    params["revenue_from"] = revenue_from

    params["include_idle"] = include_idle

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/campaign-profit",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CampaignProfit | Error | None:
    if response.status_code == 200:
        response_200 = CampaignProfit.from_dict(response.json())

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
) -> Response[CampaignProfit | Error]:
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
    days: int | Unset = UNSET,
    platforms: str | Unset = UNSET,
    model: str | Unset = UNSET,
    revenue_from: str | Unset = UNSET,
    include_idle: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[CampaignProfit | Error]:
    """Profit per campaign

     Each campaign’s spend read live from every connected ad platform, joined to the brand’s sales from
    ONE source per campaign (uploaded results, else conversion events credited by `model`, else Shopify
    / Stripe orders matched by utm_campaign). Money stays per currency; a platform that could not be
    read is listed in `unreadable`, never shown as zero. At most 92 days.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        platforms (str | Unset):
        model (str | Unset):
        revenue_from (str | Unset):
        include_idle (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignProfit | Error]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        days=days,
        platforms=platforms,
        model=model,
        revenue_from=revenue_from,
        include_idle=include_idle,
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
    days: int | Unset = UNSET,
    platforms: str | Unset = UNSET,
    model: str | Unset = UNSET,
    revenue_from: str | Unset = UNSET,
    include_idle: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> CampaignProfit | Error | None:
    """Profit per campaign

     Each campaign’s spend read live from every connected ad platform, joined to the brand’s sales from
    ONE source per campaign (uploaded results, else conversion events credited by `model`, else Shopify
    / Stripe orders matched by utm_campaign). Money stays per currency; a platform that could not be
    read is listed in `unreadable`, never shown as zero. At most 92 days.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        platforms (str | Unset):
        model (str | Unset):
        revenue_from (str | Unset):
        include_idle (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignProfit | Error
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        days=days,
        platforms=platforms,
        model=model,
        revenue_from=revenue_from,
        include_idle=include_idle,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    platforms: str | Unset = UNSET,
    model: str | Unset = UNSET,
    revenue_from: str | Unset = UNSET,
    include_idle: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[CampaignProfit | Error]:
    """Profit per campaign

     Each campaign’s spend read live from every connected ad platform, joined to the brand’s sales from
    ONE source per campaign (uploaded results, else conversion events credited by `model`, else Shopify
    / Stripe orders matched by utm_campaign). Money stays per currency; a platform that could not be
    read is listed in `unreadable`, never shown as zero. At most 92 days.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        platforms (str | Unset):
        model (str | Unset):
        revenue_from (str | Unset):
        include_idle (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignProfit | Error]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        days=days,
        platforms=platforms,
        model=model,
        revenue_from=revenue_from,
        include_idle=include_idle,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
    platforms: str | Unset = UNSET,
    model: str | Unset = UNSET,
    revenue_from: str | Unset = UNSET,
    include_idle: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> CampaignProfit | Error | None:
    """Profit per campaign

     Each campaign’s spend read live from every connected ad platform, joined to the brand’s sales from
    ONE source per campaign (uploaded results, else conversion events credited by `model`, else Shopify
    / Stripe orders matched by utm_campaign). Money stays per currency; a platform that could not be
    read is listed in `unreadable`, never shown as zero. At most 92 days.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        days (int | Unset):
        platforms (str | Unset):
        model (str | Unset):
        revenue_from (str | Unset):
        include_idle (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignProfit | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            days=days,
            platforms=platforms,
            model=model,
            revenue_from=revenue_from,
            include_idle=include_idle,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
