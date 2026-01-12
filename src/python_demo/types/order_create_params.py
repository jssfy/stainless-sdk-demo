# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .order_item_param import OrderItemParam

__all__ = ["OrderCreateParams"]


class OrderCreateParams(TypedDict, total=False):
    items: Required[Iterable[OrderItemParam]]
