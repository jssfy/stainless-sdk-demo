# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OrderItem"]


class OrderItem(BaseModel):
    price: float

    product_id: str

    quantity: int
