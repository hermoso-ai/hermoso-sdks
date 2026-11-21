from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.hermoso_tag_audience_action import HermosoTagAudienceAction
from ...models.hermoso_tag_audiences import HermosoTagAudiences
from ...types import Unset


def _get_kwargs(
    *,
    body: HermosoTagAudienceAction,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tag/audiences",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | HermosoTagAudiences | None:
    if response.status_code == 200:
        response_200 = HermosoTagAudiences.from_dict(response.json())

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
) -> Response[Error | HermosoTagAudiences]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: HermosoTagAudienceAction,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | HermosoTagAudiences]:
    """Save, preview, delete or sync a visitor segment

     `action`: `preview` (default; counts a rule set, saves nothing), `save` (`name` and rules `visited`
    (page path prefixes), `events` (any of), `not_events` (none of), `within_days` 1-180; `segment_id`
    to edit), `delete` (`segment_id`, `confirm: true`) or `sync` (`segment_id`, `platform` meta |
    google_ads | snapchat_ads | pinterest_ads | x_ads, `audience_id` (Meta: omit for a new audience;
    `ad_account_id`), `accept_terms` for Google Customer Match, `confirm: true`). A sync sends ONLY
    identified visitors whose latest consent allowed ad use, as SHA-256 hashes; without `confirm` it
    says what it would send and sends nothing. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagAudienceAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HermosoTagAudiences]
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
    body: HermosoTagAudienceAction,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | HermosoTagAudiences | None:
    """Save, preview, delete or sync a visitor segment

     `action`: `preview` (default; counts a rule set, saves nothing), `save` (`name` and rules `visited`
    (page path prefixes), `events` (any of), `not_events` (none of), `within_days` 1-180; `segment_id`
    to edit), `delete` (`segment_id`, `confirm: true`) or `sync` (`segment_id`, `platform` meta |
    google_ads | snapchat_ads | pinterest_ads | x_ads, `audience_id` (Meta: omit for a new audience;
    `ad_account_id`), `accept_terms` for Google Customer Match, `confirm: true`). A sync sends ONLY
    identified visitors whose latest consent allowed ad use, as SHA-256 hashes; without `confirm` it
    says what it would send and sends nothing. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagAudienceAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HermosoTagAudiences
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: HermosoTagAudienceAction,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | HermosoTagAudiences]:
    """Save, preview, delete or sync a visitor segment

     `action`: `preview` (default; counts a rule set, saves nothing), `save` (`name` and rules `visited`
    (page path prefixes), `events` (any of), `not_events` (none of), `within_days` 1-180; `segment_id`
    to edit), `delete` (`segment_id`, `confirm: true`) or `sync` (`segment_id`, `platform` meta |
    google_ads | snapchat_ads | pinterest_ads | x_ads, `audience_id` (Meta: omit for a new audience;
    `ad_account_id`), `accept_terms` for Google Customer Match, `confirm: true`). A sync sends ONLY
    identified visitors whose latest consent allowed ad use, as SHA-256 hashes; without `confirm` it
    says what it would send and sends nothing. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagAudienceAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HermosoTagAudiences]
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
    body: HermosoTagAudienceAction,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | HermosoTagAudiences | None:
    """Save, preview, delete or sync a visitor segment

     `action`: `preview` (default; counts a rule set, saves nothing), `save` (`name` and rules `visited`
    (page path prefixes), `events` (any of), `not_events` (none of), `within_days` 1-180; `segment_id`
    to edit), `delete` (`segment_id`, `confirm: true`) or `sync` (`segment_id`, `platform` meta |
    google_ads | snapchat_ads | pinterest_ads | x_ads, `audience_id` (Meta: omit for a new audience;
    `ad_account_id`), `accept_terms` for Google Customer Match, `confirm: true`). A sync sends ONLY
    identified visitors whose latest consent allowed ad use, as SHA-256 hashes; without `confirm` it
    says what it would send and sends nothing. Free.

    Args:
        x_hermoso_user (str | Unset):
        body (HermosoTagAudienceAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HermosoTagAudiences
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
