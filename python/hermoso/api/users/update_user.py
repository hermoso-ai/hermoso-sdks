from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.user import User
from ...models.user_update import UserUpdate
from ...types import Unset


def _get_kwargs(
    email: str,
    *,
    body: UserUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/users/{email}".format(
            email=quote(str(email), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | User | None:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

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
) -> Response[Error | User]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    body: UserUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | User]:
    """Change a person’s role or areas

     Sets the role, and optionally replaces the list of turned-off areas (omit `disabled_areas` to keep
    it; `[]` turns every area back on). Enforced on every surface at once. The answer is read back from
    the team list, never echoed from the request. Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):
        body (UserUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | User]
    """

    kwargs = _get_kwargs(
        email=email,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
    body: UserUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | User | None:
    """Change a person’s role or areas

     Sets the role, and optionally replaces the list of turned-off areas (omit `disabled_areas` to keep
    it; `[]` turns every area back on). Enforced on every surface at once. The answer is read back from
    the team list, never echoed from the request. Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):
        body (UserUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | User
    """

    return sync_detailed(
        email=email,
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    body: UserUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | User]:
    """Change a person’s role or areas

     Sets the role, and optionally replaces the list of turned-off areas (omit `disabled_areas` to keep
    it; `[]` turns every area back on). Enforced on every surface at once. The answer is read back from
    the team list, never echoed from the request. Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):
        body (UserUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | User]
    """

    kwargs = _get_kwargs(
        email=email,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
    body: UserUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | User | None:
    """Change a person’s role or areas

     Sets the role, and optionally replaces the list of turned-off areas (omit `disabled_areas` to keep
    it; `[]` turns every area back on). Enforced on every surface at once. The answer is read back from
    the team list, never echoed from the request. Admins only.

    Args:
        email (str):
        x_hermoso_user (str | Unset):
        body (UserUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | User
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
