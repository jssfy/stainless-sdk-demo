# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str
    """用户唯一标识符"""

    email: str
    """用户邮箱"""

    name: str
    """用户姓名"""

    avatar_url: Optional[str] = None
    """用户头像 URL"""

    created_at: Optional[datetime] = None
    """创建时间"""

    updated_at: Optional[datetime] = None
    """更新时间"""
