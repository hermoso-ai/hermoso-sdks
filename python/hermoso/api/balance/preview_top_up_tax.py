from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tax_preview import TaxPreview
from ...models.tax_preview_request import TaxPreviewRequest
from ...types import Unset


def _get_kwargs(
    *,
    body: TaxPreviewRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/balance/top-ups/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | TaxPreview | None:
    if response.status_code == 200:
        response_200 = TaxPreview.from_dict(response.json())

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
) -> Response[Error | TaxPreview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TaxPreviewRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | TaxPreview]:
    """Preview what a purchase charges

     Subtotal, tax and total for a credit pack or a plan before buying. No tax is added at checkout
    today, so the total is the price. Nothing is bought.

    Args:
        x_hermoso_user (str | Unset):
        body (TaxPreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaxPreview]
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
    body: TaxPreviewRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | TaxPreview | None:
    """Preview what a purchase charges

     Subtotal, tax and total for a credit pack or a plan before buying. No tax is added at checkout
    today, so the total is the price. Nothing is bought.

    Args:
        x_hermoso_user (str | Unset):
        body (TaxPreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaxPreview
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TaxPreviewRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | TaxPreview]:
    """Preview what a purchase charges

     Subtotal, tax and total for a credit pack or a plan before buying. No tax is added at checkout
    today, so the total is the price. Nothing is bought.

    Args:
        x_hermoso_user (str | Unset):
        body (TaxPreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaxPreview]
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
    body: TaxPreviewRequest,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | TaxPreview | None:
    """Preview what a purchase charges

     Subtotal, tax and total for a credit pack or a plan before buying. No tax is added at checkout
    today, so the total is the price. Nothing is bought.

    Args:
        x_hermoso_user (str | Unset):
        body (TaxPreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaxPreview
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
