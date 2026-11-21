from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversion_insights import ConversionInsights
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    customer: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    visitor_id: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["customer"] = customer

    params["email"] = email

    params["phone"] = phone

    params["external_id"] = external_id

    params["visitor_id"] = visitor_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/journey",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConversionInsights | Error | None:
    if response.status_code == 200:
        response_200 = ConversionInsights.from_dict(response.json())

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
) -> Response[ConversionInsights | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    customer: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    visitor_id: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConversionInsights | Error]:
    """One customer’s journey

     Every touch and conversion of one person, oldest first, with lifetime value per currency. Name them
    by `email`, `phone`, `external_id`, `visitor_id` or a `customer` key from GET /v1/events/customers.
    People are tied together across events by any identifier they share.

    Args:
        customer (str | Unset):
        email (str | Unset):
        phone (str | Unset):
        external_id (str | Unset):
        visitor_id (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversionInsights | Error]
    """

    kwargs = _get_kwargs(
        customer=customer,
        email=email,
        phone=phone,
        external_id=external_id,
        visitor_id=visitor_id,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    customer: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    visitor_id: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConversionInsights | Error | None:
    """One customer’s journey

     Every touch and conversion of one person, oldest first, with lifetime value per currency. Name them
    by `email`, `phone`, `external_id`, `visitor_id` or a `customer` key from GET /v1/events/customers.
    People are tied together across events by any identifier they share.

    Args:
        customer (str | Unset):
        email (str | Unset):
        phone (str | Unset):
        external_id (str | Unset):
        visitor_id (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversionInsights | Error
    """

    return sync_detailed(
        client=client,
        customer=customer,
        email=email,
        phone=phone,
        external_id=external_id,
        visitor_id=visitor_id,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    visitor_id: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[ConversionInsights | Error]:
    """One customer’s journey

     Every touch and conversion of one person, oldest first, with lifetime value per currency. Name them
    by `email`, `phone`, `external_id`, `visitor_id` or a `customer` key from GET /v1/events/customers.
    People are tied together across events by any identifier they share.

    Args:
        customer (str | Unset):
        email (str | Unset):
        phone (str | Unset):
        external_id (str | Unset):
        visitor_id (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversionInsights | Error]
    """

    kwargs = _get_kwargs(
        customer=customer,
        email=email,
        phone=phone,
        external_id=external_id,
        visitor_id=visitor_id,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    customer: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    visitor_id: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> ConversionInsights | Error | None:
    """One customer’s journey

     Every touch and conversion of one person, oldest first, with lifetime value per currency. Name them
    by `email`, `phone`, `external_id`, `visitor_id` or a `customer` key from GET /v1/events/customers.
    People are tied together across events by any identifier they share.

    Args:
        customer (str | Unset):
        email (str | Unset):
        phone (str | Unset):
        external_id (str | Unset):
        visitor_id (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversionInsights | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            customer=customer,
            email=email,
            phone=phone,
            external_id=external_id,
            visitor_id=visitor_id,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
