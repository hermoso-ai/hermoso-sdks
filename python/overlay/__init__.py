"""Hermoso: the typed Python client for the Hermoso API (https://hermoso.ai/docs/sdks/).

Everything except this file and ``_helpers.py`` is generated from the /v1 OpenAPI document. Each operation lives in
``hermoso.api.<group>.<operation>`` with ``sync``, ``sync_detailed``, ``asyncio`` and ``asyncio_detailed``; the typed
request and response models are in ``hermoso.models``.
"""

from ._helpers import DEFAULT_BASE_URL, HermosoError, create_client, paginate, run_tool, wait_for_job
from ._spec import CONTRACT_VERSION, SPEC_SHA256
from .client import AuthenticatedClient, Client

try:
    from importlib.metadata import version as _version

    __version__ = _version("hermoso")
except Exception:  # pragma: no cover - running from a source tree
    __version__ = "0+unknown"

__all__ = (
    "AuthenticatedClient",
    "Client",
    "CONTRACT_VERSION",
    "DEFAULT_BASE_URL",
    "HermosoError",
    "SPEC_SHA256",
    "create_client",
    "paginate",
    "run_tool",
    "wait_for_job",
)
