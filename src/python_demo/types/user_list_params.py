# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    email: str
    """按邮箱过滤"""

    page: int
    """页码"""

    per_page: int
    """每页数量"""
