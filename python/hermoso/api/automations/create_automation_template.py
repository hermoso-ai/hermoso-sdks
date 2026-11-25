from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.automation_template import AutomationTemplate
from ...models.automation_template_create import AutomationTemplateCreate
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    body: AutomationTemplateCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/automations/templates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AutomationTemplate | Error | None:
    if response.status_code == 200:
        response_200 = AutomationTemplate.from_dict(response.json())

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
) -> Response[AutomationTemplate | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AutomationTemplate | Error]:
    """Create an automation template

     Up to 20 automation definitions (`automations: [{engine, body}]`) or `from` ({automation_ids} |
    {template_id} | {share_token}). The ad account each runs on becomes an input; campaign and ad ids
    are dropped. `share: true` adds a link token.

    Args:
        x_hermoso_user (str | Unset):
        body (AutomationTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationTemplate | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> AutomationTemplate | Error | None:
    """Create an automation template

     Up to 20 automation definitions (`automations: [{engine, body}]`) or `from` ({automation_ids} |
    {template_id} | {share_token}). The ad account each runs on becomes an input; campaign and ad ids
    are dropped. `share: true` adds a link token.

    Args:
        x_hermoso_user (str | Unset):
        body (AutomationTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationTemplate | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[AutomationTemplate | Error]:
    """Create an automation template

     Up to 20 automation definitions (`automations: [{engine, body}]`) or `from` ({automation_ids} |
    {template_id} | {share_token}). The ad account each runs on becomes an input; campaign and ad ids
    are dropped. `share: true` adds a link token.

    Args:
        x_hermoso_user (str | Unset):
        body (AutomationTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationTemplate | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AutomationTemplateCreate,
    x_hermoso_user: str | Unset = UNSET,
) -> AutomationTemplate | Error | None:
    """Create an automation template

     Up to 20 automation definitions (`automations: [{engine, body}]`) or `from` ({automation_ids} |
    {template_id} | {share_token}). The ad account each runs on becomes an input; campaign and ad ids
    are dropped. `share: true` adds a link token.

    Args:
        x_hermoso_user (str | Unset):
        body (AutomationTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationTemplate | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
