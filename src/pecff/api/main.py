"""PECFF API Entry Point Alias for ASGI servers."""

from __future__ import annotations

from pecff.api.app import app, create_app

__all__ = ["app", "create_app"]
