from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.error import Error
from ...models.signup import Signup
from ...models.signup_create import SignupCreate


def _get_kwargs(
    *,
    body: SignupCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/signup",
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
    *,
    client: AuthenticatedClient | Client,
    body: SignupCreate,
) -> Response[Error | Signup]:
    """Start an agentic signup

     Create a Hermoso account programmatically, with no human at a browser and no existing credential —
    the one call in this API that needs no key, because the key is what it creates. Returns a Stripe
    Checkout URL and a one-time `claim_token`.

    AGENTIC SIGNUP REQUIRES A PAID PLAN. Nothing is created here: no account, no credits, no row. An
    account exists only once Stripe reports the payment completed, at which point `POST
    /v1/signup/{id}/claim` provisions it and returns your API key. The free plan is not available on
    this path — it is available to a person signing up at https://app.hermoso.ai.

    A card is entered on Stripe’s own hosted page, never here, so the checkout step itself needs a
    browser: hand `checkout_url` to whoever is paying. `claim_token` is returned exactly once and is the
    only proof this signup is yours — a checkout session id alone is not enough, because session ids
    travel in URLs.

    Args:
        body (SignupCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signup]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SignupCreate,
) -> Error | Signup | None:
    """Start an agentic signup

     Create a Hermoso account programmatically, with no human at a browser and no existing credential —
    the one call in this API that needs no key, because the key is what it creates. Returns a Stripe
    Checkout URL and a one-time `claim_token`.

    AGENTIC SIGNUP REQUIRES A PAID PLAN. Nothing is created here: no account, no credits, no row. An
    account exists only once Stripe reports the payment completed, at which point `POST
    /v1/signup/{id}/claim` provisions it and returns your API key. The free plan is not available on
    this path — it is available to a person signing up at https://app.hermoso.ai.

    A card is entered on Stripe’s own hosted page, never here, so the checkout step itself needs a
    browser: hand `checkout_url` to whoever is paying. `claim_token` is returned exactly once and is the
    only proof this signup is yours — a checkout session id alone is not enough, because session ids
    travel in URLs.

    Args:
        body (SignupCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signup
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignupCreate,
) -> Response[Error | Signup]:
    """Start an agentic signup

     Create a Hermoso account programmatically, with no human at a browser and no existing credential —
    the one call in this API that needs no key, because the key is what it creates. Returns a Stripe
    Checkout URL and a one-time `claim_token`.

    AGENTIC SIGNUP REQUIRES A PAID PLAN. Nothing is created here: no account, no credits, no row. An
    account exists only once Stripe reports the payment completed, at which point `POST
    /v1/signup/{id}/claim` provisions it and returns your API key. The free plan is not available on
    this path — it is available to a person signing up at https://app.hermoso.ai.

    A card is entered on Stripe’s own hosted page, never here, so the checkout step itself needs a
    browser: hand `checkout_url` to whoever is paying. `claim_token` is returned exactly once and is the
    only proof this signup is yours — a checkout session id alone is not enough, because session ids
    travel in URLs.

    Args:
        body (SignupCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signup]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SignupCreate,
) -> Error | Signup | None:
    """Start an agentic signup

     Create a Hermoso account programmatically, with no human at a browser and no existing credential —
    the one call in this API that needs no key, because the key is what it creates. Returns a Stripe
    Checkout URL and a one-time `claim_token`.

    AGENTIC SIGNUP REQUIRES A PAID PLAN. Nothing is created here: no account, no credits, no row. An
    account exists only once Stripe reports the payment completed, at which point `POST
    /v1/signup/{id}/claim` provisions it and returns your API key. The free plan is not available on
    this path — it is available to a person signing up at https://app.hermoso.ai.

    A card is entered on Stripe’s own hosted page, never here, so the checkout step itself needs a
    browser: hand `checkout_url` to whoever is paying. `claim_token` is returned exactly once and is the
    only proof this signup is yours — a checkout session id alone is not enough, because session ids
    travel in URLs.

    Args:
        body (SignupCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signup
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
