from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.error import Error
from ...models.signup import Signup
from ...models.signup_claim import SignupClaim


def _get_kwargs(
    id: str,
    *,
    body: SignupClaim,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/signup/{id}/claim".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | Signup | None:
    if response.status_code == 200:
        response_200 = Signup.from_dict(response.json())

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
) -> Response[Error | Signup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignupClaim,
) -> Response[Error | Signup]:
    """Claim a paid signup (poll until ready)

     Poll this until `status` is `ready`. While payment is outstanding it answers `awaiting_payment` and
    creates nothing. Once Stripe reports the payment completed it provisions the account, applies the
    plan and its credits, and returns `api_key` — ONCE.

    The key is stored only as a hash and can never be re-read. If you lose the response, re-claiming
    inside 24 hours mints a replacement and revokes the previous key, so a signup never leaves two live
    credentials behind. After that window there is no self-serve recovery: an agentic account has a
    synthetic identity and no mailbox to send a link to. Billing is always recoverable regardless — the
    payer receives Stripe’s receipts and can manage or cancel the subscription from Stripe’s own portal.

    Args:
        id (str):
        body (SignupClaim):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signup]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignupClaim,
) -> Error | Signup | None:
    """Claim a paid signup (poll until ready)

     Poll this until `status` is `ready`. While payment is outstanding it answers `awaiting_payment` and
    creates nothing. Once Stripe reports the payment completed it provisions the account, applies the
    plan and its credits, and returns `api_key` — ONCE.

    The key is stored only as a hash and can never be re-read. If you lose the response, re-claiming
    inside 24 hours mints a replacement and revokes the previous key, so a signup never leaves two live
    credentials behind. After that window there is no self-serve recovery: an agentic account has a
    synthetic identity and no mailbox to send a link to. Billing is always recoverable regardless — the
    payer receives Stripe’s receipts and can manage or cancel the subscription from Stripe’s own portal.

    Args:
        id (str):
        body (SignupClaim):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signup
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignupClaim,
) -> Response[Error | Signup]:
    """Claim a paid signup (poll until ready)

     Poll this until `status` is `ready`. While payment is outstanding it answers `awaiting_payment` and
    creates nothing. Once Stripe reports the payment completed it provisions the account, applies the
    plan and its credits, and returns `api_key` — ONCE.

    The key is stored only as a hash and can never be re-read. If you lose the response, re-claiming
    inside 24 hours mints a replacement and revokes the previous key, so a signup never leaves two live
    credentials behind. After that window there is no self-serve recovery: an agentic account has a
    synthetic identity and no mailbox to send a link to. Billing is always recoverable regardless — the
    payer receives Stripe’s receipts and can manage or cancel the subscription from Stripe’s own portal.

    Args:
        id (str):
        body (SignupClaim):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signup]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SignupClaim,
) -> Error | Signup | None:
    """Claim a paid signup (poll until ready)

     Poll this until `status` is `ready`. While payment is outstanding it answers `awaiting_payment` and
    creates nothing. Once Stripe reports the payment completed it provisions the account, applies the
    plan and its credits, and returns `api_key` — ONCE.

    The key is stored only as a hash and can never be re-read. If you lose the response, re-claiming
    inside 24 hours mints a replacement and revokes the previous key, so a signup never leaves two live
    credentials behind. After that window there is no self-serve recovery: an agentic account has a
    synthetic identity and no mailbox to send a link to. Billing is always recoverable regardless — the
    payer receives Stripe’s receipts and can manage or cancel the subscription from Stripe’s own portal.

    Args:
        id (str):
        body (SignupClaim):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signup
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
