from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.clone_quote import CloneQuote
from ...models.clone_quote_request import CloneQuoteRequest
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    body: CloneQuoteRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clones/quote",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CloneQuote | Error | None:
    if response.status_code == 200:
        response_200 = CloneQuote.from_dict(response.json())

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
) -> Response[CloneQuote | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CloneQuoteRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[CloneQuote | Error]:
    """Price a clone before running it

     What cloning an ad for this profile will cost, step by step, before anything runs. `type: image`
    prices the static clone (`clone_static`): reading the layout (a flat charge) plus the image render’s
    own hold, with the brand’s product photo attached exactly as the clone attaches it; the copy writing
    and the final brand check are billed at their real model cost and are listed with `credits: null`.
    `type: video` prices the first step of a video clone (`clone_video`: watching the original and
    planning the storyboard) as the server’s own estimate; the render is priced exactly once the plan
    exists, by calling `render_ad` with `dryRun: true`. Free: nothing is read, reserved or charged.

    Args:
        x_hermoso_user (str | Unset):
        body (CloneQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloneQuote | Error]
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
    body: CloneQuoteRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> CloneQuote | Error | None:
    """Price a clone before running it

     What cloning an ad for this profile will cost, step by step, before anything runs. `type: image`
    prices the static clone (`clone_static`): reading the layout (a flat charge) plus the image render’s
    own hold, with the brand’s product photo attached exactly as the clone attaches it; the copy writing
    and the final brand check are billed at their real model cost and are listed with `credits: null`.
    `type: video` prices the first step of a video clone (`clone_video`: watching the original and
    planning the storyboard) as the server’s own estimate; the render is priced exactly once the plan
    exists, by calling `render_ad` with `dryRun: true`. Free: nothing is read, reserved or charged.

    Args:
        x_hermoso_user (str | Unset):
        body (CloneQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloneQuote | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CloneQuoteRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[CloneQuote | Error]:
    """Price a clone before running it

     What cloning an ad for this profile will cost, step by step, before anything runs. `type: image`
    prices the static clone (`clone_static`): reading the layout (a flat charge) plus the image render’s
    own hold, with the brand’s product photo attached exactly as the clone attaches it; the copy writing
    and the final brand check are billed at their real model cost and are listed with `credits: null`.
    `type: video` prices the first step of a video clone (`clone_video`: watching the original and
    planning the storyboard) as the server’s own estimate; the render is priced exactly once the plan
    exists, by calling `render_ad` with `dryRun: true`. Free: nothing is read, reserved or charged.

    Args:
        x_hermoso_user (str | Unset):
        body (CloneQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloneQuote | Error]
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
    body: CloneQuoteRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> CloneQuote | Error | None:
    """Price a clone before running it

     What cloning an ad for this profile will cost, step by step, before anything runs. `type: image`
    prices the static clone (`clone_static`): reading the layout (a flat charge) plus the image render’s
    own hold, with the brand’s product photo attached exactly as the clone attaches it; the copy writing
    and the final brand check are billed at their real model cost and are listed with `credits: null`.
    `type: video` prices the first step of a video clone (`clone_video`: watching the original and
    planning the storyboard) as the server’s own estimate; the render is priced exactly once the plan
    exists, by calling `render_ad` with `dryRun: true`. Free: nothing is read, reserved or charged.

    Args:
        x_hermoso_user (str | Unset):
        body (CloneQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloneQuote | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
