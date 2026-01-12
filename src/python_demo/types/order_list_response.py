# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .order import Order
from .._models import BaseModel

__all__ = ["OrderListResponse"]


class OrderListResponse(BaseModel):
    data: Optional[List[Order]] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total: Optional[int] = None
