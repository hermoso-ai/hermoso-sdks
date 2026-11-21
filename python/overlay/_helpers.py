"""The small hand-written layer over the generated client: a client that reads your key, a cursor paginator, a job
waiter and a one-line tool call. Not generated; tools/sdk-generate.mjs copies it into the package."""

from __future__ import annotations

import os
import time
from collections.abc import Iterator
from types import ModuleType
from typing import Any

from .client import AuthenticatedClient
from .models.error import Error
from .types import Unset

DEFAULT_BASE_URL = "https://app.hermoso.ai"


class HermosoError(Exception):
    """An error answer from the API. ``error`` is the parsed ``Error`` model (``error.error.code``, ``.message``)."""

    def __init__(self, error: Any, status: int | None = None) -> None:
        detail = getattr(getattr(error, "error", None), "message", None)
        super().__init__(detail or f"Hermoso API error{f' (HTTP {status})' if status else ''}")
        self.error = error
        self.status = status


def create_client(
    api_key: str | None = None,
    *,
    brand: str | None = None,
    base_url: str = DEFAULT_BASE_URL,
    timeout: float = 90.0,
) -> AuthenticatedClient:
    """A client authenticated with your API key (default: the HERMOSO_API_KEY environment variable).

    ``brand`` acts on that brand (an ``id`` from ``list_brands``) instead of the one the key is pinned to.
    """
    key = api_key or os.environ.get("HERMOSO_API_KEY")
    if not key:
        raise ValueError(
            "No Hermoso API key: pass api_key or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai "
            'on the "API, MCP & CLI" tab, under "Terminal & API keys".'
        )
    import httpx2

    return AuthenticatedClient(
        base_url=base_url,
        token=key,
        headers={"X-Hermoso-User": brand} if brand else {},
        timeout=httpx2.Timeout(timeout),
    )


def _value(obj: Any, name: str) -> Any:
    v = getattr(obj, name, None)
    return None if isinstance(v, Unset) else v


def paginate(operation: ModuleType, *, client: AuthenticatedClient, **params: Any) -> Iterator[Any]:
    """Iterate every item of a cursor-paginated list, following ``next_cursor`` until ``has_more`` is false.

    ``operation`` is the generated module, e.g. ``hermoso.api.posts.list_posts``::

        for post in paginate(list_posts, client=client, status="scheduled"):
            print(post.id, post.status)
    """
    cursor_param = "cursor" if operation.__name__.endswith("list_conversion_events") else "starting_after"
    cursor = None
    while True:
        if cursor:
            params[cursor_param] = cursor
        res = operation.sync_detailed(client=client, **params)
        page = res.parsed
        if page is None or isinstance(page, Error):
            raise HermosoError(page, int(res.status_code))
        yield from (_value(page, "data") or [])
        cursor = _value(page, "next_cursor")
        if not cursor or _value(page, "has_more") is False:
            return


def wait_for_job(job_id: str, *, client: AuthenticatedClient, interval: float = 5.0, timeout: float = 1200.0) -> Any:
    """Poll a job (a render, a stitch, an upscale…) until it is ``done`` or ``error`` and return it; the file is
    ``job.url``. Polling is free; calling the tool again would start (and bill) a second render."""
    from .api.jobs import get_job

    deadline = time.monotonic() + timeout
    while True:
        res = get_job.sync_detailed(job_id, client=client)
        job = res.parsed
        if job is None or isinstance(job, Error):
            raise HermosoError(job, int(res.status_code))
        if job.status in ("done", "error"):
            return job
        if time.monotonic() > deadline:
            raise TimeoutError(f"Job {job_id} is still {job.status}; it keeps running, call wait_for_job again.")
        time.sleep(interval)


def run_tool(
    name: str,
    args: dict[str, Any] | None = None,
    *,
    client: AuthenticatedClient,
    wait: int | None = None,
    idempotency_key: str | None = None,
) -> Any:
    """Run any Hermoso tool through ``POST /v1/tools/{name}`` and return its result (a ``ToolResult``, or a ``ToolJob``
    handle when it started a render: pass ``job_id`` to ``wait_for_job``). ``GET /v1/tools/{name}`` describes each
    tool's arguments::

        plan = run_tool("plan_ad", {"product": "our cold brew, summer offer", "format": "video"}, client=client)
    """
    from .api.tools import call_tool
    from .models.tool_call import ToolCall
    from .types import UNSET

    res = call_tool.sync_detailed(
        name,
        client=client,
        body=ToolCall.from_dict(args or {}),
        wait=UNSET if wait is None else str(wait),
        idempotency_key=idempotency_key or UNSET,
    )
    out = res.parsed
    if out is None or isinstance(out, Error):
        raise HermosoError(out, int(res.status_code))
    return out
