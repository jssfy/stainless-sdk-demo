# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Product"]


class Product(BaseModel):
    id: str

    name: str

    price: float

    category: Optional[str] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    description: Optional[str] = None

    stock: Optional[int] = None

    updated_at: Optional[datetime] = None
