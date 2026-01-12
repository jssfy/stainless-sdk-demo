# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .order_item import OrderItem
from .order_status import OrderStatus

__all__ = ["Order"]


class Order(BaseModel):
    id: str

    status: OrderStatus
    """订单状态"""

    total_amount: float

    user_id: str

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    items: Optional[List[OrderItem]] = None

    updated_at: Optional[datetime] = None
