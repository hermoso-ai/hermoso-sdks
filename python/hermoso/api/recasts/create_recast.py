from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.recast import Recast
from ...models.recast_create import RecastCreate
from ...types import Unset


def _get_kwargs(
    *,
    body: RecastCreate,
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
        "url": "/v1/recasts",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | Recast | None:
    if response.status_code == 200:
        response_200 = Recast.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = Recast.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Error | Recast]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RecastCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Recast]:
    """Put a person into a video (motion transfer)

     Replace the person in a video with someone else: a saved or preset creator, a photo, or an AI person
    made from a description. The new person performs every move, expression and mouth shape of the
    original, on the same beats and cuts, in the same set and light, and the original sound is kept.
    Optionally give them a new voice, or have them speak another language with the mouth lip-synced.

    PRICED UP FRONT. Send `"dry_run": true` and the response is the exact price: the credits the job
    reserves when it starts, from the job's own pricing. It is an estimate: the real call reserves the
    same figure and is charged its actual cost, usually within a few percent of it. Nothing runs and
    nothing is charged on a dry run, except that reading a social post link uses its one lookup.

    ASYNC. A real call answers `202` with the job inside and a `Location` to poll (`GET /v1/jobs/{id}`),
    usually a few minutes. Or name a `callback_url` and the finished job is POSTed to you.

    PEOPLE AND LIKENESS. A photo of a real person needs a paid plan or a credit pack, and sending one is
    your confirmation that you have that person's permission (it is recorded). An AI person from
    `describe`, or a preset creator, works on every plan. A request that would be refused is refused
    before anything is charged, with a stable `error.code` and a plain sentence: `real_face_needs_paid`,
    `face_review_blocked`, `ref_unreadable`, `insufficient_credits`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (RecastCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Recast]
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
    body: RecastCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Recast | None:
    """Put a person into a video (motion transfer)

     Replace the person in a video with someone else: a saved or preset creator, a photo, or an AI person
    made from a description. The new person performs every move, expression and mouth shape of the
    original, on the same beats and cuts, in the same set and light, and the original sound is kept.
    Optionally give them a new voice, or have them speak another language with the mouth lip-synced.

    PRICED UP FRONT. Send `"dry_run": true` and the response is the exact price: the credits the job
    reserves when it starts, from the job's own pricing. It is an estimate: the real call reserves the
    same figure and is charged its actual cost, usually within a few percent of it. Nothing runs and
    nothing is charged on a dry run, except that reading a social post link uses its one lookup.

    ASYNC. A real call answers `202` with the job inside and a `Location` to poll (`GET /v1/jobs/{id}`),
    usually a few minutes. Or name a `callback_url` and the finished job is POSTed to you.

    PEOPLE AND LIKENESS. A photo of a real person needs a paid plan or a credit pack, and sending one is
    your confirmation that you have that person's permission (it is recorded). An AI person from
    `describe`, or a preset creator, works on every plan. A request that would be refused is refused
    before anything is charged, with a stable `error.code` and a plain sentence: `real_face_needs_paid`,
    `face_review_blocked`, `ref_unreadable`, `insufficient_credits`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (RecastCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Recast
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
    body: RecastCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | Recast]:
    """Put a person into a video (motion transfer)

     Replace the person in a video with someone else: a saved or preset creator, a photo, or an AI person
    made from a description. The new person performs every move, expression and mouth shape of the
    original, on the same beats and cuts, in the same set and light, and the original sound is kept.
    Optionally give them a new voice, or have them speak another language with the mouth lip-synced.

    PRICED UP FRONT. Send `"dry_run": true` and the response is the exact price: the credits the job
    reserves when it starts, from the job's own pricing. It is an estimate: the real call reserves the
    same figure and is charged its actual cost, usually within a few percent of it. Nothing runs and
    nothing is charged on a dry run, except that reading a social post link uses its one lookup.

    ASYNC. A real call answers `202` with the job inside and a `Location` to poll (`GET /v1/jobs/{id}`),
    usually a few minutes. Or name a `callback_url` and the finished job is POSTed to you.

    PEOPLE AND LIKENESS. A photo of a real person needs a paid plan or a credit pack, and sending one is
    your confirmation that you have that person's permission (it is recorded). An AI person from
    `describe`, or a preset creator, works on every plan. A request that would be refused is refused
    before anything is charged, with a stable `error.code` and a plain sentence: `real_face_needs_paid`,
    `face_review_blocked`, `ref_unreadable`, `insufficient_credits`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (RecastCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Recast]
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
    body: RecastCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | Recast | None:
    """Put a person into a video (motion transfer)

     Replace the person in a video with someone else: a saved or preset creator, a photo, or an AI person
    made from a description. The new person performs every move, expression and mouth shape of the
    original, on the same beats and cuts, in the same set and light, and the original sound is kept.
    Optionally give them a new voice, or have them speak another language with the mouth lip-synced.

    PRICED UP FRONT. Send `"dry_run": true` and the response is the exact price: the credits the job
    reserves when it starts, from the job's own pricing. It is an estimate: the real call reserves the
    same figure and is charged its actual cost, usually within a few percent of it. Nothing runs and
    nothing is charged on a dry run, except that reading a social post link uses its one lookup.

    ASYNC. A real call answers `202` with the job inside and a `Location` to poll (`GET /v1/jobs/{id}`),
    usually a few minutes. Or name a `callback_url` and the finished job is POSTed to you.

    PEOPLE AND LIKENESS. A photo of a real person needs a paid plan or a credit pack, and sending one is
    your confirmation that you have that person's permission (it is recorded). An AI person from
    `describe`, or a preset creator, works on every plan. A request that would be refused is refused
    before anything is charged, with a stable `error.code` and a plain sentence: `real_face_needs_paid`,
    `face_review_blocked`, `ref_unreadable`, `insufficient_credits`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (RecastCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Recast
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
