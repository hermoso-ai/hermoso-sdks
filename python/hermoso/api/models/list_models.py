from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.model_list import ModelList
from ...types import Unset


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["type"] = type_

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/models",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | ModelList | None:
    if response.status_code == 200:
        response_200 = ModelList.from_dict(response.json())

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
) -> Response[Error | ModelList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | ModelList]:
    """List the image and video models

     The live model catalog this account can render with: ids, labels, the aspect ratios, sizes and
    lengths each takes, and its list price in credits. For the exact price of one render with your
    prompt and brand, ask `POST /v1/generations/quote`: brand product photos and video audio can change
    it. Models that only edit or only animate a supplied picture are marked `needs_reference`. The
    catalog grows: read it, never hard-code it.

    Args:
        type_ (str | Unset):
        sort (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ModelList]
    """

    kwargs = _get_kwargs(
        type_=type_,
        sort=sort,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | ModelList | None:
    """List the image and video models

     The live model catalog this account can render with: ids, labels, the aspect ratios, sizes and
    lengths each takes, and its list price in credits. For the exact price of one render with your
    prompt and brand, ask `POST /v1/generations/quote`: brand product photos and video audio can change
    it. Models that only edit or only animate a supplied picture are marked `needs_reference`. The
    catalog grows: read it, never hard-code it.

    Args:
        type_ (str | Unset):
        sort (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ModelList
    """

    return sync_detailed(
        client=client,
        type_=type_,
        sort=sort,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | ModelList]:
    """List the image and video models

     The live model catalog this account can render with: ids, labels, the aspect ratios, sizes and
    lengths each takes, and its list price in credits. For the exact price of one render with your
    prompt and brand, ask `POST /v1/generations/quote`: brand product photos and video audio can change
    it. Models that only edit or only animate a supplied picture are marked `needs_reference`. The
    catalog grows: read it, never hard-code it.

    Args:
        type_ (str | Unset):
        sort (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ModelList]
    """

    kwargs = _get_kwargs(
        type_=type_,
        sort=sort,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | ModelList | None:
    """List the image and video models

     The live model catalog this account can render with: ids, labels, the aspect ratios, sizes and
    lengths each takes, and its list price in credits. For the exact price of one render with your
    prompt and brand, ask `POST /v1/generations/quote`: brand product photos and video audio can change
    it. Models that only edit or only animate a supplied picture are marked `needs_reference`. The
    catalog grows: read it, never hard-code it.

    Args:
        type_ (str | Unset):
        sort (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ModelList
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            sort=sort,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
