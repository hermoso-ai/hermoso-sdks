from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...types import File
from ...types import Unset
from io import BytesIO


def _get_kwargs(
    *,
    url_query: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media/content",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.json()))

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
) -> Response[Error | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    url_query: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | File]:
    """Download a Hermoso file

     The bytes of a file Hermoso made or hosts (a Library `url`, a job `url`), streamed with its own
    `Content-Type`. Only Hermoso-hosted files are served; any other address is refused. For an app that
    has to hand raw bytes to its host (a design editor inserting the file) and cannot read our file host
    directly.

    Args:
        url_query (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    url_query: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | File | None:
    """Download a Hermoso file

     The bytes of a file Hermoso made or hosts (a Library `url`, a job `url`), streamed with its own
    `Content-Type`. Only Hermoso-hosted files are served; any other address is refused. For an app that
    has to hand raw bytes to its host (a design editor inserting the file) and cannot read our file host
    directly.

    Args:
        url_query (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    url_query: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | File]:
    """Download a Hermoso file

     The bytes of a file Hermoso made or hosts (a Library `url`, a job `url`), streamed with its own
    `Content-Type`. Only Hermoso-hosted files are served; any other address is refused. For an app that
    has to hand raw bytes to its host (a design editor inserting the file) and cannot read our file host
    directly.

    Args:
        url_query (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    url_query: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | File | None:
    """Download a Hermoso file

     The bytes of a file Hermoso made or hosts (a Library `url`, a job `url`), streamed with its own
    `Content-Type`. Only Hermoso-hosted files are served; any other address is refused. For an app that
    has to hand raw bytes to its host (a design editor inserting the file) and cannot read our file host
    directly.

    Args:
        url_query (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return (
        await asyncio_detailed(
            client=client,
            url_query=url_query,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
