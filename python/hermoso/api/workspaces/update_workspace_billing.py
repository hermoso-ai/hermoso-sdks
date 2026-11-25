from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.workspace_billing import WorkspaceBilling
from ...models.workspace_billing_update import WorkspaceBillingUpdate
from ...types import Unset


def _get_kwargs(
    workspace_id: str,
    *,
    body: WorkspaceBillingUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/workspaces/{workspace_id}/billing".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | WorkspaceBilling | None:
    if response.status_code == 200:
        response_200 = WorkspaceBilling.from_dict(response.json())

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
) -> Response[Error | WorkspaceBilling]:
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
    body: WorkspaceBillingUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WorkspaceBilling]:
    """Bill a workspace separately

     `billed_separately` true makes the brand pay from its own balance (account holder only; it changes
    who pays, so `confirm: true` is required, and without it the change is described and nothing
    changes); false puts it back on the account’s balance, keeping its own balance for later.

    Args:
        workspace_id (str):
        x_hermoso_user (str | Unset):
        body (WorkspaceBillingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkspaceBilling]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
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
    body: WorkspaceBillingUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WorkspaceBilling | None:
    """Bill a workspace separately

     `billed_separately` true makes the brand pay from its own balance (account holder only; it changes
    who pays, so `confirm: true` is required, and without it the change is described and nothing
    changes); false puts it back on the account’s balance, keeping its own balance for later.

    Args:
        workspace_id (str):
        x_hermoso_user (str | Unset):
        body (WorkspaceBillingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkspaceBilling
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkspaceBillingUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | WorkspaceBilling]:
    """Bill a workspace separately

     `billed_separately` true makes the brand pay from its own balance (account holder only; it changes
    who pays, so `confirm: true` is required, and without it the change is described and nothing
    changes); false puts it back on the account’s balance, keeping its own balance for later.

    Args:
        workspace_id (str):
        x_hermoso_user (str | Unset):
        body (WorkspaceBillingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkspaceBilling]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkspaceBillingUpdate,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | WorkspaceBilling | None:
    """Bill a workspace separately

     `billed_separately` true makes the brand pay from its own balance (account holder only; it changes
    who pays, so `confirm: true` is required, and without it the change is described and nothing
    changes); false puts it back on the account’s balance, keeping its own balance for later.

    Args:
        workspace_id (str):
        x_hermoso_user (str | Unset):
        body (WorkspaceBillingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkspaceBilling
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
