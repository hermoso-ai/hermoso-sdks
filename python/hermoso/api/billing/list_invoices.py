from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.invoice_list import InvoiceList
from ...types import Unset


def _get_kwargs(
    *,
    brand_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["brand_id"] = brand_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/invoices",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | InvoiceList | None:
    if response.status_code == 200:
        response_200 = InvoiceList.from_dict(response.json())

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
) -> Response[Error | InvoiceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    brand_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | InvoiceList]:
    """Invoices and receipts

     The account’s invoices and payment receipts, or one separately billed brand’s (`brand_id`), newest
    first, each with its hosted page and PDF links.

    Args:
        brand_id (str | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvoiceList]
    """

    kwargs = _get_kwargs(
        brand_id=brand_id,
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
    brand_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | InvoiceList | None:
    """Invoices and receipts

     The account’s invoices and payment receipts, or one separately billed brand’s (`brand_id`), newest
    first, each with its hosted page and PDF links.

    Args:
        brand_id (str | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvoiceList
    """

    return sync_detailed(
        client=client,
        brand_id=brand_id,
        limit=limit,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    brand_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | InvoiceList]:
    """Invoices and receipts

     The account’s invoices and payment receipts, or one separately billed brand’s (`brand_id`), newest
    first, each with its hosted page and PDF links.

    Args:
        brand_id (str | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvoiceList]
    """

    kwargs = _get_kwargs(
        brand_id=brand_id,
        limit=limit,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    brand_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | InvoiceList | None:
    """Invoices and receipts

     The account’s invoices and payment receipts, or one separately billed brand’s (`brand_id`), newest
    first, each with its hosted page and PDF links.

    Args:
        brand_id (str | Unset):
        limit (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvoiceList
    """

    return (
        await asyncio_detailed(
            client=client,
            brand_id=brand_id,
            limit=limit,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
