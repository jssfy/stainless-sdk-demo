# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .product import Product
from .._models import BaseModel

__all__ = ["ProductListResponse"]


class ProductListResponse(BaseModel):
    data: Optional[List[Product]] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total: Optional[int] = None
