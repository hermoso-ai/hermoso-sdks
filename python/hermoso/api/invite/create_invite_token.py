from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.invite import Invite
from ...models.invite_create import InviteCreate
from ...types import Unset


def _get_kwargs(
    *,
    body: InviteCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/invite/tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | Invite | None:
    if response.status_code == 200:
        response_200 = Invite.from_dict(response.json())

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
) -> Response[Error | Invite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InviteCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Invite]:
    """Invite someone to this profile

     Invites one email address to the profile this key acts on, with a role and optional turned-off
    areas. `send_email: false` returns a one-time `invite_url` instead of emailing it; the invite is
    single-use and expires after 14 days. Inviting someone who is already an active member changes
    nothing (use PATCH /v1/users/{email}). Admins only.

    Args:
        x_hermoso_user (str | Unset):
        body (InviteCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Invite]
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
    body: InviteCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Invite | None:
    """Invite someone to this profile

     Invites one email address to the profile this key acts on, with a role and optional turned-off
    areas. `send_email: false` returns a one-time `invite_url` instead of emailing it; the invite is
    single-use and expires after 14 days. Inviting someone who is already an active member changes
    nothing (use PATCH /v1/users/{email}). Admins only.

    Args:
        x_hermoso_user (str | Unset):
        body (InviteCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Invite
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InviteCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Invite]:
    """Invite someone to this profile

     Invites one email address to the profile this key acts on, with a role and optional turned-off
    areas. `send_email: false` returns a one-time `invite_url` instead of emailing it; the invite is
    single-use and expires after 14 days. Inviting someone who is already an active member changes
    nothing (use PATCH /v1/users/{email}). Admins only.

    Args:
        x_hermoso_user (str | Unset):
        body (InviteCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Invite]
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
    body: InviteCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Invite | None:
    """Invite someone to this profile

     Invites one email address to the profile this key acts on, with a role and optional turned-off
    areas. `send_email: false` returns a one-time `invite_url` instead of emailing it; the invite is
    single-use and expires after 14 days. Inviting someone who is already an active member changes
    nothing (use PATCH /v1/users/{email}). Admins only.

    Args:
        x_hermoso_user (str | Unset):
        body (InviteCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Invite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
