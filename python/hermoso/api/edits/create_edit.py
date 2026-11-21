from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.edit import Edit
from ...models.edit_create import EditCreate
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    body: EditCreate,
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
        "url": "/v1/edits",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Edit | Error | None:
    if response.status_code == 200:
        response_200 = Edit.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = Edit.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Edit | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EditCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Edit | Error]:
    """Change one thing in a video

     Edit a clip from a plain instruction: "change only the mug to red", "swap the bottle for our
    product", "make it night". The motion, timing, framing and cut stay; the named thing changes, and
    the rest of the frame is held. A `reference` image anchors the material of what changes (a fabric, a
    finish, the real product). One change per call holds best, on clips of 3 to 15 seconds.

    PRICED UP FRONT. `"dry_run": true` returns the estimated credits the edit reserves when it starts,
    from the job's own pricing. The real call reserves the same figure and is charged its actual cost,
    usually within a few percent of it.

    PREVIEW FIRST (optional). `"preview_first_frame": true` edits ONE still of the clip and returns it
    with the clip's price, and nothing else runs. Look at it, then send the same request with
    `preview_still` set to the still to render the clip matched to it. A preview is one image edit; with
    `dry_run` it is priced, not made.

    ASYNC. A real clip call answers `202` with the job inside; poll `GET /v1/jobs/{id}` or name a
    `callback_url`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (EditCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Edit | Error]
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
    body: EditCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Edit | Error | None:
    """Change one thing in a video

     Edit a clip from a plain instruction: "change only the mug to red", "swap the bottle for our
    product", "make it night". The motion, timing, framing and cut stay; the named thing changes, and
    the rest of the frame is held. A `reference` image anchors the material of what changes (a fabric, a
    finish, the real product). One change per call holds best, on clips of 3 to 15 seconds.

    PRICED UP FRONT. `"dry_run": true` returns the estimated credits the edit reserves when it starts,
    from the job's own pricing. The real call reserves the same figure and is charged its actual cost,
    usually within a few percent of it.

    PREVIEW FIRST (optional). `"preview_first_frame": true` edits ONE still of the clip and returns it
    with the clip's price, and nothing else runs. Look at it, then send the same request with
    `preview_still` set to the still to render the clip matched to it. A preview is one image edit; with
    `dry_run` it is priced, not made.

    ASYNC. A real clip call answers `202` with the job inside; poll `GET /v1/jobs/{id}` or name a
    `callback_url`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (EditCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Edit | Error
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
    body: EditCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Edit | Error]:
    """Change one thing in a video

     Edit a clip from a plain instruction: "change only the mug to red", "swap the bottle for our
    product", "make it night". The motion, timing, framing and cut stay; the named thing changes, and
    the rest of the frame is held. A `reference` image anchors the material of what changes (a fabric, a
    finish, the real product). One change per call holds best, on clips of 3 to 15 seconds.

    PRICED UP FRONT. `"dry_run": true` returns the estimated credits the edit reserves when it starts,
    from the job's own pricing. The real call reserves the same figure and is charged its actual cost,
    usually within a few percent of it.

    PREVIEW FIRST (optional). `"preview_first_frame": true` edits ONE still of the clip and returns it
    with the clip's price, and nothing else runs. Look at it, then send the same request with
    `preview_still` set to the still to render the clip matched to it. A preview is one image edit; with
    `dry_run` it is priced, not made.

    ASYNC. A real clip call answers `202` with the job inside; poll `GET /v1/jobs/{id}` or name a
    `callback_url`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (EditCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Edit | Error]
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
    body: EditCreate,
    callback_url: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Edit | Error | None:
    """Change one thing in a video

     Edit a clip from a plain instruction: "change only the mug to red", "swap the bottle for our
    product", "make it night". The motion, timing, framing and cut stay; the named thing changes, and
    the rest of the frame is held. A `reference` image anchors the material of what changes (a fabric, a
    finish, the real product). One change per call holds best, on clips of 3 to 15 seconds.

    PRICED UP FRONT. `"dry_run": true` returns the estimated credits the edit reserves when it starts,
    from the job's own pricing. The real call reserves the same figure and is charged its actual cost,
    usually within a few percent of it.

    PREVIEW FIRST (optional). `"preview_first_frame": true` edits ONE still of the clip and returns it
    with the clip's price, and nothing else runs. Look at it, then send the same request with
    `preview_still` set to the still to render the clip matched to it. A preview is one image edit; with
    `dry_run` it is priced, not made.

    ASYNC. A real clip call answers `202` with the job inside; poll `GET /v1/jobs/{id}` or name a
    `callback_url`.

    Args:
        callback_url (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (EditCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Edit | Error
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
