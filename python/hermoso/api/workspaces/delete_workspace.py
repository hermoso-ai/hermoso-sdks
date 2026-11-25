from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.workspace_deletion import WorkspaceDeletion
from ...types import Unset


def _get_kwargs(
    workspace_id: str,
    *,
    confirm: bool | Unset = UNSET,
    confirm_name: str | Unset = UNSET,
    confirm_connectors: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["confirm"] = confirm

    params["confirm_name"] = confirm_name

    params["confirm_connectors"] = confirm_connectors

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/workspaces/{workspace_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | WorkspaceDeletion | None:
    if response.status_code == 200:
        response_200 = WorkspaceDeletion.from_dict(response.json())

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
) -> Response[Error | WorkspaceDeletion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    confirm_name: str | Unset = UNSET,
    confirm_connectors: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WorkspaceDeletion]:
    """Delete a workspace

     Permanently deletes the profile and everything in it. Without `confirm=true`, `confirm_name` (its
    exact name) and, when it has connected accounts, `confirm_connectors` (their number), it answers
    with the inventory of what would be lost and deletes nothing.

    Args:
        workspace_id (str):
        confirm (bool | Unset):
        confirm_name (str | Unset):
        confirm_connectors (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkspaceDeletion]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        confirm=confirm,
        confirm_name=confirm_name,
        confirm_connectors=confirm_connectors,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    confirm_name: str | Unset = UNSET,
    confirm_connectors: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WorkspaceDeletion | None:
    """Delete a workspace

     Permanently deletes the profile and everything in it. Without `confirm=true`, `confirm_name` (its
    exact name) and, when it has connected accounts, `confirm_connectors` (their number), it answers
    with the inventory of what would be lost and deletes nothing.

    Args:
        workspace_id (str):
        confirm (bool | Unset):
        confirm_name (str | Unset):
        confirm_connectors (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkspaceDeletion
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        confirm=confirm,
        confirm_name=confirm_name,
        confirm_connectors=confirm_connectors,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    confirm_name: str | Unset = UNSET,
    confirm_connectors: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WorkspaceDeletion]:
    """Delete a workspace

     Permanently deletes the profile and everything in it. Without `confirm=true`, `confirm_name` (its
    exact name) and, when it has connected accounts, `confirm_connectors` (their number), it answers
    with the inventory of what would be lost and deletes nothing.

    Args:
        workspace_id (str):
        confirm (bool | Unset):
        confirm_name (str | Unset):
        confirm_connectors (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkspaceDeletion]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        confirm=confirm,
        confirm_name=confirm_name,
        confirm_connectors=confirm_connectors,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    confirm_name: str | Unset = UNSET,
    confirm_connectors: int | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WorkspaceDeletion | None:
    """Delete a workspace

     Permanently deletes the profile and everything in it. Without `confirm=true`, `confirm_name` (its
    exact name) and, when it has connected accounts, `confirm_connectors` (their number), it answers
    with the inventory of what would be lost and deletes nothing.

    Args:
        workspace_id (str):
        confirm (bool | Unset):
        confirm_name (str | Unset):
        confirm_connectors (int | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkspaceDeletion
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            confirm=confirm,
            confirm_name=confirm_name,
            confirm_connectors=confirm_connectors,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
