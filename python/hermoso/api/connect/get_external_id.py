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
    external_id: str,
    *,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/external-ids/{external_id}".format(
            external_id=quote(str(external_id), safe=""),
        ),
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
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WhiteLabelResult]:
    """Find a brand by your own customer id

     The brand mapped to your external id (set when you create a connect link with `external_id`) and
    what is connected on it.

    Args:
        external_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WhiteLabelResult]
    """

    kwargs = _get_kwargs(
        external_id=external_id,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WhiteLabelResult | None:
    """Find a brand by your own customer id

     The brand mapped to your external id (set when you create a connect link with `external_id`) and
    what is connected on it.

    Args:
        external_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WhiteLabelResult
    """

    return sync_detailed(
        external_id=external_id,
        client=client,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WhiteLabelResult]:
    """Find a brand by your own customer id

     The brand mapped to your external id (set when you create a connect link with `external_id`) and
    what is connected on it.

    Args:
        external_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WhiteLabelResult]
    """

    kwargs = _get_kwargs(
        external_id=external_id,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WhiteLabelResult | None:
    """Find a brand by your own customer id

     The brand mapped to your external id (set when you create a connect link with `external_id`) and
    what is connected on it.

    Args:
        external_id (str):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WhiteLabelResult
    """

    return (
        await asyncio_detailed(
            external_id=external_id,
            client=client,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
