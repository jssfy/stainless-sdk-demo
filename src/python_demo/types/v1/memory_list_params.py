# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MemoryListParams"]


class MemoryListParams(TypedDict, total=False):
    end_time: Optional[str]
    """End time for time range filtering (ISO 8601 format)"""

    group_id: Optional[str]
    """Group ID"""

    limit: Optional[int]
    """Maximum number of memories to return"""

    memory_type: Optional[Literal["profile", "episodic_memory", "foresight", "event_log"]]
    """Memory type, enum values from MemoryType:

    - profile: user profile
    - episodic_memory: episodic memory (default)
    - foresight: prospective memory
    - event_log: event log (atomic facts)
    """

    offset: Optional[int]
    """Pagination offset"""

    start_time: Optional[str]
    """Start time for time range filtering (ISO 8601 format)"""

    user_id: Optional[str]
    """User ID"""
