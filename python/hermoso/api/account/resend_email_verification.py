from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contact_email import ContactEmail
from ...models.contact_email_resend import ContactEmailResend
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    body: ContactEmailResend,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/account/email/resend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ContactEmail | Error | None:
    if response.status_code == 200:
        response_200 = ContactEmail.from_dict(response.json())

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
) -> Response[ContactEmail | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactEmailResend,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ContactEmail | Error]:
    """Re-send the verification link, or set a different contact email

     With no body, re-sends the verification link to the current contact address (at most once every 10
    minutes — 429 `verification_recently_sent` otherwise). With `email`, replaces the contact address
    and starts verification over for the new one. An address that is already the sign-in email of
    another Hermoso account cannot be verified here (409 `email_in_use` when the link is clicked) and
    this account stays exactly as it is.

    Args:
        x_hermoso_user (str | Unset):
        body (ContactEmailResend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactEmail | Error]
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
    body: ContactEmailResend,
    x_hermoso_user: str | Unset = UNSET,
) -> ContactEmail | Error | None:
    """Re-send the verification link, or set a different contact email

     With no body, re-sends the verification link to the current contact address (at most once every 10
    minutes — 429 `verification_recently_sent` otherwise). With `email`, replaces the contact address
    and starts verification over for the new one. An address that is already the sign-in email of
    another Hermoso account cannot be verified here (409 `email_in_use` when the link is clicked) and
    this account stays exactly as it is.

    Args:
        x_hermoso_user (str | Unset):
        body (ContactEmailResend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactEmail | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactEmailResend,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ContactEmail | Error]:
    """Re-send the verification link, or set a different contact email

     With no body, re-sends the verification link to the current contact address (at most once every 10
    minutes — 429 `verification_recently_sent` otherwise). With `email`, replaces the contact address
    and starts verification over for the new one. An address that is already the sign-in email of
    another Hermoso account cannot be verified here (409 `email_in_use` when the link is clicked) and
    this account stays exactly as it is.

    Args:
        x_hermoso_user (str | Unset):
        body (ContactEmailResend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactEmail | Error]
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
    body: ContactEmailResend,
    x_hermoso_user: str | Unset = UNSET,
) -> ContactEmail | Error | None:
    """Re-send the verification link, or set a different contact email

     With no body, re-sends the verification link to the current contact address (at most once every 10
    minutes — 429 `verification_recently_sent` otherwise). With `email`, replaces the contact address
    and starts verification over for the new one. An address that is already the sign-in email of
    another Hermoso account cannot be verified here (409 `email_in_use` when the link is clicked) and
    this account stays exactly as it is.

    Args:
        x_hermoso_user (str | Unset):
        body (ContactEmailResend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactEmail | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
