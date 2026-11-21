from http import HTTPStatus
from typing import Any

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tool_list import ToolList
from ...types import Unset


def _get_kwargs(
    *,
    area: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_hermoso_user, Unset):
        headers["X-Hermoso-User"] = x_hermoso_user

    params: dict[str, Any] = {}

    params["area"] = area

    params["search"] = search

    params["include"] = include

    params["limit"] = limit

    params["starting_after"] = starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tools",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | ToolList | None:
    if response.status_code == 200:
        response_200 = ToolList.from_dict(response.json())

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
) -> Response[Error | ToolList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    area: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | ToolList]:
    """List the callable tools

     Everything this workspace can do over HTTP, grouped by area, each with its human-readable
    description, its JSON Schema and its `price` (what one call spends, read live). This is the
    browsable index: filter by `area`, search by task words (`search=email outreach`, ranked the way the
    MCP `find_tools` tool ranks), page with a cursor.

    READ IT, DO NOT HARD-CODE IT. The set grows continuously and a tool absent here is not a missing
    capability. By default a tool whose connector this workspace has not linked is left out, because it
    could only ever answer "not connected". Send `include=all` to list EVERY tool, including those: each
    such row has `available: false`, `unavailable_reason` (`not_connected`, `not_offered` or
    `shopify_store`), `requires_connector` and a `connect_url` to link it. That is how you build for
    customers whose accounts are connected to platforms your own test account is not. Calling one of
    them answers `401` with `error.type: connector_error` and `error.connector`.

    CONTRACT TIER: this endpoint's SHAPE is stable under the same promise as everything else in `/v1`.
    The TOOLS inside it are not frozen — their arguments improve as the tools do. Treat the roster as
    live data.

    Args:
        area (str | Unset):
        search (str | Unset):
        include (str | Unset):
        limit (int | Unset):
        starting_after (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ToolList]
    """

    kwargs = _get_kwargs(
        area=area,
        search=search,
        include=include,
        limit=limit,
        starting_after=starting_after,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    area: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | ToolList | None:
    """List the callable tools

     Everything this workspace can do over HTTP, grouped by area, each with its human-readable
    description, its JSON Schema and its `price` (what one call spends, read live). This is the
    browsable index: filter by `area`, search by task words (`search=email outreach`, ranked the way the
    MCP `find_tools` tool ranks), page with a cursor.

    READ IT, DO NOT HARD-CODE IT. The set grows continuously and a tool absent here is not a missing
    capability. By default a tool whose connector this workspace has not linked is left out, because it
    could only ever answer "not connected". Send `include=all` to list EVERY tool, including those: each
    such row has `available: false`, `unavailable_reason` (`not_connected`, `not_offered` or
    `shopify_store`), `requires_connector` and a `connect_url` to link it. That is how you build for
    customers whose accounts are connected to platforms your own test account is not. Calling one of
    them answers `401` with `error.type: connector_error` and `error.connector`.

    CONTRACT TIER: this endpoint's SHAPE is stable under the same promise as everything else in `/v1`.
    The TOOLS inside it are not frozen — their arguments improve as the tools do. Treat the roster as
    live data.

    Args:
        area (str | Unset):
        search (str | Unset):
        include (str | Unset):
        limit (int | Unset):
        starting_after (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ToolList
    """

    return sync_detailed(
        client=client,
        area=area,
        search=search,
        include=include,
        limit=limit,
        starting_after=starting_after,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    area: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | ToolList]:
    """List the callable tools

     Everything this workspace can do over HTTP, grouped by area, each with its human-readable
    description, its JSON Schema and its `price` (what one call spends, read live). This is the
    browsable index: filter by `area`, search by task words (`search=email outreach`, ranked the way the
    MCP `find_tools` tool ranks), page with a cursor.

    READ IT, DO NOT HARD-CODE IT. The set grows continuously and a tool absent here is not a missing
    capability. By default a tool whose connector this workspace has not linked is left out, because it
    could only ever answer "not connected". Send `include=all` to list EVERY tool, including those: each
    such row has `available: false`, `unavailable_reason` (`not_connected`, `not_offered` or
    `shopify_store`), `requires_connector` and a `connect_url` to link it. That is how you build for
    customers whose accounts are connected to platforms your own test account is not. Calling one of
    them answers `401` with `error.type: connector_error` and `error.connector`.

    CONTRACT TIER: this endpoint's SHAPE is stable under the same promise as everything else in `/v1`.
    The TOOLS inside it are not frozen — their arguments improve as the tools do. Treat the roster as
    live data.

    Args:
        area (str | Unset):
        search (str | Unset):
        include (str | Unset):
        limit (int | Unset):
        starting_after (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ToolList]
    """

    kwargs = _get_kwargs(
        area=area,
        search=search,
        include=include,
        limit=limit,
        starting_after=starting_after,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    area: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | ToolList | None:
    """List the callable tools

     Everything this workspace can do over HTTP, grouped by area, each with its human-readable
    description, its JSON Schema and its `price` (what one call spends, read live). This is the
    browsable index: filter by `area`, search by task words (`search=email outreach`, ranked the way the
    MCP `find_tools` tool ranks), page with a cursor.

    READ IT, DO NOT HARD-CODE IT. The set grows continuously and a tool absent here is not a missing
    capability. By default a tool whose connector this workspace has not linked is left out, because it
    could only ever answer "not connected". Send `include=all` to list EVERY tool, including those: each
    such row has `available: false`, `unavailable_reason` (`not_connected`, `not_offered` or
    `shopify_store`), `requires_connector` and a `connect_url` to link it. That is how you build for
    customers whose accounts are connected to platforms your own test account is not. Calling one of
    them answers `401` with `error.type: connector_error` and `error.connector`.

    CONTRACT TIER: this endpoint's SHAPE is stable under the same promise as everything else in `/v1`.
    The TOOLS inside it are not frozen — their arguments improve as the tools do. Treat the roster as
    live data.

    Args:
        area (str | Unset):
        search (str | Unset):
        include (str | Unset):
        limit (int | Unset):
        starting_after (str | Unset):
        x_hermoso_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ToolList
    """

    return (
        await asyncio_detailed(
            client=client,
            area=area,
            search=search,
            include=include,
            limit=limit,
            starting_after=starting_after,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
