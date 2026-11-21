from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.media import Media
from ...types import File
from ...types import Unset


def _get_kwargs(
    *,
    body: File | Unset = UNSET,
    url_query: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | Media | None:
    if response.status_code == 200:
        response_200 = Media.from_dict(response.json())

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
) -> Response[Error | Media]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: File | Unset = UNSET,
    url_query: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Media]:
    """Upload media

     Turn a file into a Hermoso-hosted URL that `POST /v1/posts` accepts. Two ways in, and exactly ONE
    per call: send the file’s raw bytes as the request body with its own `Content-Type` (name it with
    `X-File-Name`), or send `?url=` (or a JSON body `{"url": "…"}`) and we fetch it. Sending both is an
    error rather than a silent precedence — a caller who sent both has two different files in mind. A
    form-encoded or multipart body is refused with `400 unsupported_media_body`: send the bytes
    themselves, not a form around them.

    Args:
        url_query (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Media]
    """

    kwargs = _get_kwargs(
        body=body,
        url_query=url_query,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: File | Unset = UNSET,
    url_query: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Media | None:
    """Upload media

     Turn a file into a Hermoso-hosted URL that `POST /v1/posts` accepts. Two ways in, and exactly ONE
    per call: send the file’s raw bytes as the request body with its own `Content-Type` (name it with
    `X-File-Name`), or send `?url=` (or a JSON body `{"url": "…"}`) and we fetch it. Sending both is an
    error rather than a silent precedence — a caller who sent both has two different files in mind. A
    form-encoded or multipart body is refused with `400 unsupported_media_body`: send the bytes
    themselves, not a form around them.

    Args:
        url_query (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Media
    """

    return sync_detailed(
        client=client,
        body=body,
        url_query=url_query,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: File | Unset = UNSET,
    url_query: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Media]:
    """Upload media

     Turn a file into a Hermoso-hosted URL that `POST /v1/posts` accepts. Two ways in, and exactly ONE
    per call: send the file’s raw bytes as the request body with its own `Content-Type` (name it with
    `X-File-Name`), or send `?url=` (or a JSON body `{"url": "…"}`) and we fetch it. Sending both is an
    error rather than a silent precedence — a caller who sent both has two different files in mind. A
    form-encoded or multipart body is refused with `400 unsupported_media_body`: send the bytes
    themselves, not a form around them.

    Args:
        url_query (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Media]
    """

    kwargs = _get_kwargs(
        body=body,
        url_query=url_query,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: File | Unset = UNSET,
    url_query: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Media | None:
    """Upload media

     Turn a file into a Hermoso-hosted URL that `POST /v1/posts` accepts. Two ways in, and exactly ONE
    per call: send the file’s raw bytes as the request body with its own `Content-Type` (name it with
    `X-File-Name`), or send `?url=` (or a JSON body `{"url": "…"}`) and we fetch it. Sending both is an
    error rather than a silent precedence — a caller who sent both has two different files in mind. A
    form-encoded or multipart body is refused with `400 unsupported_media_body`: send the bytes
    themselves, not a form around them.

    Args:
        url_query (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (File | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Media
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            url_query=url_query,
            idempotency_key=idempotency_key,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
