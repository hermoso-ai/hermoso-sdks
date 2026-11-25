from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.automation_install import AutomationInstall
from ...models.automation_template_install import AutomationTemplateInstall
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    share_token: str,
    *,
    body: AutomationTemplateInstall,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/automations/templates/shared/{share_token}/install".format(
            share_token=quote(str(share_token), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AutomationInstall | Error | None:
    if response.status_code == 200:
        response_200 = AutomationInstall.from_dict(response.json())

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
) -> Response[AutomationInstall | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share_token: str,
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateInstall,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AutomationInstall | Error]:
    """Install a shared automation template

     The same as an install, from a template another team shared by link.

    Args:
        share_token (str):
        x_hermoso_user (str | Unset):
        body (AutomationTemplateInstall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationInstall | Error]
    """

    kwargs = _get_kwargs(
        share_token=share_token,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share_token: str,
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateInstall,
    x_hermoso_user: str | Unset = UNSET,
) -> AutomationInstall | Error | None:
    """Install a shared automation template

     The same as an install, from a template another team shared by link.

    Args:
        share_token (str):
        x_hermoso_user (str | Unset):
        body (AutomationTemplateInstall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationInstall | Error
    """

    return sync_detailed(
        share_token=share_token,
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    share_token: str,
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateInstall,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AutomationInstall | Error]:
    """Install a shared automation template

     The same as an install, from a template another team shared by link.

    Args:
        share_token (str):
        x_hermoso_user (str | Unset):
        body (AutomationTemplateInstall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationInstall | Error]
    """

    kwargs = _get_kwargs(
        share_token=share_token,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_token: str,
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateInstall,
    x_hermoso_user: str | Unset = UNSET,
) -> AutomationInstall | Error | None:
    """Install a shared automation template

     The same as an install, from a template another team shared by link.

    Args:
        share_token (str):
        x_hermoso_user (str | Unset):
        body (AutomationTemplateInstall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationInstall | Error
    """

    return (
        await asyncio_detailed(
            share_token=share_token,
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
