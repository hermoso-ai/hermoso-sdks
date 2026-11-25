from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.automation import Automation
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    automation_id: str,
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
        "url": "/v1/automations/{automation_id}".format(
            automation_id=quote(str(automation_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Automation | Error | None:
    if response.status_code == 200:
        response_200 = Automation.from_dict(response.json())

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
) -> Response[Automation | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Automation | Error]:
    """Delete an automation

     Cannot be undone: `confirm=true` is required.

    Args:
        automation_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Automation | Error]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        confirm=confirm,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Automation | Error | None:
    """Delete an automation

     Cannot be undone: `confirm=true` is required.

    Args:
        automation_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Automation | Error
    """

    return sync_detailed(
        automation_id=automation_id,
        client=client,
        confirm=confirm,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Automation | Error]:
    """Delete an automation

     Cannot be undone: `confirm=true` is required.

    Args:
        automation_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Automation | Error]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        confirm=confirm,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    confirm: bool | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Automation | Error | None:
    """Delete an automation

     Cannot be undone: `confirm=true` is required.

    Args:
        automation_id (str):
        confirm (bool | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Automation | Error
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            client=client,
            confirm=confirm,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
