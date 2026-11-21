from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.generation_create import GenerationCreate
from ...models.job import Job
from ...types import Unset


def _get_kwargs(
    *,
    body: GenerationCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_callback_url, Unset):
        headers["X-Hermoso-Callback-Url"] = x_hermoso_callback_url

    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["callback_url"] = callback_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/generations",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | Job | None:
    if response.status_code == 200:
        response_200 = Job.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = Job.from_dict(response.json())

        return response_202

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
) -> Response[Error | Job]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GenerationCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Job]:
    """Generate an image or video

     Queue one image or one video render for this profile and answer 202 with the job. Poll `GET
    /v1/jobs/{id}` until `status` is `done` (its `url` is the file) or `error`. Billed exactly as the
    same render is anywhere in Hermoso: the credits are reserved when it starts and settle to the
    measured cost. A refusal (not enough credits, a prompt the model will not render) is an error in the
    standard envelope, with the server’s own sentence in `message`. Send an `Idempotency-Key` and a
    retry never starts a second render.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (GenerationCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Job]
    """

    kwargs = _get_kwargs(
        body=body,
        callback_url=callback_url,
        x_hermoso_callback_url=x_hermoso_callback_url,
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
    body: GenerationCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Job | None:
    """Generate an image or video

     Queue one image or one video render for this profile and answer 202 with the job. Poll `GET
    /v1/jobs/{id}` until `status` is `done` (its `url` is the file) or `error`. Billed exactly as the
    same render is anywhere in Hermoso: the credits are reserved when it starts and settle to the
    measured cost. A refusal (not enough credits, a prompt the model will not render) is an error in the
    standard envelope, with the server’s own sentence in `message`. Send an `Idempotency-Key` and a
    retry never starts a second render.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (GenerationCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Job
    """

    return sync_detailed(
        client=client,
        body=body,
        callback_url=callback_url,
        x_hermoso_callback_url=x_hermoso_callback_url,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GenerationCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Job]:
    """Generate an image or video

     Queue one image or one video render for this profile and answer 202 with the job. Poll `GET
    /v1/jobs/{id}` until `status` is `done` (its `url` is the file) or `error`. Billed exactly as the
    same render is anywhere in Hermoso: the credits are reserved when it starts and settle to the
    measured cost. A refusal (not enough credits, a prompt the model will not render) is an error in the
    standard envelope, with the server’s own sentence in `message`. Send an `Idempotency-Key` and a
    retry never starts a second render.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (GenerationCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Job]
    """

    kwargs = _get_kwargs(
        body=body,
        callback_url=callback_url,
        x_hermoso_callback_url=x_hermoso_callback_url,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GenerationCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Job | None:
    """Generate an image or video

     Queue one image or one video render for this profile and answer 202 with the job. Poll `GET
    /v1/jobs/{id}` until `status` is `done` (its `url` is the file) or `error`. Billed exactly as the
    same render is anywhere in Hermoso: the credits are reserved when it starts and settle to the
    measured cost. A refusal (not enough credits, a prompt the model will not render) is an error in the
    standard envelope, with the server’s own sentence in `message`. Send an `Idempotency-Key` and a
    retry never starts a second render.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (GenerationCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Job
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            callback_url=callback_url,
            x_hermoso_callback_url=x_hermoso_callback_url,
            idempotency_key=idempotency_key,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
