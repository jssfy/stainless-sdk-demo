# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .order_status import OrderStatus

__all__ = ["OrderListParams"]


class OrderListParams(TypedDict, total=False):
    page: int

    status: OrderStatus
    """订单状态过滤"""
