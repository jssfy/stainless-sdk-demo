# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .user import User
from .._models import BaseModel

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    data: Optional[List[User]] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None
