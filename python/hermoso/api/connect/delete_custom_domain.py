from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.white_label_result import WhiteLabelResult
from ...types import Unset


def _get_kwargs(
    domain_id: str,
    *,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["confirm"] = confirm

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/connect/custom-domains/{domain_id}".format(
            domain_id=quote(str(domain_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | WhiteLabelResult | None:
    if response.status_code == 200:
        response_200 = WhiteLabelResult.from_dict(response.json())

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
) -> Response[Error | WhiteLabelResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WhiteLabelResult]:
    """Remove a connect domain

     It stops serving connect pages at once, including links already sent on it, so without
    `confirm=true` this only says what would happen.

    Args:
        domain_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WhiteLabelResult]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        confirm=confirm,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WhiteLabelResult | None:
    """Remove a connect domain

     It stops serving connect pages at once, including links already sent on it, so without
    `confirm=true` this only says what would happen.

    Args:
        domain_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WhiteLabelResult
    """

    return sync_detailed(
        domain_id=domain_id,
        client=client,
        confirm=confirm,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    domain_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WhiteLabelResult]:
    """Remove a connect domain

     It stops serving connect pages at once, including links already sent on it, so without
    `confirm=true` this only says what would happen.

    Args:
        domain_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WhiteLabelResult]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        confirm=confirm,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WhiteLabelResult | None:
    """Remove a connect domain

     It stops serving connect pages at once, including links already sent on it, so without
    `confirm=true` this only says what would happen.

    Args:
        domain_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WhiteLabelResult
    """

    return (
        await asyncio_detailed(
            domain_id=domain_id,
            client=client,
            confirm=confirm,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
