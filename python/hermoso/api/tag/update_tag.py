from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.hermoso_tag import HermosoTag
from ...models.hermoso_tag_update import HermosoTagUpdate
from ...types import Unset


def _get_kwargs(
    *,
    body: HermosoTagUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tag",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | HermosoTag | None:
    if response.status_code == 200:
        response_200 = HermosoTag.from_dict(response.json())

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
) -> Response[Error | HermosoTag]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: HermosoTagUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | HermosoTag]:
    """Change the tag’s settings, or verify it on the site

     `action: "update"` (default) sets any of `consent_default` (granted | denied), `wait_for_consent`,
    `honor_gpc`, `honor_dnt`, `forward`, `forward_events`, `allowed_domains`, `spa`, `test_mode`
    ("validate", a TikTok / Reddit test code, or "off") and `conversions` (the brand’s own events
    counted as conversions: `{"quote_requested": {"as": "Lead"}}`). `action: "verify"` reads the site
    (`url`, default the brand’s website) for the snippet and reports the last event seen. Also
    `auto_track` ({forms, outbound, downloads, scroll}) and `link_domains` (cross-domain). `action:
    "server_key"` returns a new server key ONCE for `POST /htag/s` (a backend’s own endpoint,
    Authorization: Bearer htsk_…); `action: "stripe"` with `signing_secret` (whsec_…) turns a Stripe
    webhook into Purchases through the tag. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HermosoTag]
    """

    kwargs = _get_kwargs(
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: HermosoTagUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | HermosoTag | None:
    """Change the tag’s settings, or verify it on the site

     `action: "update"` (default) sets any of `consent_default` (granted | denied), `wait_for_consent`,
    `honor_gpc`, `honor_dnt`, `forward`, `forward_events`, `allowed_domains`, `spa`, `test_mode`
    ("validate", a TikTok / Reddit test code, or "off") and `conversions` (the brand’s own events
    counted as conversions: `{"quote_requested": {"as": "Lead"}}`). `action: "verify"` reads the site
    (`url`, default the brand’s website) for the snippet and reports the last event seen. Also
    `auto_track` ({forms, outbound, downloads, scroll}) and `link_domains` (cross-domain). `action:
    "server_key"` returns a new server key ONCE for `POST /htag/s` (a backend’s own endpoint,
    Authorization: Bearer htsk_…); `action: "stripe"` with `signing_secret` (whsec_…) turns a Stripe
    webhook into Purchases through the tag. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HermosoTag
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: HermosoTagUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | HermosoTag]:
    """Change the tag’s settings, or verify it on the site

     `action: "update"` (default) sets any of `consent_default` (granted | denied), `wait_for_consent`,
    `honor_gpc`, `honor_dnt`, `forward`, `forward_events`, `allowed_domains`, `spa`, `test_mode`
    ("validate", a TikTok / Reddit test code, or "off") and `conversions` (the brand’s own events
    counted as conversions: `{"quote_requested": {"as": "Lead"}}`). `action: "verify"` reads the site
    (`url`, default the brand’s website) for the snippet and reports the last event seen. Also
    `auto_track` ({forms, outbound, downloads, scroll}) and `link_domains` (cross-domain). `action:
    "server_key"` returns a new server key ONCE for `POST /htag/s` (a backend’s own endpoint,
    Authorization: Bearer htsk_…); `action: "stripe"` with `signing_secret` (whsec_…) turns a Stripe
    webhook into Purchases through the tag. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HermosoTag]
    """

    kwargs = _get_kwargs(
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: HermosoTagUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | HermosoTag | None:
    """Change the tag’s settings, or verify it on the site

     `action: "update"` (default) sets any of `consent_default` (granted | denied), `wait_for_consent`,
    `honor_gpc`, `honor_dnt`, `forward`, `forward_events`, `allowed_domains`, `spa`, `test_mode`
    ("validate", a TikTok / Reddit test code, or "off") and `conversions` (the brand’s own events
    counted as conversions: `{"quote_requested": {"as": "Lead"}}`). `action: "verify"` reads the site
    (`url`, default the brand’s website) for the snippet and reports the last event seen. Also
    `auto_track` ({forms, outbound, downloads, scroll}) and `link_domains` (cross-domain). `action:
    "server_key"` returns a new server key ONCE for `POST /htag/s` (a backend’s own endpoint,
    Authorization: Bearer htsk_…); `action: "stripe"` with `signing_secret` (whsec_…) turns a Stripe
    webhook into Purchases through the tag. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HermosoTag
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
