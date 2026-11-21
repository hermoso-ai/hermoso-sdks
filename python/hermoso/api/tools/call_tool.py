from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tool_call import ToolCall
from ...models.tool_job import ToolJob
from ...models.tool_result import ToolResult
from ...types import Unset


def _get_kwargs(
    name: str,
    *,
    body: ToolCall,
    callback_url: str | Unset = UNSET,
    wait: str | Unset = UNSET,
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

    params["wait"] = wait

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tools/{name}".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Error | ToolJob | ToolResult | None:
    if response.status_code == 200:
        response_200 = ToolResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = ToolJob.from_dict(response.json())

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
) -> Response[Error | ToolJob | ToolResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ToolCall,
    callback_url: str | Unset = UNSET,
    wait: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | ToolJob | ToolResult]:
    """Call a tool

     Invoke a tool with a JSON body of its arguments and get its result. The body IS the argument object
    — there is no envelope to wrap it in.

    UNKNOWN ARGUMENTS are never silently dropped. A key the tool does not declare that looks like a
    misspelling or synonym of one it does (`pagId`, `platform` for `target`) is refused with `400
    invalid_arguments`, and `error.unknown_arguments` lists each one as `{name, did_you_mean}`, the
    suggestion always being an argument of THIS tool. Any other undeclared key runs the call without it:
    the result text starts with a line naming it, and the response carries `ignored_arguments: [{name,
    did_you_mean}]` (the same list is `data.ignoredArguments`). Keys starting with `_` are host metadata
    and are never named.

    The same handler the MCP server and the CLI run, on the same credential, through the same spend
    gate: a tool that costs credits costs the same credits here, and one that publishes publishes to the
    same connected account. Send an `Idempotency-Key` on anything that spends or publishes and a retry
    is safe.

    The reply carries BOTH halves of the tool's answer: `text` is the sentence (what an agent reads) and
    `data` is the structured result (what an integration reads). A tool that refuses answers with an
    HTTP error in the standard envelope, never a 200 with a failure inside it.

    CONTRACT TIER: the envelope here — the route, the auth, the errors, the rate-limit headers, the
    idempotency semantics — is stable. A tool's own arguments are not frozen: they improve with the
    tool. Read `GET /v1/tools/{name}` rather than pinning a schema.

    Args:
        name (str):
        callback_url (str | Unset):
        wait (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ToolCall): The TOOL’S OWN arguments, as a flat object. There is no wrapper: to call
            a tool that takes `query`, send `{"query":"..."}`. Read the shape from GET
            /v1/tools/{name}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ToolJob | ToolResult]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        callback_url=callback_url,
        wait=wait,
        x_hermoso_callback_url=x_hermoso_callback_url,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ToolCall,
    callback_url: str | Unset = UNSET,
    wait: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | ToolJob | ToolResult | None:
    """Call a tool

     Invoke a tool with a JSON body of its arguments and get its result. The body IS the argument object
    — there is no envelope to wrap it in.

    UNKNOWN ARGUMENTS are never silently dropped. A key the tool does not declare that looks like a
    misspelling or synonym of one it does (`pagId`, `platform` for `target`) is refused with `400
    invalid_arguments`, and `error.unknown_arguments` lists each one as `{name, did_you_mean}`, the
    suggestion always being an argument of THIS tool. Any other undeclared key runs the call without it:
    the result text starts with a line naming it, and the response carries `ignored_arguments: [{name,
    did_you_mean}]` (the same list is `data.ignoredArguments`). Keys starting with `_` are host metadata
    and are never named.

    The same handler the MCP server and the CLI run, on the same credential, through the same spend
    gate: a tool that costs credits costs the same credits here, and one that publishes publishes to the
    same connected account. Send an `Idempotency-Key` on anything that spends or publishes and a retry
    is safe.

    The reply carries BOTH halves of the tool's answer: `text` is the sentence (what an agent reads) and
    `data` is the structured result (what an integration reads). A tool that refuses answers with an
    HTTP error in the standard envelope, never a 200 with a failure inside it.

    CONTRACT TIER: the envelope here — the route, the auth, the errors, the rate-limit headers, the
    idempotency semantics — is stable. A tool's own arguments are not frozen: they improve with the
    tool. Read `GET /v1/tools/{name}` rather than pinning a schema.

    Args:
        name (str):
        callback_url (str | Unset):
        wait (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ToolCall): The TOOL’S OWN arguments, as a flat object. There is no wrapper: to call
            a tool that takes `query`, send `{"query":"..."}`. Read the shape from GET
            /v1/tools/{name}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ToolJob | ToolResult
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
        callback_url=callback_url,
        wait=wait,
        x_hermoso_callback_url=x_hermoso_callback_url,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ToolCall,
    callback_url: str | Unset = UNSET,
    wait: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Response[Error | ToolJob | ToolResult]:
    """Call a tool

     Invoke a tool with a JSON body of its arguments and get its result. The body IS the argument object
    — there is no envelope to wrap it in.

    UNKNOWN ARGUMENTS are never silently dropped. A key the tool does not declare that looks like a
    misspelling or synonym of one it does (`pagId`, `platform` for `target`) is refused with `400
    invalid_arguments`, and `error.unknown_arguments` lists each one as `{name, did_you_mean}`, the
    suggestion always being an argument of THIS tool. Any other undeclared key runs the call without it:
    the result text starts with a line naming it, and the response carries `ignored_arguments: [{name,
    did_you_mean}]` (the same list is `data.ignoredArguments`). Keys starting with `_` are host metadata
    and are never named.

    The same handler the MCP server and the CLI run, on the same credential, through the same spend
    gate: a tool that costs credits costs the same credits here, and one that publishes publishes to the
    same connected account. Send an `Idempotency-Key` on anything that spends or publishes and a retry
    is safe.

    The reply carries BOTH halves of the tool's answer: `text` is the sentence (what an agent reads) and
    `data` is the structured result (what an integration reads). A tool that refuses answers with an
    HTTP error in the standard envelope, never a 200 with a failure inside it.

    CONTRACT TIER: the envelope here — the route, the auth, the errors, the rate-limit headers, the
    idempotency semantics — is stable. A tool's own arguments are not frozen: they improve with the
    tool. Read `GET /v1/tools/{name}` rather than pinning a schema.

    Args:
        name (str):
        callback_url (str | Unset):
        wait (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ToolCall): The TOOL’S OWN arguments, as a flat object. There is no wrapper: to call
            a tool that takes `query`, send `{"query":"..."}`. Read the shape from GET
            /v1/tools/{name}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ToolJob | ToolResult]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        callback_url=callback_url,
        wait=wait,
        x_hermoso_callback_url=x_hermoso_callback_url,
        idempotency_key=idempotency_key,
        x_hermoso_user=x_hermoso_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ToolCall,
    callback_url: str | Unset = UNSET,
    wait: str | Unset = UNSET,
    x_hermoso_callback_url: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_hermoso_user: str | Unset = UNSET,
) -> Error | ToolJob | ToolResult | None:
    """Call a tool

     Invoke a tool with a JSON body of its arguments and get its result. The body IS the argument object
    — there is no envelope to wrap it in.

    UNKNOWN ARGUMENTS are never silently dropped. A key the tool does not declare that looks like a
    misspelling or synonym of one it does (`pagId`, `platform` for `target`) is refused with `400
    invalid_arguments`, and `error.unknown_arguments` lists each one as `{name, did_you_mean}`, the
    suggestion always being an argument of THIS tool. Any other undeclared key runs the call without it:
    the result text starts with a line naming it, and the response carries `ignored_arguments: [{name,
    did_you_mean}]` (the same list is `data.ignoredArguments`). Keys starting with `_` are host metadata
    and are never named.

    The same handler the MCP server and the CLI run, on the same credential, through the same spend
    gate: a tool that costs credits costs the same credits here, and one that publishes publishes to the
    same connected account. Send an `Idempotency-Key` on anything that spends or publishes and a retry
    is safe.

    The reply carries BOTH halves of the tool's answer: `text` is the sentence (what an agent reads) and
    `data` is the structured result (what an integration reads). A tool that refuses answers with an
    HTTP error in the standard envelope, never a 200 with a failure inside it.

    CONTRACT TIER: the envelope here — the route, the auth, the errors, the rate-limit headers, the
    idempotency semantics — is stable. A tool's own arguments are not frozen: they improve with the
    tool. Read `GET /v1/tools/{name}` rather than pinning a schema.

    Args:
        name (str):
        callback_url (str | Unset):
        wait (str | Unset):
        x_hermoso_callback_url (str | Unset):
        idempotency_key (str | Unset):
        x_hermoso_user (str | Unset):
        body (ToolCall): The TOOL’S OWN arguments, as a flat object. There is no wrapper: to call
            a tool that takes `query`, send `{"query":"..."}`. Read the shape from GET
            /v1/tools/{name}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ToolJob | ToolResult
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
            callback_url=callback_url,
            wait=wait,
            x_hermoso_callback_url=x_hermoso_callback_url,
            idempotency_key=idempotency_key,
            x_hermoso_user=x_hermoso_user,
        )
    ).parsed
