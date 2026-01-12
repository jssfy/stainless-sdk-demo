# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrderItemParam"]


class OrderItemParam(TypedDict, total=False):
    price: Required[float]

    product_id: Required[str]

    quantity: Required[int]
